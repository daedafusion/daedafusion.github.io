all: clean dependencies.png

dependencies.png: dependencies.dot
	dot -Tpng -o dependencies.png dependencies.dot

dependencies.dot:
	python dependencies.py

open:
	open dependencies.png

clean:
	rm -f dependencies.dot