# UNIFOOD - seu app de delyvery universitário

É MVP de API RESTFull que tem como objetivo de gerenciar o fluxo de estoque de produtos, controle de usuarios e realização de pedidos e compra.

# Coisas usadas
No projeto busquei deixar o codigo fonte o mais clean possivel, além de separar as dependencias e atribuições por pastar e usar algums patters
como repositorys, schemas, models e assim por diante bem definidos e também adicioanar algumas boas praticas de segurança como token e criptografica de senhas, middlewares e tasks para monitorar o tempo das requisições.

# Tecnologias usadas

- SQLITE
- Alembic
- FastAPI
- Pydantic
- Typing

# Dependencias 

Para executar o projeto localmente faça instalação em um ambiente virtual nos seguintes passos:

```bash
$ pip3 install virtualenv
$ virtualenv venv -p python3
$ source venv/bin/activate
$ pip install -r requirements.txt
```
