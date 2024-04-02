# API

swagger: `http://localhost:8080/docs`

### Endpoints:

- `/api/v1/applications/`
- `/api/v1/applications/{id}`
- `/healthz`
- `/metrics`

### Systemd:

- service: `crcapi.service`
- fake traffic serivce: `locust.service`
- fake traffic timer: `locust.timer`
- high load fake traffic service: `locust-stress.service`
- high load fake traffic service: `locust-stress.timer`

# Postgresql

### Settings:

- user/password: `postgres`
- host: `localhost`
- port: `5432`
- database name: `applications`
- custom postgresql.conf: `max_connections = 10`
