helm install mysql-db mysql_db/ --values mysql_db/values.yaml
helm install coin-news service_coin_news/ --values service_coin_news/values.yaml
helm install bepa service_bepa/ --values service_bepa/values.yaml
helm install peyk service_peyk/ --values service_peyk/values.yaml
helm install react service_react/ --values service_react/values.yaml
