## this is the developement environment for the template
FROM python:3.8-slim-buster AS exo-cartridge-fatman
ENV PYTHONPATH=/app
ARG EXO_ENVIRONMENT=DEVELOPMENT
ENV EXO_ENVIRONMENT=$EXO_ENVIRONMENT
ARG AWS_CREDENTIALS_FILE_CONTENTS=""
ARG AWS_CONFIG_FILE_CONTENTS=""
ENV AWS_CONFIG_FILE_CONTENTS=$AWS_CONFIG_FILE_CONTENTS
ENV AWS_CREDENTIALS_FILE_CONTENTS=$AWS_CREDENTIALS_FILE_CONTENTS
RUN mkdir /app
RUN mkdir /hu-exo-common
COPY --from=hu-exo-common-stage /hu-exo-common /hu-exo-common
COPY ./cartridge/src /app/src
COPY ./development_setup.py /app/development_setup.py
COPY ./requirements/dev_requirements.txt /app/requirements.txt
COPY ./hu-exo-devtools/scripts/entrypoint.sh /app/scripts/development-entrypoint.sh
COPY ./hu-exo-devtools/scripts/functions /app/scripts/functions
COPY ./entrypoints/development.sh /app/scripts/entrypoint.sh
WORKDIR /hu-exo-common
RUN python3 setup.py install
WORKDIR /app
RUN rm -r /hu-exo-common && \
pip3 install -r requirements.txt
ENTRYPOINT ["./scripts/entrypoint.sh"]

## this is the trimmed base layer to be used for producing Cartridges
FROM python:3.8-slim-buster AS exo-cartridge-base-template
RUN mkdir /app
RUN mkdir /hu-exo-common
ENV EXO_FORCE_LOGS_TO_STDOUT=True
ARG EXO_ENVIRONMENT=DEVELOPMENT
ENV EXO_ENVIRONMENT=$EXO_ENVIRONMENT
COPY --from=hu-exo-common-stage /hu-exo-common /hu-exo-common
COPY ./cartridge/src /app/src
COPY ./development_setup.py /app/development_setup.py
COPY ./entrypoints/template.sh /app/entrypoint.sh
WORKDIR /hu-exo-common
RUN python3 setup.py install
WORKDIR /app
RUN rm -r /hu-exo-common 
ENTRYPOINT ["./entrypoint.sh"]