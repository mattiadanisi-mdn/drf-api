ARG NGINX_VERSION=1.25.2
FROM nginx:${NGINX_VERSION}-alpine

COPY ./.certs/bit4idAPI.key /etc/ssl/certs/
COPY ./.certs/bit4idAPI.crt /etc/ssl/certs/
COPY ./nginx.conf /etc/nginx/nginx.conf
COPY ./proxy.conf /etc/nginx/proxy.conf