IMAGE_NAME ?= typhoon
IMAGE_VERSION ?= 0.6.0
IMAGE_BUILD = $(IMAGE_NAME):$(IMAGE_VERSION)

.PHONY: build compose

build:
	docker build -t $(IMAGE_BUILD) .

compose:
	docker-compose config
	docker-compose up
