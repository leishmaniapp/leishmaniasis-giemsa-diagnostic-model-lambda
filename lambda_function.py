
import os
import json
import boto3
import logging
import signal

from model import call_model_execution

AWS_REGION = "us-east-1"
DYNAMO_TABLE_NAME = "metadata-repository"

def model_execution_timeout(signum, frame):
    print("Timeout on SIGALARM")
    raise Exception("Timeout exception, model is taking too much to process")

def handler(event, context):
    
	logger = logging.getLogger()
	logger.setLevel(logging.DEBUG)
    
	results = []
	for record in event["Records"]:
		
		logger.debug(record)
        
		# 1. Read request
		rawRequest = record['body']
		requestJson = json.loads(rawRequest)  
  
		rawRequest = requestJson['Message']
		requestJson = json.loads(rawRequest)  
  
		logger.info(requestJson)
	
		# 2. Download image from s3
		bucket = requestJson['reference']['bucket']
		key = requestJson['reference']['key']
	
		filePath = f'/tmp/{key}'	
		if  not os.path.exists(filePath):
			os.makedirs(os.path.dirname(filePath))
   
		logger.info(f"Requesting from S3: {key}")
  
		try:
			s3 = boto3.client('s3')
			s3.download_file(bucket, key, filePath)
   
		except:
			logger.error("Failed to obtain image from Bucket")
			return "S3Error: Cannot fetch image from bucket"

		execution_result = {}
	
		logger.info(f"Processing image: {filePath}")
 
		try:
			# 3. Call model with image path
			signal.signal(signal.SIGALRM, handler)
			signal.alarm(30) # 30 seconds timeout
   
			modelResult = call_model_execution(filePath)
			signal.alarm(0)

			execution_result = {
				"leishmaniasis.giemsa:macrophages": modelResult
			}
   
		except:
			logger.error(f"ProcessingError: Model execution failed or timedout")
			execution_result = {
				"leishmaniasis.giemsa:macrophages": []
			}
	
		# 4. Store results in DynamoDB
		itemId = {
			'ID': requestJson['id']
		}
  
		logger.info(f"Setting new metadata")
  
		try:
	
			dynamodb = boto3.resource('dynamodb', region_name=AWS_REGION)
			table = dynamodb.Table(DYNAMO_TABLE_NAME)

			tableUpdateResult = table.update_item(
				Key = itemId,
				UpdateExpression = 'SET #attr1 = :val1, #attr2 = :val2',
  				ExpressionAttributeNames = {'#attr1': 'analysis', '#attr2': 'processed'},
				ExpressionAttributeValues = {':val1': execution_result, ':val2': True},
  				ReturnValues = "UPDATED_NEW"
			)

			results.append(tableUpdateResult)
		except:
			logger.error("Failed to update image metadata")
			return "DynamoDBError: Failed to upload or update metadata"
  
	return results