# Import required libraries
from transformers import AutoTokenizer, AutoModel
import torch

# Load tokenizer
# Tokenizer converts:
# Text -> Tokens -> Token IDs
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Load pre-trained BERT model
# Model converts Token IDs -> Embedding Vectors
model = AutoModel.from_pretrained("bert-base-uncased")

# Input texts
text1 = "I am learning Gen AI"
text2 = "Tokenization is Amazing!"

# =========================================================
# PROCESS TEXT 1
# =========================================================

# Convert text into tokens
tokens1 = tokenizer.tokenize(text1)

# Convert tokens into token IDs
tokens1_ids = tokenizer.convert_tokens_to_ids(tokens1)

# Print text, tokens and token IDs
print("============= TEXT 1 =============")
print("Original Text :", text1)

print("\nTokens :")
print(tokens1)

print("\nToken IDs :")
print(tokens1_ids)

# Convert full text into PyTorch tensor format
# return_tensors="pt" means PyTorch tensor
inputs1 = tokenizer(text1, return_tensors="pt")

# Disable gradient calculation
# because we are only testing/inferencing
with torch.no_grad():

    # Pass token IDs into BERT model
    outputs1 = model(**inputs1)

# Get embedding vectors
# last_hidden_state contains vector for every token
embeddings1 = outputs1.last_hidden_state

print("\nEmbedding Shape :")
print(embeddings1.shape)

# Print embeddings
print("\nEmbeddings :")
print(embeddings1)

# =========================================================
# PROCESS TEXT 2
# =========================================================

# Convert text into tokens
tokens2 = tokenizer.tokenize(text2)

# Convert tokens into token IDs
tokens2_ids = tokenizer.convert_tokens_to_ids(tokens2)

# Print text, tokens and token IDs
print("\n\n============= TEXT 2 =============")
print("Original Text :", text2)

print("\nTokens :")
print(tokens2)

print("\nToken IDs :")
print(tokens2_ids)

# Convert full text into tensor format
inputs2 = tokenizer(text2, return_tensors="pt")

# Disable gradient calculations
with torch.no_grad():

    # Generate embeddings
    outputs2 = model(**inputs2)

# Get embedding vectors
embeddings2 = outputs2.last_hidden_state

print("\nEmbedding Shape :")
print(embeddings2.shape)

# Print embeddings
print("\nEmbeddings :")
print(embeddings2)

# =========================================================
# UNDERSTANDING EMBEDDINGS
# =========================================================

# Example:
#
# Token:
# "learning"
#
# Might become vector like:
#
# [0.88, 0.22, -0.17, ....768 values]
#
# Each token gets its own vector.
#
# Shape Example:
# torch.Size([1, 7, 768])
#
# 1   -> batch size (1 sentence)
# 7   -> total tokens including [CLS] and [SEP]
# 768 -> embedding dimensions/features
#
# These vectors help AI understand semantic meaning mathematically.