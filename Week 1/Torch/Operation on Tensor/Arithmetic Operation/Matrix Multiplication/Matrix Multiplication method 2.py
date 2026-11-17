import torch

data1=[[1,2,3,4],[5,6,7,8]]

t1=torch.tensor(data1)
print("original Tensor \n")
print(t1)
print("\nT ranpose Tensor \n")
print(t1.T)
print("\n Matrix Multiplication btween original and its transpose Tensor \n")
y1=t1.matmul(t1.T)
print(y1)