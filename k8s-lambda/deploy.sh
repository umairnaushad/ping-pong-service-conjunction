
echo "####################################################################"
echo "####################### Deploy on Kubernetes #######################"
echo "####################################################################"
kubectl apply -f k8s-ping-pong/k8s.yaml

echo "####################################################################"
echo "####################### Deploy Lambda #######################"
echo "####################################################################"
cd lambda-ping-pong
sam local start-api -p 32104
#sam deploy --guided
