FROM python:3.7

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . /schedule_test
WORKDIR /app-dockers/schedule_test
CMD ["python", "schedule_test"]
