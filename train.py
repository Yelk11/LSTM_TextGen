# Small LSTM Network to Generate Text for Alice in Wonderland
import os
import sys
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import LSTM
from tensorflow.keras.callbacks import ModelCheckpoint
from tensorflow.keras.utils import to_categorical
import pandas as pd



# Load data
df = pd.read_csv("E:\\datasets\\bible_corpus\\t_asv.csv", usecols = ['text'])
df['text'] = df['text'].str.lower()

print(df['text'])


raw_text = ""
for x in df['text']:
    raw_text += x

print(raw_text)
# create mapping of unique chars to integers
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
# summarize the loaded data
n_chars = len(raw_text)
n_vocab = len(chars)
print("Total Characters: ", n_chars)
print("Total Vocab: ", n_vocab)
# prepare the dataset of input to output pairs encoded as integers
seq_length = 100
dataX = []
dataY = []
for i in range(0, n_chars - seq_length, 1):
	seq_in = raw_text[i:i + seq_length]
	seq_out = raw_text[i + seq_length]
	dataX.append([char_to_int[char] for char in seq_in])
	dataY.append(char_to_int[seq_out])
n_patterns = len(dataX)
print("Total Patterns: ", n_patterns)
# reshape X to be [samples, time steps, features]
X = np.reshape(dataX, (n_patterns, seq_length, 1))
# normalize
X = X / float(n_vocab)
# one hot encode the output variable
y = to_categorical(dataY)
# define the LSTM model

def build_model(hp):
    model = keras.Sequential()
    model.add(LSTM(256, input_shape=(X.shape[1], X.shape[2])))
    model.add(
        layers.Dense(
            # Define the hyperparameter.
            units=hp.Int("units", min_value=32, max_value=512, step=32),
            activation="relu",
        )
    )
    model.add(layers.Dense(10, activation="softmax"))
    model.compile(
        optimizer="adam", loss="categorical_crossentropy", metrics=["accuracy"],
    )
    return model

# define the checkpoint
filepath="weights-improvement-{epoch:02d}.hdf5"
checkpoint = ModelCheckpoint(filepath, monitor='loss', verbose=1, save_best_only=True, mode='min')
callbacks_list = [checkpoint]
# fit the model
model.fit(X, y, epochs=50, batch_size=256, callbacks=callbacks_list)

# # load the network weights
# filename = "weights-improvement-20.hdf5"
# model.load_weights(filename)
# model.compile(loss='categorical_crossentropy', optimizer='adam')
# int_to_char = dict((i, c) for i, c in enumerate(chars))
# # pick a random seed
# start = np.random.randint(0, len(dataX)-1)
# pattern = dataX[start]
# print("Seed:")
# print("\"", ''.join([int_to_char[value] for value in pattern]), "\"")
# # generate characters
# for i in range(1000):
# 	x = np.reshape(pattern, (1, len(pattern), 1))
# 	x = x / float(n_vocab)
# 	prediction = model.predict(x, verbose=0)
# 	index = np.argmax(prediction)
# 	result = int_to_char[index]
# 	seq_in = [int_to_char[value] for value in pattern]
# 	sys.stdout.write(result)
# 	pattern.append(index)
# 	pattern = pattern[1:len(pattern)]
# print("\nDone.")