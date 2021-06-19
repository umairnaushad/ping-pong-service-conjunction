# ping-pong-service-conjunction
(k8s and lambda)
The repository containts two projects. One is used to deploy both python backend servies on k8s. Second one is used to deploy one service on k8s and second service on AWS lanbda. Two clone to local machine:
<br> git clone https://github.com/umairnaushad/ping-pong-service-conjunction.git

## Pre-requisites
Make sure that you have following installer on test deployment machine
- docker
- kubernetes
- python 3.7
- AWS CLI (https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html)
- SAM CLI (https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install-linux.html)
Note:- OS should be linux because some automation scripts are using bash scripting

## Project 1 - k8s-k8s
This directory contains two projects service-1-ping-pong and service-2-ping-pong. The steps to build docker image for both are same.
### 1. Building the project
#### service-1-ping-pong
- cd k8s-k8s/service-1-ping-pong
- docker build -t umairnaushad/service-1-ping-pong:1.0.1 .
- docker push umairnaushad/service-1-ping-pong:1.0.1
- For local testing only (docker run -d -p 5001:5000 umairnaushad/service-1-ping-pong:1.0.1)
- curl http://127.0.0.1:5001/
#### service-2-ping-pong
- cd k8s-k8s/service-2-ping-pong
- docker build -t umairnaushad/service-2-ping-pong:1.0.1 .
- docker push umairnaushad/service-2-ping-pong:1.0.1
- For local testing only (docker run -d -p 5002:5000 umairnaushad/service-2-ping-pong:1.0.1)
- curl http://127.0.0.1:5002/

### 2. Executing the project
- cd k8s-k8s
- kubectl apply -f service-1-ping-pong/k8s-service-1.yaml,service-2-ping-pong/k8s-service-2.yaml

### 3. Testing the project
To test both services on kubernetes use bash file "test.sh"

### 4. For CI/CD
To build  both services on kubernetes use bash file "build.sh"
To deploy both services on kubernetes use bash file "deploy.sh"



## Project 2 - k8s-lambda
This directory contains two projects k8s-ping-pong and lambda-ping-pong.
### 1. Building the project
#### k8s-ping-pong
- cd k8s-lambda/k8s-ping-pong
- docker build -t umairnaushad/k8s-ping-pong:1.0.1 .
- docker push umairnaushad/k8s-ping-pong:1.0.1
- For local testing only (docker run -d -p 5003:5000 umairnaushad/k8s-ping-pong:1.0.1)
- curl http://127.0.0.1:5003/
#### lambda-ping-pong
- sam build
- For local testing only (sam local start-api -p 5004)
- curl http://127.0.0.1:5004/

### 3. Testing the project
To test both services use bash file "test.sh"

### 4. For CI/CD
To build  both services on kubernetes use bash file "build.sh"
To deploy both services on kubernetes use bash file "deploy.sh"
