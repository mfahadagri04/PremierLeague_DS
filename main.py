import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression

# Creating the dataframe
df = pd.read_csv("matches.csv")

# see the first 5 datas
print(df.head())

# See the last 5 datas
print(df.tail())

# Check the datasets information
print(df.info())

# Describe the dataset
print(df.describe())
print(df.describe().T)

# Checking for empty datas
print(df.isna().sum())
print(df.isnull().sum())