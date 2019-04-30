export user ?= ylivnat

targets := build push clean status

SERVICES := gateway batch worker datastore

$(targets): $(SERVICES)

$(SERVICES):
	$(MAKE) -C services/$@ $(MAKECMDGOALS)


services-dir:
	@mkdir -p services

%.git:
	git clone https://github.com/yarden-livnat/recyclus-$@ services/$*

clone: services-dir $(addsuffix .git,$(SERVICES))

repositories:
	@mkdir -p repositories/redis
	@mkdir -p repositories/gateway
	@mkdir -p repositories/jobs
	@mkdir -p repositories/datastore/db repositories/datastore/files

env:
	mkdir -p env
	@read -p "Enter password for admin on db-mongo:" pass;\
	echo "MONGO_INITDB_ROOT_PASSWORD="$$pass | cat env-template/datastore-db.env - > env/datastore-db.env; \
	echo "MONGO_URI=mongodb://recyclus-admin:"$$pass"@datastore-db:27017/datastore?authSource=admin" | cat env-template/datastore.env - > env/datastore.env

	@cp env-template/batch.env env
	@echo JWT_SECRET_KEY=`LC_ALL=C tr -dc 'A-Za-z0-9!"#$%&'\''()*+,-./:;<=>?@[\]^_\`{|}~' </dev/urandom | head -c 13` | cat env-template/gateway.env - > env/gateway.env


setup-clean:
	rm -rf env repositories

setup: setup-clean env repositories

#
# prod/dev environments
#

prod: setup
	@echo production environment ready

dev: setup clone build
	@echo dev environment ready


#
# docker swarm
#

define swarm-status
$(shell docker info | grep Swarm | sed 's/Swarm: //g')
endef

start:
ifeq ($(swarm-status),inactive)
	docker swarm init
endif
	docker stack deploy -c production.yml recyclus
	docker service ls

stop:
	docker stack rm recyclus

exit:
	docker swarm leave --force


.PHONY: $(targets) $(SERVICES) services-dir setup-clean dev clone start stop exit