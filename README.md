# Units Sold Forecasting

## 📌 Project Overview
This project focuses on forecasting **units sold** for a retail store using historical inventory, pricing, and temporal features.  
The goal is to build a machine learning model that can accurately predict future demand and support better inventory management decisions.

The dataset is sourced from Kaggle:  
**Retail Store Inventory Forecasting** by *Anirudh Chauhan*.

---

## 📂 Repository Structure

Units-sold-forecasting/
├── Data cleaning and understanding.ipynb
├── Model.ipynb
├── retail_store_inventory.csv
├── requirements.txt
└── README.md

---

## ⚙️ Environment & Dependencies

Install dependencies using:

pip install -r requirements.txt

### requirements.txt
pandas>=1.3.0  
numpy>=1.21.0  
matplotlib>=3.4.0  
seaborn>=0.11.0  
scikit-learn>=1.0.0  
xgboost>=1.7.0  
lightgbm>=3.3.0  
jupyterlab>=3.0.0  
ipython>=7.0.0  
optuna>=3.0.0  
statsmodels>=0.13.0  
prophet>=1.1.1  
tqdm>=4.60.0  

---

## 🧹 Data Cleaning & Understanding
Notebook: Data cleaning and understanding.ipynb

- Data inspection and missing value handling  
- Date parsing and time feature extraction  
- Exploratory data analysis (EDA)  
- Clean dataset preparation  

---

## 🧠 Modeling Pipeline
Notebook: Model.ipynb

### Objective
Predict units_sold based on inventory, pricing, and time-based features.

### Workflow Summary
1. Data loading and preprocessing  
2. Feature engineering and encoding  
3. Train-test split with reproducibility  
4. Model training (Linear Regression, Random Forest, XGBoost, LightGBM)  
5. Evaluation using MAE, RMSE, and R²  
6. Visualization and feature importance analysis  

---

## 📊 Results (Example)

Model | MAE | RMSE | R²  
Linear Regression | xx | yy | zz  
Random Forest | xx | yy | zz  
XGBoost / LGBM | xx | yy | zz  

---

## 🔍 Key Takeaways
- Tree-based models outperform linear baselines  
- Time features significantly improve forecasts  
- Proper splitting avoids data leakage  

---

## 🚀 Future Improvements
- Time-series cross-validation  
- Hyperparameter tuning  
- SHAP explainability  
- Refactor into src/ scripts  
- Model persistence  

---

## 📜 License
Educational and research use only.
