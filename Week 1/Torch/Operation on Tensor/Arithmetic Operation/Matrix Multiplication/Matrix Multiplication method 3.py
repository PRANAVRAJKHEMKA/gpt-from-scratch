import torch

data1 = [[1,2,3,4],
         [5,6,7,8]]

t1 = torch.tensor(data1)

print("Original Tensor \n")
print(t1)

print("\nTranspose Tensor \n")
print(t1.T)

print("\nMatrix Multiplication between original and its transpose Tensor \n")

y1 = torch.empty((2,2), dtype=t1.dtype)

torch.matmul(t1, t1.T, out=y1)

print(y1)