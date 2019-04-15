# Recyclus services 

A microserives-based system for running remote [Cyclus](http://fuelcycle.org "Cyclus Homepage" simulations. The system 
consist of several microservices:
* [gateway](https://github.com/yarden-livnat/recyclus-gateway.git)
* [batch](https://github.com/yarden-livnat/recyclus-batch.git)
* [worker](https://github.com/yarden-livnat/recyclus-worker.git)
* [datstore](https://github.com/yarden-livnat/recyclus-datastore.git)

This repository contains docker files for running recyclus-services in various configurations on a single machine or on 
a cluster using docker swarm.

## Installation

### Dependencies
* Docker : https://www.docker.com
* make

### Development environment
`make dev`

This will set up the development environment. 
* create ./services directory and clone the micoservices projects from github
* create ./repositories directory where the services will maintain their data for debuging purposes
* asks for an admin passpord for mongodb service


### Production environment 
`make setup`

 
## Running

### Option 1: Run on local machine using docker-compose
This option is available when using a development environment. It is based on the ./docker-compose.yml file.
The services will be built and loaded from the ./services directory

* Start: `docker-compose up -d`
* Stop: `docker-compose down`

### Option 2: Swarm cluster

This option is based on ./docker-stack.yml file. It is similar to ./docker-compose.yml but uses the published docker 
images of the services.

#### Setup the cluster
* start a swarm cluster on a manager machine
* join the swarm from each machine
* Alt: to test locally on a single machine use: `docker swarm init`

#### Deploy
`docker stack deploy -c docker-stack.yml recyclus`

#### Take down
`docker stack rm recyclus`

#### Take down swarm
`docker swarm leave --force`


