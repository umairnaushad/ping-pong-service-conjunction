#!/bin/sh

echo "####################################################################"
echo "########################### Building k8s ###########################"
echo "####################################################################"
cd k8s-ping-pong
docker build -t umairnaushad/k8s-ping-pong:1.0.1 .
docker push umairnaushad/k8s-ping-pong:1.0.1
cd ..

echo "####################################################################"
echo "####################### Building Service 2 #########################"
echo "####################################################################"
cd lambda-ping-pong
sam build
cd ..
