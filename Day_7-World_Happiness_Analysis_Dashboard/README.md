# 🧠 Day 7 — World Happiness Analysis Dashboard  

> 🎯 *Streamlit-powered dashboard uncovering global happiness trends through data visualization*  

🌐 **[Deployed App Link → Click Here](https://day-7-world-happiness-report-2015-dashboard.streamlit.app/)**  

---

## 📘 Overview  

This interactive dashboard visualizes the **World Happiness Report 2015**, enabling users to explore how factors such as GDP, health, freedom, and corruption influence happiness across different regions and countries.  

It provides a rich, dynamic view of global well-being metrics through maps, charts, and statistical relationships — all built in Streamlit for real-time exploration.  

---

## 📊 Dataset  

- **Source:** [Kaggle – World Happiness Report 2015](https://www.kaggle.com/datasets/unsdsn/world-happiness)  
- **Description:** Contains happiness scores and related factors for countries worldwide in 2015.  
- **Shape:** `158 rows × 12 columns`  
- **Key Features:**  
  - `Country`, `Region`, `Happiness Rank`, `Happiness Score`  
  - `Economy (GDP per Capita)`, `Family`, `Health (Life Expectancy)`  
  - `Freedom`, `Trust (Government Corruption)`, `Generosity`  

---

## ⚙️ Workflow  

1. **Data Loading & Preprocessing**  
   - Auto-downloads dataset via **KaggleHub** or loads from local CSV  
   - Cleans and renames columns for uniformity  
   - Handles missing values and formatting  

2. **Exploratory Data Analysis (EDA)**  
   - Global choropleth map for happiness distribution  
   - Top 10 happiest countries visualization  
   - Scatter plots for GDP, freedom, and corruption comparisons  

3. **Feature Insights**  
   - Regional happiness averages and shares  
   - Correlation heatmap of numerical features  
   - Dynamic trendline comparison between happiness and any factor  

4. **Dashboard Deployment**  
   - Interactive UI built using **Streamlit** + **Plotly Express**  
   - Deployed seamlessly on **Streamlit Cloud**  

---

## 🧩 Tech Stack  

| Component | Technology Used |
|------------|----------------|
| **Language** | Python 3.12 |
| **Dashboard Framework** | Streamlit |
| **Visualization** | Plotly Express |
| **Data Handling** | Pandas, NumPy |
| **Dataset Access** | KaggleHub |
| **Statistical Modeling** | Statsmodels |
| **Deployment** | Streamlit Cloud |

---

## 📈 Results  

| Visualization | Insight |
|----------------|----------|
| 🌍 Global Map | Shows geographic variation in happiness levels |
| 💸 GDP vs Happiness | High GDP correlates strongly with happiness |
| 🕊️ Freedom vs Corruption | Higher freedom and lower corruption → happier nations |
| 📊 Correlation Heatmap | Identifies strongest predictors of happiness |
| 🏆 Top 10 Chart | Lists countries with the highest happiness scores |

> ✅ *Average Global Happiness Score: 5.38 | Happiest Region: Western Europe*  

---

## 🧠 Key Learnings  

- Learned how to integrate **Kaggle datasets directly** in Streamlit using KaggleHub.  
- Designed **multi-visual dashboards** with dynamic interactivity (filters, sliders, dropdowns).  
- Understood **correlation patterns** between socio-economic indicators and happiness.  
- Gained experience in **data storytelling** using visual analytics.  
- Deployed a complete data app using **Streamlit Cloud** end-to-end.  

---

## 📚 References  

- [Kaggle: World Happiness Report Dataset](https://www.kaggle.com/datasets/unsdsn/world-happiness)  
- [Streamlit Documentation](https://docs.streamlit.io/)  
- [Plotly Express Gallery](https://plotly.com/python/plotly-express/)  
- [World Happiness Report 2015 – UN Sustainable Development Solutions Network](https://worldhappiness.report/)  

---

> *Evolving from code to cognition — the AI way 🤖*  

