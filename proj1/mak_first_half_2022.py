import pandas as pd
import matplotlib.pyplot as plt

def calculate_eman(data, window):
    alpha = 2 / (window + 1)
    eman = data.copy()
    eman.iloc[0] = data.iloc[0]

    for i in range(1, len(data)):
        eman.iloc[i] = alpha * data.iloc[i] + (1 - alpha) * eman.iloc[i - 1]
    return eman

def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    short_ema = calculate_eman(data['Zamkniecie'], short_window)
    long_ema = calculate_eman(data['Zamkniecie'], long_window)

    macd_line = short_ema - long_ema

    signal_line = calculate_eman(macd_line, signal_window)

    histogram = macd_line - signal_line

    return macd_line, signal_line, histogram

df = pd.read_csv('mak_d.csv')
df['Data'] = pd.to_datetime(df['Data'])

start_date = '2022-01-01'
end_date = '2022-07-31'
df = df[(df['Data'] >= start_date) & (df['Data'] <= end_date)]

macd, signal, _ = calculate_macd(df)

closing_price_mean = df['Zamkniecie'].mean()

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 7), sharex=True)

ax1.plot(df['Data'], df['Zamkniecie'], label='Zamknięcie');
ax1.legend();
ax2.plot(df['Data'], macd, label='MACD', color='black');
ax2.plot(df['Data'], signal, label='Sygnał', color='red');
ax2.legend();
plt.show()



