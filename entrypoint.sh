#!/bin/bash

# Default values if not provided
: "${DB_HOST:=odoo18db}"
: "${PORT:=5432}"
: "${USER:=odoo18}"
: "${PASSWORD:=odoo18}"
: "${DB_NAME:=odoo18_db}"

exec python3 /opt/odoo/odoo-bin \
    -c /etc/odoo.conf \
    --db_host="$DB_HOST" \
    --db_port="$PORT" \
    --db_user="$USER" \
    --db_password="$PASSWORD" \
    -d "$DB_NAME" \
    # -u all \
    # --stop-after-init \
    --log-level=debug
    -i base
