#!/bin/sh
export SERVICE_1_PORT=5001
export SERVICE_2_PORT=5002
export SERVICE_1_URL=http://service-1-ping-pong-svc:5001/
export SERVICE_1_URL=http://service-2-ping-pong-svc:5002/

echo "####################################################################"
echo "######################## Building Service 1 ########################"
echo "####################################################################"

pwd
ls -lrt
cd service-1-ping-pong
docker build -t umairnaushad/service-1-ping-pong:1.0.0 .
docker push umairnaushad/service-1-ping-pong:1.0.0
cd ..

echo "####################################################################"
echo "####################### Building Service 2 #########################"
echo "####################################################################"

pwd
ls -lrt
cd service-2-ping-pong
docker build -t umairnaushad/service-2-ping-pong:1.0.0 .
docker push umairnaushad/service-2-ping-pong:1.0.0
cd ..

echo "####################################################################"
echo "####################### Deploy on Kubernetes #######################"
echo "####################################################################"
kubectl delete -f service-1-ping-pong/k8s-service-1.yaml,service-2-ping-pong/k8s-service-2.yaml
kubectl apply -f service-1-ping-pong/k8s-service-1.yaml,service-2-ping-pong/k8s-service-2.yaml
