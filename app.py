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
        
        print(f"DEBUG: Received Data -> {data}")

        required_keys = ['batting_team', 'bowling_team', 'current_score', 'overs', 'wickets', 'crr']
        for key in required_keys:
            if key not in data or data[key] == "":
                return jsonify({'error': f'Missing or empty field: {key}'}), 400

        input_df = pd.DataFrame({
            'batting_team': [str(data['batting_team'])],
            'bowling_team': [str(data['bowling_team'])],
            'current_score': [int(data['current_score'])],
            'overs': [float(data['overs'])],
            'wickets': [int(data['wickets'])],
            'crr': [float(data['crr'])]
        })

        prediction = model.predict(input_df)[0]

        result = int(prediction) if not hasattr(prediction, '__iter__') else int(prediction[0])
        
        return jsonify({
            'status': 'success', 
            'predicted_score': result
        })
        
    except Exception as e:
        print(f"ERROR: {str(e)}") 
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)