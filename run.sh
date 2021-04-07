# build 
docker build .

# run and publish port
docker run --rm -it --network=host e3d148b6acff ip addr show eth0

# docker stop all containers before remove
docker stop $(docker ps -a --format="{{.ID}}")

# docker rm all containers
docker rm $(docker ps -a --format="{{.ID}}")

# docker rm all images
docker rmi $(docker images -a --format="{{.ID}}")