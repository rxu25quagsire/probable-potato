#Importing all necessary libraries and frameworks
from flask import Flask, request, render_template
import pandas as pd
from sklearn.model_selection import train_test_split, GridSearchCV
from xgboost import XGBClassifier

#Creating the flask app
app = Flask(__name__)

#Names of all features of interest from the CSV file
csv_feature_names = [
    'radius_mean',
    'texture_mean',
    'perimeter_mean',
    'area_mean',
    'smoothness_mean',
    'compactness_mean',
    'concavity_mean',
    'concave points_mean',  # note the space here!
    'symmetry_mean',
    'fractal_dimension_mean'
]

#Names of features used in the web application.
feature_names = [
    "radius", "texture", "perimeter", "area", "smoothness",
    "compactness", "concavity", "concave_points", "symmetry", "fractal_dimension"
]

#Function that reads data, cleans data, establishes training and testing groups.
def load_and_preprocess_data():
    #Reading the wisconsin diagnostic breast cancer dataset. 
    df = pd.read_csv('wisco.csv')
    #Cleaning the dataset
    df = df.drop(df.columns[0], axis=1)  # drop ID column
    df = df.drop(df.columns[11:31], axis=1)  # drop unwanted columns
    #Mapping to numerical values (Malignant = 1, Benign = 0)
    df['diagnosis'] = df['diagnosis'].map({'M': 1, 'B': 0})

    #Renaming CSV columns... assistance from ChatGPT
    rename_map = dict(zip(csv_feature_names, feature_names))
    df.rename(columns=rename_map, inplace=True)

    #Establishing training and testing groups for XGboost model.
    X = df[feature_names]
    y = df['diagnosis']
    return train_test_split(X, y, test_size=0.2, random_state=1)

#Function that runs the XGboost model with hyperparameters
def train_model(X_train, y_train):
    #Hyperparameter grid
    param_grid = {
        'n_estimators': [100, 200],
        'max_depth': [3, 5, 7],
        'learning_rate': [0.01, 0.1],
        'subsample': [0.8, 1],
        'colsample_bytree': [0.8, 1]
    }
    #Brute forcing combinations in the hyperparameter grid until the most optimal combination is found
    grid_search = GridSearchCV(XGBClassifier(random_state=1), param_grid, cv=5,
                               scoring='accuracy', n_jobs=-1, verbose=0)
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_

X_train, X_test, y_train, y_test = load_and_preprocess_data()
model = train_model(X_train, y_train)
#Running both functions which trains/tunes the XGBoost on the Wisconsin Diagnostic Breast Cancer dataset.

@app.route('/')
def home():
    return render_template('springproject.html')
#Launching the springproject.html when user accesses http://127.0.0.1:5000/, home function.

@app.route('/submit', methods=['POST'])
#Running the submit function when the user accesses http://127.0.0.1:5000/submit
def submit():
    input_data = [float(request.form.get(f)) for f in feature_names]
    input_df = pd.DataFrame([input_data], columns=feature_names)
    pred = model.predict(input_df)[0]
    label = "Malignant" if pred == 1 else "Benign"
    #Grabs data from html file, uses the model to predict.
    with open("data.txt", "a") as f:
        f.write(",".join(map(str, input_data)) + f",{label}\n")
    #Adds data and diagnosis to a txt file.

    return f"Prediction: {label}. Your input has been saved."
    #Returns prediction for user.

if __name__ == "__main__":
    app.run(debug=True)
