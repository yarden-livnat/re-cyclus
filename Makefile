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
	@echo "set env"
	mkdir -p env
	@read -p "Enter password for admin on db-mongo:" pass;\
	echo "MONGO_INITDB_ROOT_PASSWORD="$$pass | cat env-template/datastore-db.env - > env/datastore-db.env; \
	echo "MONGO_URI=mongodb://recyclus-admin:"$$pass"@datastore-db:27017/datastore?authSource=admin" | cat env-template/datastore.env - > env/datastore.env

	@cp env-template/batch.env env

	@echo JWT_SECRET_KEY=`LC_ALL=C tr -dc 'A-Za-z0-9!"#$%&'\''()*+,-./:;<=>?@[\]^_\`{|}~' </dev/urandom | head -c 13` | cat env-template/gateway.env - > env/gateway.env


setup: env


prod: env repositories


dev: clone repositories setup build
	@echo dev environment ready

clean-repositories:
	rm -rf repositories

clean: clean-repositories repositories
	rm -rf env

.PHONY: $(targets) $(SERVICES) services-dir setup clean-repositories dev clone local