PWD := $(shell pwd)

run:
	docker run -t --name jekyll --rm -v $(PWD):/usr/src/app -p 4000:4000 starefossen/github-pages 
