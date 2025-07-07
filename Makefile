DOCKER_IMAGE_NAME = waiyankyawsdk1999/odoo17

# Auto-generate version from Git
VERSION := $(shell [ -d .git ] && git rev-list --count HEAD || echo "0")

.PHONY: build push latest deploy

build:
	docker build -t $(DOCKER_IMAGE_NAME):$(VERSION) -t $(DOCKER_IMAGE_NAME):latest .

push:
	docker push $(DOCKER_IMAGE_NAME):$(VERSION)
	docker push $(DOCKER_IMAGE_NAME):latest

latest:
	@echo "Current version (Git commits count): $(VERSION)"

deploy: build push
