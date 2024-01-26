# Use an official Python runtime as a parent image
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install requests
RUN pip install -r requirements.txt
COPY . /app
CMD ["python", "mongodb_loader/datafetch_load_mongodb.py"]
