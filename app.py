from flask import Flask, render_template, request
import pickle
import numpy as np

# Load trained model
with open('customer-churn.pkl', 'rb') as f:
    model = pickle.load(f)

app = Flask(__name__)

# Home page
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Read form data
    features = [float(x) for x in request.form.values()]
    final_features = np.array([features])

    # Model prediction (0 or 1)
    pred = model.predict(final_features)[0]

    # Convert prediction to label
    if int(pred) == 1:
        result = "Churn"
    else:
        result = "Not Churn"

    return render_template(
        'index.html',
        prediction=result
    )

if __name__ == '__main__':
    app.run(debug=True)

