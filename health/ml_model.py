import joblib
import os

model_path = os.path.join(os.path.dirname(__file__), 'models', 'svc.pkl')
model = joblib.load(model_path)

def predict(input_data):
    return model.predict(input_data)
