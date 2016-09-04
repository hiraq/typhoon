IMAGE_NAME ?= typhoon
IMAGE_VERSION ?= 0.6.0
IMAGE_BUILD = $(IMAGE_NAME):$(IMAGE_VERSION)

.PHONY: build

build:
	docker build -t $(IMAGE_BUILD) .
