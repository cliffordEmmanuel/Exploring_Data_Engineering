"""
This project is aimed at practicing a basic ETL using aws s3 bucket.
It involves: 
    - downloading data from an s3 bucket
    - performing some transformation
    - uploading the transformed data in two different file formats
"""
import boto3
import pandas as pd


def main():
    # initializing the s3 resource
    s3 = boto3.client('s3')
    bucket = 'blossom-data-eng-clifford'

    # downloading the file from s3 bucket
    s3.download_file('blossom-data-engs', 'free-7-million-company-dataset.zip', 'company_data.zip')

    # reading the file using pandas
    data = pd.read_csv('company_data.zip', compression='gzip')

    # removing the rows that have null values in the domain column...
    data.dropna(subset=['domain'], inplace=True)

    # writing the output files
    data.to_parquet('free-7-million-company-dataset.parquet')
    data.to_json('free-7-million-company-dataset-json.gzip', compression='gzip')

    # now on to using the uploading to the s3 bucket
    s3.upload_file('free-7-million-company-dataset.parquet', bucket, 'free-7-million-company-dataset.parquet')
    s3.upload_file('free-7-million-company-dataset-json.gzip', bucket, 'free-7-million-company-dataset-json.gzip')


if __name__ == "__main__":
    main()
