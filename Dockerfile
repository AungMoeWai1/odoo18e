FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential gcc git xvfb wget ca-certificates && \
    wget https://github.com/wkhtmltopdf/packaging/releases/download/0.12.6.1-2/wkhtmltox_0.12.6.1-2.jammy_amd64.deb && \
    dpkg -i wkhtmltox_0.12.6.1-2.jammy_amd64.deb || apt-get -f install -y && \
    apt-get install -y libpq-dev libxml2-dev libxslt1-dev zlib1g-dev \
        libsasl2-dev libldap2-dev libjpeg-dev libssl-dev libffi-dev && \
    rm wkhtmltox_0.12.6.1-2.jammy_amd64.deb && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /opt/odoo

# Copy Odoo Enterprise source
COPY ./odoo /opt/odoo

# Copy configuration and entrypoint
# COPY ./odoo.conf /etc/odoo.conf
COPY ./requirements.txt /opt/requirements.txt

# Install Python dependencies
RUN pip install --upgrade setuptools
RUN pip install --upgrade pip
RUN pip install -r /opt/requirements.txt
RUN pip install pydantic
RUN pip install pandas
RUN pip install firebase-admin
# Expose Odoo ports
EXPOSE 8069 8071

# Start Odoo
ENTRYPOINT ["/entrypoint.sh"]

