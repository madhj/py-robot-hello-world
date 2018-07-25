default: start

run: setup start

setup:
	pip install -r requirements.txt

start:
	pybot HelloWorld.txt
