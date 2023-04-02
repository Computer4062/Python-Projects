import torch
import json
import utils
from training import states
import random

def getWord():
    file = open('messages.txt', 'r')
    message = file.readline()
    file.close()

    file = open('messages.txt', 'w')
    file.write(' ')
    file.close()

    return message

def sendWord(word):
    file = open('reply.txt', 'w')
    file.write(word)
    file.close()

intents = json.load(open('intents.json', 'r'))
data = states()

input_size = data[0]
hidden_size = data[1]
output_size = data[2]
device = data[6]
all_words = data[3]
tags = data[4]

model_state = data[5]
NeuralNet = utils.NueralNetwork(input_size, hidden_size,output_size).to(device)
NeuralNet.load_state_dict(model_state)
NeuralNet.eval()

while True:
    sentence = getWord()

    if(sentence == 'exit'):
        sendWord('okay bye')
        break

    sentence = utils.tokenize(sentence)
    words = utils.bag_of_words(sentence, all_words)
    words = words.reshape(1, words.shape[0])
    words = torch.from_numpy(words).to(device)

    output = NeuralNet(words)
    predicted = torch.argmax(output, 1)

    tag = tags[predicted.item()]

    for intent in intents['intents']:
        if tag == intent['tag']:
            responses = intent['responses']
            sendWord(random.choice(responses))








