#Recyclus services 

A microserives-based system for running remote [Cyclus](http://fuelcycle.org "Cyclus Homepage" simulations. The system 
consist of several microservices:
* [gateway](https://github.com/yarden-livnat/recyclus-gateway.git)
* [batch](https://github.com/yarden-livnat/recyclus-batch.git)
* [worker](https://github.com/yarden-livnat/recyclus-worker.git)
* [datstore](https://github.com/yarden-livnat/recyclus-datastore.git)

This repository contains docker files for running recyclus-services in various configurations on a single machine or on 
a cluster using docker swarm.

### Option 1: A single machine  (docker-compose)

Start Recyclus services on a local machine

* Start: `docker-compose up -d`
* Stop: `docker-compose down`

### Option 2: Swarm cluster

#### Setup the cluster
* start a swarm cluster on a manager machine
* join the swarm from each machine
* Alt: to test locally on a single machine: `docker swarm init`

#### Deploy
`docker stack deploy -c docker-stack.yml recyclus`

#### Take down
`docker stack rm recyclus`

#### Take down swarm
`docker swarm leave --force`


