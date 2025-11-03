# 🩺 Day 3 — AI-Based Diabetes Diagnosis  

> 🎯 *Medical Diagnosis Feature Importance Analysis using Permutation Importance & SHAP*  

---

## 📘 Overview  

This project interprets a **Random Forest–based Diabetes Prediction Model** using **Explainable AI (XAI)** techniques — **SHAP** and **Permutation Importance**.  
It identifies and ranks the most influential medical factors contributing to diabetes diagnosis, ensuring both model accuracy and interpretability.  

---

## 📊 Dataset  

- **Source:** Pima Indians Diabetes Dataset (UCI Machine Learning Repository)  
- **Description:** Contains diagnostic measurements for 768 women aged 21+, including glucose levels, BMI, and family history indicators.  
- **Shape:** `(768, 9)` → 8 features + 1 target (`Outcome`)  
- **Target Variable:**  
  - `0` → Non-diabetic  
  - `1` → Diabetic  

---

## ⚙️ Workflow  

1. **Data Loading & Exploration**  
   - Loaded dataset and explored structure, missing values, and class balance  
   - Verified data quality and statistical distribution  

2. **Data Preparation**  
   - Selected key medical features  
   - Applied **StandardScaler** for logistic regression  
   - Split into training (80%) and test (20%) sets  

3. **Model Training**  
   - Trained and evaluated **Logistic Regression**, **Random Forest**, and **XGBoost**  
   - Compared metrics: Accuracy, AUC, and F1-score  

4. **Explainability (XAI) Techniques**  
   - **SHAP Analysis:** To understand global and local feature impact  
   - **Permutation Importance:** To measure each feature’s effect on prediction accuracy  

5. **Feature Importance Comparison**  
   - Combined SHAP and Permutation scores to validate consistent top predictors  

6. **Insights & Visualization**  
   - Summarized key medical indicators influencing diabetes risk  

---

## 🧩 Tech Stack  

| Category | Tools / Libraries |
|-----------|------------------|
| **Language** | Python |
| **Libraries** | pandas, numpy, seaborn, matplotlib |
| **Machine Learning** | scikit-learn, XGBoost |
| **Explainability (XAI)** | SHAP |
| **Visualization** | Matplotlib, Seaborn |
| **Environment** | Jupyter Notebook / Anaconda |

---

## 📈 Results  

| Model | Accuracy | AUC | F1 Score |
|--------|-----------|-----|----------|
| Logistic Regression | 0.714 | 0.823 | — |
| Random Forest | 0.760 | 0.812 | — |
| XGBoost | 0.734 | 0.805 | — |

### 🔍 Feature Importance Rankings  

| Rank | Feature | SHAP Importance | Permutation Importance |
|------|----------|-----------------|-------------------------|
| 1 | **Glucose** | 0.1272 | 0.0695 |
| 2 | **BMI** | 0.0705 | 0.0357 |
| 3 | **Age** | 0.0593 | 0.0325 |
| 4 | DiabetesPedigreeFunction | 0.0424 | 0.0182 |
| 5 | Pregnancies | 0.0315 | 0.0117 |
| 6 | Insulin | 0.0189 | 0.0169 |
| 7 | SkinThickness | 0.0169 | -0.0013 |
| 8 | BloodPressure | 0.0164 | 0.0214 |

> ✅ **Top Predictor (Both Methods): Glucose**  
> Indicates that blood glucose levels are the most decisive factor in diabetes classification.

---

## 🧠 Key Learnings  

- SHAP provides **transparent and interpretable model explanations**.  
- Permutation Importance complements SHAP by measuring **feature impact on accuracy**.  
- Consistent ranking across both validates **reliable medical predictors**.  
- Explainable AI helps build **trustworthy healthcare ML models**.  
- Data scaling and proper preprocessing are vital for model performance.  

---

## 📚 References  

- [UCI Machine Learning Repository – Pima Indians Diabetes Dataset](https://archive.ics.uci.edu/ml/datasets/pima+indians+diabetes)  
- [SHAP Documentation](https://shap.readthedocs.io/en/latest/)  
- [Scikit-learn Permutation Importance](https://scikit-learn.org/stable/modules/permutation_importance.html)

---

> *Every model is a milestone on the path to mastery 🧠*  

