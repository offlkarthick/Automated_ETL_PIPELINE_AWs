import json
import boto3
import os

glue = boto3.client("glue")

GLUE_JOB_NAME = 's3-glue-s3'  # recommended

def lambda_handler(event, context):
    try:


        response = glue.start_job_run(
            JobName=GLUE_JOB_NAME
        )

        print(f"Glue job started: {response['JobRunId']}")

        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Glue job started",
                "jobRunId": response["JobRunId"]
            })
        }

    except Exception as e:
        print("Error:", str(e))
        raise e
