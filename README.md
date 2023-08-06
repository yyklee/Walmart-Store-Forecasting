# Walmart Demand Forecasting - Store Level Prediction

Performed Demand Forecasting using time series analysis, bagging and boosting models on weekly sales data.

## About the Project
This project presents hierarchical sales data from Walmart. The aim is to forecast weekly sales for the next 20 weeks. The data, covers 45 stores in the US and includes department level weekly sales. In addition, it has explanatory variables such as holiday, cpi, unemployment rate, and store size. 

### 1) Problem Statement
Walmart wants to know the accurate point forecasts for the upcoming weekly sales for each 45 stores. 

### 2) Model Evaluation 
The accuracy of the point forecasts will be evaluated using the Root Mean Squared Scaled Error (MAPE).

### 3) About the Data
Walmart dataset with weekly sales data in 45 stores across the United States [(data source)](https://www.kaggle.com/competitions/walmart-recruiting-store-sales-forecasting/data). It has a grouped time series format. The time range of dataset is from 2010-02-05 to 2012-10-26. The dataset consists of the following 3 tables:
1. stores.csv: Contains information about the store number, type and size
2. features.csv: Contains information about external weekly features such as cpi, holiday, unemployment rate 
3. train.csv: Contains the historical daily unit sales data per store and department 


## Outline
We started with a high level data exploration of Walmart dataset to understand details and variation. Then we used different Hierarchy of data set for modelling based on stores, departments and categories in the dataset.
We tried to use Ensemble Tree-based Regressors, Prophet forecasting method tied with XGBoost, as well as traditional time series model (SARIMAX). The results for each models, average MAPE across the stores.

| Model Name | Model Hierarchy Level | Total Number of Models | Model Score |
|---|---|---|---|
| Random Forest Regressor | Per Store | 45 | 0.09 |
| XGBoost | Per Store | 45 | 0.12 |
| Prophet + XGBoost | Per Store | 45 | 0.11 |
| __SARIMAX__ | __Per Store__ | __45__ | __0.05__ |
<!-- ![table.png](table.png) -->
