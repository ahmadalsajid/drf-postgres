FROM python:3.12-alpine3.20
ENV PYTHONUNBUFFERED=1

WORKDIR /app
RUN apk update && \
    apk add curl && \
    rm -rf /var/cache/apk/*

COPY requirements.txt /app
RUN python -m pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /app
EXPOSE 8000
#HEALTHCHECK  --start-period=30s \
#  CMD curl http://localhost:8000/healthcheck/ || exit 1

ENTRYPOINT ["sh", "create-superuser.sh"]

# worker should be according to the CFN config
# --workers=WORKERS, The number of worker processes. This number should generally be between 2-4 workers per core in the server.
# Gunicorn relies on the operating system to provide all of the load balancing when handling requests. Generally they recommend (2 x $num_cores) + 1 as the number of workers to start off with.
CMD ["gunicorn", "--workers=3", "--timeout=120", "--bind 0.0.0.0:8000", "university.wsgi"]