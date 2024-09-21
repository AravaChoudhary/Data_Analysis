import pandas as pd
import streamlit as st
from eda import eda

st.title("Restaurant Data Analysis")

st.header("1. Welcome")
st.write("Welcome to the Restaurant Data Analysis app! This application allows you to explore and analyze a dataset of restaurants to uncover insights and trends.")

st.header("2. Dataset Overview")
st.write("This dataset includes essential information about various restaurants. Key columns include:")
st.write("- **name**: The name of the restaurant")
st.write("- **votes**: The total number of votes received")
st.write("- **approx_cost(for two people)**: The estimated cost for two diners")
st.write("- **listed_in(type)**: The category of the restaurant (e.g., casual dining, fine dining, etc.)")

st.header("3. How to Use This App")
st.write("• Explore the data overview, descriptive statistics, and a variety of visualizations.")
st.write("• Navigate through the sections to understand trends related to cost distribution, restaurant types, and voting patterns.")

st.header("4. Visualizations Explained")
st.write("• **Histogram**: Displays the distribution of costs for two diners, helping you understand the pricing landscape.")
st.write("• **Count Plot**: Illustrates the number of restaurants across different types, giving insight into the diversity of offerings.")
st.write("• **Pie Charts**: Show the distribution of restaurants that offer online ordering and table booking options.")

df = pd.read_csv("Zomato data .csv")
eda(df)