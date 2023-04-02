import json
from utils import tokenize, stem, bag_of_words, NueralNetwork, Dataset
import numpy as np
import torch
import torch.nn as nn

intents = json.load(open('intents.json', 'r'))

all_words = []
tags = []
word_list = []

for intent in intents['intents']:
    tag = intent['tag']
    tags.append(tag)

    for pattern in intent['patterns']:
        w = tokenize(pattern)
        all_words.extend(w)
        word_list.append((w, tag))

ignore_words = ['?', '!', '.' ,',']
all_words = [stem(w) for w in all_words if w not in ignore_words]

all_words = sorted(set(all_words))
tag = sorted(set(tags))

samples = []
targets = []

for (pattern_sentence, tag) in word_list:
    bag = bag_of_words(pattern_sentence, all_words)
    samples.append(bag)

    label = tags.index(tag)
    targets.append(label)

samples = np.array(samples)
targets = np.array(targets)

batch_size = 8
hidden_size = 8
output_size = len(tags)
input_size = len(samples[0])
learning_rate = 0.01
num_epochs = 100

dataset = Dataset(samples, targets)
train_loader = torch.utils.data.DataLoader(dataset, batch_size = 10, shuffle = True, num_workers = 0)

device = torch.device('cpu')
model = NueralNetwork(input_size, hidden_size, output_size).to(device)

criteria = nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr = learning_rate)

def accuracy(model, dataset):
    samples, targets = next(iter(dataset))

    with torch.no_grad():
        outputs = model(samples)

    output = torch.argmax(outputs, 1)
    correct = torch.sum(output == targets)
    accuracy = (correct * 1.0) / len(dataset)

    return accuracy.item()

for epoch in range(num_epochs):
    for (sample, target) in train_loader:
        samples = sample.to(device)
        targets = target.to(dtype = torch.long).to(device)

        optimizer.zero_grad()

        outputs = model(samples)
        loss = criteria(outputs, targets)

        loss.backward()
        optimizer.step()

    if (epoch + 1) % 100 == 0:
        acc = accuracy(model, train_loader)
        print(f'| Epoch: [{epoch + 1} / {num_epochs}] | Loss: {loss.item():.4f} | accuracy: {acc} |')

print(f'final loss {loss.item():.4f}')
acc = accuracy(model, train_loader)
print(f'final accuracy {acc}')

torch.save(model.state_dict(), 'starbotmodel.pth')

def states():
    model_state = model.state_dict()
    return [input_size, hidden_size, output_size,  all_words, tags, model_state, device]