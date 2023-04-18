import torch
import torchvision
import matplotlib.pyplot as plt
import numpy as np
import torch.nn as nn

transforms = torchvision.transforms.Compose([torchvision.transforms.ToTensor(), torchvision.transforms.Normalize((0.3,0.3,0.3), (0.3,0.3,0.3))])
device = torch.device('cpu')

class Net(nn.Module):
    def __init__(self):
        super(Net, self).__init__()
        self.conv1 = nn.Conv2d(3, 6, 5) # in out kernalsize stride = 1
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.pool = nn.MaxPool2d(2, stride = 2)
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
        x = torch.log_softmax(self.fc3(x), dim = 1)
        return x

def accuracy(model, ds):
    images, labels = next(iter(ds))

    with torch.no_grad():
        prediction = model(images)

    predicted = torch.argmax(prediction, dim = 1)
    num_correct = torch.sum(labels == predicted)
    accuracy = (num_correct * 1.0) / len(ds)
    return accuracy.item()

def main():
    print("\n Begin Cifar 10 with raw data CNN demo")
    np.random.seed(1)
    torch.manual_seed(1)

    print("\n loading 5000 train and 1000 test images")

    train_ds = torchvision.datasets.CIFAR10('./data', download=True, train=True, transform=transforms)
    test_ds = torchvision.datasets.CIFAR10('./data', download=True, train=True, transform=transforms)
    train_dl = torch.utils.data.DataLoader(train_ds, batch_size=10, shuffle=True, num_workers=2)
    test_dl = torch.utils.data.DataLoader(test_ds, batch_size=10, shuffle=True, num_workers=2)

    batch_size = 10
    #train_dl = torch.utils.data.DataLoader(train_ds, batch_size = batch_size, shuffle = True)

    print("\n Creating CNN with 2 conv and 400 - 120 - 84 - 10 layers")
    net = Net().to(device)

    max_epochs = 20
    ep_log_interval = 5
    lr = 0.005

    loss = nn.NLLLoss()
    optimizer = torch.optim.SGD(net.parameters(), lr = lr)

    print(f"\n batch_size = {batch_size}")
    print(f"loss = {str(loss)}")
    print(f"optimizer = {optimizer}")
    print(f"max_epochs = {max_epochs}")
    print(f"learning rate = {lr}")

    print("\n Starting Training")

    net.train()

    for epoch in range(max_epochs):
        epoch_loss = 0
        for (id, data) in enumerate(train_dl):

            image, label = data

            optimizer.zero_grad()
            prediction = net(image)

            loss_value = loss(prediction, label)
            epoch_loss += loss_value.item()

            loss_value.backward()
            optimizer.step()

        #if epoch % ep_log_interval == 0:
        print(f"epoch = {epoch + 1} loss = {epoch_loss}", end = "")
        net.eval()
        acc = accuracy(net, train_ds)
        net.train()
        print(f" acc = {acc}")

    print("End training")

    #evaluation

    print("\n Computing model accuracy")
    net.eval()
    acc_test = accuracy(net, test_ds)
    print(f"Accurecy on test data = {acc_test}")

    print("\n saving model")

    torch.save(net.state_dict(), "./cnn.pth")

    #making predictions

    print("\n Prediction for test image[29]")

    images, label = next(iter(train_dl))
    img = images[0]
    img_np = img.numpy()  # 3,32,32
    img_np = np.transpose(img_np, (1, 2, 0))
    plt.imshow(img_np)
    plt.show()

    labels = ['plane', 'car', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']

    img = img.reshape(1, 3, 32, 32) #make it a batch

    with torch.no_grad():
        prediction = net(img)

    predicted = torch.argmax(prediction)
    print(predicted)
    print(predicted.item())
    print(labels[predicted.item()])

    if predicted.item() == label[0].item(): print("Correct")
    else: print("wrong")

    print("\n End CIFAR-10 CNN demo")

if __name__ == "__main__":
    main()

















