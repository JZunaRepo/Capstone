import boto3
import pandas as pd
import io

# some initial variables
bucket_name = "ds24aws"
object_key = 'bcancer.csv'

# open client
client = boto3.client('s3')

### DOWNLOADING SINGLE OBJECTS FROM A BUCKET ###
response = client.get_object(
    Bucket=bucket_name,
    Key=object_key,
)

# read in data from request
data = response['Body'].read()

# transform into pandas dataframe by reading in bytes
df = pd.read_csv(io.BytesIO(data))

# print head
print(df.head())
