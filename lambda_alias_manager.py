 import boto3
import time
from botocore.exceptions import ClientError

client = boto3.client('lambda')

def update_lambda_aliases():
    paginator = client.get_paginator('list_functions')
    for page in paginator.paginate():
        for function in page['Functions']:
            function_name = function['FunctionName']
            
            try:
                # Publish a new version
                new_version_response = client.publish_version(FunctionName=function_name)
                new_version = new_version_response['Version']
                print(f"Published new version {new_version} for function {function_name}")
                
                # Update the DEV alias to point to $LATEST
                client.update_alias(
                    FunctionName=function_name,
                    Name='DEV',
                    FunctionVersion='$LATEST'
                )
                print(f"Updated DEV alias for {function_name} to point to $LATEST")
 
                # Update the PROD alias to point to the new version
                client.update_alias(
                    FunctionName=function_name,
                    Name='PROD',
                    FunctionVersion=new_version
                )
                print(f"Updated PROD alias for {function_name} to point to version {new_version}")
 
            except ClientError as e:
                if e.response['Error']['Code'] == 'ThrottlingException':
                    print(f"Rate limit exceeded for function {function_name}. Retrying...")
                    time.sleep(1)  # Pause to avoid rate limiting issues
                    # Retry once more or implement a backoff strategy here
                else:
                    print(f"An error occurred with function {function_name}: {e}")
 
if name == '__main__':
    update_lambda_aliases()