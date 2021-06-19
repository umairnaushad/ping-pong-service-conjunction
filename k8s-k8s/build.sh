#!/bin/sh

echo "####################################################################"
echo "######################## Building Service 1 ########################"
echo "####################################################################"
cd service-1-ping-pong
docker build -t umairnaushad/service-1-ping-pong:1.0.1 .
docker push umairnaushad/service-1-ping-pong:1.0.1
cd ..

echo "####################################################################"
echo "####################### Building Service 2 #########################"
echo "####################################################################"
cd service-2-ping-pong
docker build -t umairnaushad/service-2-ping-pong:1.0.1 .
docker push umairnaushad/service-2-ping-pong:1.0.1
cd ..