# 🧠 Day 13 — Breast Cancer Classification 

> 🎯 *Supervised Learning Approach for Medical Diagnosis with Hyperparameter-Tuned Random Forest Models.*

---

## 📘 Overview  

This project builds a complete machine learning workflow to classify breast tumors as malignant or benign using the Breast Cancer Wisconsin dataset.  
Through preprocessing, EDA, model building, hyperparameter tuning, and feature analysis, the project delivers a reliable and interpretable diagnostic model.  
The final tuned Random Forest model achieves **96% accuracy**, making it suitable for medical decision-support applications.

---

## 📊 Dataset  

- **Source:** UCI Machine Learning Repository / Scikit-Learn  
- **Description:** Contains 569 samples and 30 diagnostic features characterizing breast tumors  
- **Shape:** 569 rows × 30 features + 1 target  
- **Target:**  
  - 0 → Malignant  
  - 1 → Benign  

---

## ⚙️ Workflow  

1. **Data Loading & Exploration**  
   - Viewed structure, info, summary statistics  
   - Checked missing values, duplicates, class distribution  

2. **Preprocessing & EDA**  
   - Feature-target separation, train-test split, scaling  
   - Visualized target distribution and correlation heatmap  

3. **Model Building & Tuning**  
   - Built baseline Random Forest model  
   - Applied GridSearchCV for hyperparameter optimization  

4. **Evaluation & Insights**  
   - Compared baseline vs tuned model performance  
   - Analyzed feature importance  

5. **Model Saving**  
   - Saved trained model and scaler for future deployment  

---

## 🧩 Tech Stack  

| Category | Tools / Libraries |
|---------|--------------------|
| Language | Python |
| ML Framework | Scikit-Learn |
| Data Handling | Pandas, NumPy |
| Visualization | Matplotlib, Seaborn |
| Model Saving | Joblib / Pickle |
| Environment | Jupyter Notebook |

---

## 📈 Results  

| Metric | Baseline RF | Tuned RF |
|--------|-------------|----------|
| Accuracy | 96.49% | 96.49% |
| Precision (Malignant) | 0.98 | 0.98 |
| Recall (Malignant) | 0.93 | 0.93 |
| Precision (Benign) | 0.96 | 0.96 |
| Recall (Benign) | 0.99 | 0.99 |
| Best Params | — | `{n_estimators:200, max_depth:None, min_samples_split:2, min_samples_leaf:1, bootstrap:True}` |

> ✅ *The Random Forest model performs consistently well both before and after tuning, showing excellent stability and generalization.*  

---

## 🧠 Key Learnings  

- Built an end-to-end ML pipeline from preprocessing to evaluation.  
- Used GridSearchCV for systematic hyperparameter tuning.  
- Understood how Random Forest identifies important diagnostic features.  
- Evaluated medical ML models using precision, recall, and confusion matrices.  
- Learned how to save and prepare models for deployment.

---

## 📚 References  

- UCI Breast Cancer Wisconsin Dataset  
- Scikit-Learn Documentation  
- Breiman, L. (2001). *Random Forests*  
- Seaborn & Matplotlib Documentation  

---

> *Model by model, building the foundations of intelligence 🏗️*

