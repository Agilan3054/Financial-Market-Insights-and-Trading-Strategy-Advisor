#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install requests pandas')


# In[2]:


import requests
import pandas as pd

api_key = "1F2HIS0GLZE3E3DC"
symbol = "AAPL"  # Apple stock

url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={symbol}&outputsize=full&apikey={api_key}"
response = requests.get(url)
data = response.json()

df = pd.DataFrame(data['Time Series (Daily)']).T
df.columns = ['open', 'high', 'low', 'close', 'volume']
df.to_csv('/home/ec2-user/SageMaker/stock_data.csv')


# In[3]:


import boto3

s3 = boto3.client('s3')
bucket_name = "financial-market-data-agilan"
s3.upload_file("/home/ec2-user/SageMaker/stock_data.csv", bucket_name, "stock_data.csv")

