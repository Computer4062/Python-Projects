import torch
import torchvision
import matplotlib.pyplot as plt
import numpy as np
import torch.nn as nn
import random
import warnings
import os
import time

warnings.filterwarnings("ignore")

transform = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize((0.5,0.5,0.5),(0.5,0.5,0.5))
])

def text():
    print('=======================================================')
    print('                    IMAGE COMPARER                     ')
    print('        compares images with the cifar 10 dataset      ')
    print('Download the model from the ModelCreator.py before using')
    print('                       the AI                          ')
    print('   run python ModelCreator.py in the terminal or use a ')
    print('          or use a code editor to run the file         ')
    print('=======================================================')

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        self.conv1 = nn.Conv2d(3, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.pool = nn.MaxPool2d(2, 2)

        self.fc1 = nn.Linear(16 * 5 * 5, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):
        x = nn.functional.relu(self.conv1(x))
        x = self.pool(x)
        x = nn.functional.relu(self.conv2(x))
        x = self.pool(x)

        x = x.reshape(-1, 16 * 5 * 5)
        x = nn.functional.relu(self.fc1(x))
        x = nn.functional.relu(self.fc2(x))
        x = torch.log_softmax(self.fc3(x), 1)

        return x


def main():
    text()

    test = torchvision.datasets.CIFAR10('./first/data', download = True, train = False, transform = transform)
    test_dl = torch.utils.data.DataLoader(test, batch_size = 10, shuffle = True, num_workers = 2)
    test2 = torchvision.datasets.CIFAR10('./second/data', download = True, train = False, transform = transform)
    test2_dl = torch.utils.data.DataLoader(test2, batch_size = 10, shuffle = True, num_workers = 2)

    found = True
    modelname = ''

    while found:
        modelname = input('Enter the location of the model you saved: ')
        if os.path.exists(modelname):
            found = False
        else:
            print('File was not found')

    devicename = input('Enter the name of the device you are using: ')

    net = Net().to(torch.device(devicename))
    net.load_state_dict(torch.load(modelname))

    image1, _ = next(iter(test_dl))
    image2, _ = next(iter(test2_dl))

    correct = 0

    epochs = int(input('Enter the amount of images you want to compare: '))

    for x in range(epochs):
        num1 = random.randint(0, 9)
        num2 = random.randint(0, 9)

        img1 = image1[num1]
        img2 = image2[num2]

        img_np = img1.numpy()
        img_np = np.transpose(img_np, (1, 2, 0))

        img_np2 = img2.numpy()
        img_np2 = np.transpose(img_np2, (1, 2, 0))

        plt.rcParams["figure.figsize"] = [7.00, 3.50]
        plt.rcParams["figure.autolayout"] = True
        data = np.random.rand(5, 5)
        plt.subplot(1, 2, 1)
        plt.imshow(img_np)
        plt.subplot(1, 2, 2)
        plt.imshow(img_np2)

        labels = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

        img1 = img1.reshape(1, 3, 32, 32)
        img2 = img2.reshape(1, 3, 32, 32)

        with torch.no_grad():
            prediction1 = net(img1)
            prediction2 = net(img2)

        predicted1 = torch.argmax(prediction1)
        predicted2 = torch.argmax(prediction2)

        print(f'item1 is a {labels[predicted1.item()]}, item2 is a {labels[predicted2.item()]}')

        if predicted2.item() == predicted1.item():
            print('Both items are the same \n')
            correct += 1
            plt.text(-20, 0.0005, 'Match found', {'color': 'C0', 'fontsize': 26})
        else:
            print('Both items are different \n')

        plt.show()
        plt.close()

    print(f'{correct} matches were found out of {epochs}')

if __name__ == '__main__':
    main()








