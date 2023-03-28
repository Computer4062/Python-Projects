import random
import json
import torch
from model import NeuralNet
from dataset import bag_of_words, tokenizer, states

intents = json.load(open('intents.json', 'r'))

FILE = 'starbotmodel.pth'
data = torch.load(FILE)

state = states()

input_size = state[0]
hidden_size = state[1]
output_size = state[2]
all_words = state[3]
tags = state[4]
model_state = state[5]
device = state[6]

model = NeuralNet(input_size, hidden_size, output_size).to(device)
model.load_state_dict(model_state)
model.eval()

print('\nLets chat (type exit to exit)')
print('StarBot')

while True:
    sentence = input(">>")
    if sentence == 'exit':
        break

    sentence = tokenizer(sentence)
    words = bag_of_words(sentence, all_words)
    words = words.reshape(1, words.shape[0])
    words = torch.from_numpy(words).to(device)

    output = model(words)
    predicted = torch.argmax(output)

    tag = tags[predicted.item()]

    for intent in intents['intents']:
        if tag == intent['tag']:
            responses = intent['responses']
            print(f'starbot >> {random.choice(responses)}')















