#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3
import json

# Set up your AWS QuickSight client
client = boto3.client('quicksight', region_name='ap-south-1')  

# Replace these with your actual values
aws_account_id = '050451377047'
dashboard_name = 'MyDashboard'
source_entity = {
    'SourceTemplate': {
        'DataSetReferences': [
            {
                'DataSetArn': 'arn:aws:quicksight:ap-south-1:your-aws-account-id:dataset/0504513',
                'DataSet': 'stock_data.csv'
            }
        ],
        'Arn': 'arn:aws:quicksight:ap-south-1:050451377047:template/0504513'
    }
}

# Create the dashboard
response = client.create_dashboard(
    AwsAccountId=aws_account_id,
    DashboardId='0504513',  
    Name=dashboard_name,
    SourceEntity=source_entity,
    Permissions=[
        {
            'Principal': 'arn:aws:iam::050451377047:user/Agilan',
            'Actions': ['quicksight:DescribeDashboard', 'quicksight:ListDashboardVersions', 'quicksight:UpdateDashboard']
        },
    ],
    ThemeArn='arn:aws:quicksight:ap-south-1:050451377047:theme/default'  
)

# Print the response to confirm the dashboard was created
print(json.dumps(response, indent=4))

