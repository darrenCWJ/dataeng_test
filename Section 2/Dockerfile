#pull postgres image from docker
FROM postgres:14.3

#create user, password 
ENV POSTGRES_USER docker
ENV POSTGRES_PASSWORD docker 

#create db tables
COPY create_table.sql /docker-entrypoint-initdb.d/