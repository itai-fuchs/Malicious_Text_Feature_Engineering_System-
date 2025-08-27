#1
#initialization open shift project
oc delete all --all
oc delete pvc --all
oc delete configmap --all
oc delete secret --all




#4
# run API
oc apply -f fastApi_diployment.yaml -n itaifuchs-dev
oc apply -f fastApi_service.yaml -n itaifuchs-dev
oc apply -f fastApi_route.yaml -n itaifuchs-dev
oc rollout status deploy/data-loader-api -n 0533orel-dev
oc get route data-loader-api -n itaifuchs-dev


#kafka container
# create image & container
docker run -d --name broker  -p 9092:9092 `
    -e KAFKA_CFG_NODE_ID=1 `
    -e KAFKA_CFG_PROCESS_ROLES=broker,controller `
    -e KAFKA_CFG_CONTROLLER_LISTENER_NAMES=CONTROLLER `
    -e KAFKA_CFG_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 `
    -e KAFKA_CFG_ADVERTISED_LISTENERS=PLAINTEXT://broker:9092 `
    -e KAFKA_CFG_CONTROLLER_QUORUM_VOTERS=1@localhost:9093 `
    bitnami/kafka:latest

#rollback
docker rm -f broker
