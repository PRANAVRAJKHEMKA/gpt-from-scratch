import torch
import torch.nn as nn

class studentmodel(nn.Module):
    def __init__(self):
        super().__init__()
        print("Model Created")
    def forward(self , x):
        print("input recieved",x)
        return x


model=studentmodel()

studentdata = torch.tensor([6., 85., 80., 75.])
output=model(studentdata)
print("output",output)