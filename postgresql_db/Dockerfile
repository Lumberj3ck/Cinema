FROM postgres

ENV DATABASE=cinema_project
ENV PASSWORD=h*99IgJdEc8*
ENV USER=lumberjack

EXPOSE 5432

RUN /bin/bash -c "sudo -u postgres psql" 
RUN create database ${DATABASE}; \
    && CREATE USER ${USER} WITH PASSWORD ${PASSWORD};\
    && ALTER ROLE ${USER} SET client_encoding TO 'utf8';\  
    && ALTER ROLE ${USER} SET default_transaction_isolation TO 'read committed'; \
    && ALTER ROLE ${USER} SET timezone TO 'UTC'; \
    && GRANT ALL PRIVILEGES ON DATABASE ${DATABASE} TO ${USER};