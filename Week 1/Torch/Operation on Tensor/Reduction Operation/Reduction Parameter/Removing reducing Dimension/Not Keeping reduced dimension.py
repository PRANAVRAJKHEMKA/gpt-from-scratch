import torch

data=[[1,2,3,4],[5,6,7,8]]

t=torch.tensor(data)
s=t.sum(dim=0,keepdim=False)
print(s,s.shape)