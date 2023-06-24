FROM node:lts-alpine3.18

WORKDIR /app/app_react

COPY /app_react/package*.json /app/app_react

RUN npm install

ENTRYPOINT ["/bin/sh", "entrypoint.sh"]
