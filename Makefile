all: clean test

init:
	pip install -r requirements.txt

test:
	nosetests --with-coverage --cover-erase --cover-package=algorist --cover-html tests/*

clean:
	rm -rf cover
	rm -rf build
	rm -rf dist
	rm -rf .coverage
