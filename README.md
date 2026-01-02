Units Sold Forecasting
Project Description

This project aims to forecast the number of units sold at a retail store using various factors such as inventory levels, prices, weather, etc. Through data cleaning, exploratory analysis, feature engineering, and machine learning models, the goal is to make accurate sales predictions.

Dataset

The dataset used in this project is from Kaggle: Retail Store Sales Forecasting
. The dataset contains the following columns:

date: The date of the sales transaction

sales: The number of units sold on that day

price: The price of the product

inventory: The inventory level on that day

weather: Weather condition on that day

Other possible factors affecting sales

Technologies Used

Python

Jupyter Notebook

Pandas - For data processing

Matplotlib/Seaborn - For data visualization

Scikit-learn - For model training and prediction

Project Structure
Units-sold-forecasting/
│
├── Data cleaning and understanding.ipynb   # Data cleaning and initial exploration
├── Feature Engineering.ipynb               # Feature engineering
├── Model.ipynb                            # Model training and forecasting
├── retail_store_inventory.csv             # The dataset
└── README.md                              # Project documentation

How to Use

Clone the Repository
Clone the repository to your local machine.

Install Dependencies
Install the required Python libraries by using the provided requirements.txt file.

Run Jupyter Notebook
Start Jupyter Notebook and open the Data cleaning and understanding.ipynb notebook to begin processing the data.

Train the Model and Make Predictions
Open the Model.ipynb notebook to train various machine learning models and forecast the number of units sold. Evaluate the models' performance and compare results.

Model Evaluation

The following evaluation metrics are used to assess the performance of the forecasting models:

RMSE (Root Mean Squared Error)

R² (Coefficient of Determination)

These metrics help evaluate the accuracy of the predictions.

Visualization and Analysis

Matplotlib and Seaborn are used in this project for visualizing the data, including:

Time series plots of sales data

Comparison between predicted and actual sales values

Future Improvements

Add more features (e.g., promotions, competitor prices) to improve forecast accuracy.

Use more advanced time-series forecasting models (e.g., SARIMA, Prophet) for comparison.

Implement automated testing and validation for the models.

References

Kaggle: Retail Store Sales Forecasting Dataset

Scikit-learn Documentation
