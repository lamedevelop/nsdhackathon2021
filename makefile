PROJECT_NAME ?= CandyDeliveryApi
VERSION = $(shell python3 setup.py --version | tr '+' '-')
PROJECT_NAMESPACE ?= Oleggr
REGISTRY_IMAGE ?= $(PROJECT_NAMESPACE)/$(PROJECT_NAME)

all:
	@echo "make lint	- Check code with flake8"
	@echo "make test	- Run tests"
	@echo "make local	- Run app locally"
	@echo "make docker	- Run app in docker"
	@exit 0

lint:
	flake8 app --count --exit-zero --exclude=app/db/migrations/ --max-complexity=10 --max-line-length=127 --statistics
	flake8 tests --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics

test:
	pytest -s

local:
	uvicorn app.main:app --reload --host 0.0.0.0

docker:
	docker-compose up --build

db:
	docker-compose run -d --service-ports db
