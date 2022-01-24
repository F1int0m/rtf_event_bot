FROM python:3.9

WORKDIR /opt

COPY requirements.txt requirements.txt

RUN pip3 install --requirement /opt/requirements.txt;

COPY . .

ENTRYPOINT python3 /opt/main.py