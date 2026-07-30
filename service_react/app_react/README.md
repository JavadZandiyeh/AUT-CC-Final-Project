# React UI — price history and subscriptions

Create React App frontend for the [AUT Cloud Computing Final Project](../../README.md). It provides two forms that call the Peyk API: coin price history and alert subscription.

## Features (implemented)

- **Price History Form** — `POST` `{apiUrl}price/` with `coin_name`; renders returned rows as `coin_name / price / time_stamp`
- **Subscription Form** — `POST` `{apiUrl}subscribe/` with `email`, `coin_name`, and `difference_percentage` (0–100)

API base URL is defined in `src/config.js`:

```js
export const apiUrl = "http://localhost:8001/"
```

Change this value if Peyk is not reachable at that address (for example under Kubernetes LoadBalancer or a different host port).

## Layout

```text
service_react/
├── Dockerfile                 # node:lts-alpine3.18, npm install, entrypoint
└── app_react/
    ├── package.json
    ├── entrypoint.sh          # npm start
    ├── public/
    └── src/
        ├── App.jsx            # UI and Axios calls
        ├── config.js          # apiUrl
        ├── index.js
        └── App.test.js        # Default CRA test (outdated vs current UI)
```

## Dependencies

Main runtime packages from `package.json`: React 18.2, `react-dom`, `react-scripts` 5, Axios 1.4. Testing libraries from CRA are present; `react-cool-form` is listed but not used by `App.jsx`.

## Scripts

From `app_react/`:

```bash
npm install
npm start      # http://localhost:3000
npm test       # CRA Jest runner (current App.test.js expects removed CRA boilerplate text)
npm run build  # production build to build/
```

Do not run `npm run eject` unless you intentionally want an irreversible CRA eject.

## Docker

Compose service `react` builds `react:v1` from `service_react/Dockerfile`, mounts `app_react`, exposes port `3000`, and starts via `entrypoint.sh` → `npm start`.

## Limitations

- API host is hardcoded; no runtime env injection for `apiUrl`
- No CORS setup is provided in Peyk; browser requests from another origin may fail until CORS is configured
- `App.test.js` still asserts “learn react” and does not cover the forms

## Related docs

- [Project README](../../README.md)
- [Peyk API](../../service_peyk/README.md)
- [Deployments](../../deployments/README.md)
