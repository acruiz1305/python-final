"""
Name: Andrea Ruiz
CS 230: Section 05
Data: Top 2000 Global Companies
URL:

Description:

This program analyzes the top 2000 global companies with various charts and graphs. It explores
different features such as looking at the top 10, a map with their location, a scatterplot, distribution
plot, pie chart, bar charts and more! Some even include an analysis of what the data signifies. There
are interactive features, such as the map, a quiz, panda dataframe, bar chart and more. It also has
different web pages for organization. It includes modules learned in class and three extras: CSV, Seaborn
and Plotly Express. This program shows the capabilities of python and coding. I hope you enjoy 😊

"""

import streamlit as st
import csv
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


st.title('Top 2000 Global Companies')
st.write('Made by Andrea Ruiz')

st.header('What is a top 2000 company?')
st.text('A top 2000 company one that is ranked by sales, profit, assets and market value globally. It varies from industry to country. The Forbes Global 2000 is created by Forbes magazine, who seek out the highest ranking companies out there. See below for a few of them!')

st.header('Top 10 Companies')



with open('T2000.csv', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    data = list(reader)

df = pd.DataFrame(data)

df['Sales ($billion)'] = df['Sales ($billion)'].astype(float)

df = df.dropna(subset=['Sales ($billion)', 'Company'])

top10_df = df.sort_values(by='Sales ($billion)', ascending=False).head(10) #[DA3] find the top largest in a column


# [VIZ1] bar chart using seaborn
plt.figure(figsize=(12, 6))
lime_greens = ["#f0ffd6","#e5ffad","#daff85","#cfff5c","#c2ff33","#b3ff00","#a3e600","#94cc00","#85b300","#769900"]
sns.barplot(
    x='Company',
    y='Sales ($billion)',
    data=top10_df,
    palette=lime_greens
)

plt.title('Top 10 Global Companies by Sales ($ Billion)')
plt.xlabel('Company')
plt.ylabel('Sales ($ Billion)')
plt.xticks(rotation=45, ha='right')

st.pyplot(plt.gcf())




st.header('About this website')
st.text('Explore this website to learn about the companies location, key metrics, analysis and more! There are lots of interactive features and fun graphs to heighten your learning. ')



