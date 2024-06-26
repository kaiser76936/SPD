setup:
		python3 -m venv ~/.flask-ml-azure
		#source ~/.flask-ml-azure/bin/activate
		
install:
		pip install --upgrade pip &&\
				pip install -r requeriments.txt
				
test:
		python -m pytest -vv --cov=hello test_hello.py
		#python -m pytest --nbval notebook.ipynb
		
lint:
		pylint --disable=R,C hello.py

all: install lint test