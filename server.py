from flask import Flask, request, jsonify
import joblib
import numpy as np
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Define model paths
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, 'joblibs/model_mentalhealth.joblib')
SCALER_PATH = os.path.join(BASE_DIR, 'joblibs/scaler.joblib')

# Load ML model and scaler
model = joblib.load(MODEL_PATH)
scaler = joblib.load(SCALER_PATH)

# Define score interpretation rules
def get_label(score, category):
    if category == 'depression':
        if score <= 9: return 'Normal'
        elif score <= 13: return 'Mild'
        elif score <= 20: return 'Moderate'
        elif score <= 27: return 'Severe'
        else: return 'Extremely Severe'
    elif category == 'anxiety':
        if score <= 7: return 'Normal'
        elif score <= 9: return 'Mild'
        elif score <= 14: return 'Moderate'
        elif score <= 19: return 'Severe'
        else: return 'Extremely Severe'
    elif category == 'stress':
        if score <= 14: return 'Normal'
        elif score <= 18: return 'Mild'
        elif score <= 25: return 'Moderate'
        elif score <= 33: return 'Severe'
        else: return 'Extremely Severe'
    return 'Unknown'

# Setup Flask
app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()
        answers = data.get('answers')
        if not answers or len(answers) != 42:
            return jsonify({"error": "Exactly 42 answers are required."}), 400

        # Convert to numpy array and reshape
        arr = np.array(answers).reshape(1, -1)
        arr_scaled = scaler.transform(arr)

        # Predict with model
        prediction = model.predict(arr_scaled)[0]  # could also be regression

        # Simulate scoring if using a custom model
        depression_score = sum(answers[i] for i in [2, 4, 9, 15, 20, 23, 30, 33, 37, 41])
        anxiety_score = sum(answers[i] for i in [1, 3, 8, 14, 18, 25, 28, 34, 40, 39])
        stress_score = sum(answers[i] for i in [0, 5, 6, 7, 10, 11, 12, 16, 17, 21, 22, 24])

        response = {
            "depression": depression_score,
            "anxiety": anxiety_score,
            "stress": stress_score,
            "labels": {
                "depression": get_label(depression_score, 'depression'),
                "anxiety": get_label(anxiety_score, 'anxiety'),
                "stress": get_label(stress_score, 'stress')
            }
        }
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5003)
