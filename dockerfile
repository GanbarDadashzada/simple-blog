FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p /app/db_files

EXPOSE 90

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "90"]
