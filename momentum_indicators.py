import pandas as py
import pandas_ta as ta
import plotly.graph_objects as go

historical_data = py.read_csv("./data/BRENT.CMDUSD_Candlestick_4_Hour_ASK_01.01.2019-16.03.2024.csv",header=0)
df = historical_data.tail(500)
df["RSI_10"] = ta.rsi(df.Close,length=10)
print(df.to_string())
fig = go.Figure(data=[
    go.Candlestick(x=df['Local time'],
                   open = df['Open'],
                   high = df['High'],
                   low = df['Low'],
                   close = df['Close']),
                   go.Scatter(x=df.index,y=df["RSI_10"],name='RSI',yaxis='y2')

])
fig.show()
