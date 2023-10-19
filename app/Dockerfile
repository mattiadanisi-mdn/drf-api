ARG PYTHON_VERSION=3.9.18
FROM python:${PYTHON_VERSION}-alpine

COPY . /app

ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

RUN pip install -r /app/requirements.txt \
    && mkdir -p /app/static \
    && chown -R appuser:appuser app

USER appuser

WORKDIR /app/

EXPOSE 8000

ENTRYPOINT [ "sh", "entrypoint.sh" ]