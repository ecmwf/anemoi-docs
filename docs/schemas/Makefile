all: ../_static/dependencies.svg

../_static/dependencies.svg: dependencies.dot Makefile
	dot -o ../_static/dependencies.svg -Tsvg dependencies.dot
