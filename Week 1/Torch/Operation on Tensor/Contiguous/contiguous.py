import torch

data=[[1,2,3],[4,5,6]]

t=torch.tensor(data)

print(t.is_contiguous())

t1=t.T

print(t1.is_contiguous())

t1=t1.contiguous()

print(t1.is_contiguous())
