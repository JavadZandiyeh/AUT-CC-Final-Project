# Deployments (Helm)

Kubernetes packaging for the [AUT Cloud Computing Final Project](../README.md). Each major service has an application Helm chart; helper scripts install or delete all releases.

## Charts

| Directory | Release name (`install.sh`) | Role |
| --- | --- | --- |
| `mysql_db/` | `mysql-db` | MySQL 8.0 chart (adapted stable/mysql-style chart) with project init SQL |
| `service_coin_news/` | `coin-news` | CoinNews image + ConfigMap `config.yml` |
| `service_bepa/` | `bepa` | Bepa worker Deployment, ConfigMap, Secret |
| `service_peyk/` | `peyk` | Peyk API Deployment, ConfigMap, Secret |
| `service_react/` | `react` | React UI Deployment |

Chart `values.yaml` files set image repositories/tags, service types/ports, env-like config, and (for Bepa/Peyk/React) `hostPath` volume mounts. Review and adjust those paths, passwords, and service types for your cluster before install.

## Prerequisites

- Kubernetes cluster with Helm 3
- Images available to the cluster:
  - `mysql:8.0` (chart default)
  - `amirhossein21/coinnews.macos:v0.2`
  - `bepa:v1`, `peyk:v1`, `react:v1` (build from service Dockerfiles and load/push as needed)

## Install / uninstall

```bash
cd deployments
./install.sh
```

`install.sh` runs:

```bash
helm install mysql-db mysql_db/ --values mysql_db/values.yaml
helm install coin-news service_coin_news/ --values service_coin_news/values.yaml
helm install bepa service_bepa/ --values service_bepa/values.yaml
helm install peyk service_peyk/ --values service_peyk/values.yaml
helm install react service_react/ --values service_react/values.yaml
```

Remove releases:

```bash
./delete.sh
```

## Notable values

- **MySQL**: root password, `admin` user, database `coin_db`, and `initializationFiles.create_tables.sql` for schema (see [mysql_db/README.md](mysql_db/README.md)).
- **CoinNews**: richer sample unit list and worker settings than the Compose `service_coin_news/config.yml`.
- **Bepa**: `INTERVAL_SECONDS`, `COINNEWS_ENDPOINT` pointing at the in-cluster CoinNews service name, MySQL settings.
- **Peyk / React**: `LoadBalancer` services on ports `8001` and `3000` by default; React still needs a matching Peyk URL in `config.js` unless you change the frontend.

Autoscaling templates exist but `autoscaling.enabled` defaults to `false`. Ingress is mostly disabled except CoinNews chart defaults (`ingress.enabled: true` with example host).

## Related docs

- [Project README](../README.md)
- [MySQL chart notes](mysql_db/README.md)
- [Bepa](../service_bepa/README.md)
- [Peyk](../service_peyk/README.md)
- [React UI](../service_react/app_react/README.md)
