import joblib
import numpy as np

def load_model():
    return joblib.load("Heart_app/heart_model.pkl")
