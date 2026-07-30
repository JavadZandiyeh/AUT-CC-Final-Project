# Bepa — price poller and alert worker

Python background service that polls CoinNews, stores prices in MySQL, and sends Mailgun emails when subscription thresholds are met.

Part of the [AUT Cloud Computing Final Project](../README.md).

## Role in the system

Bepa is not an HTTP API. It runs an infinite loop:

1. Fetch coin name list from CoinNews  
2. Ensure names exist in `Coin`  
3. Fetch each coin’s current price  
4. Compare with the latest `Prices` row  
5. Notify matching `AlertSubscriptions` via Mailgun  
6. Insert the new price  
7. Sleep `INTERVAL_SECONDS`

## Layout

```text
service_bepa/
├── Dockerfile          # Multi-stage Python 3.9 Alpine image
├── requirements.txt    # requests, pymysql
├── bepa.py             # Main poll/alert loop
└── db_handler.py       # MySQL access (PyMySQL DictCursor)
```

## Dependencies

- `requests==2.28.2`
- `pymysql==1.0.3`

## Configuration

| Variable | Required | Description |
| --- | --- | --- |
| `INTERVAL_SECONDS` | Yes | Seconds between poll cycles |
| `COINNEWS_ENDPOINT` | Yes | Base URL (no trailing path), e.g. `http://coin_news:8000` |
| `MYSQL_HOST` | Yes | MySQL hostname |
| `MYSQL_PORT` | Yes | MySQL port |
| `MYSQL_DATABASE` | Yes | Database name |
| `MYSQL_ROOT_PASSWORD` | Yes | Password for DB user `root` |

Bepa always connects as MySQL user `root` (not `MYSQL_USER`).

CoinNews endpoints used:

- `GET {COINNEWS_ENDPOINT}/api/data/` → JSON list of coin names  
- `GET {COINNEWS_ENDPOINT}/api/data/{coin_name}/` → JSON object with `value` (price)

## Run with Docker Compose

From the repository root, Bepa is started with the rest of the stack (`./run.sh` or `docker-compose up`). Compose sets `INTERVAL_SECONDS=180` and `COINNEWS_ENDPOINT=http://coin_news:8000`, and loads `env/shared.env`.

Image build context: this directory (`bepa:v1`).

## Run the worker locally (without Compose)

With MySQL and CoinNews reachable and env vars set:

```bash
cd service_bepa
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python bepa.py
```

## Email alerts

`send_email` posts to the Mailgun Messages API. Credentials and sandbox domain are hardcoded in `bepa.py`. For any shared or production use, move them to secrets/env and rotate keys.

## Known limitations

- Change formula is marked with a `TODO` in source  
- `triggered_subscription` does not include `coin_name` in the SQL `WHERE` clause  
- Published Compose port `8002` is unused by this process  
- No unit tests in this service directory

## Related docs

- [Project README](../README.md)
- [Peyk API](../service_peyk/README.md)
- [Deployments](../deployments/README.md)
