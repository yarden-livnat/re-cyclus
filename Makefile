export user ?= ylivnat

targets := build push clean status

SERVICES := gateway batch worker datastore

$(targets): $(SERVICES)

$(SERVICES):
	$(MAKE) -C services/$@ $(MAKECMDGOALS)



services-dir:
	@mkdir services

%.git:
	git clone https://github.com/yarden-livnat/recyclus-$@ services/$*

clone: services-dir $(addsuffix .git,$(SERVICES))

repositories:
	@mkdir -p repositories/redis
	@mkdir -p repositories/gateway
	@mkdir -p repositories/jobs
	@mkdir -p repositories/datastore/db repositories/datastore/db

setup: clone repositories


.PHONY: $(targets) $(SERVICES) services-dir repositories