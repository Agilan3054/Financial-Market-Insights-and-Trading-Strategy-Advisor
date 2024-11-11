#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from pyspark.sql import SparkSession
from pyspark.sql.functions import col, to_date

spark = SparkSession.builder.appName("StockDataPreprocessing").getOrCreate()
df = spark.read.csv("s3://financial-market-data-agilan/stock_data.csv", header=True, inferSchema=True)

# Convert date column and filter relevant columns
df = df.withColumn("date", to_date(col("timestamp"))).select("date", "open", "high", "low", "close", "volume")
df.show()


# In[ ]:




