
FROM alpine:latest

RUN apk update
RUN apk add --no-cache python3 py3-pip
RUN apk add --no-cache build-base libpq libpq-dev
WORKDIR /app

COPY requirements.txt .
COPY *.py ./ 
COPY generated ./generated   


RUN python3 -m venv venv
RUN source venv/bin/activate && pip3 install -r requirements.txt



ENV CSSI_DATABASE_USERNAME=cssi_web_user
ENV CSSI_DATABASE_PASSWORD=cssiwebuser2024portal

CMD ["venv/bin/python3", "app.py"]

