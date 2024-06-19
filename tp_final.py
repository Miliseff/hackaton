
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
import seaborn as sns    
from scipy.stats import shapiro
import pylab

import statsmodels.api as sm
from statsmodels.compat import lzip
import statsmodels.stats.api as smf
from statsmodels.stats.stattools import durbin_watson
from scipy.stats import shapiro

from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.metrics import mean_squared_error
import pandas as pd
import chardet

#File2='https://api.worldbank.org/v2/es/indicator/SM.POP.NETM?downloadformat=excel'
File='migrations.xls'

df_data = pd.read_excel(File)


#print(df_data.head())

#print(df_data.isnull().sum())

df_data=df_data.dropna(axis=0)


#df_data_2 = df_data[df_data.isnull().any(axis=1)]

#print(df_data.iloc[0])
#df = df.drop ('city', axis = 1)

#anios=['1960','1961','1962','1963','1962']

#df_data=df_data.drop(anios, axis = 1)

indices = range(2,44)
df_data  = df_data.drop(df_data.columns[indices], axis=1)
#print(df_data.head())


sns.histplot(df_data['2003'], bins=15, kde=True)
plt.show()
