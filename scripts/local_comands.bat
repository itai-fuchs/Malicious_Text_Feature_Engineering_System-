docker network create app-network

#kafka container
#rollback
docker rm -f broker

docker run -d --name broker -p 9092:9092 --network app-network `
    -e KAFKA_NODE_ID=1 `
    -e KAFKA_PROCESS_ROLES=broker,controller `
    -e KAFKA_CONTROLLER_LISTENER_NAMES=CONTROLLER `
    -e KAFKA_LISTENERS=PLAINTEXT://:9092,CONTROLLER://:9093 `
    -e KAFKA_INTER_BROKER_LISTENER_NAME=PLAINTEXT `
-e KAFKA_ADVERTISED_LISTENERS=PLAINTEXT://broker:9092 `
    -e KAFKA_CONTROLLER_QUORUM_VOTERS=1@localhost:9093 `
    apache/kafka:latest

cd C:\Users\itai\PycharmProjects\Malicious_Text_Feature_Engineering_System-\Retriever



cd ../retriever
#retriever

#rollback
docker rm -f retriever_container
docker rmi retriever_image

# Build the retriever_image
docker build -t retriever_image .

# Run the container
docker run -d --name retriever_container --network app-network retriever_image

#preprocessor

cd ../preprocessor
#rollback
docker rm -f preprocessor_container
docker rmi preprocessor_image

# Build the preprocessor_image
docker build -t preprocessor_image .

# Run the container
docker run -d --name preprocessor_container --network app-network preprocessor_image

#persister
cd ../persister
#rollback
docker rm -f persister_container
docker rmi persister_image

# Build the persister_image
docker build -t persister_image .

# Run the container
docker run -d --name persister_container --network app-network persister_image


#enricher
#rollback
docker rm -f enricher_container
docker rmi enricher_image

# Build the enricher_image
docker build -t enricher_image .

# Run the container
docker run -d --name enricher_container --network app-network enricher_image