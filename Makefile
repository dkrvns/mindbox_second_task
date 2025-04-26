DC = docker compose
EXEC = docker exec -it
LOGS = docker logs
ENV = --env-file .env.template
APP_FILE = docker_compose/docker-compose.yaml
APP_CONTAINER = web_app.api
MIGRATE = migration
API = api

.PHONY: app
app:
	${DC} -f ${APP_FILE} ${ENV} --profile ${API} up --build -d

.PHONY: migrate
migrate:
	${DC} -f ${APP_FILE} ${ENV} --profile ${MIGRATE} up --build -d


.PHONY: app-down
app-down:
	${DC} -f ${APP_FILE} ${ENV} --profile ${API} down

.PHONY: app-shell
app-shell:
	${EXEC} ${APP_CONTAINER} bash

.PHONY: app-logs
app-logs:
	${LOGS} ${APP_CONTAINER} -f