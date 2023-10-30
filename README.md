## Example SQS request
```json
{
   "Records":[
      {
         "messageId":"baa7d961-9ff9-404f-96cf-14635bf11dda",
         "receiptHandle":"AQEBWPLAQpR03En9i+/Tf1OgbbpZm3ZcD2HbvepAjSQwCCp+iVPwVQM28Jx4CjlzKV/TVq81YRk5baOkLGxZaoJVYyOE5Cqm0tj4XblrozAthliKeT2icEl9IYFQ8MMUk8noyQeiuE+qafVp/7HAlhqjm4I7jqVahzttiFX5KaJKI9ZQqTiWwGld9ZfL0+c8p44PmbuZg3pu4JIJzbyydmusynlr4FvLLlEmdZdkoxMLL4sZ0PgcSoWE5gaFg1Ea/elBs76VMzJEkV1PqXavUJXioogIb9A0NUu9Y3B/pZTVFEdyo5RvED58nJ+OX0cEJQiueGvpyXeyzeZh9WlxBBtbkxi4Ss/hGnxTor5hjZxsOJFBHbdEvBoYbMW5HqJ0FZocm/T+147fqL/IzmknkXxjDA==",
         "body":"{\n  \"Type\" : \"Notification\",\n  \"MessageId\" : \"71327974-5a9b-5173-a56d-24db3f074e8b\",\n  \"TopicArn\" : \"arn:aws:sns:us-east-1:458787618751:leishmaniasis-giemsa\",\n  \"Message\" : \"{\\\"id\\\":\\\"0@dc6381da-0cab-46c0-8e08-dc7693028d6b\\\",\\\"disease\\\":\\\"leishmaniasis-giemsa\\\",\\\"reference\\\":{\\\"bucket\\\":\\\"diagnostic-images-repository\\\",\\\"key\\\":\\\"public/dc6381da-0cab-46c0-8e08-dc7693028d6b/0.jpg\\\"},\\\"date\\\":\\\"2023-10-12T15:32:45.123456Z\\\",\\\"size\\\":1944,\\\"diagnosis\\\":\\\"dc6381da-0cab-46c0-8e08-dc7693028d6b\\\",\\\"sample\\\":0,\\\"topic\\\":{\\\"TopicArn\\\":\\\"arn:aws:sns:us-east-1:458787618751:leishmaniasis-giemsa\\\"}}\",\n  \"Timestamp\" : \"2023-10-22T18:01:00.738Z\",\n  \"SignatureVersion\" : \"1\",\n  \"Signature\" : \"cMLEAiYqtsAeLQ6vMmpxNbVqY5SybzbgvqzeWFpQMUkR1QW+07DfjmV+DF9kR3OLczH46D66tIMiAiuHUmq9nAJ5qMF6Nf1UClIYKZ8CAvlqvCEJDrqui5BaQfq/7iuH/2joNissUUyJ7rMiiLm3oBGlfuXVgm2gBIkMvs6Scne7YjEfCAq5q1es84/vYMYM0DEJwn2iBdnxw+kXb25/VjyE0+FTU1WZknhdWcmZLgT6LUkG1D3PeSenDetCpaCgesvYZNvtk6sGbKzrMOXtwRb0tYV7vUY5WTZQ+qhGE/33fKex/wPyjqSnDWX3QcxRlI+u4G98lPUa9tcF/Pw8yw==\",\n  \"SigningCertURL\" : \"https://sns.us-east-1.amazonaws.com/SimpleNotificationService-01d088a6f77103d0fe307c0069e40ed6.pem\",\n  \"UnsubscribeURL\" : \"https://sns.us-east-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:us-east-1:458787618751:leishmaniasis-giemsa:091ef57f-6624-4b8d-9a24-a5e56db2e989\"\n}",
         "attributes":{
            "ApproximateReceiveCount":"1",
            "AWSTraceHeader":"Root=1-6535635c-c1410de4969135035db1bd92;Parent=40056853305d500d;Sampled=1",
            "SentTimestamp":"1697997660782",
            "SenderId":"AIDAIT2UOQQY3AUEKVGXU",
            "ApproximateFirstReceiveTimestamp":"1697997660789"
         },
         "messageAttributes":{
            
         },
         "md5OfBody":"e388f4c50cf5810aa5c195d18bb008e7",
         "eventSource":"aws:sqs",
         "eventSourceARN":"arn:aws:sqs:us-east-1:458787618751:LeishmaniasisGiemsaQueue",
         "awsRegion":"us-east-1"
      }
   ]
}
```

## Example message payload
```json
{
	"id": "0@dc6381da-0cab-46c0-8e08-dc7693028d6b",
	"disease": "leishmaniasis-giemsa",
	"reference": {
		"bucket": "diagnostic-images-repository",
		"key": "public/dc6381da-0cab-46c0-8e08-dc7693028d6b/0.jpg"
	},
	"date": "2023-10-12T15:32:45.123456Z",
	"size": 1944,
	"diagnosis": "dc6381da-0cab-46c0-8e08-dc7693028d6b",
	"sample": 0
}
```

## Expected result
```json
{
	"leishmaniasis.giemsa:macrophages": [
		{"x": 638, "y": 1218},
		{"x": 394, "y": 1109}
	]
}
```