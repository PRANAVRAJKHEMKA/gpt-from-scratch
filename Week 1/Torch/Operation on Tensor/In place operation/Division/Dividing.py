import torch

data=[[10,20,30],[40,50,60]]

t=torch.tensor(data,dtype=torch.float32)

print("Original tensor \n \n",t,"\n \n")

t.div_(5)

print("after Dividing , tensor \n \n",t,"\n \n")