from fastapi import FastAPI
from fastapi import File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from rag import collection

app = FastAPI() # create an instance of the FastAPI class

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)
from fastapi.middleware.cors import CORSMiddleware

import shutil # shutil is used to save the uploaded file to a specific location
from rag import (
    generate_response, read_pdf,
      chunk_text, 
      create_embed_chunks,
        store_in_chromadb,
          search_query,
          collection
)

@app.get("/")
def home():
    return {"message": "Welcome to the RAG API"}

# pdp upload endpoint
@app.post("/upload_pdf/")
def upload_pdf(file: UploadFile = File(...)):
#save uploaded file to a specific location
    pdf_path = f"../uploads/{file.filename}"
    with open(pdf_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)
    # read the pdf file and extract the text
    text = read_pdf(pdf_path)
    # chunk the text into smaller pieces
    chunks = chunk_text(text)
    # create embeddings for each chunk
    embeddings = create_embed_chunks(chunks)

    # store the embeddings in chromadb
    store_in_chromadb(chunks,embeddings)

    return {"message": "PDF uploaded and processed successfully",
            "file_name": file.filename,
            "total_chunks": len(chunks)
            }


# Ask question endpoint
@app.post("/ask_question/")
def ask_question(query: str):
    # search for the relevant chunks based on the user query
    results = search_query(query)
    documents = results['documents'][0] # this will return the original text of the chunks that are relevant to the user query. We will use this context to generate a response using the OpenAI API. The reason we are using the original text of the chunks is because we want to generate a response based on the original text of the chunks and not based on the embeddings of the chunks. The embeddings are used to find the relevant chunks based on the user query but we want to generate a response based on the original text of the chunks.   
    context = " ".join(documents) # join the relevant chunks to create a context for the OpenAI API to generate a response. We are joining the relevant chunks with a newline character to create a context that is easy for the OpenAI API to understand. The OpenAI API will use this context to generate a response based on the user query. The reason we are using a newline character to join the relevant chunks is because it will help the OpenAI API to understand that these are separate pieces of information and not just one long piece of text. This will help the OpenAI API to generate a more accurate response based on the user query.
    # generate a response using the OpenAI API
    response = generate_response(query, context)
    return {
        "query": query,
        "response": response
        }

# view chromadb collection endpoint
@app.get("/view_data/")
def view_data():
    data = collection.get(
        include=["documents", "embeddings", "ids"]
    )
    return {
        "total_chunks": len(data['documents']),
        "documents": data['documents']

    }