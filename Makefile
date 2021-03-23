VENV_NAME?=venv
MODULE=py4envi
LIBS=py4envi setup.py
PYTHON=${VENV_NAME}/bin/python3

venv: $(VENV_NAME)/bin/activate

$(VENV_NAME)/bin/activate: test-requirements.txt requirements.txt setup.py
	python -m virtualenv -p python3 $(VENV_NAME)
	${PYTHON} -m pip install -U pip
	${PYTHON} -m pip install -r test-requirements.txt -r requirements.txt
	touch $(VENV_NAME)/bin/activate

clean:
	rm -rf ./$(VENV_NAME)
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	rm -rf ./build
	rm -rf ./dist
	rm -rf *.egg-info

lint: venv
	${PYTHON} -m autopep8 --in-place -a -a -r ${LIBS} tests
	${PYTHON} -m autoflake --in-place --recursive --remove-all-unused-imports ${LIBS} tests
	${PYTHON} -m mypy --ignore-missing-imports ${LIBS} tests

test: venv
	${PYTHON} -m pytest tests --capture=no --verbose 

coverage: venv
	${PYTHON} -m pytest --cov=py4envi

dist:
	rm -rf *.egg-info
	${PYTHON} setup.py sdist bdist_wheel

install: dist
	${PYTHON} -m pip uninstall -y $(MODULE)
	${PYTHON} -m pip install .
