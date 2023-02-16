"Setting up a lambda function to recieve s3 put object event (triggered when a file is added to the bucket)"

def lambda_handler(event, context):
    pass

# Args:
#     event:
#         a valid S3 PutObject event -
#         see https://docs.aws.amazon.com/AmazonS3/latest/userguide/notification-content-structure.html
#     context:
#         a valid AWS lambda Python context object - see
#         https://docs.aws.amazon.com/lambda/latest/dg/python-context.html

#         https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html


# iam = boto3.client('iam', region_name='us-east-1')
# policy = '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"},"Action": "sts:AssumeRole"}]}
# response = iam.create_role( RoleName=role_name, AssumeRolePolicyDocument=lambda_role_document)
# print(iam.list_roles())