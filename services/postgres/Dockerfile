FROM postgis/postgis
# Install system packages for building PostgreSQL extensions
RUN apt-get update && apt-get install -y \
    git \
    build-essential \
    postgresql-server-dev-all \
    postgresql-12-rum \
    less \
    make \
    vim

RUN git clone https://github.com/postgrespro/rum /tmp/rum



WORKDIR /tmp/rum
RUN make USE_PGXS=1
RUN make USE_PGXS=1 install
# Install RUM extension for PostgreSQL

WORKDIR /tmp/db

RUN mkdir /data && chown postgres /data

# copy over the pagila database;
# we rename the files so that they get executed in the correct order
COPY schema.sql /docker-entrypoint-initdb.d/01.sql
