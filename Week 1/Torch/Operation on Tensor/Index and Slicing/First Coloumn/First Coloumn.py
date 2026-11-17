import torch

data=[[1,2,3,4],[5,6,7,8]]

t=torch.tensor(data)

print(t)

print("first coloumn")

print(t[:,0])