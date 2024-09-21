import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def eda(df):
    st.title("General Information About the Data")
    st.write("# Data Overview")
    st.write(df.head())

    st.write("### Descriptive Statistics")
    st.write(df.describe())

    # Average cost distribution
    st.write("### Distribution of Approximate Cost for Two People")
    st.write("This histogram shows the distribution of approximate costs for two people at the restaurants.")
    plt.figure(figsize=(8, 5))
    sns.histplot(df['approx_cost(for two people)'].dropna(), kde=True)
    plt.title('Distribution of Approximate Cost for Two People')
    plt.xlabel('Cost')
    st.pyplot(plt.gcf())

    # Count plot for types of restaurants
    st.write("### Count of Restaurants by Type")
    st.write("This count plot displays the number of restaurants categorized by their type.")
    plt.figure(figsize=(10, 6))
    sns.countplot(x=df['listed_in(type)'])
    plt.xlabel("Type Of Restaurant")
    st.pyplot(plt.gcf())

    # Get the top 10 restaurants based on votes
    top_10_restaurants = df[['name', 'votes']].sort_values(by='votes', ascending=False).head(10)
    st.write("### Top 10 Restaurants Based on Votes")
    st.write(top_10_restaurants)

    # Votes by type of restaurant
    st.write("### Total Votes by Type of Restaurant")
    st.write("This line plot shows the total votes received by each type of restaurant.")
    grouped_data = df.groupby('listed_in(type)')['votes'].sum()
    result = pd.DataFrame({'votes': grouped_data})
    plt.figure(figsize=(10, 6))
    plt.plot(result, c='green', marker="o")
    plt.xlabel("Type Of Restaurant", c="blue", size=20)
    plt.ylabel("Votes", c="red", size=20)
    st.pyplot(plt.gcf())

    # Pie chart for distribution of online orders
    st.write("### Distribution of Online Orders")
    st.write("This pie chart illustrates the percentage of restaurants that offer online ordering.")
    online_order_distribution = df['online_order'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(online_order_distribution, labels=online_order_distribution.index, autopct='%1.1f%%', startangle=90)
    plt.title('Distribution of Online Orders')
    st.pyplot(plt.gcf())

    # Pie chart for distribution of book table options
    st.write("### Distribution of Book Table Options")
    st.write("This pie chart shows the percentage of restaurants that allow table bookings.")
    book_table_distribution = df['book_table'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(book_table_distribution, labels=book_table_distribution.index, autopct='%1.1f%%', startangle=90)
    plt.title('Distribution of Book Table Options')
    st.pyplot(plt.gcf())

    # Heatmap
    st.write("### Heatmap of Online Orders by Restaurant Type")
    st.write("This heatmap visualizes the relationship between restaurant types and their online ordering options.")
    pivot_table = df.pivot_table(index='listed_in(type)', columns='online_order', aggfunc='size', fill_value=0)
    plt.figure(figsize=(10, 6))
    sns.heatmap(pivot_table, annot=True, cmap='YlGnBu', fmt='d')
    plt.title("Heatmap")
    plt.xlabel("Online Order")
    plt.ylabel("Listed In (Type)")
    st.pyplot(plt.gcf())