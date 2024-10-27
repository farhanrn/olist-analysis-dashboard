# Order.py

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
    st.title("🛒 Order Analysis")
    # ======================================= CARDS ======================================================== 
    st.subheader("Order Delivery Status")
    Status = ["Delivered", "Cancelled"]
    Value = ["112,781", "7"]

    # Create two columns in Streamlit
    columns = st.columns(2)
    for idx, status in enumerate(Status):  # Unpack enumerate into idx and status
        with columns[idx]:
            st.metric(label=status, value=Value[idx])  # Use st.metric instead of ui.metric_card

    # =============================== TOTAL ORDER BY MONTH =====================================================
    st.subheader("Total Order Per Month")
    # Convert order_purchase_timestamp to datetime format
    all_data['order_purchase_timestamp'] = pd.to_datetime(all_data['order_purchase_timestamp'])
    # Add month_year column
    all_data['month_year'] = all_data['order_purchase_timestamp'].dt.strftime('%Y-%m')

    #[SELECTOR] Set default start and end dates for the date picker
    start_date = st.date_input("Select Start Date", value=pd.to_datetime("2016-01-01"), max_value=pd.to_datetime("2016-12-01"))
    end_date = st.date_input("Select End Date", value=pd.to_datetime("2018-01-31"), max_value=pd.to_datetime("2018-08-31"))
    # Filter data based on selected date range
    filtered_data = all_data[
        (all_data['order_purchase_timestamp'] >= pd.to_datetime(start_date)) &
        (all_data['order_purchase_timestamp'] <= pd.to_datetime(end_date))
    ]
    # Group by month_year and count orders
    order_per_month = filtered_data.groupby(['month_year']).count()[['order_id']]
    # Plot the data
    fig, ax = plt.subplots(figsize=(20, 8))
    sns.lineplot(data=order_per_month, marker='o', markersize=5, color='green', ax=ax)
    ax.set_xlabel('Year-Month', fontsize=12)
    # Add data labels
    for x, y in zip(order_per_month.index, order_per_month['order_id']):
        ax.text(x, y, f'{y}', ha='center', va='bottom')
    # Display the plot in Streamlit
    st.pyplot(fig)
    # Running insight
    insight_revenue_1 = "The data reveals a fluctuating trend with several peaks and troughs. The highest peak is observed in November 2017 with 8636 orders, followed by a significant decline in December 2017 to 6116 orders. Subsequently, there is a gradual increase until April 2018, reaching 8163 orders. The trend then exhibits a downward trajectory, with the lowest point recorded in August 2018 at 7294 orders. Overall, the chart suggests a pattern of seasonality in the order volume, with higher numbers during certain periods and lower numbers during others."
    def stream_data_1():
        for word in insight_revenue_1.split(" "):
            yield word + " "
            time.sleep(0.02)
    if st.button("See Insight", key="insight_1"):
        st.write_stream(stream_data_1)
    
    # =============================== ORDER PURCHASE DAY OF WEEK =====================================================
    st.subheader("Order Purchase day of Week")
    # Extract day of the week from order purchase timestamp
    all_data['order_purchase_dayofweek'] = all_data['order_purchase_timestamp'].dt.dayofweek
    # Group by day of the week and count orders
    orders_by_dayofweek = all_data.groupby('order_purchase_dayofweek')['order_id'].count().reset_index()
    # Map day of the week numbers to names
    dayofweek_mapping = {
        0: 'Monday',
        1: 'Tuesday',
        2: 'Wednesday',
        3: 'Thursday',
        4: 'Friday',
        5: 'Saturday',
        6: 'Sunday'
    }
    orders_by_dayofweek['order_purchase_dayofweek'] = orders_by_dayofweek['order_purchase_dayofweek'].map(dayofweek_mapping)
    # Rename columns for clarity
    orders_by_dayofweek.columns = ['Day of Week', 'Order Count']
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='Day of Week', y='Order Count', data=orders_by_dayofweek, palette="pastel") #add ax
    plt.ylabel('Order Count')
    plt.xticks(rotation=45, ha='right')  # Rotate x-axis labels for better readability

    # Add data labels on each bar
    for bar in ax.containers: #add this section
        ax.bar_label(bar)

    plt.tight_layout()  # Adjust layout to prevent labels from overlapping
    #plt.show()
    st.pyplot()
    # Running insight
    insight_revenue_2 = "Tuesday and Wednesday are the busiest days for orders, with 18,312 and 18,344 orders respectively. Thursday follows closely with 17,605 orders, while Friday sees a slight decrease to 16,855 orders. The order count then drops significantly on Saturday and Sunday, with 16,122 and 12,155 orders respectively. Monday has the lowest order count at 13,395. This indicates a clear pattern of higher order activity during the weekdays compared to the weekends."
    def stream_data_2():
        for word in insight_revenue_2.split(" "):
            yield word + " "
            time.sleep(0.02)
    if st.button("See Insight", key="insight_2"):
        st.write_stream(stream_data_2)
    
    # ======================================== Average Order Value ================================================================================================================================
    st.subheader("Average Order Value Per Each Product Category")
    # Calculate AOV by product category
    aov_by_category = all_data.groupby('product_category_name_english')['price'].mean().reset_index()
    aov_by_category = aov_by_category.sort_values(by='price', ascending=False).iloc[:20]

    # Calculate AOV by payment method
    aov_by_payment = all_data.groupby('payment_type')['price'].mean().reset_index()
    aov_by_payment = aov_by_payment.sort_values(by='price', ascending=False)

    # Visualization for AOV by product category
    plt.figure(figsize=(24, 9))
    palette = sns.color_palette("deep", as_cmap=True)
    ax = sns.barplot(x='product_category_name_english', y='price', data=aov_by_category, palette=palette)
    plt.ylabel('Average Order Value')
    plt.xticks(rotation=90, ha='right')  # Rotate x-axis labels for better readability
    # Customize tick label sizes
    ax.tick_params(axis='x', labelsize=16)
    ax.tick_params(axis='y', labelsize=16)

    # Add data labels on each bar
    for bar in ax.containers:
        ax.bar_label(bar)

    plt.tight_layout()  # Adjust layout to prevent labels from overlapping
    st.pyplot()
    # Running insight
    insight_revenue_3 = "The Computers category has the highest average order value at 1078.72, followed by Small Appliances - Home Oven and Coffee at 641.19. The remaining categories exhibit a declining trend in average order value, with Security and Services having the lowest average order value at 141.845"
    def stream_data_3():
        for word in insight_revenue_3.split(" "):
            yield word + " "
            time.sleep(0.02)
    if st.button("See Insight", key="insight_3"):
        st.write_stream(stream_data_3)

# ======================================================================================================
if __name__ == "__main__":
    main()