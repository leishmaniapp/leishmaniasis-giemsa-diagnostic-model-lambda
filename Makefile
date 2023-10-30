all: build

test: Dockerfile lambda_function.py model.py requirements.txt
	docker build --platform linux/amd64 -t leishmaniasis-macrophages-analysis:test .

build: Dockerfile lambda_function.py model.py requirements.txt
	docker build --platform linux/amd64 -t leishmaniasis-macrophages-analysis .

.PHONY: aws
aws: build
	docker tag leishmaniasis-macrophages-analysis:latest 458787618751.dkr.ecr.us-east-1.amazonaws.com/diagnostic-models:leishmaniasis-giemsa-diagnostic-model-lambda
	docker push 458787618751.dkr.ecr.us-east-1.amazonaws.com/diagnostic-models:leishmaniasis-giemsa-diagnostic-model-lambda

.PHONY: run
run: build
	docker run --rm -it -p 9000:8080 -e AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} -e AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} leishmaniasis-macrophages-analysis:test