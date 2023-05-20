FROM python:3.9

COPY . /app

RUN pip install --no-cache -r /app/requirements.txt \
  && pip install --no-cache -r /app/requirements-optional.txt \
  && chmod +x /app/entrypoint.sh

WORKDIR /app

ENTRYPOINT ["./entrypoint.sh"]
