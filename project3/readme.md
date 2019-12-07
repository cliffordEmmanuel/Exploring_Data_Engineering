# Project3: End to End Extract Transform Load(ETL) Pipeline

This project completed a basic end to end ETL pipeline for a basic data processing task
*Tools used were:*
- **Jupyter lab**
- **PySpark**
- **Postgresql**
- **Dbeaver**

Data used was gotten from stackoverflow: questions, answers and users<br>
*The following tasks were done:*
1. **Data Extraction:**
  - load the data using pyspark from postgres (extra configuration required to connect to the database)
2. **Data Transformation:**
  - select users from a specific country
  - extract the country and city into new columns
  - join this with the questions and extract questions with at least 20 view counts
  - join the answers to results
3. **Data Loading:**
  - using sql create a schema and a table to store the results obtained after transformation
  - using spark write the results into the table
  - create a btree and hash indexes on specific columns
  - create a view to display some information
  - create a materialised view as well
4. **SQL Data Manipulation**
  - write some basic queries to the data on the database
