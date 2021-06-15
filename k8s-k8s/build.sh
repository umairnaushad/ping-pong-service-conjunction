#!/bin/sh
echo "Building Service 1"
pwd
ls -lrt
cd k8s-k8s/service-1-ping-pong
docker build -t umairnaushad/service-1-ping-pong:1.0.0 .
docker push umairnaushad/service-1-ping-pong:1.0.0
cd ..
cd ..

echo "Building Service 2"
pwd
ls -lrt
cd k8s-k8s/service-2-ping-pong
docker build -t umairnaushad/service-2-ping-pong:1.0.0 .
docker push umairnaushad/service-2-ping-pong:1.0.0

echo "Completed"