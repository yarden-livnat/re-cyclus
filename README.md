# Recyclus services 

A microservices-based system for running remote [Cyclus](http://fuelcycle.org "Cyclus Homepage") simulations. 
The system consist of several microservices:
* [gateway](https://github.com/yarden-livnat/recyclus-gateway.git)
* [batch](https://github.com/yarden-livnat/recyclus-batch.git)
* [worker](https://github.com/yarden-livnat/recyclus-worker.git)
* [datstore](https://github.com/yarden-livnat/recyclus-datastore.git)
* [redis]()
* [mongodb]()

This repository contains docker files for running recyclus-services in various configurations on a single machine or on 
a cluster using docker swarm.

#### Dependencies
* Docker : https://www.docker.com
* make


## Quick Start

Setup production environment: `make prod`
* Start docker swarm: `docker swarm init`
* Deploy recyclus services on local machine: `docker stack deploy -c docker-compose.yml recyclus`
* Interact with the system via python package: [Recyclus](https://github.com/yarden-livnat/recyclus.git)
* Take down: `docker stack rm recyclus`
* Shut down the swarm: `docker swarm leave --force`


## Development
Set up the development environment: `make dev`
* Create ./services directory and clone the micoservices projects from github
* Create ./repositories directory where the services will maintain their data for debuging purposes
* Asks for an admin password for mongodb service

#### Running
* Start: `docker-compose up -d`
* Stop: `docker-compose down`


## Distributed Deployment 
Modify the docker-stack.yml file to fit your distributed environment and deploy using 
```
docker stack -f docker-stack.yml recyclus
```
