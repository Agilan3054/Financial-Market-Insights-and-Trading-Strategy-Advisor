#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3

s3 = boto3.client('s3')
bucket_name = "financial-market-data-agilan"
s3.upload_file('data/stock_data.csv', bucket_name, 'stock_data.csv')
s3.upload_file('data/social_data_with_sentiment.csv', bucket_name, 'social_data_with_sentiment.csv')

