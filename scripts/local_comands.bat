#3
#build api image
docker build -t itaifuchs/app-api:mongodb .
docker push itaifuchs/data-loader-api:mongodb


#retriever

#rollback
docker rm -f retriever_container
docker rmi retriever_image

# Build the retriever_image
docker build -t retriever_image .
docker push itaifuchs/retriever_image:v1.0

# Run the container
docker run -d --name retriever_container retriever_image

