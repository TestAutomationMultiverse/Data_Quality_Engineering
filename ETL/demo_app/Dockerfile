FROM python:slim

WORKDIR /app
RUN apt-get update \
    && apt-get -y install libpq-dev gcc
    
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]
