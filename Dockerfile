
FROM ubuntu:18же.04
ENV DEBIAN_FRONTEND noninteractive
USER root

RUN apt-get update && apt-get install gnupg -y

# It should be the same key as https://www.postgresql.org/media/keys/ACCC4CF8.asc
RUN apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 --recv-keys B97B0AFCAA1A47F044F244A07FCC7D46ACCC4CF8

# Add PostgreSQL's repository. It contains the most recent stable release
#     of PostgreSQL, ``9.3``.
RUN echo "deb http://apt.postgresql.org/pub/repos/apt/ precise-pgdg main" > /etc/apt/sources.list.d/pgdg.list


RUN apt-get install curl  git postgresql-11 postgresql-contrib python3 pip3 -y


USER postgres
ENV PGVERSION 11
RUN /etc/init.d/postgresql start &&\
    psql --command "CREATE USER courseuser WITH SUPERUSER PASSWORD 'database2020';" &&\
    createdb -O courseuser mycourse &&\
    /etc/init.d/postgresql stop

USER postgres
RUN echo "local all all md5" > /etc/postgresql/$PGVERSION/main/pg_hba.conf &&\
    echo "host all all 0.0.0.0/0 md5" >> /etc/postgresql/$PGVERSION/main/pg_hba.conf
RUN cat database/postgresql.conf >> /etc/postgresql/$PGVERSION/main/postgresql.conf
VOLUME  ["/etc/postgresql", "/var/log/postgresql", "/var/lib/postgresql"]
EXPOSE 5432
USER root

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD ./src /code/

CMD service postgresql start && python3 ./manage.py runserver
EXPOSE 8000