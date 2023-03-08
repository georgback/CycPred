#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from keras.preprocessing import sequence
#import multiprocessing
import sys
import os
import argparse

#parsing input arguments
parser = argparse.ArgumentParser(description='anaylyze all memefiles in a directory')
parser.add_argument("input", help="file with newline seperated sequences of length 50")
parser.add_argument("output", help="outputfile for predictions")
parser.add_argument("--numpy",help="stores result in a npy file instead of a text file",action="store_true")
parser.add_argument("-n","--threads", help="number of threads used. Applys to tensorflow and multiprocessing. Otherwise all available cores are used"
                    ,type=int)
args = parser.parse_args()

if args.threads:
    n_jobs = args.threads
    tf.config.threading.set_intra_op_parallelism_threads(n_jobs)
    tf.config.threading.set_inter_op_parallelism_threads(n_jobs)
else:
    n_jobs = os.cpu_count()



#preprocessing of seqences   
alphabet={"A":0,"G":1,"T":2,"C":3}


seqs = np.array(open(args.input,'r').read().splitlines())

#integer encoding
#default replacement of unkown character with A
seqs = np.array([np.array([alphabet.setdefault(y,0) for y in t]) for t in seqs])



one_hot = to_categorical(seqs)


#fwd and reverse prediction +returning the mean
def pred_with_comp(model,array,batch_size=512,complement=[2,3,0,1]):
    pred=model.predict(sequence.pad_sequences(array,50),batch_size=batch_size).reshape(len(array))
    rev_pred=model.predict(sequence.pad_sequences(array[:,:,complement][:,::-1]),batch_size=batch_size).reshape(len(array))
    return((pred+rev_pred)/2)

model=tf.keras.models.load_model(os.path.join(sys.path[0],"CycPred"),compile=False)

preds=pred_with_comp(model,one_hot)

if args.numpy:
    np.save(args.output,preds)
else:
    np.savetxt(args.output,preds)

