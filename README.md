# trabalho-dataops-mlops
Trabalho da pós graduação matéria: DataOps e MLOps. Esteira CI/CD Python

# Projeto CI/CD - Pipeline de Dados

Este projeto tem como objetivo implementar um pipeline de dados em Python com integração contínua (CI) utilizando GitHub Actions.

## Tecnologias utilizadas

* Python 3.11
* Pytest
* GitHub Actions

## Pipeline CI

O workflow automatiza as seguintes etapas:

* Instalação de dependências
* Execução de testes automatizados
* Execução do pipeline de dados

## Testes

Os testes foram implementados utilizando pytest para validar o processamento dos dados.

## Execução

Para rodar localmente:

```bash
pip install -r requirements.txt
pytest
python app/pipeline.py
```

## Saída

O pipeline gera um arquivo `summary.csv` com o resumo dos dados processados.

## Resultado

A pipeline foi validada com sucesso utilizando GitHub Actions.
