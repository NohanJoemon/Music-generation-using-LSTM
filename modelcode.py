from keras.models import Sequential
from keras.layers import LSTM, Dropout, TimeDistributed, Dense, Activation, Embedding
from keras.callbacks import ModelCheckpoint
from keras.utils import *

def make_model(num_unique_chars):
    model = Sequential()
    
    model.add(Embedding(input_dim = num_unique_chars, output_dim = 512, batch_input_shape = (1, 1))) 
  

    model.add(LSTM(256, return_sequences = True, stateful = True))
    model.add(Dropout(0.2))
    
    model.add(LSTM(256, return_sequences = True, stateful = True))
    model.add(Dropout(0.2))
    
    model.add(LSTM(256,return_sequences=True, stateful = True)) 
    model.add(Dropout(0.2))
    
    model.add((Dense(num_unique_chars)))
    model.add(Activation("softmax"))
    
    return model