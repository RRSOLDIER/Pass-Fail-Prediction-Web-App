import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split


data = {
    'marks': [10,20,30,40,50,60,70,80,90,100],
    'attendance': [30,40,50,60,70,80,85,90,95,100],
    'study_hours': [1,2,2,3,4,5,6,7,8,9],
    'passed': [0,0,0,0,0,1,1,1,1,1]
}

df = pd.DataFrame(data)
X = df[['marks', 'attendance', 'study_hours']]
y = df['passed']


x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
model = LogisticRegression()
model.fit(x_train, y_train)


joblib.dump(model, 'model.pkl')


def predict_result(marks, attendance, study_hours):
    loaded_model = joblib.load('model.pkl')
    prediction = loaded_model.predict([[marks, attendance, study_hours]])
    return int(prediction[0])
