import torch
import numpy as np

data=[[9,8],[6,5]]

t_data=torch.tensor(data)

print(t_data)

t_rand=torch.rand_like(t_data,dtype=float)

print(t_rand)