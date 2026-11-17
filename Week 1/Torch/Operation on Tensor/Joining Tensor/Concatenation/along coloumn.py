import torch

data1=[[1,2,3,4],[5,6,7,8]]

t1=torch.tensor(data1)

data2=[[12,13,15,16],[66,25,44,78]]

t2=torch.tensor(data2)

t3=torch.cat((t1,t2),dim=1)  # dim can also be -1
print(t3)