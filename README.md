# Metasharks test task

Тестовое задание metasharks

## Installation

Чтобы запустить проект, выполните следующие команды

```bash
cat .env.temp > .env
docker compose up --build
```

После успешного запуска сервера, выполните в другом окне

```bash
docker compose exec web python manage.py migrate
```

## Usage

Последующие запуски проекта

```bash
docker compose up
```

## Docs

Документация доступна по адресу http://0.0.0.0:8000/docs/
