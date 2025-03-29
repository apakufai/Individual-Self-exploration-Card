FROM python:3.10-slim

ENV MODE PROD

COPY ISeC/app /app/
COPY ISeC/requirements.txt /requirements.txt

RUN pip install gunicorn && pip install -r requirements.txt

WORKDIR app

CMD ["gunicorn", "app:application", "-b", "0.0.0.0:8000"]