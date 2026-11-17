
import torch
import torch.nn as nn


class StudentModel(nn.Module):

    def __init__(self):
        super().__init__()

        # 1. Department embedding
        # 4 departments, 3 values per department
        self.department_embedding = nn.Embedding(4, 3)

        # 2. Linear layers
        # 4 numerical + 3 embedding = 7 input features
        self.layer1 = nn.Linear(7, 3)
        self.layer2 = nn.Linear(3, 2)

    def forward(self, numerical_data, department):

        # Step 1: Retrieve department embedding
        department_vector = self.department_embedding(department)

        print("Numerical data:", numerical_data)
        print("Department index:", department)
        print("Department vector:", department_vector)

        # Step 2: Combine both types of data
        combined = torch.cat(
            (numerical_data, department_vector),
            dim=-1
        )

        print("Combined data:", combined)
        print("Combined shape:", combined.shape)

        # Step 3: Pass through Linear layers
        x = self.layer1(combined)
        x = self.layer2(x)

        return x


# Create model
model = StudentModel()

# Student information
numerical_data = torch.tensor([6., 85., 80., 75.])
department = torch.tensor(0)

# Give data to the model
output = model(numerical_data, department)

print("\nFinal output:", output)
print("Final output shape:", output.shape)
