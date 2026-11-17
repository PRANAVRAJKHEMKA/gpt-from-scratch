import torch

data1=[[1,2,3,4],[5,6,7,8]]

data2=[[10,20,30,40]]

t1=torch.tensor(data1)

t2=torch.tensor(data2)

print("tensor one shape",t1.shape)
print("tensor second shape",t2.shape)
print(t1+t2)