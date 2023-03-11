import torch
import torchvision
import torch.nn as nn

transforms = torchvision.transforms.Compose([
    torchvision.transforms.ToTensor(),
    torchvision.transforms.Normalize((0.3, 0.3, 0.3), (0.3, 0.3, 0.3))
])


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


def accuracy(net, data):
    images, labels = next(iter(data))

    with torch.no_grad(): prediction = net(images)

    predicted = torch.argmax(prediction, dim=1)
    num_correct = torch.sum(predicted == labels)
    accuracy = (num_correct * 1.0) // len(data)
    return accuracy.item()


def main():
    print('Image comparer model loader')
    print('5000 training images and 1000 testing images of raw data')

    first_train = torchvision.datasets.CIFAR10('./first/data', train=True, download=True, transform=transforms)
    second_train = torchvision.datasets.CIFAR10('./second/data', train=True, download=True, transform=transforms)
    first_test = torchvision.datasets.CIFAR10('./first/data', train=False, download=True, transform=transforms)
    second_test = torchvision.datasets.CIFAR10('./second/data', train=False, download=True, transform=transforms)

    first_train_dl = torch.utils.data.DataLoader(first_train, batch_size=10, shuffle=True, num_workers=2)

    devicename = input('Enter the name of the device: ')

    device = torch.device(devicename)

    epochs = int(input('Enter the amount of epochs you want: '))
    lr = float(input('Enter the learning rate of the nueral network: '))

    net = Net().to(device)

    optimizer = torch.optim.SGD(net.parameters(), lr=lr)
    criteria = nn.NLLLoss()

    print('Training starts')

    net.train()

    for epoch in range(epochs):
        train_loss = 0
        print("[", end = "")
        for (id, data) in enumerate(first_train_dl):
            images, labels = data

            optimizer.zero_grad()

            prediction = net(images)
            loss = criteria(prediction, labels)
            train_loss += loss.item()

            loss.backward()
            optimizer.step()

            if id % 100 == 0:
                print(">", end = "")

        print("]")
        acc = accuracy(net, first_train)
        print(f'\n epoch: {epoch + 1}, loss: {train_loss}, accuracy: {acc}')

    print('computing model accuracy')

    acc = accuracy(net, first_test)
    print(f'Accuracy of the model is: {acc}')

    print('saving model')

    path = input('Enter the name of model you want to save: ')
    torch.save(net.state_dict(), path)

if __name__ == '__main__':
    main()
