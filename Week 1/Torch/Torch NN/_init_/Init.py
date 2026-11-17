import torch
import torch.nn as nn

class studentmodel(nn.Module):
    def __init__(self):
        super().__init__()
        print("Model Created")

model=studentmodel()