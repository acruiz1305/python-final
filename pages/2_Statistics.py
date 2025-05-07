import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Stats & Analysis')

# [PY5] a dictionary to access keys and values
continent_counts = {}
with open('T2000.csv', 'r', encoding='utf-8') as file:
    header = file.readline()  # skip header
    for line in file:
        values = line.strip().split(',')
        continent = values[7]

        if continent in ['USA', 'Africa']:
            continent = 'Other'
        continent_counts[continent] = continent_counts.get(continent, 0) + 1

labels = list(continent_counts.keys())
sizes = list(continent_counts.values())

lime_greens = ["#f0ffd6","#e5ffad","#daff85","#cfff5c","#c2ff33","#b3ff00","#a3e600","#94cc00","#85b300","#769900"]

sns.set_style("white")
plt.figure(figsize=(8, 8))

plt.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    colors=lime_greens,
)

plt.title('Top 2000 Companies by Continent', fontsize=14, pad=20)

st.pyplot(plt.gcf())

adjust_example2 = '<p style="font-family:Franklin Gothic Medium; color:#f70078; font-size: 25px;">1. Economic Powerhouses Drive Corporate Presence'
st.markdown(adjust_example2, unsafe_allow_html=True)

adjust_example3 = '<p style="font-family:Franklin Gothic Medium; color:#32CD32; font-size: 15px;">Asia leads the pack thanks to giants like China, Japan, South Korea, and increasingly India. These nations combine strong manufacturing, massive domestic markets, and government support for growth. China alone makes up a huge portion of Asia’s share, especially in banking, telecom, and energy.'
st.markdown(adjust_example3, unsafe_allow_html=True)

adjust_example4 = '<p style="font-family:Franklin Gothic Medium; color:#32CD32; font-size: 15px;">North America’s 32.6% is fueled mostly by the U.S., the world’s largest economy with deep capital markets and global tech, finance, and healthcare leaders. Canada adds strength with key players in banking and natural resources.'
st.markdown(adjust_example4, unsafe_allow_html=True)

adjust_example5 = '<p style="font-family:Franklin Gothic Medium; color:#f70078; font-size: 25px;">2. Europe: Aging Giants with Structural Constraints'
st.markdown(adjust_example5, unsafe_allow_html=True)

adjust_example6 = '<p style="font-family:Franklin Gothic Medium; color:#32CD32; font-size: 15px;">Europe’s 23.9% reflects its industrial legacy. While countries like Germany, the UK, and France still host major corporations, growth has been slower. Regulatory complexity, aging populations, and less aggressive investment in tech have limited its recent momentum.'
st.markdown(adjust_example6, unsafe_allow_html=True)

adjust_example7 = '<p style="font-family:Franklin Gothic Medium; color:#f70078; font-size: 25px;">3. Underrepresentation: Scale and History'
st.markdown(adjust_example7, unsafe_allow_html=True)

adjust_example8 = '<p style="font-family:Franklin Gothic Medium; color:#32CD32; font-size: 15px;">South America (2%), Oceania (2.2%), and "Other" regions (1.4%) are underrepresented mostly due to smaller economies and historical factors. Political instability, weaker capital markets, and limited exposure to high-growth industries like tech all play a role. Oceania, mostly Australia, still stands out in mining and finance.'
st.markdown(adjust_example8, unsafe_allow_html=True)

adjust_example9 = '<p style="font-family:Franklin Gothic Medium; color:#32CD32; font-size: 15px;">Regions like Africa and parts of the Middle East face similar barriers—lower GDPs, fewer publicly listed firms, and a reliance on state-run enterprises that often don’t appear in these rankings.'
st.markdown(adjust_example9, unsafe_allow_html=True)


st.subheader('Lowest Profitable Companies: ')
df = pd.read_csv('T2000.csv')
df.set_index('Global Rank')

bottom_3 = df.sort_values(by='Profits ($billion)').head(3) #[DA2] sort in ascending order for bottom 3

st.write(bottom_3[['Company', 'Profits ($billion)']])
adjust_example1 = '<p style="font-family:Franklin Gothic Medium; color:#a5a7a8; font-size: 13px;">This doesnt account for revenue by the way :)'
st.markdown(adjust_example1, unsafe_allow_html=True)

adjust_example10 = '<p style="font-family:Franklin Gothic Medium; color:#f70078; font-size: 25px;"> Negative Profit Margins Among Financial Institutions:'
st.markdown(adjust_example10, unsafe_allow_html=True)

adjust_example11 = '<p style="font-family:Franklin Gothic Medium; color:#32CD32; font-size: 15px;">The reported losses from Bankia (-$24.5 billion), Dexia (-$16.2 billion), and the National Bank of Greece (-$16.0 billion) highlight the vulnerabilities of financial institutions operating under systemic stress. These figures represent some of the steepest losses among the top 2000 global companies, and all three entities share a common thread: exposure to severe economic or sovereign debt crises.'
st.markdown(adjust_example11, unsafe_allow_html=True)

adjust_example12 = '<p style="font-family:Franklin Gothic Medium; color:#f70078; font-size: 25px;">1. Bankia (Spain, -$24.5B)'
st.markdown(adjust_example12, unsafe_allow_html=True)

adjust_example13 = '<p style="font-family:Franklin Gothic Medium; color:#32CD32; font-size: 15px;">Bankias massive loss is emblematic of Spains banking crisis following the 2008 global financial meltdown and the bursting of its real estate bubble. Poor risk management, overexposure to bad loans, and structural weaknesses led to its partial nationalization in 2012. The losses reflect both direct write-downs and the cost of restructuring.'
st.markdown(adjust_example13, unsafe_allow_html=True)

adjust_example14 = '<p style="font-family:Franklin Gothic Medium; color:#f70078; font-size: 25px;">2. Dexia (Belgium/France, -$16.2B)'
st.markdown(adjust_example14, unsafe_allow_html=True)

adjust_example15 = '<p style="font-family:Franklin Gothic Medium; color:#32CD32; font-size: 15px;">Dexias collapse is tied to the European sovereign debt crisis. As a major lender to governments and municipalities, its overreliance on short-term funding backfired when confidence in sovereign debt markets evaporated. It required multiple bailouts, and the loss reflects deteriorated asset values and rescue costs.'
st.markdown(adjust_example15, unsafe_allow_html=True)

adjust_example16 = '<p style="font-family:Franklin Gothic Medium; color:#f70078; font-size: 25px;">3. National Bank of Greece (-$16.0B)'
st.markdown(adjust_example16, unsafe_allow_html=True)

adjust_example17 = '<p style="font-family:Franklin Gothic Medium; color:#32CD32; font-size: 15px;">Greeces prolonged economic crisis, marked by austerity, high unemployment, and default risk, severely impacted its financial sector. The National Bank of Greece faced massive loan defaults, devaluation of sovereign bonds, and capital flight—all contributing to its multi-billion-dollar loss.'
st.markdown(adjust_example17, unsafe_allow_html=True)



st.subheader('Cumulative Sales (in Billions)')
df1 = pd.read_csv('T2000.csv')

pivot_df = df1.pivot_table('Sales ($billion)', 'Continent', aggfunc='sum') # [DA9] perform a calculation on a column (sum) values
st.dataframe(pivot_df)


st.subheader('Distribution of Companies and Sales')
df1 = pd.read_csv('T2000.csv')

df1 = df.sort_values(by="Sales ($billion)", ascending=False).head(127)

plot = sns.displot(df1, x="Sales ($billion)", kde=True, color='#9EF01A') # [VIZ4] a distribution plot

plot.set_axis_labels('Sales ($ Billion)', 'Frequency (Number of companies)')

st.pyplot(plot.fig)

adjust_example18 = '<p style="font-family:Franklin Gothic Medium; color:#f70078; font-size: 15px;">A right-skewed distribution (also known as a positively skewed distribution) occurs when the right tail (larger values) is longer or fatter than the left tail. In the context of this distribution for the top 30 global companies sales, it suggests that most companies have relatively lower sales, but a few companies have very high sales, which pull the distributions tail to the right.'
st.markdown(adjust_example18, unsafe_allow_html=True)

adjust_example19 = '<p style="font-family:Franklin Gothic Medium; color:#f70078; font-size: 15px;">This indicates that a small number of companies dominate in sales, while the majority have more modest figures. For analysis, this may suggest the need for logarithmic transformations or different statistical methods to account for the extreme values.'
st.markdown(adjust_example19, unsafe_allow_html=True)

adjust_example20 = '<p style="font-family:Franklin Gothic Medium; color:#a5a7a8; font-size: 13px;">All text paragraphs come from generative AI. In no way may it all be correct. This is just for decorative purposes'
st.markdown(adjust_example20, unsafe_allow_html=True)




