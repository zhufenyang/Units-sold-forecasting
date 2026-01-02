Project Overview

This project focuses on forecasting the number of units sold in a retail store using multiple influencing factors such as inventory levels, product pricing, and weather conditions. The goal is to explore the dataset, engineer meaningful features, and apply machine learning models to predict future sales more accurately.

This project is designed as a practical data science and machine learning exercise, covering the full workflow from data cleaning to model evaluation.

Dataset

The dataset used in this project comes from Kaggle:
Retail Store Sales Forecasting Dataset

It includes historical retail data with variables that may affect daily sales performance, such as:

Date

Units sold

Product price

Inventory level

Weather conditions

Other operational features

Tools and Technologies

Python

Jupyter Notebook

Pandas for data manipulation

Matplotlib and Seaborn for data visualization

Scikit-learn for machine learning modeling

Project Structure

The repository is organized as follows:

Data cleaning and understanding.ipynb
Handles data cleaning, preprocessing, and initial exploratory data analysis.

Feature Engineering.ipynb
Focuses on creating and transforming features to improve model performance.

Model.ipynb
Contains model training, prediction, and evaluation steps.

retail_store_inventory.csv
The original dataset used for analysis and modeling.

README.md
Project documentation.

Workflow

Data Cleaning and Exploration
The raw dataset is cleaned and explored to understand distributions, missing values, and relationships between variables.

Feature Engineering
Relevant features are selected and transformed to better capture sales patterns.

Modeling Approach

A LightGBM regression model is used as the primary forecasting model.
The target variable (Units Sold) is log-transformed using log1p to stabilize variance.

Feature engineering includes:

Lagged demand features (1, 7, 14, 28 days)

Rolling mean and standard deviation

Time-based features (day of week, month, weekend)

Frequency encoding for high-cardinality identifiers (Store ID, Product ID)

The dataset is split using a time-based validation strategy to avoid data leakage.
Model performance is evaluated using RMSE, MAE, and RMSLE on the validation set.

Several baseline models (Linear Regression and Random Forest) are implemented for comparison.

Model Training
Machine learning models are trained using historical data to forecast units sold.

Model Evaluation
Model performance is evaluated using standard regression metrics.

Model Evaluation Metrics

The following metrics are used to assess model performance:

Root Mean Squared Error (RMSE)

R-squared (R²)

These metrics help quantify prediction accuracy and model reliability.

Visualization

The project includes visual analysis such as:

Sales trends over time

Relationships between sales and key variables

Comparison between predicted and actual sales values

Visualizations help interpret model behavior and business insights.

Future Improvements

Potential enhancements for this project include:

Incorporating additional features such as promotions or competitor pricing

Applying time-series-specific models such as SARIMA or Prophet

Performing cross-validation to improve model robustness

Converting notebooks into reusable Python scripts or a simple web app

References

Kaggle Retail Store Sales Forecasting Dataset
https://www.kaggle.com/datasets/anirudhchauhan/retail-store-inventory-forecasting-dataset

Scikit-learn Documentation
