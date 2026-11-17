#Flattening images before fully connected layers.

#Preparing batches of training data.

#Changing dimensions between neural network layers.

#Organizing sequence and feature dimensions.

import torch

t1=torch.arange(24).reshape(2,12)

print("oiginal tensor \n \n" , t1 ,'\n \n')

t2=t1.reshape(4,6)

print("reshaped  tensor \n \n" , t2 ,'\n \n')