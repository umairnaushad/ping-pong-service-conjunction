#!/bin/sh

echo "####################################################################"
echo "####################### Deploy on Kubernetes #######################"
echo "####################################################################"
kubectl apply -f service-1-ping-pong/k8s-service-1.yaml,service-2-ping-pong/k8s-service-2.yaml
echo "Deploying please wait ..."
sleep 20
kubectl get po -n devops-ping-pong