import torch

data=[[1,2,3],[4,5,6]]

t=torch.tensor(data)

print("Original tensor \n \n",t,"\n \n")

t.sub_(5)

print("after subtractig , tensor \n \n",t,"\n \n")