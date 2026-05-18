# Import required libraries
from transformers import AutoTokenizer, AutoModel
import torch

# Load tokenizer
# Tokenizer converts text -> tokens -> token IDs
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Load pre-trained BERT model
# Model converts token IDs -> embeddings(vectors)
model = AutoModel.from_pretrained("bert-base-uncased")

# Input text
text = "I am learning Gen AI"

# Convert text into token IDs
# return_tensors="pt" means return PyTorch tensors
inputs = tokenizer(text, return_tensors="pt")

# Print token IDs
print("Token IDs:")
print(inputs["input_ids"])

# Convert token IDs back to readable tokens
tokens = tokenizer.convert_ids_to_tokens(inputs["input_ids"][0])

print("\nTokens:")
print(tokens)

# Disable gradient calculation
# (used during inference/testing for better performance)
with torch.no_grad():

    # Pass token IDs into BERT model
    outputs = model(**inputs)

# Get contextual embeddings
# last_hidden_state contains vector for each token
embeddings = outputs.last_hidden_state

# Print embedding tensor shape
print("\nEmbedding Shape:")
print(embeddings.shape)

# Shape explanation:
# [batch_size, number_of_tokens, embedding_dimension]
#
# Example:
# torch.Size([1, 7, 768])
#
# 1   -> one sentence
# 7   -> total tokens including [CLS] and [SEP]
# 768 -> vector size for each token

# Print embeddings
print("\nEmbeddings:")
print(embeddings)

# Example:
# Token:
# "learning"
#
# Might become vector like:
# [0.88, 0.22, -0.17, ....768 values]
#
# These numbers represent semantic meaning mathematically.