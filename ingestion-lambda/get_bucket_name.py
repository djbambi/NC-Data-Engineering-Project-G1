import boto3

client = boto3.client("s3")

"""Bucket has a random suffix which needs to be found,
this function searches s3 for a bucket which contains a keyword"""


def find_bucket_by_keyword(keyword):
    bucket_name = None

    bucket_list = client.list_buckets()["Buckets"]

    for bucket in bucket_list:
        if keyword in bucket["Name"]:
            bucket_name = bucket["Name"]

    return bucket_name


ingestion_bucket = find_bucket_by_keyword("ingestion")
