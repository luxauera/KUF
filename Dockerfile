FROM python:3.11-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt -q

EXPOSE 5000

CMD ["python", "app.py"]