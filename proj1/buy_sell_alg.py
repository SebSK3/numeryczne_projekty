from enum import Enum
class Position(Enum):
    NONE = 0
    LONG = 1
    SHORT = -1

def buy_sell_alg(df, macd, signal, starting_money=1000):
    money = starting_money
    quantity = 0
    position = Position.NONE
    for i in range(1, len(df)):
        if macd.iloc[i] > signal.iloc[i] and macd.iloc[i - 1] <= signal.iloc[i - 1] and position != Position.LONG:
            # Kupno
            position = Position.LONG
            buy_price = df['Zamkniecie'].iloc[i]
            quantity = money / buy_price
            df.at[df.index[i], 'Kupno'] = buy_price
            money = 0
        elif macd.iloc[i] < signal.iloc[i] and macd.iloc[i - 1] >= signal.iloc[i - 1] and position != Position.SHORT:
            # Sprzedaż
            position = Position.SHORT
            sell_price = df['Zamkniecie'].iloc[i]
            df.at[df.index[i], 'Sprzedaz'] = sell_price
            money = quantity * sell_price
        df.loc[df.index[i], 'Pieniedzy'] = money

    # Zamknij ostatnią pozycję
    if position == Position.LONG:
        sell_price = df['Zamkniecie'].iloc[-1]
        df.at[df.index[-1], 'Sprzedaz'] = sell_price
        money = quantity * sell_price
    df.loc[df.index[-1], 'Pieniedzy'] = money
    return money
