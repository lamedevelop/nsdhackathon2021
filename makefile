PROJECT_NAME ?= CandyDeliveryApi
VERSION = $(shell python3 setup.py --version | tr '+' '-')
PROJECT_NAMESPACE ?= Oleggr
REGISTRY_IMAGE ?= $(PROJECT_NAMESPACE)/$(PROJECT_NAME)

all:
	@echo "make local	- Run app locally"
	@exit 0

local:
	docker-compose up --build
