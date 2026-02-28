import os
import joblib
import pandas as pd
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# 1. Path Fix: Ensure Render finds the model regardless of folder structure
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Note: Use 'pipe.pkl' because your logs showed that's what your code expects
model_path = os.path.join(BASE_DIR, 'pipe.pkl') 

try:
    # We use joblib as it is more stable for ML models than standard pickle
    model = joblib.load(model_path)
    print("Model loaded successfully!")
except Exception as e:
    print(f"Error loading model: {e}")
    model = None

@app.route('/')
def home():
    return "CricPredict API is Running!"

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({'error': 'Model not loaded on server'}), 500
        
    try:
        data = request.get_json()
        
        # Create DataFrame matching your model's training format
        input_df = pd.DataFrame({
            'batting_team': [data['batting_team']],
            'bowling_team': [data['bowling_team']],
            'current_score': [int(data['current_score'])],
            'overs': [float(data['overs'])],
            'wickets': [int(data['wickets'])],
            'crr': [float(data['crr'])]
        })
        
        prediction = model.predict(input_df)[0]
        return jsonify({'status': 'success', 'predicted_score': int(prediction)})
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400

# 2. Port Binding Fix: Render tells the app which port to use via an Env Var
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    # '0.0.0.0' is required for the internet to reach your Render container
    app.run(host="0.0.0.0", port=port)