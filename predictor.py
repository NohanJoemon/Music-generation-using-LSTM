from generate import gen_sequence,convert_to_midi

def predict(gen_seq_length,wpath,path_char_to_index,writepath):
    while True:
        try:
            seq = gen_sequence(gen_seq_length,wpath,path_char_to_index)
            print(seq)
            convert_to_midi(seq,writepath)
            return 
        except:
            continue

