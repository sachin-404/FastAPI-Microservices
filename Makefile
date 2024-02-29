install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt
		
format:
	black *.py mylib/*.py

lint:
	pylint --disable=R,C *.py mylib/*.py
	
test:
	python -m pytest -vv --cov=mylib test_logic.py

build:
	docker build -t wiki-microservice .

run:
	docker run -p 8000:8000 wiki-microservice
	
deploy:
	# deploy

all: install format lint test deploy