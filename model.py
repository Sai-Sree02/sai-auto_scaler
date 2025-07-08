import numpy as np
from sklearn.linear_model import LinearRegression

model = LinearRegression()
model.fit(np.array([[0], [1], [2]]), np.array([100, 200, 300]))  # Dummy training

def predict_traffic(metrics, config):
    print("[Predict] Forecasting future traffic based on metrics...")
    x = np.array([[metrics['requests_per_minute']]])
    prediction = model.predict(x)[0]
    return prediction
