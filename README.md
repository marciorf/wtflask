# wtflask

Depois de clonar o projeto: 

`pip install -r requirements.txt`

`flask run` < Nao funciona

`PYTHONPATH=api:$PYTHONPATH flask run` < funciona

`nosetests tests/*.py` < Nao funciona

`PYTHONPATH=api:$PYTHONPATH nosetests tests/*.py` < funciona
