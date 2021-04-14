# build 
docker build .

# run and publish port
docker run --rm -it --network=host 39199308ac0a ip addr show eth0

# docker stop all containers before remove
docker stop $(docker ps -a --format="{{.ID}}")

# docker rm all containers
docker rm $(docker ps -a --format="{{.ID}}")

# docker rm all images
docker rmi $(docker images -a --format="{{.ID}}")

docker system prune