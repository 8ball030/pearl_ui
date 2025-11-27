.PHONY: build
build:
	npm run build
dev:
	npm run dev
preview:
	npm run preview
lint:
	npm run lint
format:
	npm run format
check:
	npm run check

all: format lint check build