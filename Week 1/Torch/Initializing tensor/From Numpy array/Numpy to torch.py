import torch
import numpy as np

data = [[5,6],[9, 4]]
x_data = torch.tensor(data)
np_array=np.array(data)

print(np_array)

t=torch.from_numpy(np_array)
print(t)