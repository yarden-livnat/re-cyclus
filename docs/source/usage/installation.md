Installation
------------

Dependencies

* Docker : https://www.docker.com
* make

Quick start
-----------

Recyclus services consists of several services that can run on one or more machines using either docker-compose
or docker stack. The configuration files for the services are located in ./env directory.  

`make setup`

will create the env directory and configuration files. 

Production
----------
In production Recyclus Services deploy ready-to-run Docker images of the services using a deployment specification
docker-stack.yml

