# Used Car Price Prediction Web Service

## Overview
This project implements a RESTful web service that hosts a trained machine learning algorithm for predicting used car prices. The service provides endpoints to sample input data, explain the model, and evaluate new data points for price prediction.

## Features
- Trained machine learning algorithm for used car price prediction
- RESTful API with the following endpoints:
  - GET /sample_request: Returns a sample input JSON for a used car
  - GET /parameters_explanation: Provides an explanation of the input fields and expected values
  - POST /home: Accepts input data about a used car and returns the predicted price

## Dataset
The model was trained on a dataset containing information about used cars. The dataset includes the following features:

1. name: The name or model of the car
2. year: The year of manufacture
3. selling_price: The price at which the car is being sold (target variable)
4. km_driven: The number of kilometers the car has been driven
5. fuel: The type of fuel used (e.g., Petrol, Diesel, CNG)
6. seller_type: The type of seller (e.g., Individual, Dealer)
7. transmission: The type of transmission (e.g., Manual, Automatic)
8. Owner: The number of previous owners

This dataset is suitable for demonstrating the use of regression techniques in Machine Learning, particularly for price prediction tasks.

⌨️ [Dataset Credit Link](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho/data)


## Setup and Installation
1. Clone the repository
2. Install required dependencies: `pip install -r requirements.txt`
3. First run the web service: run all the cells of `ml_server.ipynb`
4. Then run the client app: `streamlit run st_clients/client_app.py`

## Usage
The web service runs on `http://localhost:8501/`

### Endpoints
1. Sample: `GET /usedcar/sample_request`
2. Explain: `GET /parameters_explanation`
3. Evaluate/predict: `POST /home`

## Technologies Used
- Python
- Flask (for RESTful API)
- Scikit-learn (for machine learning model)
- Pandas (for data manipulation)
- Streamlit (user interface)