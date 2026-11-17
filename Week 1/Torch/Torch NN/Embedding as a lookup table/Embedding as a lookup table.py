
import torch
import torch.nn as nn

# Create an embedding table:
# 4 departments, 3 values per department
embedding = nn.Embedding(4, 3)

# Ten students, each represented by one department index
departments = torch.tensor([
    0, 1, 0, 2, 1,
    0, 2, 3, 0, 3
])

# Retrieve embedding vectors for all ten students
output = embedding(departments)

# Display shapes
print("Embedding table:")
print(embedding.weight)
print("Table shape:", embedding.weight.shape)

print("\nDepartment indices:")
print(departments)
print("Input shape:", departments.shape)

print("\nEmbedding output:")
print(output)
print("Output shape:", output.shape)
