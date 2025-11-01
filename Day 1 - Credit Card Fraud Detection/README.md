# 💳 Day 01 — Credit Card Fraud Detection  

> 🎯 *Advanced Data Cleaning & Outlier Detection Pipeline using Isolation Forests and Robust Scaling*  

## 📘 Overview  

This project focuses on **detecting fraudulent credit card transactions** using machine learning models.  
Fraud detection is a **highly imbalanced classification problem**, where the goal is to correctly identify rare fraudulent cases without triggering excessive false alarms.  

The project implements multiple models — including **Logistic Regression**, **Decision Tree**, **Random Forest**, **XGBoost**, and **LightGBM** — and evaluates them based on **Precision**, **Recall**, **F1-Score**, **ROC-AUC**, and **PR-AUC** to select the best-performing algorithm.

---

## 📊 Dataset  

- **Source:** [Kaggle - Credit Card Fraud Detection Dataset](https://www.kaggle.com/mlg-ulb/creditcardfraud)  
- **Description:** Contains anonymized transaction data with features like `V1` to `V28` (PCA components), `Amount`, and the target variable `Class` (1 = Fraud, 0 = Legitimate).  
- **Shape:** 284,807 rows × 31 columns  
- **Imbalance:** Fraud cases ≈ 0.17% of total transactions  

---

## ⚙️ Workflow  

1. **Data Preprocessing**  
   - Handled missing values and normalized transaction amounts using **StandardScaler**  
   - Split the dataset into training and testing sets (80:20)  

2. **Exploratory Data Analysis (EDA)**  
   - Visualized class imbalance and feature distributions  
   - Correlation analysis to identify key transaction features  

3. **Model Training**  
   - Trained five models:  
     - Logistic Regression  
     - Decision Tree  
     - Random Forest  
     - XGBoost  
     - LightGBM  

4. **Model Evaluation**  
   - Compared models using metrics: **Precision**, **Recall**, **F1-Score**, **ROC-AUC**, and **PR-AUC**  
   - Visualized **ROC** and **Precision-Recall curves** for performance interpretation  

5. **Model Saving**  
   - Saved the best model (**Random Forest**) using `joblib` for deployment  

---

## 🧩 Tech Stack  

| Category | Tools |
|-----------|--------|
| Language | Python 🐍 |
| Libraries | Pandas, NumPy, Scikit-learn, XGBoost, LightGBM, Matplotlib, Seaborn |
| Model Persistence | Joblib |
| Environment | Jupyter Notebook / Google Colab |

---

## 📈 Results  

| Model | F1-Score | ROC-AUC | PR-AUC |
|--------|-----------|----------|---------|
| Logistic Regression | 0.1039 | 0.9711 | 0.7231 |
| Decision Tree | 0.4802 | 0.9017 | 0.2760 |
| Random Forest | **0.8182** | **0.9630** | **0.8586** |
| XGBoost | 0.7391 | 0.9792 | 0.8558 |
| LightGBM | 0.6093 | 0.9496 | 0.7407 |

> ✅ *Random Forest achieved the highest F1-Score (0.82) and PR-AUC (0.86), making it the best-performing model.*

---

## 🖼️ Outputs  

- Confusion Matrices for each model  
- ROC Curves and Precision-Recall Curves  
- Model comparison bar charts (ROC-AUC & PR-AUC)  
- Final results table summarizing all metrics  

---

## 🧠 Key Learnings  

- Learned to handle **imbalanced datasets** using evaluation metrics like PR-AUC  
- Understood trade-offs between **precision and recall** in fraud detection  
- Gained hands-on experience with **tree-based ensemble models**  
- Practiced saving and loading trained ML models using Joblib  

---

## 📚 References  

- [Credit Card Fraud Detection Dataset — Kaggle](https://www.kaggle.com/mlg-ulb/creditcardfraud)  
- [Scikit-Learn Documentation](https://scikit-learn.org/stable/)  
- [XGBoost Documentation](https://xgboost.readthedocs.io/en/stable/)  
- [LightGBM Documentation](https://lightgbm.readthedocs.io/en/latest/)  

---

> *Learning. Building. Innovating. Evolving — the true spirit of AI 🌟* 
