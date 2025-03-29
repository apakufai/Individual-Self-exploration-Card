FROM python:3.10-slim

COPY ISeC/requirements.txt /requirements.txt
RUN pip install gunicorn && pip install -r requirements.txt

COPY ISeC/app /app/
WORKDIR app

CMD ["gunicorn", "app:application", "-b", "0.0.0.0:8000"]