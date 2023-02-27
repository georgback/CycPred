# CycPred
Tensorflow model for the prediction of cyclizability of provided DNA sequences of length 50

Usage:

python CycPred.py inputfile outputfile

Inputfile must be sequences of length 50 bp, seperated by newlines

Outputfile is a text file with newline seperated predicted cyclizability values for each sequence

optional arguments
--numpy : stores result in npy binary file instead of textfile
-n --threads : give number of threads. Default is all available threads



required packages:
python >=3.9
Tensorflow version 2.6.0

installation guide:

1. install conda (miniconda is advised)
2. create new environment either using the command

      - conda create -n my_env tensorflow=2.6.0 scikit-learn python>3.9
      
      - or
            
      - conda env create -f CycPred.yml

