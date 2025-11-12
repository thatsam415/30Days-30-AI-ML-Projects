# 🧠 Day 9 — Car Price Prediction  

> 🎯 *A Feature-Driven Machine Learning Approach for Predicting Used Car Resale Values with Regression Pipelines*  

---

## 📘 Overview  

This project focuses on developing a data-driven regression model to accurately predict the selling prices of used cars.  
By leveraging **feature engineering** and **automated ML pipelines**, the project uncovers key factors influencing car resale values and builds a scalable, reproducible prediction system.  

---

## 📊 Dataset  

- **Source:** [Kaggle – Vehicle Dataset from Cardekho](https://www.kaggle.com/datasets/nehalbirla/vehicle-dataset-from-cardekho)  
- **Description:** Contains information on 4,340 used cars including manufacturing year, kilometers driven, fuel type, transmission, and ownership details.  
- **Shape:** (4340, 8)  
- **Target Variable:** `selling_price` (continuous)  
- **Feature Types:** Mix of numerical and categorical features  

---

## ⚙️ Workflow  

1. **Data Understanding and Cleaning**  
   - Loaded and explored the dataset to check structure, null values, and unique counts.  
   - Ensured data consistency and removed redundant columns.  

2. **Feature Engineering and Preprocessing**  
   - Created new features such as `Car_Age` and `Price_per_km`.  
   - Built preprocessing pipelines using `ColumnTransformer` for scaling and encoding.  

3. **Model Development**  
   - Trained a `RandomForestRegressor` inside a unified ML pipeline.  
   - Applied log transformation on target variable for variance stabilization.  

4. **Model Evaluation and Interpretation**  
   - Evaluated using **RMSE** and **R² Score** metrics.  
   - Analyzed **feature importances** to identify key price influencers.  

5. **Visualization and Deployment**  
   - Created EDA plots for trend understanding.  
   - Saved trained pipeline (`car_price_pipeline.joblib`) for reuse and deployment.  

---

## 🧩 Tech Stack  

| Category | Tools & Libraries | Purpose |
|-----------|------------------|----------|
| **Data Handling** | Pandas, NumPy | Data manipulation and feature computation |
| **Visualization** | Matplotlib, Seaborn | Data visualization and insights |
| **Machine Learning** | Scikit-learn | Model building, pipelines, preprocessing |
| **Model** | RandomForestRegressor | Predictive regression algorithm |
| **Utilities** | Joblib, Warnings, Filedialpy | Model saving, file handling, warnings control |

---

## 📈 Results  

| Metric | Value | Interpretation |
|---------|--------|----------------|
| **RMSE** | 221,840.41 | Average prediction error ≈ ₹2.2 lakhs |
| **R² Score** | 0.839 | Model explains 83.9% variance in price |
| **Top Features** | Price_per_km, km_driven, fuel_Diesel, Car_Age | Strongest predictors of resale value |

> ✅ The model achieved high accuracy and interpretability, confirming that well-engineered features significantly enhance predictive power.  

---

## 🧠 Key Learnings  

- Feature engineering is crucial for improving model interpretability and accuracy.  
- Automated pipelines prevent data leakage and simplify model deployment.  
- Ensemble models like Random Forests handle complex non-linear relationships effectively.  
- Log-transforming the target variable can stabilize variance and improve regression performance.  
- Proper evaluation using RMSE and R² ensures reliable model validation.  

---

## 📚 References  

- [Scikit-learn Documentation](https://scikit-learn.org/stable/documentation.html)  
- [Pandas Documentation](https://pandas.pydata.org/docs/)  
- [NumPy Documentation](https://numpy.org/doc/)  
- [Matplotlib Documentation](https://matplotlib.org/stable/index.html)  
- [Seaborn Documentation](https://seaborn.pydata.org/)  
- Géron, A. (2022). *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow (3rd Ed.)*  
- James, G., Witten, D., Hastie, T., & Tibshirani, R. (2021). *An Introduction to Statistical Learning (2nd Ed.)*  

---

> *Practicing precision, patience, and progress in ML 🧩*

