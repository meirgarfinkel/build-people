import boto3
import os

def get_parameter(name, with_decryption=True):
    client = boto3.client("ssm", region_name=os.environ.get("AWS_REGION", "us-east-1"))
    response = client.get_parameter(Name=name, WithDecryption=with_decryption)
    return response["Parameter"]["Value"]
