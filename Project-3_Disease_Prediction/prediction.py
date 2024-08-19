from flask import Flask, render_template, request
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

app = Flask(__name__)

# Load and prepare data
data = pd.read_csv('Training.csv')
data.fillna(0, inplace=True)

X = data.drop(columns=['prognosis'])
X = X.loc[:, ~X.columns.str.contains('^Unnamed')]
y = data['prognosis']
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)

X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

log_reg = LogisticRegression()
log_reg.fit(X_train, y_train)

@app.route('/', methods=['GET'])
def landing_page():
    return render_template('landing.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict_page():
    if request.method == 'POST':
        user_input = [int(request.form.get(col, 0)) for col in X.columns]
        input_data = pd.DataFrame([user_input], columns=X.columns)
        
        prediction = log_reg.predict(input_data)
        disease = label_encoder.inverse_transform(prediction)[0]
        return render_template('index.html', disease=disease, symptoms=X.columns)
    return render_template('index.html', disease=None, symptoms=X.columns)

if __name__ == '__main__':
    app.run(debug=True)
