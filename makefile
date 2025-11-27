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
test:
	npm run test

check-diff:
	git diff --exit-code

release:
	npm run release -- --ci

all: format lint check build