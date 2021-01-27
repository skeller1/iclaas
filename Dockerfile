FROM odoo:14.0

USER root

RUN apt-get update && \
  apt-get install -y --no-install-recommends \
    build-essential \
    python3-dev \
    python3-wheel \
    python3-cffi \
    libcairo2 \
    libpango-1.0-0 \
    libpangocairo-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info \
    && rm -rf /var/lib/apt/lists/*

Run pip3 install WeasyPrint==52.2

USER ODOO
