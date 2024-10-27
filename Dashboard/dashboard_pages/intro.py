import streamlit as st
import pandas as pd
import numpy as np
dataset = "https://raw.githubusercontent.com/farhanrn/olist-analysis-dashboard/refs/heads/main/Data/all_data.csv"
df = pd.read_csv(dataset)
# ======================================================================================================
def main():
    st.image("https://github.com/farhanrn/olist-analysis-dashboard/blob/main/Dashboard/dataset-cover.png")
    # Introduction Section
    st.title("Olist E-Commerce Analysis")
    st.subheader("Complete Dashboard with Various Insights")
    # ======================================================================================================
    # Brief Description
    st.write("""
    Olist is a unicorn company founded by Tiago Dalvi in ​​Brazil that operates in the retail sector and has been established since 2015.
    The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. 
    Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers       
    """)
    # ======================================================================================================
    # Key Features
    st.markdown("### Main Goals:")
    st.write("""
    This dashboard is equipped with interactive features that allow for a deeper exploration of the data. 
    The aim of this project is to provide an interactive and informative dashboard for studying and extracting insights from the E-Commerce Public Dataset.
    """)
    # ======================================================================================================
    # Dataframe 
    st.markdown("### Dataset Preview:")
    st.dataframe(df)
    # ======================================================================================================
    # Footer Section
    st.markdown("### Contact me:")
    st.write("""
    For any inquiries, please reach me at [linkedin](https://www.linkedin.com/in/farhan-rahman0601/).
    """)

# Call the main function
if __name__ == "__main__":
    main()