import pandas as pd
import matplotlib.pyplot as plt

def calculate_ema(data, N):
    alpha = 2 / (N + 1)
    ema = data.copy()
    ema.iloc[0] = data.iloc[0]

    for i in range(1, len(data)):
        ema.iloc[i] = alpha * data.iloc[i] + (1 - alpha) * ema.iloc[i - 1]
    return ema

def calculate_macd(data, short_window=12, long_window=26, signal_window=9):
    short_ema = calculate_ema(data['Zamkniecie'], short_window)
    long_ema = calculate_ema(data['Zamkniecie'], long_window)

    macd_line = short_ema - long_ema

    signal_line = calculate_ema(macd_line, signal_window)

    histogram = macd_line - signal_line

    return macd_line, signal_line, histogram

def analyze(start = None, end = None, last = None, plot=True):
    df = pd.read_csv('mak_d.csv')
    df['Data'] = pd.to_datetime(df['Data'])

    if start != None and end != None:
        df = df[(df['Data'] >= start) & (df['Data'] <= end)]

    if last != None:
        df = df.tail(last)
    macd, signal, _ = calculate_macd(df)

    if plot:
        _, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10), sharex=True)
        ax1.plot(df['Data'], df['Zamkniecie'], label='Cena przy zamknięciu');
        ax1.legend();
        ax2.plot(df['Data'], macd, label='MACD', color='black');
        ax2.plot(df['Data'], signal, label='Sygnał', color='red');
        ax2.legend();
        plt.show()
    return df, macd, signal



