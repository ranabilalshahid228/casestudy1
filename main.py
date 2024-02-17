import pandas as pd
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler, PolynomialFeatures
# Define global variables (initialization)
X_train, X_test, y_train, y_test = None, None, None, None
model, mse_train, r2_train = None, None, None
prediction = None  # Define prediction globally

def load_data():
    df = pd.read_csv('datagarment.csv')  # replace with your data file
    X = df[['department', 'quarter', 'no_of_workers', 'defects_day']].copy()

    production_speed = {'Gloves': 3, 'T-Shirt': 2, 'Sweatshirt': 1}
    X['production_speed'] = X['department'].map(production_speed)

    y = df['Total_Produced']
    return train_test_split(X, y, test_size=0.2, random_state=15, shuffle=True)

def train_model(X_train, y_train):
    categorical_features = ['department', 'quarter']
    numeric_features = ['no_of_workers', 'defects_day']

    numeric_transformer = StandardScaler()
    categorical_transformer = OneHotEncoder()

    preprocessor = ColumnTransformer(
        transformers=[
            ('num', numeric_transformer, numeric_features),
            ('cat', categorical_transformer, categorical_features)
        ])

    poly_features = PolynomialFeatures(degree=2, include_bias=False)
    model = make_pipeline(preprocessor, poly_features, LinearRegression())

    param_grid = {'polynomialfeatures__degree': [1, 2, 3]}
    grid_search = GridSearchCV(model, param_grid, cv=5)

    X_train_values = X_train
    y_train_values = y_train.values

    grid_search.fit(X_train_values, y_train_values)

    best_model = grid_search.best_estimator_

    y_pred_train = best_model.predict(X_train_values)
    mse_train = mean_squared_error(y_train_values, y_pred_train)
    r2_train = r2_score(y_train_values, y_pred_train)
    mse_train = mse_train / (y_train.max() - y_train.min())  # Normalize MSE

    print(f'R-squared (Train): {r2_train}')

    return best_model, mse_train, r2_train

# Load data and train model when the script runs
X_train, X_test, y_train, y_test = load_data()
model, mse_train, r2_train = train_model(X_train, y_train)


def predict(data):
    input_data = pd.DataFrame(data, index=[0])
    production_speed = {'Gloves': 3, 'T-Shirt': 2, 'Sweatshirt': 1}
    input_data['production_speed'] = input_data['department'].map(production_speed)
    input_data_transformed = model.named_steps['columntransformer'].transform(input_data)

    prediction = model.predict(input_data)
    rounded_prediction = int(round(prediction[0]))  # Round to the nearest integer
    return rounded_prediction


# Sample input data
sample_input = {
    'department': 'Gloves',  # You might need to encode this as per your model's training
    'quarter': 'Quarter1',         # You might need to encode this as per your model's training
    'no_of_workers': 50,
    'defects_day': 5
}

# Predict the output for the sample input
predicted_output = predict(sample_input)

print(f"Predicted Total Produced: {predicted_output}")
