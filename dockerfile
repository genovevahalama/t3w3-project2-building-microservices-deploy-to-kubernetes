#FROM python:3.8-slim

#WORKDIR /app
#COPY ./requirements.txt /app/
#RUN pip install -r requirements.txt
#COPY ./datafetch_load_mongodb.py /app/

#CMD ["python", "datafetch_load_mongodb.py"]

FROM python:3.8-slim

WORKDIR /app
COPY ./requirements.txt /app/
RUN pip install -r requirements.txt
COPY ./app/datafetch_load_mongodb.py /app/

CMD ["python", "./app/datafetch_load_mongodb.py"]