# 🏡 Day 4 — Regularization on California Housing Dataset  

> 🎯 *Regularization Techniques Comparison: Lasso vs Ridge vs ElasticNet*  

---

## 📘 Overview  

A comparative analysis of **Lasso**, **Ridge**, and **ElasticNet** regularization techniques applied to the **California Housing Dataset**.  
The project demonstrates how regularization improves model **stability**, **generalization**, and **interpretability** in linear regression.  

---

## 📊 Dataset  

- **Source:** `fetch_california_housing()` from Scikit-learn  
- **Description:** Real-world regression dataset derived from the 1990 U.S. Census, predicting median house values based on demographics and housing features.  
- **Shape:** 20,640 samples × 9 columns (8 features + 1 target)  
- **Target Variable:** `MedHouseVal` — Median house value (in $100,000s)  

| Feature | Description |
|----------|-------------|
| MedInc | Median income in the block group |
| HouseAge | Average age of houses |
| AveRooms | Average number of rooms per household |
| AveBedrms | Average number of bedrooms |
| Population | Population of the block group |
| AveOccup | Average number of occupants per household |
| Latitude | Latitude coordinate |
| Longitude | Longitude coordinate |

---

## ⚙️ Workflow  

1. **📥 Data Loading & Preprocessing**  
   - Loaded dataset using `fetch_california_housing()`  
   - Checked missing values, data types, and summary statistics  
   - Scaled numerical features using `StandardScaler()`  

2. **📈 Model Development & Evaluation**  
   - Trained **Linear Regression (OLS)** as a baseline  
   - Applied **Lasso**, **Ridge**, and **ElasticNet** with cross-validation  
   - Compared models using **R²**, **RMSE**, and **non-zero coefficients**  
   - Visualized coefficient magnitudes, Lasso paths, and residuals  

3. **💾 Model Saving**  
   - Saved trained models using **Joblib** for future predictions  

---

## 🧩 Tech Stack  

| Category | Tools & Libraries |
|-----------|-------------------|
| **Language** | Python 3.x |
| **Data Handling** | Pandas, NumPy |
| **Machine Learning** | Scikit-learn |
| **Visualization** | Matplotlib |
| **Model Persistence** | Joblib |
| **Environment** | Jupyter Notebook |

---

## 📈 Results  

| Model | R² Score | RMSE | Non-zero Coefficients | Observation |
|--------|-----------|------|-----------------------|--------------|
| **Linear Regression (OLS)** | 0.5758 | 0.7456 | 8 | Baseline model |
| **Lasso Regression (L1)** | **0.5765** | **0.7450** | 8 | Slight improvement; minimal shrinkage |
| **Ridge Regression (L2)** | 0.5758 | 0.7456 | 8 | Similar to OLS; smoother coefficients |
| **ElasticNet (L1 + L2)** | 0.5765 | 0.7450 | 8 | Balanced effect between Lasso and Ridge |

> ✅ *Regularization slightly improved generalization and model stability while maintaining simplicity and interpretability.*

---

## 🧠 Key Learnings  

- Understood how **L1, L2, and ElasticNet** regularization affect linear regression models.  
- Learned to use **cross-validation** for tuning hyperparameters like `alpha` and `l1_ratio`.  
- Observed that **regularization controls overfitting** by shrinking large coefficients.  
- Gained experience in **visualizing model behavior** through coefficient paths and residual plots.  
- Learned **model saving** and reusability using Joblib for real-world applications.  

---

## 📚 References  

- [Scikit-learn Documentation — Linear Models](https://scikit-learn.org/stable/modules/linear_model.html)  
- [Scikit-learn Datasets — California Housing](https://scikit-learn.org/stable/datasets/real_world.html#california-housing-dataset)  

---

> *From raw data to refined predictions — learning never stops 📈*

