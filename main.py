from matplotlib import pylab as plt
import pandas as pd

pd.plotting.register_matplotlib_converters()

df1 = pd.read_csv("AAPL.csv")
print(df1.head())
df1['Date'] = pd.to_datetime(df1.Date)
print(df1.head())

df2 = pd.read_csv("Samsung.KS.csv")
print(df2)
df2['Date'] = pd.to_datetime(df2.Date)

index2 = []
for date2 in df2.Date:
    if df1.index[df1.Date == date2].values.size:
        index2.append(int(df1.index[df1.Date == date2].values[0]))
print(index2)

plt.figure("Samsung")
plt.plot(df1["Date"], df1["Close"], 'r-', linewidth=0.6, label="APPL")
plt.plot(df2["Date"], df2["Close"], 'b-', linewidth=0.6, label="Samsung")
plt.xlabel("Dates")
plt.legend(loc="upper left")

plt.show()
