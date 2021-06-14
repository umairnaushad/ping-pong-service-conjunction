# ping-pong-service-conjunction
(k8s and lambda)
The repository containts two projects. One is used to deploy both python backend servies on k8s. Second one is used to deploy one service on k8s and second service on AWS lanbda.

## k8s-k8s
This directory contains two projects service-1-ping-pong and service-2-ping-pong. The steps to build docker image for both are same.
### 1. Building the project
#### service-1-ping-pong
- cd k8s-k8s/service-1-ping-pong
- docker build -t umairnaushad/service-1-ping-pong:1.0.0 .
- docker push umairnaushad/service-1-ping-pong:1.0.0
- For local testing only (docker run -d -p 5000:5000 umairnaushad/service-1-ping-pong:1.0.0)
- kubectl apply -f k8s-service-1.yaml
#### service-2-ping-pong
- cd k8s-k8s/service-2-ping-pong
- docker build -t umairnaushad/service-2-ping-pong:1.0.0 .
- docker push umairnaushad/service-2-ping-pong:1.0.0
- For local testing only (docker run -d -p 5001:5001 umairnaushad/service-2-ping-pong:1.0.0)
- kubectl apply -f k8s-service-2.yaml

### 2. Executing the project
- cd k8s-k8s
- kubectl apply -f service-1-ping-pong/k8s-service-1.yaml,service-2-ping-pong/k8s-service-2.yaml


## k8s-lambda
