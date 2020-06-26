FROM python:3.7-slim

WORKDIR /api

COPY . /api

RUN pip install flask
RUN pip3 install flask-rest

EXPOSE 8000

CMD ["python" "api.py"]
