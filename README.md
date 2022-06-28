# xgboost-base-image

This is the base image to be used by deploy-service[https://github.com/kumarvikas1/deploy-service] to deploy a model on the kubernetes cluster.

Local Setup

Build Image

```
minikube start

eval $(minikube docker-env)

docker build -t xgboost-base-imag:1 .
```
