# app.py
# 🌍 World Happiness Report 2015 Dashboard | Streamlit + Plotly 

import streamlit as st
import pandas as pd
import plotly.express as px
import kagglehub
from kagglehub import KaggleDatasetAdapter
import os


# -------------------------------------------------------
# 1. Page Setup
# -------------------------------------------------------
st.set_page_config(page_title="🌍 World Happiness Dashboard", layout="wide")
st.title("😊 World Happiness Analysis Dashboard")
st.caption("An interactive data visualization dashboard analyzing global happiness insights using Streamlit and Plotly.")
st.markdown("""
    <style>
        [data-testid="stSidebar"] {
            min-width: 350px;
            max-width: 350px;
        }
        [data-testid="stSidebarNav"] {
            background-color: #0e1117;
        }
        [data-testid="stSidebar"] .css-1v3fvcr {
            padding-right: 20px;
        }
        [data-testid="stSidebar"] {
            overflow-y: auto;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
# 2. Load Dataset
# -------------------------------------------------------
# Load the latest version
try:
    # Load dataset from Kaggle if not found locally
    DATASET_NAME = "unsdsn/world-happiness"
    FILE_PATH = "2015.csv"

    if not os.path.exists(FILE_PATH):
        st.warning("Downloading dataset from Kaggle...")
        df = kagglehub.load_dataset(
            KaggleDatasetAdapter.PANDAS,
            DATASET_NAME,
            FILE_PATH
        )
        df.to_csv(FILE_PATH, index=False)
        st.success("Dataset downloaded and saved locally ✅")
    else:
        df = pd.read_csv(FILE_PATH)

except Exception as e:
    st.error(f"⚠️ Error loading dataset: {e}")


# Rename columns for consistency
df.rename(columns={
    'Country': 'Country',
    'Region': 'Region',
    'Happiness Rank': 'Rank',
    'Happiness Score': 'Happiness Score',
    'Economy (GDP per Capita)': 'GDP per Capita',
    'Health (Life Expectancy)': 'Life Expectancy',
    'Freedom': 'Freedom',
    'Trust (Government Corruption)': 'Corruption',
    'Family': 'Social Support'
}, inplace=True, errors='ignore')

# -------------------------------------------------------
# 3. Sidebar Filters
# -------------------------------------------------------
st.sidebar.header("🎛️ Filter Options")

min_score = float(df["Happiness Score"].min())
max_score = float(df["Happiness Score"].max())

score_range = st.sidebar.slider("Select Happiness Score Range", min_score, max_score, (min_score, max_score))
regions = sorted(df["Region"].dropna().unique())
selected_region = st.sidebar.multiselect("Select Region(s)", regions, default=regions)

filtered_df = df[
    (df["Happiness Score"] >= score_range[0]) &
    (df["Happiness Score"] <= score_range[1]) &
    (df["Region"].isin(selected_region))
]

# -------------------------------------------------------
# 4. Global Map
# -------------------------------------------------------
st.subheader("🌍 Global Happiness Scores (2015)")
fig_map = px.choropleth(
    filtered_df,
    locations="Country",
    locationmode="country names",
    color="Happiness Score",
    hover_name="Country",
    color_continuous_scale="Viridis",
    title="Happiness Score by Country - 2015"
)
fig_map.update_layout(height=500, margin={"r":0,"t":50,"l":0,"b":0})
st.plotly_chart(fig_map, use_container_width=True)

# -------------------------------------------------------
# 5. Top 10 Happiest Countries
# -------------------------------------------------------
st.subheader("🏆 Top 10 Happiest Countries")
top10 = filtered_df.nlargest(10, "Happiness Score")
fig_bar = px.bar(
    top10,
    x="Country",
    y="Happiness Score",
    color="Happiness Score",
    color_continuous_scale="Tealgrn",
    title="Top 10 Happiest Countries (2015)"
)
fig_bar.update_layout(xaxis_title="", yaxis_title="Happiness Score", height=400)
st.plotly_chart(fig_bar, use_container_width=True)

# -------------------------------------------------------
# 6. GDP vs Happiness
# -------------------------------------------------------
st.subheader("📈 GDP per Capita vs Happiness Score")
fig_scatter = px.scatter(
    filtered_df,
    x="GDP per Capita",
    y="Happiness Score",
    size="Social Support",
    color="Region",
    hover_name="Country",
    title="GDP vs Happiness (Bubble size = Social Support)",
)
fig_scatter.update_layout(height=500)
st.plotly_chart(fig_scatter, use_container_width=True)

# -------------------------------------------------------
# 7. Average Happiness by Region
# -------------------------------------------------------
st.subheader("🌎 Average Happiness by Region")
region_avg = df.groupby("Region")["Happiness Score"].mean().sort_values(ascending=False).reset_index()
fig_region = px.bar(
    region_avg,
    x="Region",
    y="Happiness Score",
    color="Happiness Score",
    color_continuous_scale="Blues",
    title="Average Happiness Score by Region"
)
fig_region.update_layout(xaxis_title="", yaxis_title="Avg Happiness Score", height=400)
st.plotly_chart(fig_region, use_container_width=True)

# -------------------------------------------------------
# 8. Freedom vs Corruption
# -------------------------------------------------------
st.subheader("🕊️ Freedom vs Corruption by Region")
fig_fc = px.scatter(
    filtered_df,
    x="Freedom",
    y="Corruption",
    size="Happiness Score",
    color="Region",
    hover_name="Country",
    title="Freedom vs Corruption (Lower Corruption = Happier Nations)"
)
fig_fc.update_layout(height=500)
st.plotly_chart(fig_fc, use_container_width=True)

# -------------------------------------------------------
# 9. Regional Share of Global Happiness
# -------------------------------------------------------
st.subheader("🥧 Regional Share of Global Happiness")
region_sum = df.groupby("Region")["Happiness Score"].sum().reset_index()
fig_pie = px.pie(
    region_sum,
    names="Region",
    values="Happiness Score",
    title="Regional Share of Total Happiness (2015)",
    hole=0.4
)
st.plotly_chart(fig_pie, use_container_width=True)

# -------------------------------------------------------
# 10. Correlation Heatmap
# -------------------------------------------------------
st.subheader("🔥 Correlation Between Numeric Features")
numeric_df = filtered_df.select_dtypes(include=['float64', 'int64'])
corr = numeric_df.corr()
fig_corr = px.imshow(
    corr,
    text_auto=True,
    color_continuous_scale="RdBu_r",
    title="Feature Correlation Heatmap"
)
fig_corr.update_layout(height=500)
st.plotly_chart(fig_corr, use_container_width=True)

# -------------------------------------------------------
# 11. Correlation Strength with Happiness
# -------------------------------------------------------
st.subheader("📊 Correlation Strength with Happiness Score")
corr_strength = corr["Happiness Score"].drop("Happiness Score").sort_values(ascending=True)
fig_corr_strength = px.bar(
    corr_strength,
    x=corr_strength.values,
    y=corr_strength.index,
    orientation='h',
    color=corr_strength.values,
    color_continuous_scale="Viridis",
    title="Correlation of Each Feature with Happiness Score"
)
fig_corr_strength.update_layout(height=400, xaxis_title="Correlation", yaxis_title="")
st.plotly_chart(fig_corr_strength, use_container_width=True)

# -------------------------------------------------------
# 12. Dynamic Comparison
# -------------------------------------------------------
st.subheader("🎯 Compare Any Feature with Happiness Score")
numeric_cols = numeric_df.columns.tolist()
selected_feature = st.selectbox("Select Feature", [col for col in numeric_cols if col != "Happiness Score"])

fig_compare = px.scatter(
    df,
    x=selected_feature,
    y="Happiness Score",
    color="Region",
    hover_name="Country",
    trendline="ols",
    title=f"{selected_feature} vs Happiness Score (2015)"
)
st.plotly_chart(fig_compare, use_container_width=True)

# -------------------------------------------------------
# 13. Key Insights Summary
# -------------------------------------------------------
st.markdown("### 💬 Key Insights")
st.info(f"""
- 🌍 **Average Global Happiness Score:** {df['Happiness Score'].mean():.2f}  
- 🏆 **Happiest Country:** {df.loc[df['Happiness Score'].idxmax(), 'Country']}  
- 😞 **Least Happy Country:** {df.loc[df['Happiness Score'].idxmin(), 'Country']}  
- 🌎 **Happiest Region:** {region_avg.iloc[0]['Region']}  
- 🌍 **Least Happy Region:** {region_avg.iloc[-1]['Region']}  
- 📊 **Score Gap (Top vs Bottom Region):** {(region_avg['Happiness Score'].max() - region_avg['Happiness Score'].min()):.2f} points  
- 💸 **Most Influential Factor:** {corr_strength.idxmax()} (Correlation = {corr_strength.max():.2f})  
- ⚖️ **Least Influential Factor:** {corr_strength.idxmin()} (Correlation = {corr_strength.min():.2f})  
- 💭 Countries with **higher GDP**, **social support**, and **life expectancy** consistently score higher on happiness.  
- 🚫 Regions with **higher corruption** and **lower freedom** show significantly lower happiness scores.  
""")

# -------------------------------------------------------
# 14. Download Filtered Data
# -------------------------------------------------------
st.download_button(
    label="📥 Download Filtered Data as CSV",
    data=filtered_df.to_csv(index=False).encode('utf-8'),
    file_name="filtered_happiness_2015.csv",
    mime="text/csv"
)

# -------------------------------------------------------
# 15. Sidebar Information
# -------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.info("""
📘 **About this Dashboard**

This interactive dashboard visualizes the **World Happiness Report (2015)**.  
It lets you explore:
- Global and regional happiness trends  
- GDP, health, and freedom correlations  
- Feature relationships and heatmaps  
- Downloadable filtered data  

Built using **Streamlit + Plotly + Pandas**
""")







