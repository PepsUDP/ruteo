FROM postgis/postgis:latest

RUN apt-get update && apt-get install -y \
    postgresql-16-pgrouting \
    python3 \
    python3-pip \
    procps \
    postgis

RUN apt-get clean \
    && rm -rf /var/lib/apt/lists/*

COPY . .

RUN pip3 install -r requirements.txt
