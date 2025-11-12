# 🧠 Day 12 — Iris Flower Classification using SHAP  

> 🎯 *Interpreting Machine Learning Models using SHAP Values (Explainable ML on Iris Dataset)*  

---

## 📘 Overview  

This project focuses on building an interpretable **Random Forest Classifier** for predicting Iris flower species and explaining its predictions using **SHAP (SHapley Additive exPlanations)**.  
The aim is to enhance **model transparency** and understand how each feature influences prediction outcomes through both **global** and **local explainability**.  

---

## 📊 Dataset  

- **Source:** Scikit-learn’s built-in Iris dataset (originally introduced by R.A. Fisher, 1936)  
- **Description:** Contains 150 samples of three Iris species — *Setosa*, *Versicolor*, and *Virginica* — with four numeric features.  
- **Features:** Sepal Length (cm), Sepal Width (cm), Petal Length (cm), Petal Width (cm)  
- **Shape:** (150, 4)  
- **Type:** Multiclass Classification  

---

## ⚙️ Workflow  

1. **Data Exploration & Preprocessing**  
   - Loaded the dataset, explored structure, summary statistics, and feature distributions  
   - Scaled features and mapped target labels for readability  
   - Split data into train and test sets for evaluation  

2. **Model Building & Explainability**  
   - Trained a **Random Forest Classifier** with 200 estimators  
   - Evaluated using accuracy, classification report, confusion matrix, and cross-validation  
   - Applied **SHAP** to interpret feature importance using summary, bar, and waterfall plots  

---

## 🧩 Tech Stack  

| Tool / Library | Purpose |
|-----------------|----------|
| **Python** | Core programming language |
| **Pandas & NumPy** | Data handling and manipulation |
| **Scikit-learn** | Model building and evaluation |
| **Matplotlib & Seaborn** | Data visualization |
| **SHAP** | Model explainability and interpretation |
| **Joblib** | Model saving for deployment |

---

## 📈 Results  

| Metric | Score |
|--------|--------|
| **Accuracy (Test Set)** | 0.8947 |
| **Cross-Validation Mean Accuracy** | 0.9667 |
| **Std. Deviation (CV)** | 0.0211 |
| **Most Influential Features** | Petal Length (cm), Petal Width (cm) |

> ✅ The model achieved high accuracy and strong interpretability, with SHAP confirming that **petal measurements** are the key determinants in species classification.

---

## 🧠 Key Learnings  

- Gained hands-on experience with **Explainable AI (XAI)** concepts using SHAP.  
- Learned to visualize and interpret **feature importance** at both global and local levels.  
- Understood how **Random Forest** handles nonlinear relationships in classification.  
- Observed the importance of **data preprocessing and scaling** for consistent performance.  
- Developed an appreciation for integrating **interpretability tools** in ML pipelines.  

---

## 📚 References  

- Lundberg, S.M., & Lee, S.-I. (2017). *A Unified Approach to Interpreting Model Predictions.*  
  Advances in Neural Information Processing Systems (NIPS), 30.  
  [SHAP Documentation](https://shap.readthedocs.io/en/latest/)  

---

> *Every algorithm is an opportunity to think smarter 🧮*

