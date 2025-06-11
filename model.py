from tensorflow.keras.models import load_model

def load_lstm_model(path='app/lstm_model.h5'):
    model = load_model(path)
    return model
