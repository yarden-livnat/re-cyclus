export user ?= ylivnat

targets := all build push clean

SERVICES := gateway batch worker datastore

$(targets): $(SERVICES)

$(SERVICES):
	@echo $(MAKE) -C services/$@ $(MAKECMDGOALS)

.PHONY: $(targets) $(SERVICES)


%.git:
	git clone https://github.com/yarden-livnat/recyclus-$@ services/$*

clone: services-dir $(addsuffix .git,$(SERVICES))

services-dir:
	@mkdir services

