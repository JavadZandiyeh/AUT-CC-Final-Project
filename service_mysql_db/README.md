# MySQL init scripts (Docker Compose)

SQL applied when the Compose `mysql_db` service initializes a new data directory (`/docker-entrypoint-initdb.d`).

Part of the [AUT Cloud Computing Final Project](../README.md).

## Contents

- `script/create_tables.sql` — creates `Coin`, `Prices`, and `AlertSubscriptions` in the database created from `MYSQL_DATABASE` (`coin_db`)

Persistent data is stored under `data/` (gitignored). Deleting that directory forces MySQL to re-run init scripts on next start.

Kubernetes uses the equivalent schema via Helm `initializationFiles` in [`../deployments/mysql_db`](../deployments/mysql_db/README.md).

## Related docs

- [Project README](../README.md)
- [Deployments / MySQL chart](../deployments/mysql_db/README.md)
