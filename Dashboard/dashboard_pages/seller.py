# sales.py

import streamlit as st
import pandas as pd
import numpy as np
import streamlit_shadcn_ui as ui  # type: ignore
import locale  # Import locale for currency formatting
import matplotlib.pyplot as plt
import seaborn as sns
import time

# Dataset Preparation
dataset = "https://raw.githubusercontent.com/farhanrn/olist-analysis-dashboard/refs/heads/main/Data/all_data.csv"
all_data = pd.read_csv(dataset)
# ======================================================================================================
def main():
    st.title("🧑‍💼 Seller Analysis")
    # =============================== Total Sellers per Product Category =====================================================
    st.subheader("Total Seller per Product Category")
    sellers_per_category = all_data.groupby('product_category_name_english')['seller_id'].nunique().reset_index()
    sellers_per_category.columns = ['Product Category', 'Total Sellers']
    sellers_per_category = sellers_per_category.sort_values(by='Total Sellers', ascending=False)

    # Visualization
    plt.figure(figsize=(30, 12))  # Adjust figure size for better readability
    ax = sns.barplot(x='Product Category', y='Total Sellers', data=sellers_per_category, palette='pastel')
    plt.xticks(rotation=90, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent labels from overlapping
    # Customize tick label sizes
    ax.tick_params(axis='x', labelsize=20)
    ax.tick_params(axis='y', labelsize=20)
    # Add data labels to the bars
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.0f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 10), textcoords='offset points')
    st.pyplot()
    # Running insight
    insight_revenue_1 = "Health & beauty, sports, home appliances, and furniture are the leading categories, each with over 200 sellers, indicating high market saturation in these areas. Categories like computers, toys, and baby products follow closely, maintaining a competitive seller count between 100 and 200. As the chart progresses to the right, the number of sellers gradually decreases, showing less competition in specialized categories like security products, CNG stations, and cars & models. This suggests that while some product areas have a robust seller presence, niche categories offer opportunities for new sellers due to limited competition." 
    def stream_data_1():
        for word in insight_revenue_1.split(" "):
            yield word + " "
            time.sleep(0.02)
    if st.button("See Insight", key="insight_1"):
        st.write_stream(stream_data_1)

    # =============================== Active Sellers Over Time =====================================================
    st.subheader("Active Sellers Over Time")
    all_data['order_purchase_timestamp'] = pd.to_datetime(all_data['order_purchase_timestamp'], errors='coerce')
    # Group data by year-month and count unique sellers
    sellers_over_time = all_data.groupby(all_data['order_purchase_timestamp'].dt.to_period('M'))['seller_id'].nunique().reset_index()

    # Rename columns for clarity
    sellers_over_time.columns = ['Month-Year', 'Active Sellers']

    # Convert 'Month-Year' to datetime objects
    sellers_over_time['Month-Year'] = sellers_over_time['Month-Year'].dt.to_timestamp()  # Convert Period to Timestamp

    # Visualization
    plt.figure(figsize=(12, 4))
    ax = sns.lineplot(x='Month-Year', y='Active Sellers', data=sellers_over_time, marker='o')
    plt.xlabel('Year-Month')
    plt.ylabel('Number of Active Sellers')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability
    plt.tight_layout()  # Adjust layout to prevent labels from overlapping
    plt.grid(True)  # Add a grid for better visualization

    # Add data labels
    for x, y in zip(sellers_over_time['Month-Year'], sellers_over_time['Active Sellers']):
        ax.text(x, y, str(y), ha='center', va='bottom')  # Adjust ha, va as needed

    st.pyplot()
    # Running insight
    insight_revenue_2 = "Starting at 127 sellers in October 2016, the count rises consistently, with occasional plateaus, such as in mid-2017 and early 2018, where growth slows temporarily. Significant growth points appear between January 2017 and October 2017, where the number of sellers jumps from 214 to 747, indicating strong onboarding or expansion during this period. By August 2018, the count reaches 1,250, suggesting sustained growth and a continued trend of seller acquisition over time." 
    def stream_data_2():
        for word in insight_revenue_2.split(" "):
            yield word + " "
            time.sleep(0.02)
    if st.button("See Insight", key="insight_2"):
        st.write_stream(stream_data_2)
    
    # ============= The distribution of seller ratings on Olist, its impact on sales performance=====================================================
    col1, col2 = st.columns(2)
    with col1 :
        st.subheader("Distribution of Seller Ratings")
        plt.figure(figsize=(10, 6))
        sns.histplot(all_data['avg_review_score'], bins=10, kde=True)
        plt.xlabel('Average Review Score')
        plt.ylabel('Number of Sellers')
        st.pyplot()
    with col2 :
        st.subheader("Relationship Between Seller Ratings and Sales")
        plt.figure(figsize=(10, 6))
        sns.scatterplot(x='avg_review_score', y='price', data=all_data)
        plt.xlabel('Average Review Score')
        plt.ylabel('Sales')
        st.pyplot()
    # Running insight
    insight_revenue_3 = "In general, there is a positive correlation between seller rating and the number of orders, where higher-rated sellers (4.0 to 5.0) tend to receive more orders, while lower-rated sellers (below 2.0) receive fewer orders, typically less than 1000. However, there are exceptions where some low-rated sellers still manage to obtain a relatively high number of orders, although this is rare. For ratings above 4.0, the frequency of orders increases significantly, with many sellers receiving between 1000 to 5000 orders, and some even exceeding 6000, especially around ratings of 4.8 to 5.0, indicating a very high order volume. Although many high-rated sellers receive large orders, there are also those who receive only a small number, suggesting that factors other than rating also influence the number of orders." 
    def stream_data_3():
        for word in insight_revenue_3.split(" "):
            yield word + " "
            time.sleep(0.02)
    if st.button("See Insight", key="insight_3"):
        st.write_stream(stream_data_3)
# ======================================================================================================
if __name__ == "__main__":
    main()
