````md
# RAG (Retrieval-Augmented Generation) Complete Explanation

# What is RAG?

RAG stands for:

- Retrieval
- Augmented
- Generation

RAG is a technique where:
1. Documents are stored in a vector database
2. Relevant information is retrieved when a user asks a question
3. That information is provided to an LLM (Large Language Model)
4. The LLM generates an accurate answer

---

# Why Use RAG?

Without RAG:
- LLM only knows trained data
- Cannot access private PDFs/documents
- May hallucinate answers

With RAG:
- LLM can answer using your custom data
- More accurate responses
- No need to retrain the model

---

# Complete RAG Flow

```text
PDF
 ↓
Extract Text
 ↓
Chunk Text
 ↓
Create Embeddings
 ↓
Store in Vector Database
 ↓
User Question
 ↓
Convert Question to Embedding
 ↓
Similarity Search
 ↓
Retrieve Relevant Chunks
 ↓
Send Context to LLM
 ↓
Generate Final Answer
```

---

# Your RAG Code

```python
"""
PdfReader is a class that reads a PDF file and extracts the text from it.
It uses the pypdf library to read the PDF file and extract the text.
"""

from pypdf import PdfReader

"""
SentenceTransformer is a class that uses the sentence-transformers
library to create embeddings for the extracted text.
"""

from sentence_transformers import SentenceTransformer

# Used to connect to vector database and store embeddings
import chromadb

# Used to generate responses from OpenAI
from openai import OpenAI

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Create vector database collection
client = chromadb.Client()
collection = client.create_collection(name="pdf_data")

# Read PDF and extract text
def read_pdf(file_path):
    reader = PdfReader(file_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text()

    return text


# Chunk text into smaller pieces
def chunk_text(text, chunk_size=500):

    chunks = []

    for i in range(0, len(text), chunk_size):

        chunk = text[i:i+chunk_size]

        chunks.append(chunk)

    return chunks


# Generate embeddings and store them
def embed_chunks(chunks):

    for chunk in chunks:

        embedding = model.encode(chunk)

        collection.add(
            embeddings=[embedding.tolist()],
            documents=[chunk],
            ids=[str(uuid.uuid4())]
        )
```

---

# Step-by-Step Explanation

---

# 1. Import PDF Reader

```python
from pypdf import PdfReader
```

## Purpose

Used to:
- Open PDF files
- Read pages
- Extract text content

---

# 2. Import SentenceTransformer

```python
from sentence_transformers import SentenceTransformer
```

## Purpose

Used to:
- Convert text into embeddings (vectors)

---

# What is an Embedding?

Embedding means converting text into numerical vectors.

Example:

```text
"Dog"    → [0.12, 0.88, 0.45]
"Puppy"  → [0.11, 0.87, 0.40]
"Car"    → [0.92, 0.15, 0.31]
```

Notice:
- Dog and Puppy vectors are similar
- Car vector is different

This helps AI understand semantic meaning.

---

# Why Do We Need Embeddings?

Traditional search:

```python
"car" == "vehicle" ❌
```

Embedding search:

```python
"car" ≈ "vehicle" ✅
```

This is called:

# Semantic Search

The system understands meaning instead of exact words.

---

# 3. Import ChromaDB

```python
import chromadb
```

## Purpose

ChromaDB is a:

# Vector Database

It stores:
- embeddings
- document chunks
- metadata

And performs:
- similarity search

---

# 4. Import OpenAI

```python
from openai import OpenAI
```

## Purpose

Used later to:
- generate answers from retrieved chunks

---

# 5. Load Embedding Model

```python
model = SentenceTransformer('all-MiniLM-L6-v2')
```

## Purpose

Loads a pretrained embedding model.

This model converts text into vectors.

---

# Why This Model?

`all-MiniLM-L6-v2` is:
- lightweight
- fast
- accurate for semantic search
- commonly used in RAG systems

---

# 6. Create ChromaDB Collection

```python
client = chromadb.Client()
collection = client.create_collection(name="pdf_data")
```

## Purpose

Creates a collection/table in vector DB.

Example structure:

| ID | Embedding | Text |
|---|---|---|
| 1 | [0.11,0.22...] | Java supports OOP |

---

# 7. Read PDF Function

```python
def read_pdf(file_path):
```

## Purpose

Reads PDF and extracts all text.

---

## Full Explanation

```python
reader = PdfReader(file_path)
```

Opens the PDF.

---

```python
text = ""
```

Stores extracted text.

---

```python
for page in reader.pages:
```

Loops through every page.

---

```python
text += page.extract_text()
```

Extracts text from each page.

---

```python
return text
```

Returns complete PDF text.

---

# 8. Chunking Function

```python
def chunk_text(text, chunk_size=500):
```

## Purpose

Splits large text into smaller chunks.

---

# Why Chunking is Important?

Bad approach:

```text
Entire PDF → one embedding ❌
```

Good approach:

```text
Split into smaller chunks ✅
```

Benefits:
- better retrieval
- lower memory usage
- more accurate search
- better LLM responses

---

# Chunking Logic

```python
for i in range(0, len(text), chunk_size):
```

Moves in steps of 500 characters.

Example:

```text
0-500
500-1000
1000-1500
```

---

```python
chunk = text[i:i+chunk_size]
```

Creates one chunk.

---

```python
chunks.append(chunk)
```

Adds chunk to list.

---

```python
return chunks
```

Returns all chunks.

Example:

```python
[
  "Java is...",
  "Spring Boot is...",
  "Microservices are..."
]
```

---

# 9. Embedding Function

```python
def embed_chunks(chunks):
```

## Purpose

Creates embeddings for every chunk.

---

```python
for chunk in chunks:
```

Loops through all chunks.

---

```python
embedding = model.encode(chunk)
```

Most important step.

Converts text into vector.

Example:

```text
"Java supports multithreading"

↓

[0.12, 0.55, 0.88, ...]
```

---

# Why Vectors?

Vectors allow mathematical comparison.

The system can calculate:
- cosine similarity
- vector distance

to find similar meanings.

---

# 10. Store Embeddings in ChromaDB

```python
collection.add(
    embeddings=[embedding.tolist()],
    documents=[chunk],
    ids=[str(uuid.uuid4())]
)
```

## Purpose

Stores:
- embedding vector
- original text chunk
- unique ID

---

# What Gets Stored?

| ID | Embedding | Document |
|---|---|---|
| abc123 | [0.12,0.44...] | Java supports OOP |

---

# How Retrieval Works Later

When user asks:

```text
"What is multithreading?"
```

System does:

1. Convert question into embedding
2. Compare with stored embeddings
3. Find most similar chunks
4. Send those chunks to LLM

---

# Query Embedding Example

```python
query_embedding = model.encode(user_query)
```

---

# Similarity Search Example

```python
results = collection.query(
    query_embeddings=[query_embedding.tolist()],
    n_results=3
)
```

---

# Example Retrieval

Retrieved chunks:

```text
"Java supports multithreading..."
```

```text
"Threads are lightweight processes..."
```

---

# Final Prompt to LLM

```python
prompt = f"""
Answer the question using the context below.

Context:
{retrieved_chunks}

Question:
{user_query}
"""
```

---

# Final Architecture

```text
                ┌─────────────┐
                │    PDF      │
                └──────┬──────┘
                       │
                       ▼
              ┌────────────────┐
              │ Extract Text   │
              └──────┬─────────┘
                     │
                     ▼
              ┌────────────────┐
              │ Chunk Text     │
              └──────┬─────────┘
                     │
                     ▼
              ┌────────────────┐
              │ Create Vector  │
              │ Embeddings     │
              └──────┬─────────┘
                     │
                     ▼
              ┌────────────────┐
              │ Store in       │
              │ ChromaDB       │
              └──────┬─────────┘
                     │
                     ▼
              ┌────────────────┐
              │ User Question  │
              └──────┬─────────┘
                     │
                     ▼
              ┌────────────────┐
              │ Query          │
              │ Embedding      │
              └──────┬─────────┘
                     │
                     ▼
              ┌────────────────┐
              │ Similarity     │
              │ Search         │
              └──────┬─────────┘
                     │
                     ▼
              ┌────────────────┐
              │ Retrieve       │
              │ Relevant Data  │
              └──────┬─────────┘
                     │
                     ▼
              ┌────────────────┐
              │ Send to LLM    │
              └──────┬─────────┘
                     │
                     ▼
              ┌────────────────┐
              │ Final Answer   │
              └────────────────┘
```

---

# Important Improvements

## Better Chunking

Instead of character-based chunking:
- token-based chunking
- sentence-based chunking
- overlapping chunks

Example:

```python
chunk_size = 500
overlap = 100
```

Why overlap?
Because context may split between chunks.

---

# Better Production Stack

| Component | Recommended |
|---|---|
| PDF Parser | PyMuPDF |
| Chunking | LangChain TextSplitter |
| Embedding Model | BAAI/bge-small-en |
| Vector DB | ChromaDB / Pinecone |
| LLM | GPT-4 / Llama |
| Retrieval | Cosine Similarity |

---

# Simple Real-Life Analogy

| RAG Component | Real-Life Example |
|---|---|
| PDF | Book |
| Embedding | Meaning fingerprint |
| Vector DB | Smart library |
| Retrieval | Finding relevant pages |
| LLM | Teacher explaining answer |

---

# Key Understanding

Embeddings do NOT store exact words.

They store:
# Semantic Meaning

That is why:

```text
car
vehicle
automobile
```

can match together.

---

# Final Summary

Your current system:

```text
PDF
 ↓
Extract Text
 ↓
Chunk Text
 ↓
Generate Embeddings
 ↓
Store in ChromaDB
```

Future complete RAG:

```text
User Question
 ↓
Convert to Embedding
 ↓
Similarity Search
 ↓
Retrieve Chunks
 ↓
Send Context to LLM
 ↓
Generate Answer
```
````
