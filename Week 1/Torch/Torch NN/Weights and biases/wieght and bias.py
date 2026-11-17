import torch
import torch.nn as nn

class studentmodel(nn.Module):
    def __init__(self):
        super().__init__()
        print("Model Created")
        self.layer1=nn.Linear(4,3)
        self.layer2=nn.Linear(3,2)


    def forward(self , x):
        print("input recieved",x)
        x=self.layer1(x)
        x=self.layer2(x)
        return x


model=studentmodel()

studentdata = torch.tensor([6., 85., 80., 75.])
output=model(studentdata)
print("output",output,output.shape)

print("Layer 1 weights:")
print(model.layer1.weight)

print("Layer 1 bias:")
print(model.layer1.bias)

print("Layer 2 weights:")
print(model.layer2.weight)

print("Layer 2 bias:")
print(model.layer2.bias)

total = sum(p.numel() for p in model.parameters())

print("Total parameters:", total)