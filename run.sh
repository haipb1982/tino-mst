# build 
docker build .

# run and publish port
docker run --rm -it --network=host fad8b73976c3 ip addr show eth0
