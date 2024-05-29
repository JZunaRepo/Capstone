import boto3
## View buckets
client = boto3.client('s3')

response = client.list_buckets()

for b in response.get("Buckets", None):
    print(b.get("Name", None))

#Upload files to boto 3
local_file = 'data/bcancer.csv' 
bucket = 'ds24aws'
s3_file = 'bcancer.csv'

s3 = boto3.resource('s3')
s3.meta.client.upload_file(local_file,bucket,s3_file)