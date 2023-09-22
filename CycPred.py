#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
import sys


from cycpred.cycpred_functions import cycpred_commandline




def main():
    model=tf.keras.models.load_model(os.path.join(sys.path[0],"model"),compile=False)
    cycpred_commandline(model)

if __name__ == "__main__":
    main()
