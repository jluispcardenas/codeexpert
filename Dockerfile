# My Site
# Version: 1.0
FROM python:3
# Install Python and Package Libraries
RUN apt-get update && apt-get upgrade -y && apt-get autoremove && apt-get autoclean
RUN apt-get install -y libffi-dev libssl-dev libxml2-dev libxslt-dev libpython3-dev python3-dev libjpeg-dev default-mysql-client default-libmysqlclient-dev libsqlclient-dev libssl-dev libfreetype6-dev zlib1g-dev net-tools libmemcached-dev zlib1g-dev apache2 libapache2-mod-wsgi-py3 && a2enmod rewrite && a2enmod wsgi
COPY apache2.template /etc/apache2/sites-available/codeexpert.conf
RUN a2ensite codeexpert && service apache2 restart

WORKDIR /home/codeexpert

# Project Files and Settings
COPY requirements.txt /home/codeexpert/requirements.txt
RUN pip3 install -r /home/codeexpert/requirements.txt
# Server
EXPOSE 800

CMD ["apache2ctl", "-D", "FOREGROUND"]

