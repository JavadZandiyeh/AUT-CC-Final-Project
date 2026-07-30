# MySQL Helm chart (project usage)

This directory packages MySQL for the [AUT Cloud Computing Final Project](../../README.md) Kubernetes deployment. It is based on a classic single-instance MySQL Helm chart layout (Deployment, Service, PVC, Secrets, optional metrics/ServiceMonitor, init SQL ConfigMap).

For the full system overview and Compose-based MySQL setup, see the [project README](../../README.md) and [deployments README](../README.md).

## Role in this project

- Image: `mysql:8.0` (see `values.yaml`)
- Database: `coin_db`
- Credentials in values (change for any shared cluster): root password `pass`, user `admin` / password `pass`
- Schema created via `initializationFiles.create_tables.sql`:
  - `Coin`
  - `Prices`
  - `AlertSubscriptions`

The same logical schema is applied under Docker Compose from `../../service_mysql_db/script/create_tables.sql`.

## Install (as used by this repo)

From `deployments/`:

```bash
helm install mysql-db mysql_db/ --values mysql_db/values.yaml
```

Or use `../install.sh`, which installs this chart first.

Uninstall:

```bash
helm delete mysql-db
```

## Configuration relevant to this project

| Value | Project setting | Notes |
| --- | --- | --- |
| `image` / `imageTag` | `mysql` / `8.0` | Matches Compose |
| `mysqlRootPassword` | `pass` | Also used by Bepa/Peyk as root |
| `mysqlUser` / `mysqlPassword` | `admin` / `pass` | Created by the chart; app code uses `root` |
| `mysqlDatabase` | `coin_db` | Application database |
| `initializationFiles` | `create_tables.sql` | Creates DB objects above |
| `persistence.enabled` | `true` (chart default) | PVC for data |
| `metrics.enabled` | `false` (default) | Optional mysqld exporter |

Other chart knobs (probes, SSL, affinity, ServiceMonitor, extra volumes, etc.) remain available in `values.yaml` but are not required for the course demo path.

## Prerequisites

- Kubernetes with a working volume provisioner if persistence is enabled
- Helm 3

## Relationship to upstream chart docs

Older generic “stable/mysql” archive notices and long parameter tables from the upstream chart are omitted here on purpose. This README documents **how this repository uses the chart**. For exhaustive template behavior, inspect `templates/` and `values.yaml` in this folder.

## Related docs

- [Deployments](../README.md)
- [Project README](../../README.md)
