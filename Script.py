Question 1 :

import pandas as pd
df = pd.read_excel("/Users/saibodavula/Downloads/company.xlsx")

df

df.boxplot(column=["Measure X"])
df["Measure X"].mean()
df["Measure X"].std()
df["Measure X"].var()


Question 4 : 

from scipy.stats import binom
bi=binom(5,0.005)

bi.pmf(1)

Question 5 : 

import numpy as np
x1=np.array([-2000,-1000,0,1000,2000,3000])

x1.mean()
x1.std()
