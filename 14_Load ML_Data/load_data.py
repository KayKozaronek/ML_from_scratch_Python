# 4 Methods of loading data

# 1. PURE PYTHON METHOD WITH CSV (USUALLY SLOWER 
#  -> NOT RECOMMENDED)
import csv 
import numpy as np

FILE_NAME = "./spambase.data"

with open(FILE_NAME, "r") as f:
    data = list(csv.reader(f, delimiter= ","))

data = np.array(data)

print(data.shape)
n_samples, n_features = data.shape
n_features -= 1 
X = data[:,0:n_features]
y = data[:, n_features]
print(X.shape, y.shape)

# 2. Numpy 1
data = np.loadtxt(FILE_NAME, delimiter=",")
print(data.shape)

# 3. Numpy 2 (Here we can deal with missing data)
# Has more options than first method
data = np.genfromtxt(FILE_NAME, delimiter=",", 
                    dtype = np.float32, skip_header= 0, 
                    missing_values = "", # Specify values to ignore
                    filling_values = 9999) 
print(data.shape)

# 4. Pandas (Even more powerful, more options and faster)
import pandas as pd 

df = pd.read_csv(FILE_NAME, delimiter=",", header=None, 
                dtype = np.float32, 
                #skip_rows = 0,
                na_values=[""]) #Tells pandas which values to ignore

# df = df.fillna(9999)

data = df.to_numpy()

data.shape
