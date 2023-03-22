import torch
import torchvision
import pandas as pd
import skimage
import os
import torch.nn as nn

class DataLoader(torch.utils.data.Dataset):
    def __init__(self, csv_file, root_dir, transform = None):
        self.annotations = pd.read_csv(csv_file)
        self.root_dir = root_dir
        self.transform = transform

    def __len__(self):
        return len(self.annotations)

    def __getitem__(self, index):
        img_path = os.path.join(self.root_dir, self.annotations.iloc[index, 0])
        image = skimage.io.imread(img_path)
        y_label = torch.tensor(int(self.annotations.iloc[index, 1]))

        if self.transform:
            image = self.transform(image)

        return (image, y_label)

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()

        self.conv1 = nn.Conv2d(1, 6, 5)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.pool = nn.MaxPool2d(2, 2)

        self.l1 = nn.Linear(16 * 5 * 5, 120)
        self.l2 = nn.Linear(120, 84)
        self.l3 = nn.Linear(84, 2)

    def forward(self, x):
        x = nn.functional.relu(self.conv1(x))
        x = self.pool(x)
        x = nn.functional.relu(self.conv2(x))
        x = self.pool(x)

        x = x.reshape(-1, 16 * 5 * 5)

        x = nn.functional.relu(self.l1(x))
        x = nn.functional.relu(self.l2(x))
        x = torch.log_softmax(self.l3(x), 1)

        return x

def text():
    print('=======================================================')
    print('            FACE COMPARER MODEL DOWNLOAD               ')
    print('    creates an AI model that compares faces using a    ')
    print('                   pre built model                     ')
    print('   run python Compare.py in the terminal or use a      ')
    print('     or use a code editor to use the AI after          ')
    print('                 running this programme                ')
    print('=======================================================')

def accuracy(net, data):
    images, labels = next(iter(data))
    with torch.no_grad(): predictions = net(images)

    predicted = torch.argmax(predictions, 1)
    num_correct = torch.sum(predicted)
    accuracy = (1.0 * num_correct) / len(data)

    return accuracy

def main():
    text()

    learning_rate = 1e-3

    print('Creating and training of a comparer model begins here')
    print('Loading dataset')

    transform = torchvision.transforms.Compose([
        torchvision.transforms.ToTensor(),
        torchvision.transforms.Resize((32, 32))
    ])

    dataset = DataLoader(csv_file = 'labels.csv', root_dir = 'img', transform = transform)

    train = torch.utils.data.DataLoader(dataset, batch_size = 32, shuffle = True)
    test = torch.utils.data.DataLoader(dataset, batch_size = 32, shuffle = True)

    devicename = input('Enter the name of the device you want to use(cpu, cuda): ')
    epochs = int(input('Enter the amount of epochs you want to run: '))

    device = torch.device(devicename)

    net = Net().to(device)
    criteria = nn.NLLLoss()
    optimizer = torch.optim.SGD(net.parameters(), lr = learning_rate)

    count = 0

    for epoch in range(epochs):
        net.train()
        train_loss = 0

        if count == 0:
            print('[', end = '')
            count = 1

        for (id, data) in enumerate(train):
            images, labels = data
            optimizer.zero_grad()

            prediction = net(images)
            loss = criteria(prediction, labels)
            train_loss += loss.item()

            loss.backward()
            optimizer.step()

        if epoch % 25 == 0: print('>', end = '')

        if epoch % 1000 == 0:
            print(']')
            net.eval()
            acc = accuracy(net, train)
            print(f'epoch: {epoch} | loss: {train_loss} | accuracy: {acc} ')
            count = 0

    print('\n Computing model accuracy: ')
    print('---------------------------')
    acc = accuracy(net, test)
    print(f'The model has an accuracy of {acc} ')

    print('\n Saving model')
    print('-------------')

    modelname = input("Give the name for the model you trained: ")

    torch.save(net.state_dict(), modelname)

if __name__ == '__main__':
    main()













