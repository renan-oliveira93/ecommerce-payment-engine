# E-commerce Payment Engine

Microsserviço de processamento assíncrono de pagamentos, orientado a eventos (Stripe → RabbitMQ → workers). 

## Stack

Python 3.12+, FastAPI, RabbitMQ, PostgreSQL 16+, Docker Compose.

## Setup local

1. Criar e ativar o ambiente virtual:

   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   ```

2. Instalar as dependências (runtime + desenvolvimento):

   ```bash
   pip install -r requirements.txt -r requirements-dev.txt
   ```

3. Instalar os hooks de pre-commit:

   ```bash
   pre-commit install
   ```

4. Copiar as variáveis de ambiente de exemplo:

   ```bash
   cp .env.example .env
   ```

5. Subir a infraestrutura local (Postgres, RabbitMQ, Jaeger):

   ```bash
   docker-compose up -d
   ```

   - RabbitMQ management UI: http://localhost:15672 (usuário/senha em `docker-compose.yml`)
   - Jaeger UI: http://localhost:16686

## Rodando a aplicação

```bash
uvicorn src.api.main:app --reload
```

## Qualidade de código

```bash
ruff check .
ruff format .
mypy src
```

## Testes

```bash
pytest tests/unit                 # testes unitários
pytest tests/integration -m integration  # testes de integração (requerem Docker)
pytest --cov                      # com cobertura
```
