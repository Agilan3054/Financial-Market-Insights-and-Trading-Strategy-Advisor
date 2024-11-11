#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3
import pandas as pd

comprehend = boto3.client("comprehend")
df = pd.read_csv('data/social_data.csv')

sentiments = []
for content in df['content']:
    response = comprehend.detect_sentiment(Text=content, LanguageCode="en")
    sentiments.append(response['Sentiment'])
df['sentiment'] = sentiments
df.to_csv('data/social_data_with_sentiment.csv', index=False)

