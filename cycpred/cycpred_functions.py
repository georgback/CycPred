#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 22 10:48:21 2023

@author: back1622
"""


import numpy as np
import tensorflow as tf
from tensorflow.keras.utils import to_categorical
from keras.preprocessing import sequence
import sys
import os
import argparse
import pkg_resources

def pred_with_comp(model,array,batch_size=512,complement=[2,3,0,1]):
    pred=model.predict(sequence.pad_sequences(array,50),batch_size=batch_size).reshape(len(array))
    rev_pred=model.predict(sequence.pad_sequences(array[:,:,complement][:,::-1]),batch_size=batch_size).reshape(len(array))
    return((pred+rev_pred)/2)


def read_fasta(txt):
    
    #basi fasta read in
    seqs = []
    tmp_line=""
    with open(txt,'r') as f:
        for line in f:
            if line[0]==">":
                if tmp_line =="":
                    continue
                else:
                    seqs.append(tmp_line)
                    tmp_line=""
            else:
                tmp_line = tmp_line+line.strip()
        #adding last line to list
        seqs.append(tmp_line)
    return(seqs)


def cycpred_commandline(model):
    parser = argparse.ArgumentParser(description='anaylyze all memefiles in a directory')
    parser.add_argument("input", help="sequence file with sequences of length 50bp or longer")
    parser.add_argument("output", help="outputfile for predictions")
    parser.add_argument("--fasta",help="input file is in fasta format",action="store_true")
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


    #read in fasta if specified
    if args.fasta:
        seqs = np.array(read_fasta(args.input))
        
    else:
        
        seqs = np.array(open(args.input,'r').read().splitlines())


    split = np.array([len(x)-49 for x in seqs])

    if np.any(split<1):
        sys.exit("Some sequences shorter than 50. Sequences need to be at least 50bp in length.")





    #integer encoding
    #replacement character of 99,
    seqs = [np.array([alphabet.setdefault(y,99) for y in t.upper()]) for t in seqs]

     
    #find all sequences longer than 50 and create windows size 50 for those sequences
    if np.any(split>1):
        seqs = np.array([x[y:y+50] for x in seqs for y in range(len(x)-49)])  
    else:
        seqs = np.array(seqs)
    try:
        seqs = to_categorical(seqs,num_classes=4)
    except:
        sys.exit("Encoding failed. Most likely reason is the occurrence of a character except A T G C ")

    #model=tf.keras.models.load_model(os.path.join(sys.path[0],"CycPred"),compile=False)
    predictions=pred_with_comp(model,seqs)
    if np.any(split>1):
        counter = 0
        temp_res = []
        for x in split:
            temp_res.append(predictions[counter:counter+x])
            counter+=x
        predictions=np.array(temp_res,dtype=object)
        if args.numpy:
            np.save(args.output,predictions)
        else:
            #np.savetxt(args.output,predictions)
            with open(args.output,"w") as f:
                for x in predictions:
                    f.writelines("\t".join([str(val) for val in x])+"\n")
    else:       
        if args.numpy:
            np.save(args.output,predictions)
        else:
            np.savetxt(args.output,predictions)

    print("Outputfile was written")

                
        
