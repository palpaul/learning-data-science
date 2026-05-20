""" pdfReader is a class that reads a PDF file and extracts the text from it.
 It uses the pypdf library to read the PDF file and extract the text.
   The extract_text method takes a file path as input and returns the extracted text as a string. """

import os

from pypdf import PdfReader
from dotenv import load_dotenv
load_dotenv()

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

from openai import OpenAI

# Generate response using OpenAI
def generate_response(query, context):
    #hard code api key here for testing purpose, you can load it from environment variable or you can directly pass the api key here
    #  openai_client = OpenAI(api_key="")
    # load the api key from environment variable or you can directly pass the api key here
    api_key = os.getenv("OPENAI_API_KEY")  # make sure to set the OPENAI_API_KEY environment variable with your OpenAI API key  
    print("API Key:", api_key)  # Debugging line to check if the API key is loaded correctly
    if not api_key:
        return "Error: OpenAI API key not found. Please set the OPENAI_API_KEY environment variable."
    openai_client = OpenAI(api_key=api_key)

    prompt = f"""
Answer the question based only on the provided context.

Context:
{context}

Question:
{query}
"""

    try:

        response = openai_client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        final_answer = response.choices[0].message.content

        return final_answer

    except Exception as e:
        return f"Error: {str(e)}"
