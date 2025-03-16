FROM python:3.12-slim

WORKDIR /app

COPY ./requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY entrypoint.sh /app/
RUN chmod +x ./entrypoint.sh

COPY . /app/

ENV PYTHONPATH=/app
ENV FLASK_APP=wsgi:create_app
ENV FLASK_ENV=development

EXPOSE 5000

ENTRYPOINT ["./entrypoint.sh"]