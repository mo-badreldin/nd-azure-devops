hello:
	echo "this is my first make command"

install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

lint:
	pylint --disable=R,C,E1120 hello.py

test_adder:
	python -m pytest -vv test_adder.py

test_hello:
	python -m pytest -vv test_hello.py

test: test_adder test_hello

exec:
	python hello.py
