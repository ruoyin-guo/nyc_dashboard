import pandas as pd
import numpy as np


trimpath = "D:\McGill\COMP598\hw4\submission_template\data\\trim_data.csv"
newdatapath = "D:\McGill\COMP598\hw4\submission_template\data\\new_data.csv"
df0 = pd.read_csv(trimpath, usecols=[1, 2, 8, 19], names=[
                  'Created Date', 'Closed Date', 'Incident Zip', 'Status'])
df0 = df0[df0['Status'] == "Closed"]

# drop NA
df0.dropna(inplace=True)

# add column of response hours,
df0['Month'] = df0['Closed Date'].str.slice(0, 2)

df0['Created Date'] = pd.to_datetime(
    df0['Created Date'], format='%m/%d/%Y %I:%M:%S %p')
df0['Closed Date'] = pd.to_datetime(
    df0['Closed Date'], format='%m/%d/%Y %I:%M:%S %p')
df0['Diff'] = (df0['Closed Date']-df0['Created Date']) / np.timedelta64(1, 'h')

df0.drop(['Created Date', 'Closed Date', 'Status'], axis=1, inplace=True)

# remove negative duration
df0 = df0[df0['Diff'] >= 0]

# save processed data in 'dataclean.csv'
df0.to_csv(newdatapath, index=False)
