import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as pltdates
import datetime as dt
import wave

from main_functions import readFile, getData, plotGraph

currentfile = readFile("csv_files/AZ_LV_DO_mgL.csv")

clean = currentfile.loc[currentfile['flagID']!="Bad Data"]

clean.head(10)
clean.dtypes

clean = clean.drop_duplicates(subset=['dateTimeUTC'], keep='first')

plt.plot(clean['dateTimeUTC'], clean['value'])
plt.show()
