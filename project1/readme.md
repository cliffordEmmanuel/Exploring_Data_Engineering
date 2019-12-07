# Project1: Extract Transform Load(ETL) with Amazon S3

This was aimed at building a basic **ETL pipeline** to **read data** from a source, **transform it** and **load the output** into the cloud.<br>
*The tools used were:*
- **Pandas**
- **Jupyter lab**
- **Amazon Simple Storage Serivce(S3)**

Data used was the [7+ Million Companies dataset](https://www.kaggle.com/peopledatalabssf/free-7-million-company-dataset), which has info about companies company size, location, domain name etc..<br>
*The script does the following:*
- Download the 7+ Million Dataset from an S3 bucket.
- Read the file with pandas
- Filter out companies without a domain using pandas
- Write the output after filtering in the following formats
  - Parquet
  - JSON(compressed using gzip)
- Upload the output files into another S3 bucket
