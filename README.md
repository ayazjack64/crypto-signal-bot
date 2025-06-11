# Crypto Signal Bot

This is a Telegram bot that uses an LSTM model to generate cryptocurrency trading signals.

## Usage

1. Train and save your `lstm_model.h5` inside the `app/` folder.
2. Set your Telegram bot token in `.env`.
3. Run the bot with:

```bash
python app/bot.py
```

Or use Docker:

```bash
docker build -t crypto-signal-bot .
docker run --env-file .env crypto-signal-bot
```
