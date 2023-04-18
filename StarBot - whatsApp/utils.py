import numpy as np
import torch
import torch.nn as nn
import nltk

class NueralNetwork(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(NueralNetwork, self).__init__()
        self.l1 = nn.Linear(input_size, hidden_size)
        self.l2 = nn.Linear(hidden_size, hidden_size)
        self.l3 = nn.Linear(hidden_size, output_size)

    def forward(self, x):
        x = nn.functional.relu(self.l1(x))
        x = nn.functional.relu(self.l2(x))
        x = torch.log_softmax(self.l3(x), 1)

        return x

class Dataset(torch.utils.data.Dataset):
    def __init__(self, data, targets):
        self.n_samples = len(data)
        self.data_samples = data
        self.target_samples = targets

    def __getitem__(self, index):
        return self.data_samples[index], self.target_samples[index]

    def __len__(self):
        return self.n_samples

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stem(word):
    return nltk.stem.porter.PorterStemmer().stem(word.lower())

def bag_of_words(tokenize_sentence, all_words):
    tokenize_sentence = [stem(w) for w in tokenize_sentence]
    bag = np.zeros(len(all_words), np.float32)

    for idx, word in enumerate(all_words):
        if word in tokenize_sentence:
            bag[idx] = 1.0

    return bag

