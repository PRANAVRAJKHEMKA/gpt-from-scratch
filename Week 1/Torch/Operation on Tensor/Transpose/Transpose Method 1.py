import torch

data=[[1,2,3],[4,5,6]]

t=torch.tensor(data)

print("oiginal tensor")
print(t)

print("tranpose tensor")
print(t.T)