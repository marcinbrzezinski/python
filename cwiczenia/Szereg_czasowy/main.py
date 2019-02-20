import pandas as pd
from dateutil import parser
import matplotlib.pyplot as plt

df = pd.read_csv('~/Pulpit/prophet/examples/example_yosemite_temps.csv')

df['Datetime'] = pd.to_datetime(df['ds'], format = "%Y-%m-%d %H:%M:%S")
df['Day'] = df['Datetime'].apply(lambda x: x.day)

data = df.groupby(['Day'])['y'].agg('mean')


print(data)
