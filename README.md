
![Logo](http://localhost:8501/media/194eeebed066454e1b6311f1dc2d4c2c7c2885b6decc3df2d0c9af81.jpg)



# Olist E-Commerce Analysis

Olist is a unicorn company founded by Tiago Dalvi in ​​Brazil that operates in the retail sector and has been established since 2015. The dataset has information of 100k orders from 2016 to 2018 made at multiple marketplaces in Brazil. Its features allows viewing an order from multiple dimensions: from order status, price, payment and freight performance to customer location, product attributes and finally reviews written by customers. This dashboard is equipped with interactive features that allow for a deeper exploration of the data. The aim of this project is to provide an interactive and informative dashboard for studying and extracting insights from the E-Commerce Public Dataset.


## Features

- Revenue Analysis
- Order Analysis
- Product Analysis
- Seller Analysis
- Review Analysis
- Customer Analysis



## Deployment
The Project Already Deployed in Streamlit here is

[Link Demo]()


## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```
## Setup Environment - Shell/Terminal
```
mkdir olist_ecommerce_analysis
cd olist_ecommerce_analysis
pipenv install
pipenv shell
pip install -r requirements.txt
```
## Run steamlit app
```
streamlit run dashboard.py
```
