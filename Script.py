Question 11

import numpy as np
from scipy import stats

x1=stats.norm.interval(0.96,200,30)
x2=stats.norm.interval(0.94,200,30)
x3=stats.norm.interval(0.98,200,30) 


Question 20

import numpy as np
import pandas as pd
from scipy.stats import norm
df = pd.read_csv("/Users/saibodavula/Downloads/Cars.csv")

x1=(1-stats.norm.cdf(38,loc=(np.mean(df["MPG"])),scale=(np.std(df["MPG"]))))

x1

x2=(stats.norm.cdf(40,loc=(np.mean(df["MPG"])),scale=(np.std(df["MPG"]))))

x2 

x3 = ((stats.norm.cdf(50,loc=(np.mean(df["MPG"])),scale=(np.std(df["MPG"])))-stats.norm.cdf(20,loc=(np.mean(df["MPG"])),scale=(np.std(df["MPG"])))))
x3

Question 21 

import numpy as np
from scipy.stats import shapiro
import pandas as pd

df = pd.read_csv("/Users/saibodavula/Downloads/Cars.csv")

df["AT"].hist()

df["Waist"].hist()

x1=df["Waist"]

shapiro(x1)

x2=df["AT"]

shapiro(x2)

x3=df["MPG"]
shapiro(x3)



Question 22

stats.norm.ppf(0.60) 


Question 23 

stats.t.ppf(0.99,25-1)


Question 24

import pandas as pd
import numpy as np

sample_mean = 260
pop_mean = 270
sample_std = 90
sample_size = 18

t = (sample_mean - pop_mean) / (sample_std / np.sqrt(sample_size))
  # degrees of freedom
p = 1 - stats.t.cdf(t, sample_size-1)

print("The probability that 18 randomly selected bulbs would have an average life of no more than 260 days if the CEO's claim were true is:", p)

