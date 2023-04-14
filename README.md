# Arquitetura de serviço em Python

Este projeto é um exemplo de arquitetura feito em python visando um desenvolvimento mais
agil e com foco no negócio em que esse novo sistema inserido está.

# Estrutura
Esta arquitetura está utilizando como gerenciamento de dependências o [Poetry](https://python-poetry.org/docs/).
<br/>
Como framework base vai ser utilizado o [FastAPI](https://fastapi.tiangolo.com).
<br />
Para adicionar novas dependencias ao projeto utilize o comando abaixo:
```
poetry add [dependencia]
```
Com ele vai ser instalado a dependencia e ser automaticamente adicionado no poetry.lock, assim evitando
ter problemas com atualização da dependencia toda vez que o projeto for baixado e instalado.
<br/>