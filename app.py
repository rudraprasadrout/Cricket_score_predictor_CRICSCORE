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
        
        overs_val = float(data['overs'])
        full_overs = int(overs_val)
        extra_balls = int(round((overs_val - full_overs) * 10))
        total_balls = (full_overs * 6) + extra_balls

        input_df = pd.DataFrame({
            'battingTeam': [data['batting_team']],
            'bowlingTeam': [data['bowling_team']],
            'current_score': [int(data['current_score'])],
            'balls': [total_balls],
            'wickets': [int(data['wickets'])],
            'CRR': [float(data['crr'])]
        })
        
        prediction = model.predict(input_df)[0]
        return jsonify({'status': 'success', 'predicted_score': int(prediction)})
        
    except Exception as e:
        print(f"New Error: {str(e)}")
        return jsonify({'error': str(e)}), 400

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)