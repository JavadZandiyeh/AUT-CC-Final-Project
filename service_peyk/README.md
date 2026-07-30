# Peyk — subscription and price history API

Django 4.2 + Django REST Framework service that exposes HTTP endpoints for alert subscriptions and stored coin price history. Data is read from and written to the shared MySQL `coin_db` database.

Part of the [AUT Cloud Computing Final Project](../README.md).

## Role in the system

| Client action | Peyk endpoint | Database |
| --- | --- | --- |
| Subscribe to price-change alerts | `POST /subscribe/` | Insert into `AlertSubscriptions` |
| View stored prices | `POST /price/` | Select from `Prices` |

The React UI calls these endpoints. Bepa writes `Prices` / `Coin` and evaluates subscriptions separately.

## Layout

```text
service_peyk/
├── Dockerfile
├── requirements.txt
└── project_peyk/
    ├── entrypoint.sh          # manage.py runserver ${APP_IP}:${APP_PORT}
    ├── manage.py
    ├── project_peyk/          # Django project settings, URLs, WSGI/ASGI
    └── app_peyk/
        ├── models.py          # Coin, Prices, AlertSubscriptions (managed=DB tables)
        ├── serializers.py
        ├── views.py
        ├── urls.py
        └── tests.py           # Placeholder only
```

## Dependencies

From `requirements.txt`:

- Django 4.2  
- djangorestframework 3.14.0  
- mysqlclient 1.4.3  
- pymysql 1.0.3  
- requests 2.28.2  

## API

Base URL in Compose: `http://localhost:8001/`  
Django admin is also mounted at `/admin/`.

### `POST /subscribe/`

Request JSON:

```json
{
  "email": "user@example.com",
  "coin_name": "bitcoin",
  "difference_percentage": 5
}
```

- `difference_percentage`: integer 0–100  
- Coin must already exist in `Coin` or the API returns HTTP 400  
- Unique constraint: `(email, coin_name)`  

Success: HTTP 200 with a message derived from the saved subscription.  
Validation / DB errors: HTTP 400.

### `POST /price/`

Request JSON:

```json
{
  "coin_name": "bitcoin"
}
```

Success: HTTP 200 with `message` as a list of `{coin_name, time_stamp, price}` objects.  
Unknown coin or errors: HTTP 400.

Implementation note: history is loaded with a raw SQL query on `Prices`, not the Django ORM queryset API.

## Configuration

| Variable | Description |
| --- | --- |
| `APP_IP` | Bind address (Compose: `0.0.0.0`) |
| `APP_PORT` | Port (Compose: `8001`) |
| `MYSQL_DATABASE` | DB name |
| `MYSQL_HOST` | DB host |
| `MYSQL_PORT` | DB port |
| `MYSQL_ROOT_PASSWORD` | Password for user `root` |

Django settings use engine `django.db.backends.mysql` and user `root`. `DEBUG` is `True`; `SECRET_KEY` is hardcoded in `settings.py` (not suitable for production).

## Run with Docker Compose

Started by `./run.sh` / `docker-compose up` as service `peyk` (image `peyk:v1`). Working directory inside the container is `/app/project_peyk`; entrypoint runs `python3 manage.py runserver`.

## Run locally

```bash
cd service_peyk
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd project_peyk
export APP_IP=0.0.0.0 APP_PORT=8001
export MYSQL_DATABASE=coin_db MYSQL_HOST=127.0.0.1 MYSQL_PORT=3306 MYSQL_ROOT_PASSWORD=pass
python3 manage.py runserver ${APP_IP}:${APP_PORT}
```

Requires a reachable MySQL instance with the project schema already applied.

## Testing

`app_peyk/tests.py` contains no cases. Default CRA/Django scaffolds elsewhere in the repo are not Peyk API tests.

## Related docs

- [Project README](../README.md)
- [Bepa worker](../service_bepa/README.md)
- [React UI](../service_react/app_react/README.md)
- [Deployments](../deployments/README.md)
