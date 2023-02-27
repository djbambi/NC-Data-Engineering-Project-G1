The simple routine to store and retriev the dase credentials in the AWS secrets

1. you will need to put the .env file, containing creds, in the project root directory and gitignore it

2. the "dotenv" module needs to be installed : >> pip install python-dotenv 
corresponding line in the requirements.txt: python-dotenv ==1.0.0

3. to be able to get secrets in your lambda, modify the terraform iam.tf file:

- in the  ' data "aws_iam_policy_document" "s3_document" { }', include the following:
"
 statement {
    actions = ["secretsmanager:GetSecretValue"]
    resources = ["*"
    ]
  }
"


4. to put the credentials into AWS secrets, start the sandbox with awsume and then run 
"sm_env_util.py" script from any directory

5. to retrive the secrets to connect to database, you can use the code from 
"lambda_connection_examples.py"
