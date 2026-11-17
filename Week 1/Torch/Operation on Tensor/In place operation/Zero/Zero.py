import torch

data=[[1,2,3],[4,5,6]]

t=torch.tensor(data)

print("Original tensor \n \n",t,"\n \n")

t.zero_()

print("after making all elements zero , tensor \n \n",t,"\n \n")