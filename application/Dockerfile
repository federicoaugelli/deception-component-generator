FROM python:3.9-slim

WORKDIR /

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0", "--port", "9090"]
