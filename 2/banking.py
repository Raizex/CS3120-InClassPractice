import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('banking.csv')

marital_data = pd.DataFrame()

for status in data['marital'].unique():
    marital = data.loc[data['marital']==status]['y'].value_counts()
    marital_data[status] = marital

print(marital_data,'\n')

frequencies = marital_data.iloc[1] / (marital_data.iloc[0] + marital_data.iloc[1])
marital_frequencies = pd.DataFrame(frequencies, columns=['1'])
marital_frequencies['0'] = 1 - marital_frequencies['1']

print(marital_frequencies)

marital_frequencies.plot.bar(stacked=True)
marital_data.T.plot.bar(stacked=True)