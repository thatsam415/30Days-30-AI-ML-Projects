# ⚡ Day 2 — Energy Consumption Forecasting  

> 🎯 *Advanced Time Series Forecasting using Gradient Boosting (XGBoost and LightGBM)*  

---

## 📘 Overview  

This project focuses on **forecasting household energy consumption** using historical power usage data.  
By analyzing time-series patterns and key electrical parameters, the model aims to predict future energy demand efficiently and accurately.  

---

## 📊 Dataset  

- **Source:** [UCI Machine Learning Repository — Individual Household Electric Power Consumption Dataset](https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption)  
- **Description:** Contains minute-level measurements of electric power consumption in a single household over ~4 years (Dec 2006 – Nov 2010).  
- **Shape:** ~2 million rows × 9 columns  
- **Frequency:** 1-minute sampling rate  
- **Target:** `Global_active_power` (kilowatts)  

---

## ⚙️ Workflow  

1. **Data Preprocessing**  
   - Handled missing values and merged Date + Time into a single datetime column  
   - Generated additional time-based features — *hour, day, month, weekday*  
   - Aggregated minute-level data into hourly averages  

2. **Exploratory Data Analysis (EDA)**  
   - Visualized daily and seasonal power consumption patterns  
   - Checked correlations between voltage, sub-metering, and total power  

3. **Feature Engineering & Selection**  
   - Derived total sub-metered power and removed redundant columns  
   - Selected relevant predictors influencing total consumption  

4. **Model Development**  
   - Trained **LightGBM** and **XGBoost** regression models  
   - Split dataset (80 % train / 20 % test) and tuned hyperparameters  

5. **Model Evaluation & Saving**  
   - Evaluated using **MAE**, **RMSE**, and **R² Score**  
   - Saved trained models (`lgb_energy_model.joblib`, `xgb_energy_model.joblib`) and preprocessed data  

---

## 🧩 Tech Stack  

| Category | Tools |
|-----------|--------|
| Language | Python 🐍 |
| Libraries | Pandas, NumPy, Matplotlib, Seaborn, Scikit-learn, LightGBM, XGBoost, Joblib |
| Environment | Jupyter Notebook / VS Code |
| Version Control | Git & GitHub |

---

## 📈 Results  

| Model | MAE | RMSE | R² Score |
|--------|------|------|----------|
| LightGBM | 0.048 | 0.072 | 0.94 |
| XGBoost | 0.051 | 0.076 | 0.92 |

> ✅ *LightGBM achieved the best accuracy with the lowest MAE and highest R² (0.94), making it the preferred model for forecasting.*  

---

## 🧠 Key Learnings  

- Learned how to handle and resample high-frequency time-series data  
- Improved understanding of **feature engineering** for temporal datasets  
- Gained experience training **gradient boosting** models (XGBoost / LightGBM)  
- Evaluated models using regression metrics (MAE, RMSE, R²)  
- Practiced model persistence for reuse and deployment  

---

## 📚 References  

- [UCI Machine Learning Repository – Individual Household Electric Power Consumption](https://archive.ics.uci.edu/dataset/235/individual+household+electric+power+consumption)  
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)  
- [LightGBM Documentation](https://lightgbm.readthedocs.io/en/latest/)  
- [XGBoost Documentation](https://xgboost.readthedocs.io/en/stable/)  

---

> *Turning data into insights and insights into intelligence 💡*
