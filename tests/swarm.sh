#!/usr/bin/env bash

#docker-machine create --driver virtualbox -virtualbox-share-folder `pwd`/repositories:/repositories vm1
#docker-machine create --driver virtualbox -virtualbox-share-folder `pwd`/repositories:/repositories vm2
#docker-machine create --driver virtualbox -virtualbox-share-folder `pwd`/repositories:/repositories vm3

docker-machine start vm1
docker-machine start vm2
docker-machine start vm3

SWARM_MASTER=vm1
IP=`docker-machine ip $SWARM_MASTER`

docker-machine ssh $SWARM_MASTER "docker swarm init --advertise-addr $IP"
SWARM_TOKEN=`docker-machine ssh $SWARM_MASTER "docker swarm join-token worker -q"`


docker-machine ssh vm2 "docker swarm join --token $SWARM_TOKEN $IP:2377"
docker-machine ssh vm3 "docker swarm join --token $SWARM_TOKEN $IP:2377"

eval $(docker-machine env vm1)
docker stack deploy -c docker-compose.yml recyclus

docker stack ps recyclus

docker stack rm recyclus

eval $(docker-machine env -u)
