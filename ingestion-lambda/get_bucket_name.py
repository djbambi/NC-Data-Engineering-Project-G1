import boto3

client = boto3.client("s3")


def find_bucket_by_keyword(keyword):
    """ Bucket has a random suffix which needs to be found,
    this function searches s3 for a bucket which contains a keyword """

    bucket_name = None

    try:
        bucket_list = client.list_buckets()["Buckets"]

    except Exception:
        raise ConnectionError("Could not find ingestion bucket")

    for bucket in bucket_list:
        if keyword in bucket["Name"]:
            bucket_name = bucket["Name"]

    return bucket_name
