# CoinNews configuration

This folder does **not** contain CoinNews application source. The stack runs the external image `amirhossein21/coinnews.macos:v0.2` and mounts configuration from here (Compose) or from the Helm chart ConfigMap (Kubernetes).

Part of the [AUT Cloud Computing Final Project](../README.md).

## Compose

`docker-compose.yml` binds `config.yml` into the container at `/go/src/app/config.yml` and publishes port `8000`.

Current Compose `config.yml` highlights:

- `http_port: 8000`
- `worker_enable: true`, `worker_interval: 5`
- Sample units: `bitcoin`, `docoin`

## Kubernetes

See `../deployments/service_coin_news/` — values embed a larger unit list and additional fields such as `change_probability` / `change_factor`.

## Consumer API (as used by Bepa)

Bepa calls:

- `GET /api/data/` — list of coin names  
- `GET /api/data/{coin_name}/` — object including numeric `value`

Exact CoinNews behavior beyond these calls depends on the image, not on code in this repository.

## Related docs

- [Project README](../README.md)
- [Bepa](../service_bepa/README.md)
- [Deployments](../deployments/README.md)
