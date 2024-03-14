# pull base image

FROM python:3.10.9

WORKDIR /code

# install dependenci
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY ./ code
