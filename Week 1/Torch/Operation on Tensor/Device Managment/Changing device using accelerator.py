import torch

data=[[1,2,3,4],[5,6,7,8]]

t=torch.tensor(data)

print("before",t.device)

print(torch.accelerator.is_available())

if torch.accelerator.is_available():
    t=t.to(torch.accelerator.current_accelerator())

print("after",t.device)