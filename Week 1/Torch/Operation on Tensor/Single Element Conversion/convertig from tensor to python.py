import torch

data=[1,2,3,4,5]

t=torch.tensor(data)

sum=t.sum()
print("Before conversation")
print(sum,type(sum))

convert=sum.item()

print("after conversion")

print(convert,type(convert))