import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import plotly.express as px

st.title('US Companies')

df = pd.read_csv('T2000.csv')

us_df = df[df["Country"] == "USA"]  # [DA6] sorted and analyzed data with a pivot table

selected_cols = ["Global Rank", "Company", "Sales ($billion)", "Profits ($billion)", "Longitude_final", "Latitude_final"]
filtered_df = us_df[selected_cols]

filtered_df.set_index('Global Rank', inplace=True)

st.dataframe(filtered_df)

st.subheader('The relationship between profit and sales')

df1 = pd.read_csv('T2000.csv')

df1['Sales ($billion)'] = df1['Sales ($billion)'].astype(float)
df1['Profits ($billion)'] = df1['Profits ($billion)'].astype(float)

us_df = df1[df1['Country'] == 'USA']

top20_us = us_df.sort_values(by='Sales ($billion)', ascending=False).head(20)  # [VIZ3] a scatterplot of the top US 20

fig, ax = plt.subplots(figsize=(10, 6))
sns.scatterplot(
    data=top20_us,
    x='Profits ($billion)',
    y='Sales ($billion)',
    hue='Company',
    color='limegreen',
    s=100,
    ax=ax
)

ax.set_title('Top 20 US Companies: Sales vs. Profits')
ax.set_xlabel('Profits ($billion)')
ax.set_ylabel('Sales ($billion)')
ax.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

st.pyplot(fig)

sales = np.array(df1["Sales ($billion)"])
profits = np.array(df1["Profits ($billion)"])
corr_array = np.corrcoef(sales, profits)
correlation = corr_array[0, 1]

st.write(f"The correlation between Sales and Profits is {correlation:.2f}")


df = pd.read_csv("T2000.csv")

us_df = df[df["Country"] == "USA"]

us_df = us_df[["Company", "Sales ($billion)", "Profits ($billion)"]].dropna()  # [DA1] cleaning the data for empty values

num_companies = st.slider("How many companies to show?", 5, 20, 10)
options = ["Descending", "Ascending"]
sort_order = st.radio("How do you want it to display?", options)

top_df = us_df.sort_values("Profits ($billion)", ascending=False).head(num_companies)

if sort_order == "Ascending":
    top_df = top_df[::-1] #same data, just backwards

# [VIZ5] interactive bar chart
fig = px.bar(
    top_df,
    x="Company",
    y="Profits ($billion)",
    title="Top US Companies by Profit & Sales:",
    color="Sales ($billion)",
    color_continuous_scale="mint",
)

st.plotly_chart(fig)