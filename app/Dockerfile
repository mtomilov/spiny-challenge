FROM python:3.7-slim
RUN apt update && apt install cron -y
RUN pip install --upgrade pip \
    && pip install poetry \
    && poetry config virtualenvs.create false
RUN mkdir /app
WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root
COPY . .
ENTRYPOINT ["bash", "./entrypoint.sh"]
