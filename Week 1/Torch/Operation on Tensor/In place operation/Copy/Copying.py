import torch

data1=[[1,2,3],[4,5,6]]

data2=[[10,20,30],[40,50,60]]

t1=torch.tensor(data1)

t2=torch.tensor(data2)

print("Original tensor \n \n",t1,"\n ",t2,"\n")

t1.copy_(t2)

print("after Copying , tensor \n \n",t1,"\n ",t2,"\n")