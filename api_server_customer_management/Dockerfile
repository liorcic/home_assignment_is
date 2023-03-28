FROM python:3.9-slim-buster

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY src/ .

EXPOSE 8000

CMD ["python", "main.py"]