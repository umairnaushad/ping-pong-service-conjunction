#!/bin/sh

echo "####################################################################"
echo "####################### Deploy on Kubernetes #######################"
echo "####################################################################"
cd k8s-k8s
kubectl apply -f service-1-ping-pong/k8s-service-1.yaml,service-2-ping-pong/k8s-service-2.yaml