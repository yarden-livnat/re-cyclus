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

* Setup base environment: `make prod`
* Start the services: `docker-compose -f docker-compose.yml up -d`
* Stop the services: `docker-compose down`

To interact with the services use python package: [Recyclus](https://github.com/yarden-livnat/recyclus.git)


## Development
Set up the development environment: `make dev`. This will Create ./services directory and clone the micoservices 
projects from github.

* Start the services: `docker-compose up`
* Stop the services: `docker-compose down`

In this setup, each service container will mount the appropriate "./services/SERVICE" code directory. 

## Distributed Deployment 
Distributed deployment is done using docker swarm.

To use docker swam on a single machine
* start: `make start`
* stop: `make stop`
* exit swarm mode: `make exit`

In order to deploy on multiple machine you'll need to modify and adapt docker-stack.yml
