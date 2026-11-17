import torch

t=torch.arange(24).reshape(2,3,4)

p=t.permute(2,0,1)

print(t,t.shape)
print(p,p.shape)