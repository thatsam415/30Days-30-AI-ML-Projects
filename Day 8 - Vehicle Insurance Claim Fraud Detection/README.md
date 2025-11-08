
# 🚗 Day 8 — Vehicle Insurance Claim Fraud Detection  

> 🎯 *Detecting fraudulent vehicle insurance claims using Machine Learning (Random Forest + SMOTE)*  

---

## 📘 Overview  

This project focuses on identifying fraudulent vehicle insurance claims using **Machine Learning**.  
By leveraging a **Random Forest Classifier** combined with **SMOTE**, the model effectively handles data imbalance and distinguishes between genuine and fraudulent claims.

---

## 📊 Dataset  

- **Source:** [Vehicle Insurance Claim Fraud Dataset – Kaggle](https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection)  
- **Description:** Contains vehicle, policy, and accident-related details with a binary target variable indicating whether a claim is fraudulent (`FraudFound_P`).  
- **Shape:** ~15,000 records × 33 features  
- **Key Features:**  
  - PolicyType, Fault, VehicleCategory, AccidentArea, NumberOfSuppliments, Age, DriverRating, etc.  
- **Target Variable:** `FraudFound_P` → (1 = Fraudulent, 0 = Genuine)  

---

## ⚙️ Workflow  

1. **Data Preprocessing & Exploration**  
   - Handled missing values and encoded categorical variables.  
   - Scaled numeric features and visualized class imbalance.  

2. **Model Development & Evaluation**  
   - Applied **SMOTE** to oversample minority (fraudulent) cases.  
   - Trained a **Random Forest Classifier** using a pipeline.  
   - Evaluated using **Precision, Recall, F1-score, ROC-AUC, and PR-AUC** metrics.  

3. **Optimization & Feature Analysis**  
   - Performed **GridSearchCV** for hyperparameter tuning.  
   - Identified most influential features via **Feature Importance** and **SHAP** analysis.  

---

## 🧩 Tech Stack  

| Category | Tools & Libraries |
|-----------|------------------|
| **Programming Language** | Python |
| **Data Handling** | pandas, numpy |
| **Visualization** | matplotlib, seaborn |
| **Modeling** | scikit-learn (RandomForestClassifier) |
| **Balancing Technique** | imblearn (SMOTE) |
| **Model Evaluation** | scikit-learn metrics (ROC-AUC, Precision, Recall, F1) |
| **Model Saving** | joblib |
| **Development Environment** | Jupyter Notebook / VS Code |

---

## 📈 Results  

| Metric | Score (Approx.) |
|---------|----------------|
| **Accuracy** | 94% |
| **ROC-AUC** | 0.83 |
| **Precision (Fraud Class)** | 0.75 |
| **Recall (Fraud Class)** | 0.02 |
| **Average Precision (PR-AUC)** | 0.21 |

> ✅ *The model shows strong precision and discrimination ability, but recall for fraud detection can be improved with further tuning.*

---

## 🧠 Key Learnings  

- Learned how to handle **imbalanced datasets** using SMOTE.  
- Built an end-to-end **classification pipeline** with preprocessing and model integration.  
- Understood the importance of **evaluation metrics** beyond accuracy (e.g., ROC-AUC, PR-AUC).  
- Gained insights into **feature importance** and model interpretability using SHAP.  
- Recognized trade-offs between **precision** and **recall** in real-world fraud detection systems.  

---

## 📚 References  

- [Vehicle Insurance Claim Fraud Dataset – Kaggle](https://www.kaggle.com/datasets/shivamb/vehicle-claim-fraud-detection)  
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)  
- [Imbalanced-learn (SMOTE)](https://imbalanced-learn.org/stable/)  
- [SHAP Explainability Library](https://shap.readthedocs.io/en/latest/)  
- [Matplotlib](https://matplotlib.org/) & [Seaborn](https://seaborn.pydata.org/)  

---

> *Each dataset tells a story — it’s our job to make it speak 📊*
