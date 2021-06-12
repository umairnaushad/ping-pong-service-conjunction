# ping-pong-service-conjunction
(k8s and lambda)
The repository containts two projects. One is used to deploy both python backend servies on k8s. Second one is used to deploy one service on k8s and second service on AWS lanbda.

## k8s-k8s
This directory contains two projects service-1-ping-pong and service-2-ping-pong. The steps to build docker image for both are same.
- docker build -t umairnaushad/service-1-ping-pong:1.0.0 .
- docker push umairnaushad/service-1-ping-pong:1.0.0
