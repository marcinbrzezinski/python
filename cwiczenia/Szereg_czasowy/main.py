import pandas as pd
from dateutil import parser
import matplotlib.pyplot as plt

df = pd.read_csv('~/Pulpit/prophet/examples/example_yosemite_temps.csv')

df['Date'] = df['ds'].apply(lambda x: parser.parse(x).month)

data = df.groupby(['Date'])['y'].agg('mean')        # mean - średnia

ax = data.plot(color='blue')

plt.show()


print(data)
