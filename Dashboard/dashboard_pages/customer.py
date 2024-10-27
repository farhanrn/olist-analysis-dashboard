# customer.py
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

# ======================================================================================================
def main():
    st.title("👥 Customer Segmentation Analysis")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("New vs. Repeat Customers")
        # Group data by customer type and count orders
        # Check if 'customer_unique_id' is the intended column to identify customer type
        # Assuming a new customer has only one order_id associated with their customer_unique_id
        all_data['customer_type'] = all_data.groupby('customer_unique_id')['order_id'].transform('nunique').apply(lambda x: 'Repeat' if x > 1 else 'New')
        customer_type_counts = all_data.groupby('customer_type')['order_id'].count().reset_index()

        # Plot
        plt.figure(figsize=(6, 4))
        ax = sns.barplot(x='customer_type', y='order_id', data=customer_type_counts, palette="pastel") # Changed y to 'order_unique_id'
        plt.xlabel('Customer Type')
        plt.ylabel('Number of Orders')

        # Add data labels on each bar
        for container in ax.containers:
            ax.bar_label(container)

        st.pyplot()

    with col2:
        st.subheader("Payment Methods Used")
        plt.figure(figsize=(6, 4))
        ax = sns.countplot(x='payment_type', data=all_data, palette="pastel")
        plt.xlabel('Payment Method')
        plt.ylabel('Number of Orders')
        plt.xticks(rotation=45, ha='right')

        # Add data labels on each bar
        for bar in ax.containers:
            ax.bar_label(bar)

        plt.tight_layout()
        st.pyplot()
    
    insight_customer1 = "The charts indicate that the majority of customers are new, with 105,189 orders compared to only 7,599 from repeat customers, suggesting that customer retention might be low or that the business attracts a continuous influx of first-time buyers. In terms of payment methods, credit cards are the most popular, accounting for 83,250 orders, followed by boleto with 21,929 orders. Other payment methods like debit cards and vouchers have significantly lower usage, with 1,615 and 5,994 orders respectively. This distribution suggests that customers prefer credit-based payments, with boleto as a secondary choice, potentially reflecting regional payment preferences or customer trust in certain methods." 
    def stream_data_1():
        for word in insight_customer1.split(" "):
            yield word + " "
            time.sleep(0.02)
    if st.button("See Insight", key="insight_1"):
        st.write_stream(stream_data_1)
    # =========================================RFM ANALYSIS =========================================================
    st.subheader("RFM : Recency, Frequency and Monetary Value")
    all_data["order_purchase_timestamp"] = pd.to_datetime(all_data["order_purchase_timestamp"])
    rfm_df = all_data.groupby(by="customer_unique_id", as_index=False).agg({
        "order_purchase_timestamp": "max",  # mengambil tanggal order terakhir
        "order_id": "nunique",  # menghitung jumlah order
        "price": "sum"  # menghitung jumlah revenue yang dihasilkan
    })
    rfm_df.columns = ["customer_unique_id", "max_order_timestamp", "frequency", "monetary"]

    # menghitung kapan terakhir pelanggan melakukan transaksi (hari)
    rfm_df["max_order_timestamp"] = rfm_df["max_order_timestamp"].dt.date
    recent_date = all_data["order_purchase_timestamp"].dt.date.max()
    # Access the 'days' attribute directly from the timedelta object
    rfm_df["recency"] = (recent_date - rfm_df["max_order_timestamp"]).apply(lambda x: x.days)
    st.write(rfm_df)

    # =========================================CUSTOMER SEGMENTATION =========================================================
    st.subheader("Customer Segmentation")
    # Sorting RFM 
    rfm_df['r_rank'] = rfm_df['recency'].rank(ascending=False)
    rfm_df['f_rank'] = rfm_df['frequency'].rank(ascending=True)
    rfm_df['m_rank'] = rfm_df['monetary'].rank(ascending=True)
    # normalizing the rank of the customers
    rfm_df['r_rank_norm'] = (rfm_df['r_rank']/rfm_df['r_rank'].max())*100
    rfm_df['f_rank_norm'] = (rfm_df['f_rank']/rfm_df['f_rank'].max())*100
    rfm_df['m_rank_norm'] = (rfm_df['m_rank']/rfm_df['m_rank'].max())*100
    rfm_df.drop(columns=['r_rank', 'f_rank', 'm_rank'], inplace=True)
    # Calculating RFM Socre
    rfm_df['RFM_score'] = 0.15*rfm_df['r_rank_norm']+0.28 * \
    rfm_df['f_rank_norm']+0.57*rfm_df['m_rank_norm']
    rfm_df['RFM_score'] *= 0.05
    rfm_df = rfm_df.round(2)
    # Segmenting CUstomer
    rfm_df["customer_segment"] = np.where(
        rfm_df['RFM_score'] > 4.5, "Top customers", (np.where(
            rfm_df['RFM_score'] > 4, "High value customer",(np.where(
                rfm_df['RFM_score'] > 3, "Medium value customer", np.where(rfm_df['RFM_score'] > 1.6, 'Low value customers', 'lost customers'))))))
    
    customer_segment_df = rfm_df.groupby(by="customer_segment", as_index=False).customer_unique_id.nunique()
    customer_segment_df['customer_segment'] = pd.Categorical(customer_segment_df['customer_segment'], [
    "lost customers", "Low value customers", "Medium value customer",
    "High value customer", "Top customers"
])
    plt.figure(figsize=(10, 5))
    colors_ = ["#72BCD4", "#72BCD4", "#D3D3D3", "#D3D3D3", "#D3D3D3"]

    sns.barplot(
        x="customer_unique_id",
        y="customer_segment",
        data=customer_segment_df.sort_values(by="customer_segment", ascending=False),
        palette=colors_
    )
    plt.title("Number of Customer for Each Segment", loc="center", fontsize=15)
    plt.ylabel(None)
    plt.xlabel(None)
    plt.tick_params(axis='y', labelsize=12)
    st.pyplot()

    insight_customer2 = "The chart shows the distribution of customers across different value segments, with Low value customers making up the largest segment, followed by Medium value customers and Lost customers. The number of High value customers and Top customers is significantly lower, indicating that a large portion of the customer base is low-value or inactive. This distribution suggests a need for strategies to increase customer value and retain higher-value customers, potentially by encouraging repeat purchases and enhancing customer engagement for the low and medium-value segments." 
    def stream_data_2():
        for word in insight_customer2.split(" "):
            yield word + " "
            time.sleep(0.02)
    if st.button("See Insight", key="insight_2"):
        st.write_stream(stream_data_2)

# ======================================================================================================
if __name__ == "__main__":
    main()
