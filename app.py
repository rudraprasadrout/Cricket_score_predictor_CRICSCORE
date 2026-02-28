from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)

# Load the pickle files
pipe = pickle.load(open('pipe.pkl', 'rb'))

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # 1. Convert Overs to Total Balls (Standard T20 Logic)
        overs_input = float(data['overs'])
        overs_int = int(overs_input)
        balls_in_over = round((overs_input - overs_int) * 10)
        total_balls = (overs_int * 6) + balls_in_over

        # 2. Map input to Model columns
        # Based on your CSV: battingTeam, bowlingTeam, current_score, balls, CRR, wickets
        input_data = pd.DataFrame({
            'battingTeam': [data['batting_team']],
            'bowlingTeam': [data['bowling_team']],
            'current_score': [float(data['current_score'])],
            'balls': [total_balls],
            'CRR': [float(data['crr'])],
            'wickets': [float(data['wickets'])]
        })

        # 3. Predict
        res = pipe.predict(input_data)
        
        return jsonify({
            'status': 'success',
            'predicted_score': int(res[0])
        })

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == '__main__':
    app.run(debug=True, port=5000)