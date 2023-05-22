import pandas as pd
from dsw_methodpy import dsw_method

import numpy as np
from scipy.interpolate import pchip_interpolate
from scipy.stats import gaussian_kde
import pandas as pd
import matplotlib.pyplot as plt

# File name
df = pd.read_csv('Example Raman Spectra.csv')  # Read the CSV file

# Get the input values for Xi and Yi (0-indexed)
xi: int = 0  # Replace with your desired value
yi: int = 10  # Replace with your desired value

# Input spectra
X = df.iloc[:, xi].values
Y = df.iloc[:, yi].values

X, Ybc, SNR = dsw_method(X, Y, 25, True)


