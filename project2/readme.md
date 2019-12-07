# Batch Processing for Data Mining

This was aimed at using **pyspark** for a **text mining** job.<br>
*Tools used were:*
- **Jupyter lab**
- **PySpark**
- **Amazon Simple Storage Service(S3)**

Data used was the [data scientist job market dataset](https://www.kaggle.com/sl6149/data-scientist-job-market-in-the-us) and the [us stocks](https://www.kaggle.com/marketahead/all-us-stocks-tickers-company-info-logos) <br>
*The notebook does the following:*
- load the datasets from an S3 bucket to a local machine
- read the data with pyspark
- join the 2 datasets
- write a function to generate n-grams from given text/description
- write another function to create 2 dataframes:
