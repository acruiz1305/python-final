import streamlit as st
import pandas as pd

df = pd.read_csv('T2000.csv')

# [VIZ2] a panda dataframe with all values
df.set_index('Global Rank', inplace=True)

st.title("Interactive Data!")

st.subheader("Original Data:")
st.write(df)

default_columns = df.columns[:3].tolist() # first 3 columns


columns_to_display = st.multiselect('Select Columns to Display:',df.columns.tolist(),default=default_columns) # [ST3] multiselect for data

filtered_df = df[columns_to_display]

st.subheader("Your Data:")
st.write(filtered_df)

st.header('Quiz your knowledge!')
st.write('Use the boxes to filter data and select the best choice')

def show_feedback(answer, user_input, correct="Incorrect"): # [PY1] a function with 2+ parameters, one default value
    if user_input == answer:
        if answer == "Agricultural Bank of China":
            congratulations = "🎉 Congratulations, you've completed the quiz! 🎉"
            st.success("Correct")
            # [PY2] a function that returns more than one value
            return st.write("Good job!", congratulations)
        else:
            st.success("Correct")
            return st.write("Good job!", "")
    else:
        st.error(correct)
        return st.write("So close, try again!", "")

# Q1
st.header("1. Which company has a market value of 130.4?")
options_q1 = [company for company in df["Company"] if company.startswith("B")][:5] # [DA4] filter data by one condition,.startswith("B")
user_q1 = st.radio("Choose the company:", options_q1, key="q1") # [ST2] using radio buttons to select an answer
show_feedback("BP", user_q1)

# Q2
st.header("2. Which company has the latitude final of 34.6312?")
options_q2 = [company for company in df["Company"] if " " in company and "e" in company.lower()][:5] # [PY4] list comp with must contain a space " " and has the letter "e"
user_q2 = st.radio("Choose the company:", options_q2, key="q2")
show_feedback("General Electric", user_q2)

# Q3
st.header("3. Under the continent Asia, which company is shown third?")
options_q3 = [company for company in df[(df["Continent"] == "Asia") & (df["Company"].str.len() > 9)]["Company"]][:5] # [DA5] two or more conditions using and
user_q3 = st.radio("Choose the company:", options_q3, key="q3")
show_feedback("Agricultural Bank of China", user_q3)

# for Q2 and Q3, I didn't want to combind project requirements.txt so, I made 2 seperate codes to fulfill each individually