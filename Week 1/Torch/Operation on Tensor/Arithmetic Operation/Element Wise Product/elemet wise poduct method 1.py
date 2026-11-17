import torch

data1=[[1,2,3,4],[5,6,7,8]]
data2=[[65,34,32,64],[12,13,14,17]]
t1=torch.tensor(data1)
t2=torch.tensor(data2)
print("original Tensor \n")
print(t1)
print(t2)
y1=t1*t2
print("Element Wise Product")
print(y1)