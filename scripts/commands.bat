#1
#initialization open shift project
oc delete all --all
oc delete pvc --all
oc delete configmap --all
oc delete secret --all


#3
#build api image
docker build -t itaifuchs/app .
docker push itaifuchs/app .


#4
# run API
oc apply -f fastApi_diployment.yaml -n itaifuchs-dev
oc apply -f fastApi_service.yaml -n itaifuchs-dev
oc apply -f fastApi_route.yaml -n itaifuchs-dev
oc rollout status deploy/data-loader-api -n 0533orel-dev
oc get route data-loader-api -n itaifuchs-dev



