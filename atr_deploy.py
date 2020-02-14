import json
import os
import logging

def lambda_handler(event, context):
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    logger.info('## ENVIRONMENT VARIABLES')
    logger.info(os.environ)
    logger.info(f"s3 key {event}")
    #['Records'][0]['object']['key']
    return {
        'statusCode': 200,
        'body': json.dumps(event)
    }
