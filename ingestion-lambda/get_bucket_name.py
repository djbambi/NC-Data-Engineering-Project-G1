import boto3

client = boto3.client("s3")

def find_bucket_by_keyword(keyword):
    bucket_name = None
    
    bucket_list = client.list_buckets()["Buckets"]
                                        
    for bucket in bucket_list:
        if keyword in bucket["Name"]:
            bucket_name = bucket["Name"]
                                 
    return bucket_name


ingestion_bucket = find_bucket_by_keyword("ingestion")