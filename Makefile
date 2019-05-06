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



#
# dev environments
#

dev: clone build
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
	docker stack deploy -c docker-stack.yml recyclus
	docker service ls

stop:
	docker stack rm recyclus

exit:
	docker swarm leave --force


.PHONY: $(targets) $(SERVICES) services-dir dev clone start stop exit