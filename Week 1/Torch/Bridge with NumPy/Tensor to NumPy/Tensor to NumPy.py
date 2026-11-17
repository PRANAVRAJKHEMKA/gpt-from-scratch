import torch

data=[[1,2,3],[4,5,6]]

t=torch.tensor(data)

print("Tensor \n \n")

print(t , type(t))

print("after converting from tensor to numpy \n \n ")

n=t.numpy()

print(n,type(n))