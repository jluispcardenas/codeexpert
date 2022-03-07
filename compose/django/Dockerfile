# Version: 1.0
FROM python:3
ENV PYTHONUNBUFFERED 1

ENV APP_PROJ=/home/codeexpert/

RUN useradd codeexpert

# Install Python and Package Libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean

COPY ./requirements /requirements

# Project Files and Settings
RUN pip3 install --no-cache-dir -r /requirements/base.txt

COPY ./compose/django/start.sh /start.sh
RUN sed -i 's/\r//' /start.sh
RUN chmod +x /start.sh && chown codeexpert /start.sh

COPY . $APP_PROJ

RUN chown -R codeexpert $APP_PROJ

WORKDIR $APP_PROJ

USER codeexpert
