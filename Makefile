hello:
	echo "this is my first make command"

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test_adder:
	python -m pytest -vv test_adder.py

test_hello:
	python -m pytest -vv test_hello.py
all: hello install
