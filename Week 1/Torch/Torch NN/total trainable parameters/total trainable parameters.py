
import torch
import torch.nn as nn

# Student model
class StudentModel(nn.Module):

    def __init__(self):
        super().__init__()

        self.department_embedding = nn.Embedding(4, 3)
        self.layer1 = nn.Linear(7, 3)
        self.layer2 = nn.Linear(3, 2)

    def forward(self, numerical_data, department):

        department_vector = self.department_embedding(department)

        combined = torch.cat(
            (numerical_data, department_vector),
            dim=0
        )

        x = self.layer1(combined)
        x = self.layer2(x)

        return x


# Create model
model = StudentModel()

# Count parameters
total = 0

print("PARAMETER DETAILS")
print("-------------------------")

for name, parameter in model.named_parameters():

    count = parameter.numel()

    print(name)
    print("Shape:", parameter.shape)
    print("Parameters:", count)
    print()

    total += count

print("-------------------------")
print("Total trainable parameters:", total)
