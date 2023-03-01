import json
import boto3
from get_bucket_name import ingestion_bucket
import re

client = boto3.client("s3")


def upload_to_s3(tables_dict, timestamp):
    """ This function takes a dictionary of table data,
    (output by get_sql_data function).
    and uploads each table to s3, to the correct key,
    and makes a folder for each table that need to be uploaded in full """

    for key in tables_dict.keys():
        table_rows_list = tables_dict[key]
        table_name = key

        bucket_key = f"{timestamp}/{table_name}.csv"
        if "full" in table_name:
            name_search = re.search("full_(.*)_table", table_name)
            extracted_name = name_search.group(1)
            bucket_key = f"{extracted_name}/{table_name}.csv"

        comma_seperated_rows = []

        for row in table_rows_list:
            stringified_rows = []

            for element in row:
                stringified_rows.append(json.dumps(element, default=str))

            comma_seperated_rows.append(",".join(stringified_rows))

        csv_string = "\n".join(comma_seperated_rows)
        client.put_object(
            Body=csv_string,
            Bucket=ingestion_bucket,
            Key=bucket_key)
