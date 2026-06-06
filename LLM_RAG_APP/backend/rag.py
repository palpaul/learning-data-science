""" pdfReader is a class that reads a PDF file and extracts the text from it.
 It uses the pypdf library to read the PDF file and extract the text.
   The extract_text method takes a file path as input and returns the extracted text as a string. """

import os

from pypdf import PdfReader
from dotenv import load_dotenv
load_dotenv()

# For quick testing you can hard-code an API key here (Claude or OpenAI).
# Example (uncomment to use):
# api_key = "sk-..."  # placed here only for local testing; avoid committing secrets.

"""SentenceTransformer is a class that uses the sentence-transformers library to create embeddings for the extracted text.
 It uses the SentenceTransformer class from the sentence-transformers library to create embeddings for the extracted text"""

from sentence_transformers import SentenceTransformer

#used to connect to vectordb and store the embeddings
import chromadb
#OpenAI is a class that uses the OpenAI API to generate responses based on the extracted text and the user query.
from openai import OpenAI

#load the model
model = SentenceTransformer('all-MiniLM-L6-v2') # this is a small model that is good for generating embeddings for short texts. You can choose a different model if you want to generate embeddings for longer texts.


# crete  the table collection in chromadb
client = chromadb.Client()
collection = client.create_collection(name="pdf_data")

# read the pdf file and extract the text
def read_pdf(file_path):
    reader = PdfReader(file_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text


#chunk the text into smaller pieces and create embeddings for each chunk
def chunk_text(text, chunk_size=500):
    chunks = []
    for i in range(0, len(text), chunk_size):
        chunk = text[i:i+chunk_size]
        chunks.append(chunk)
    return chunks

#embedding the chunks and storing them in chromadb
# chunks converts into embeddings
# example : hello --- [0.1, 0.2, 0.3, 0.4] this is the embedding for the word hello

def create_embed_chunks(chunks):
        embeddings = model.encode(chunks)
        return embeddings
        # here why are we adding the embedding to the collection? because we want to store the embeddings in the collection so that we can use them later to generate responses based on the user query. The metadata is used to store the original text of the chunk so that we can use it later to generate responses based on the user query.    

# store the embeddings in chromadb
def store_in_chromadb(chunks,embeddings):
     collection.add(documents = chunks,embeddings=embeddings.tolist(),ids=[str(i) for i in range(len(chunks))])
     return "Embeddings stored in chromadb successfully"

# search for the relevant chunks based on the user query
def search_query(query):
    # create embedding for user query
    user_query_embedding = model.encode(query)
    # search similar chunks in ChromaDB
    results = collection.query(
        query_embeddings=[user_query_embedding.tolist()],
        n_results=2
    )

    return results

# Generate response using OpenAI if available, otherwise Claude/Anthropic
def generate_response(query, context):
    openai_key = os.getenv("OPENAI_API_KEY")
    claude_key = os.getenv("ANTHROPIC_API_KEY") or os.getenv("CLAUDE_API_KEY")

    if not openai_key and not claude_key:
        return "Error: No API key found. Set OPENAI_API_KEY or ANTHROPIC_API_KEY/CLAUDE_API_KEY in the environment."

    prompt = f"""
Answer the question based only on the provided context.

Context:
{context}

Question:
{query}
"""

    if openai_key:
        try:
            from openai import OpenAI as OpenAIClient

            client = OpenAIClient(api_key=openai_key)
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"OpenAI error: {str(e)}"

    try:
        from anthropic import Anthropic
    except Exception:
        return "Error: Anthropic client not installed. Install the 'anthropic' package or set OPENAI_API_KEY."

    try:
        client = Anthropic(api_key=claude_key)
        resp = client.completions.create(
            model="claude-2.1",
            prompt=prompt,
            max_tokens_to_sample=1000,
        )
        if isinstance(resp, dict):
            return resp.get("completion") or resp.get("text") or str(resp)
        return getattr(resp, "completion", None) or getattr(resp, "text", str(resp))
    except Exception as e:
        return f"Claude error: {str(e)}"
