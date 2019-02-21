import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('banking.csv')

marital_data = pd.DataFrame()

for status in data['marital'].unique():
    marital = data.loc[data['marital']==status]['y'].value_counts()
    marital_data[status] = marital

print(marital_data)

frequencies = marital_data.iloc[1] / (marital_data.iloc[0] + marital_data.iloc[1])
marital_frequencies = pd.DataFrame(frequencies, columns=['f']).T

print(marital_frequencies)