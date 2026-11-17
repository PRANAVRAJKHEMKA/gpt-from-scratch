import torch

data1=[[1,2,3,4],[5,6,7,8]]
data2=[[65,34,32,64],[12,13,14,17]]
t1=torch.tensor(data1)
t2=torch.tensor(data2)
print("original Tensor \n")
print(t1)
print(t2)
y1 = torch.rand_like(t1, dtype=torch.float32)
print("Element Wise Product")
torch.mul(t1,t2,out=y1)
print(y1)