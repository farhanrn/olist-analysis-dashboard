# Product.py

import streamlit as st
import pandas as pd
import numpy as np
import streamlit_shadcn_ui as ui  # type: ignore
import locale  # Import locale for currency formatting
import matplotlib.pyplot as plt
import seaborn as sns
import time

# Dataset Preparation
all_data = pd.read_csv('src/all_data.csv')
# ======================================================================================================
def main():
    st.title("🛍️ Product Analysis")
    # =============================== Top 20 Product Sold =====================================================
    st.subheader("Top 20 Product Sold")
    plt.figure(figsize=(18, 8))  # Adjust figure size for better readability
    top_20_categories = all_data['product_category_name_english'].value_counts().head(20).index
    ax = sns.countplot(y='product_category_name_english', data=all_data, order=top_20_categories, palette='pastel')
    plt.xlabel('Count', fontsize=12)
    plt.ylabel('Category', fontsize=12)
    # Add data labels to the bars
    for p in ax.patches:
        ax.annotate(f'{p.get_width():.0f}', (p.get_width() + 0.5, p.get_y() + p.get_height() / 2), ha='left', va='center')
    st.pyplot()
    # Running insight
    insight_revenue_1 = "The chart titled Category presents the count of items in different product categories. Bed, Bath, Table emerges as the top category with the highest count of items at 11,594. Health & Beauty follows closely with 9,707 items, and Sports & Leisure has 8,689 items. The remaining categories exhibit a descending trend in count, with Luggage & Accessories having the lowest count at 1,144"
    def stream_data_1():
        for word in insight_revenue_1.split(" "):
            yield word + " "
            time.sleep(0.02)
    if st.button("See Insight", key="insight_1"):
        st.write_stream(stream_data_1)
    
    # =============================== Average Freight Cost Analysis of Top 20 Product Caetegories =====================================================
    st.subheader("Average Freight Cost of Top 20 Products")
    top_20_categories = all_data['product_category_name_english'].value_counts().head(20).index

    # Filter the DataFrame to incSlude only the top 20 categories
    filtered_data = all_data[all_data['product_category_name_english'].isin(top_20_categories)]

    # Group by product category and calculate average freight value
    avg_freight_by_product = filtered_data.groupby('product_category_name_english')['freight_value'].mean().reset_index()

    # Sort by average freight value in descending order
    avg_freight_by_product = avg_freight_by_product.sort_values(by='freight_value', ascending=False)

    # Visualization
    plt.figure(figsize=(16, 9))
    ax = sns.barplot(x='product_category_name_english', y='freight_value', data=avg_freight_by_product, palette="pastel")
    #plt.title('Average Freight Cost of Top 20 Products')
    plt.xlabel('')
    plt.ylabel('Average Freight Cost')
    plt.xticks(rotation=90, ha='right')
    plt.tight_layout()

    # Add data labels to the bars
    for p in ax.patches:
        ax.annotate(f'{p.get_height():.2f}', (p.get_x() + p.get_width() / 2., p.get_height()),
                    ha='center', va='center', xytext=(0, 10), textcoords='offset points')
    st.pyplot()
    # Running insight
    insight_revenue_2 = "Office Furniture has the highest average freight cost at 39.66, followed by Luggage Accessories at 27.67, indicating that these items are likely bulkier or heavier, leading to higher shipping expenses. Most other products have relatively similar average freight costs, ranging between 22.72 and 15.60. This suggests that products like Fashion Bag Accessories and Telephony, with lower costs, may be lighter or easier to ship. The data highlights that certain categories, such as office furniture and luggage, significantly impact shipping budgets, while the freight costs for other categories remain relatively moderate and consistent"
    def stream_data_2():
        for word in insight_revenue_2.split(" "):
            yield word + " "
            time.sleep(0.02)
    if st.button("See Insight", key="insight_2"):
        st.write_stream(stream_data_2)
    
# ======================================================================================================
if __name__ == "__main__":
    main()

