# syntax=docker/dockerfile:1.2
FROM python:3
RUN mkdir -p /app
WORKDIR /app
COPY requirements.txt /app
RUN --mount=type=cache,target=/root/.cache python -m pip install -r requirements.txt
COPY start.sh /app/
COPY owen_api /app/owen_api
COPY model_artifacts /app/model_artifacts
CMD [ "sh", "start.sh" ]
