all: ../_static/dependencies.svg ../_static/dependencies.png

../_static/dependencies.svg: dependencies.dot Makefile
	dot -o ../_static/dependencies.svg -Tsvg dependencies.dot

../_static/dependencies.png: dependencies.dot Makefile
	dot -o ../_static/dependencies.png -Tpng dependencies.dot
