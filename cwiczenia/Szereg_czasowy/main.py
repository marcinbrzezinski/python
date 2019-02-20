import pandas as pd
from dateutil import parser
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv('~/Pulpit/prophet/examples/example_yosemite_temps.csv')

df['Datetime'] = pd.to_datetime(df['ds'], format="%Y-%m-%d %H:%M:%S")
df['Hour'] = df['Datetime'].apply(lambda x: x.hour)
df['Weekday'] = df['Datetime'].apply(lambda x: x.weekday())
df['Month'] = df['Datetime'].apply(lambda x: x.month)

data = df.groupby(['Hour', 'Month'])['y'].agg('mean').reset_index()

plt.imshow(np.array(pd.pivot_table(data, values='y',
                                   index='Month',
                                   columns='Hour').fillna(0)
                    ),
           cmap='coolwarm',
           label='Cout',
           interpolation='spline36',
           aspect='auto'
           )

# print(data)
plt.show()
