# 🏭 Day 6 - Predictive Maintenance System  

> 🎯 *Machine Failure Prediction System using Logistic Regression on AI4I 2020 Sensor Data*

---

## 📘 Overview  

This project focuses on developing a **Predictive Maintenance System** that anticipates industrial machine failures before they occur.  
By leveraging **Logistic Regression** and the **AI4I 2020 Predictive Maintenance Dataset**, this system analyzes sensor parameters such as temperature, torque, rotational speed, and tool wear to predict machine health.  
The model enables early fault detection, reduces downtime, and supports data-driven maintenance scheduling in industrial environments.

---

## 📊 Dataset  

- **Source:** [AI4I 2020 Predictive Maintenance Dataset — UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/datasets/AI4I+2020+Predictive+Maintenance+Dataset)  
- **Description:** Contains 10,000 simulated records of industrial sensor data with operational and failure indicators.  
- **Shape:** 10,000 rows × 14 columns  
- **Target Variable:** `Machine failure` (0 = No Failure, 1 = Failure)  

| Feature | Description |
|----------|-------------|
| Type | Machine type (L, M, H) |
| Air temperature [K] | Ambient air temperature |
| Process temperature [K] | Internal process temperature |
| Rotational speed [rpm] | Rotational speed of the equipment |
| Torque [Nm] | Rotational force applied |
| Tool wear [min] | Duration of tool usage |
| TWF, HDF, PWF, OSF, RNF | Specific failure types |

---

## ⚙️ Workflow  

1. **Data Understanding & Cleaning**  
   - Explored dataset structure, verified data types, and checked for null values.  
   - Cleaned column names and ensured consistency.  

2. **Feature Engineering & Selection**  
   - Derived new feature `Temp_diff = Process_Temperature - Air_Temperature`.  
   - Dropped irrelevant identifiers (`UDI`, `Product_ID`, etc.).  

3. **Preprocessing Pipeline**  
   - Numeric features: imputed & standardized using `StandardScaler`.  
   - Categorical features: encoded using `OneHotEncoder`.  

4. **Model Development**  
   - Built Logistic Regression pipeline with preprocessing.  
   - Trained model on 80% training data, validated on 20% test data.  

5. **Model Evaluation**  
   - Evaluated with metrics: Accuracy, Precision, Recall, F1, ROC-AUC.  
   - Visualized results using Confusion Matrix & ROC Curve.  

6. **Interpretation & Insights**  
   - Analyzed logistic regression coefficients for feature importance.  
   - Identified key drivers of machine failure (Torque, Tool Wear, Temperature Difference).  

---

## 🧩 Tech Stack  

| Category | Tools / Libraries |
|-----------|------------------|
| **Language** | Python |
| **Data Manipulation** | pandas, numpy |
| **Visualization** | matplotlib, seaborn |
| **Machine Learning** | scikit-learn |
| **Preprocessing** | StandardScaler, OneHotEncoder, ColumnTransformer |
| **Evaluation** | accuracy_score, confusion_matrix, roc_auc_score |
| **Environment** | Jupyter Notebook |

---

## 📈 Results  

| Metric | Description | Value |
|---------|--------------|--------|
| **Accuracy** | Overall model performance | ~97% |
| **Precision** | Reliability of positive predictions | High |
| **Recall** | Correctly detected failures | High |
| **ROC-AUC** | Ability to distinguish classes | ≈ 0.99 |

> ✅ The model achieved strong performance and reliability while maintaining interpretability through logistic regression coefficients.

---

## 🧠 Key Learnings  

- Learned how to design a complete ML pipeline for **predictive maintenance**.  
- Understood the importance of **data preprocessing** and feature scaling in linear models.  
- Gained insights into **interpreting logistic regression coefficients** for industrial datasets.  
- Discovered how derived features like **temperature difference** improve predictive accuracy.  
- Strengthened skills in **model evaluation** using confusion matrices and ROC-AUC visualization.  

---

## 📚 References  

- [AI4I 2020 Predictive Maintenance Dataset (UCI)](https://archive.ics.uci.edu/ml/datasets/AI4I+2020+Predictive+Maintenance+Dataset)  
- [Scikit-learn Documentation](https://scikit-learn.org/stable/)  
- [Seaborn Visualization Library](https://seaborn.pydata.org/)  
- [Matplotlib Official Guide](https://matplotlib.org/)  
- Yedjou, S. M. (2020). *AI4I 2020 Predictive Maintenance Dataset: A Benchmark for Industry 4.0 Machine Learning.*

---

> *Data-driven learning, one layer deeper each day 🌊*

