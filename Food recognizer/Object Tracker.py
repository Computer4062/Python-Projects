import torch
import torch.nn as nn
import torchvision
import matplotlib.pyplot as plt
import numpy as np
import os

device = torch.device('cpu')

num_epochs = 15
batch_size = 10
learning_rate = 0.005

print('Food101 training with raw data')
print('importing data files')

transforms = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5)),
    torchvision.transforms.RandomHorizontalFlip(),
    torchvision.transforms.RandomCrop(size = 32)
])


train = torchvision.datasets.Food101('./data', download = True, split = 'train', transform = transforms)
test = torchvision.datasets.Food101('./data', download = True, transform = transforms)
train_dl = torch.utils.data.DataLoader(train, shuffle = True, batch_size = batch_size)

def accuracy(net, data):
    images, labels = next(iter(data))

    with torch.no_grad(): prediction = net(images)

    predicted = torch.argmax(prediction, 1)
    num_correct = torch.sum(predicted == labels)
    acc = (num_correct * 0.1) / len(data)

    return acc.item()

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        self.conv1 = nn.Conv2d(3, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.pool = nn.MaxPool2d(2, stride = 2)
        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 101)

    def forward(self, x):
        x = nn.functional.relu(self.conv1(x))
        x = self.pool(x)
        x = nn.functional.relu(self.conv2(x))
        x = self.pool(x)

        x = x.reshape(-1, 16 * 5 * 5)
        x = nn.functional.relu(self.fc1(x))
        x = torch.log_softmax(self.fc2(x), dim = 1)

        return x

net = Net().to(device)
loss = nn.NLLLoss()
optimizer = torch.optim.SGD(net.parameters(), lr = 0.005)

load = input('do you already have a model loaded: (y/n): ').lower()

if load == 'n':
    print('Training starts')
    net.train()
    for epoch in range(2):
        epoch_loss = 0
        for (id, data) in enumerate(train_dl):
            images, labels = data

            optimizer.zero_grad()

            prediction = net(images)
            loss_value = loss(prediction, labels)
            epoch_loss += loss_value.item()

            loss_value.backward()
            optimizer.step()

        net.eval()
        acc = accuracy(net, train)
        print(f'epoch: {epoch + 1}, loss = {epoch_loss}, accuracy: {acc}')
        net.train()

        print('saving model')

        name = input("Enter the name of the model to be saved: ")
        torch.save(net.state_dict(), name)

else:
    if os.path.exists('cnn.pth'):
        net = Net().to(device)
        net.load_state_dict(torch.load('cnn.pth'))

print("Computing model accuracy: ")

net.eval()
acc = accuracy(net, test)
print(f'accuracy: {acc}')

print('testing images in the data set')

correct = 0
state = ['bad', 'not okay', 'okay', 'good', 'excellent']

for i in range(5):
    images, items = next(iter(train_dl))
    img = images[0]
    img_np = img.numpy()  # 3,32,32
    img_np = np.transpose(img_np, (1, 2, 0))
    plt.imshow(img_np)

    temp = []
    labels = []

    file = open('data.txt', 'r')
    temp.append(file.readlines())
    file.close()

    for i in temp:
        for k in i:
            labels.append(k)

    img.reshape(1, 3, 32, 32)

    with torch.no_grad(): prediction = net(img)

    predicted = torch.argmax(prediction)

    if items[0].item() == predicted.item():
        correct += 1
        print(f"\n test correct")
    else:
        if items[0].item() != predicted.item():
            print(f"\n test wrong, predicted {labels[predicted.item()]}")

    plt.show()

print(f'state of the nueral network is {state[correct]}')










