#!/bin/sh

echo "####################################################################"
echo "########################### Building k8s ###########################"
echo "####################################################################"

pwd
ls -lrt
cd k8s-ping-pong
docker build -t umairnaushad/k8s-ping-pong:1.0.1 .
docker push umairnaushad/k8s-ping-pong:1.0.1
cd ..

echo "####################################################################"
echo "####################### Building Service 2 #########################"
echo "####################################################################"

echo "####################################################################"
echo "####################### Deploy on Kubernetes #######################"
echo "####################################################################"
kubectl apply -f k8s-ping-pong/k8s.yaml
