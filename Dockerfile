FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /usr/src/app
COPY requirements.text ./


RUN pip uninstall django
RUN pip install -r requirements.text

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

