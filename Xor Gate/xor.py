import torch
import numpy as np
import torch.nn as nn

data_x = np.array([[1,1],[0,0],[1,0],[0,1]])
data_y = np.array([[1,0,0,0]]).T

data_x = torch.autograd.Variable(torch.FloatTensor(data_x))
data_y = torch.autograd.Variable(torch.FloatTensor(data_y))

input_dimension = 2
output_dimension = 1
epochs = 15000
learning_rate = 0.005

class XorDetector(nn.Module):
    def __init__(self, input_size, output_size):
        super(XorDetector, self).__init__()
        self.l1 = nn.Linear(input_size, output_size)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        out = self.sigmoid(x)
        return self.l1(out)

model = XorDetector(input_dimension, output_dimension)
criteria = nn.BCEWithLogitsLoss()
optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)

for epoch in range(epochs):
    optimizer.zero_grad()
    predict = model(data_x)
    loss = criteria(predict, data_y)
    loss.backward()
    optimizer.step()

    if (epoch + 1) % (epochs / 5) == 0:
        print(f"Epoch: {epoch + 1}, Training Loss: {loss.item()} ")

def prediction(a,b):
    array = np.array([[a,b]])
    array = torch.autograd.Variable(torch.FloatTensor(array))
    return array

a = int(input("Enter a number here: "))
b = int(input("Enter a number here: "))

array = prediction(a,b)

for x in array:
    prediction = model(x)
    print(f"input: {list(map(int, x))}, prediction: {int(prediction > 1)}")



