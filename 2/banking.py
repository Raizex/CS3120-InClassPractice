import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('banking.csv')
married = data.loc[data['marital'] == 'married'].loc[:, ['marital','y']]
single = data.loc[data['marital'] == 'single'].loc[:, ['marital','y']]
print(married)
print(single)