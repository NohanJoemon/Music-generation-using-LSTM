from modelcode import make_model
import json
import numpy as np
from music21 import *
import os

def gen_sequence(gen_seq_length,wpath,path_char_to_index):
    
    with open(path_char_to_index) as f:
        char_to_index = json.load(f)
    index_to_char = {i:ch for ch, i in char_to_index.items()}
    num_unique_chars = len(index_to_char)
    
    model = make_model(num_unique_chars)
    model.load_weights(wpath)
     
    sequence_index = [char_to_index['Z']]

    for _ in range(gen_seq_length):
        num_dq=0
        batch = np.zeros((1, 1))
        batch[0, 0] = sequence_index[-1]
        
        predicted_probs = model.predict_on_batch(batch).ravel()
        sample = np.random.choice(range(num_unique_chars), size = 1, p = predicted_probs)
        sequence_index.append(sample[0])   
        if sample[0]=='"':
            num_dq+=1

    seq = ''.join(index_to_char[c] for c in sequence_index)
    seq='M:6/8\n'+str(seq)
    if num_dq%2==1:
        seq=str(seq)+str('"')
    return seq


def convert_to_midi(abc,writepath):
    c = converter.subConverters.ConverterABC()
    c.registerOutputExtensions = ("midi", )
    c.parseData(abc)
    s = c.stream
    s.write('midi', fp=writepath)
    