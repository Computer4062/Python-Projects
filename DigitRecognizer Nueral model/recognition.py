import torch
import torchvision
import matplotlib.pyplot as plt
import torch.nn as nn
import time

transforms = torchvision.transforms.Compose([torchvision.transforms.ToTensor(), torchvision.transforms.Normalize((0.5, ),(0.5, ))])

trainset = torchvision.datasets.MNIST("./train", download=True, train = True, transform = transforms)
valueset = torchvision.datasets.MNIST("./test", download = True, train = False, transform = transforms)
train_dl = torch.utils.data.DataLoader(trainset, batch_size = 64, shuffle = True)
test_dl = torch.utils.data.DataLoader(valueset, batch_size = 64, shuffle = True)

input_size = 784
hidden_sizes = [128, 64]
output_size = 10

model = nn.Sequential(nn.Linear(input_size, hidden_sizes[0]),
                      nn.ReLU(),
                      nn.Linear(hidden_sizes[0], hidden_sizes[1]),
                      nn.ReLU(),
                      nn.Linear(hidden_sizes[1], output_size),
                      nn.LogSoftmax(dim=1))

criteria = nn.NLLLoss()
images, labels = next(iter(train_dl))
images = images.view(images.shape[0], -1)

predictions = model(images)
optimizer = torch.optim.SGD(model.parameters(), lr = 0.003, momentum = 0.9)

epochs = 5
time0 = time.time()

for epoch in range(epochs):
    for images, labels in train_dl:
        optimizer.zero_grad()
        images = images.view(images.shape[0], -1)

        predictions = model(images)

        loss = criteria(predictions, labels)
        loss.backward()
        optimizer.step()

        print(f"epoch: {epoch}, training loss: {loss.item()}")

print(f"training time was done in {(time.time() - time0) / 60} minutes")

images, labels = next(iter(test_dl))
img = images[0].view(1, 784)

with torch.no_grad(): predictions = model(img)

ps = torch.exp(predictions)
probability = list(ps.numpy()[0])

print("predicted digit = ", probability.index(max(probability)))

plt.imshow(images[0].numpy().squeeze(), cmap='gray_r')
plt.show()














