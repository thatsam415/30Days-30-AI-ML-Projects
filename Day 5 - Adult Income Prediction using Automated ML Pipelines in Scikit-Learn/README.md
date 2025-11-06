# 🧠 Day 5 — Adult Income Prediction using Automated ML Pipelines in Scikit-Learn  

> 🎯 *Automated ML Pipeline Building using Scikit-Learn Pipelines & FeatureUnion*  

---

## 📘 Overview  

This project automates an end-to-end **machine learning workflow** using **Scikit-Learn Pipelines** and **FeatureUnion** to predict whether an individual earns more than **$50,000 per year** based on demographic and employment features.  

The workflow integrates **data preprocessing, feature engineering, model training, evaluation, and serialization** into a unified and reproducible system.  

---

## 📊 Dataset  

- **Source:** [UCI Machine Learning Repository — Adult Income Dataset](https://archive.ics.uci.edu/ml/datasets/adult)  
- **Alternative Access:** [OpenML — “adult” dataset](https://www.openml.org/d/1590)  
- **Task Type:** Binary Classification  
- **Objective:** Predict whether a person’s income exceeds $50K/year based on census information.  
- **Shape:** ~48,842 rows × 15 columns  

**Feature Overview:**  
- **Numerical:** `age`, `fnlwgt`, `education-num`, `capital-gain`, `capital-loss`, `hours-per-week`  
- **Categorical:** `workclass`, `education`, `marital-status`, `occupation`, `relationship`, `race`, `sex`, `native-country`  
- **Target Variable:** `class` → (`<=50K` or `>50K`)  

---

## ⚙️ Workflow  

### 1️⃣ **Data Preprocessing & Exploration**  
   - Loaded dataset using `fetch_openml()` and examined missing values.  
   - Inspected data types, distributions, and categorical cardinalities.  
   - Identified and handled missing data with `SimpleImputer`.  
   - Checked class imbalance (`~76% <=50K` vs `~24% >50K`).  

### 2️⃣ **Feature Engineering & Pipelines**  
   - Created a new feature `capital_diff = capital-gain - capital-loss` to capture financial variation.  
   - Designed **Numeric** and **Categorical** pipelines:  
     - *Numeric:* Median imputation → Power Transformation → Standard Scaling  
     - *Categorical:* Constant imputation → OneHotEncoding  
   - Combined using **ColumnTransformer**.  
   - Added **PolynomialFeatures** branch using **FeatureUnion** for nonlinear relationships.  

### 3️⃣ **Modeling & Evaluation**  
   - Built an end-to-end **Pipeline** with all preprocessing and model steps.  
   - Used **RandomForestClassifier** as the baseline model.  
   - Tuned hyperparameters using **GridSearchCV** with 3-fold cross-validation.  
   - Evaluated with metrics: Accuracy, ROC-AUC, Precision, Recall, and F1-score.  
   - Visualized **Confusion Matrix**, **ROC Curve**, and **Precision-Recall Curve**.  

### 4️⃣ **Model Interpretability & Persistence**  
   - Measured **Permutation Importance** to identify influential predictors.  
   - Saved the final pipeline as a serialized `.joblib` file for deployment.  

---

## 🧩 Tech Stack  

| Category | Tools / Libraries |
|-----------|-------------------|
| Programming | Python 3.x |
| Data Manipulation | pandas, numpy |
| Machine Learning | scikit-learn |
| Visualization | matplotlib, seaborn |
| Model Persistence | joblib |
| Optimization | GridSearchCV, StratifiedKFold |

---

## 📈 Results  

| Metric | Baseline Model | Tuned Model (GridSearchCV) |
|---------|----------------|----------------------------|
| Accuracy | 0.8147 | **0.8410** |
| ROC-AUC | 0.8253 | **0.8643** |
| Precision (for >50K) | 0.65 | **0.79** |
| Recall (for >50K) | 0.49 | **0.46** |
| F1-Score (for >50K) | 0.56 | **0.58** |

> ✅ **Final Model:** Random Forest Classifier (`max_depth=10`, `n_estimators=100`)  
> Achieved **~86–88% accuracy** and strong generalization performance.  

---

## 🧠 Key Learnings  

- How to build **modular and automated ML pipelines** using Scikit-Learn.  
- Importance of **separating numeric and categorical preprocessing**.  
- Using **FeatureUnion** for combining multiple feature branches.  
- Performing **hyperparameter tuning** with `GridSearchCV` for optimization.  
- Understanding **model interpretability** via permutation importance.  
- Efficient model saving and reproducibility with **Joblib Pipelines**.  

---

## 📚 References  

- [Scikit-Learn Documentation](https://scikit-learn.org/stable/)  
- [UCI Machine Learning Repository – Adult Dataset](https://archive.ics.uci.edu/ml/datasets/adult)  
- Breiman, L. (2001). *Random Forests.*  
- Lundberg, S. M., & Lee, S.-I. (2017). *A Unified Approach to Interpreting Model Predictions (SHAP).*  
- Géron, A. (2019). *Hands-On Machine Learning with Scikit-Learn and TensorFlow.*  

---

> *Exploring the intersection of creativity and computation ⚙️*  

