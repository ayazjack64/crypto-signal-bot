import ccxt
import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from app.model import load_lstm_model

def fetch_data():
    exchange = ccxt.binance()
    ohlcv = exchange.fetch_ohlcv('BTC/USDT', timeframe='1h', limit=100)
    df = pd.DataFrame(ohlcv, columns=['timestamp', 'open', 'high', 'low', 'close', 'volume'])
    return df

def generate_signal():
    df = fetch_data()
    prices = df['close'].values.reshape(-1, 1)
    scaler = MinMaxScaler()
    scaled = scaler.fit_transform(prices)

    seq_len = 50
    last_seq = scaled[-seq_len:]
    X = np.reshape(last_seq, (1, seq_len, 1))

    model = load_lstm_model()
    pred = model.predict(X)
    predicted_price = scaler.inverse_transform(pred)[0][0]
    current_price = prices[-1][0]

    if predicted_price > current_price * 1.01:
        return f"Signal: BUY 📈\nPredicted: {predicted_price:.2f} USDT"
    elif predicted_price < current_price * 0.99:
        return f"Signal: SELL 📉\nPredicted: {predicted_price:.2f} USDT"
    else:
        return f"Signal: HOLD ⏸️\nPredicted: {predicted_price:.2f} USDT"
