# review.py

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
    st.title("⭐ Review Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Total Review Score Calculation from All Customers")
        # Calculate total review score for all customers
        total_review_score = all_data['review_score'].sum()
        # Create a bar plot
        plt.figure(figsize=(8, 6))
        ax = sns.countplot(x='review_score', data=all_data, palette="pastel")
        plt.xlabel('Review Score')
        plt.ylabel('Number of Customers')

        # Add total review score as text annotation
        plt.text(0.5, 0.95, f'Total Review Score: {total_review_score}',
                horizontalalignment='center', verticalalignment='center',
                transform=plt.gca().transAxes, fontsize=12)

        # Add data labels on each bar
        for p in ax.patches:
            ax.annotate(f'{p.get_height()}',
                        (p.get_x() + p.get_width() / 2., p.get_height()),
                        ha='center', va='center',
                        xytext=(0, 5),
                        textcoords='offset points')
        st.pyplot()

    with col2:
        st.subheader("Average Delivery Time vs Average Review Score")
        # Ensure the columns are in datetime format
        all_data['order_estimated_delivery_date'] = pd.to_datetime(all_data['order_estimated_delivery_date'])
        all_data['order_purchase_timestamp'] = pd.to_datetime(all_data['order_purchase_timestamp'])

        # Calculate average delivery time
        all_data['delivery_time'] = (all_data['order_estimated_delivery_date'] - all_data['order_purchase_timestamp']).dt.days

        # Group by review score and calculate average delivery time
        avg_delivery_by_review = all_data.groupby('review_score')['delivery_time'].mean().reset_index()

        # Visualization
        plt.figure(figsize=(8, 6))
        ax = sns.barplot(x='review_score', y='delivery_time', data=avg_delivery_by_review, palette="pastel")
        plt.xlabel('Average Review Score')
        plt.ylabel('Average Delivery Time (Days)')

        # Add data labels on each bar
        for container in ax.containers:
            ax.bar_label(container)

        st.pyplot()
    
    insight_review = "The Review Analysis chart provides insights into customer review scores and their relationship with average delivery times. On the left, the Total Review Score Calculation from All Customers bar chart shows that the highest number of reviews (64,859) are rated 5, indicating a strong customer preference for high ratings. Lower scores have fewer reviews, with ratings of 1 and 2 having significantly fewer customers, suggesting dissatisfaction may lead to lower engagement. On the right, the Average Delivery Time vs Average Review Score chart reveals that delivery time slightly decreases as the review score increases, with an average delivery time of about 24.5 days for scores 1 and 2, gradually reducing to approximately 23 days for scores 4 and 5. This suggests a potential link between faster delivery times and higher customer satisfaction." 
    def stream_data():
        for word in insight_review.split(" "):
            yield word + " "
            time.sleep(0.02)
    if st.button("See Insight"):
        st.write_stream(stream_data)
# ======================================================================================================
if __name__ == "__main__":
    main()
