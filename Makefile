all: build

build: Dockerfile lambda_function.py
	docker build --platform linux/amd64 -t leishmaniasis-macrophages-lambda:test .

.PHONY: run
run: build
	docker run --rm -it -p 9000:8080 -e AWS_ACCESS_KEY_ID=${AWS_ACCESS_KEY_ID} -e AWS_SECRET_ACCESS_KEY=${AWS_SECRET_ACCESS_KEY} leishmaniasis-macrophages-lambda:test