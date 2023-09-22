# CycPred
Tensorflow model for the prediction of cyclizability of provided DNA sequences of length 50

# Usage:

```
python CycPred.py inputfile outputfile
```

+ Inputfile must be DNA sequences consisting of only A,T,G or C of length 50 or more, seperated by newline; If fasta file is given, the --fasta flag has to be added

+ Outputfile is a text file with newline seperated predicted cyclizability values for each sequence

optional arguments

+ --numpy : stores result in npy binary file instead of textfile
+ -n --threads : give number of threads. Default is all available threads
+ --fasta : input file is treated as a fasta file

When execucted, the program performs cyclizability prediction on both the sequence and its reverse complement and reports the average value.

# Installation guide:


required packages:
+ python <=3.9
+ Tensorflow version 2.6.0
+ scikit-learn

## Using CycPred as a script :

0. ``` git clone https://github.com/georgback/CycPred ```
1. install conda (miniconda is advised)
2. configure conda (optional):

      + ``` conda config --add channels conda-forge ```
      
      +  ``` conda config --set channel_priority strict ```
      
3. create new environment either using the command
 
      +  ``` conda env create -f CycPred.yml ```

           
      or
     
     
     +  ``` conda create -n my_env tensorflow=2.6.0 scikit-learn python=3.9 ```


To test the program we provide an example file, Yeast_chromosome_V.csv.

Example execution
```
python CycPred.py Yeast_chromosome_V.csv result.txt
```

# Installation as a package

Guide to install cycpred as a package. We advise to do so in a virtual environment. 

## With conda
We advise to install this package with conda, due to easier handeling of the evnironment

0. ``` git clone https://github.com/georgback/CycPred ```
1. Install conda (miniconda is advised)
2. Create new virtual environment with conda, installing the correct python version and pip
 
      +  ```
         conda create -n cycpred python=3.9 pip
         conda activate cycpred
         ```
3. Install package
   +  ``` pip install -e . ```
  
## With pip
This works if your current python version is 3.9 or lower.

0. ``` git clone https://github.com/georgback/CycPred ```
1. Create new virtual environment 
 
      +  ```
         python -m venv env
         source env/bin/activate cycpred
         ```
2. Install package
   +  ``` pip install -e . ```
  

To test if installed into the correct bin/ you can try
   + ``` cycpred --help ```

Example execution
```
cycpred Yeast_chromosome_V.csv result.txt
```


The environment can be deacitvated with :
```deactivate```
and reactivated (in the correct directory) with:
```source env/bin/activate cycpred```



There is also a [colab notebook](https://colab.research.google.com/drive/1ng2dKkaZobSYHPWGgZKz4SFIS1peZfWh?usp=sharing) available.

## Architecture of the model:


![Architecture_more_info](https://user-images.githubusercontent.com/75431641/233105485-0bdf9e56-67f5-45ff-8b1b-612fe36d1cea.png)
![Architecture_more_info](https://github.com/georgback/CycPred/assets/75431641/4967e858-cbf2-472a-9489-683d966a72d7)

