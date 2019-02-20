import pandas as pd
import matplotlib.pyplot as plt
from fbprophet import Prophet

df = pd.read_csv('~/Pulpit/prophet/examples/example_yosemite_temps.csv')

m = Prophet()
m.fit(df)

future = m.make_future_dataframe(periods=365)
# future.tail()     - wyswietla 5 ostatnich wartości

forecast = m.predict(future)

fig = m.plot(forecast)

plt.show()
