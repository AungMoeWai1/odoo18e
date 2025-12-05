Odoo 18 Dockerized Deployment
=============================

This project contains a Dockerized Odoo 18 setup with PostgreSQL and pgAdmin, configured for easy development, deployment, and CI/CD.

Project Structure
-----------------

.. code-block:: bash

    odoo18-docker/
    ├── custom_addons/          # Create manually for   custom Odoo modules
    ├── Dockerfile              # Odoo image with       dependencies
    ├── entrypoint.sh           # Startup script for Odoo
    ├── odoo.conf               # Odoo configuration file
    ├── docker-compose.yml      # Docker services definition
    ├── myenvfile.env           # Environment variables
    ├── VERSION.txt             # Image version tag
    ├── Makefile                # Build/push utilities
    ├── .github/
        │   └── workflows/
        │       └── docker-publish.yml  # CI/CD to Docker Hub
    └── README.rst

Usage
-----

1. **Clone the repo**

.. code-block:: bash

    git clone https://github.com/YOUR_USER/odoo18-docker.git
    cd odoo18-docker

2. **Manually create** the `custom_addons/` folder:

.. code-block:: bash

    mkdir custom_addons

3. **Configure environment**

Create `myenvfile.env`:

.. code-block::

    POSTGRES_DB=postgres
    POSTGRES_USER=odoo
    POSTGRES_PASSWORD=odoo
    PGADMIN_DEFAULT_EMAIL=admin@example.com
    PGADMIN_DEFAULT_PASSWORD=admin

4. **Start containers**

.. code-block:: bash

    docker-compose up -d

5. **Access**

- Odoo: http://localhost:8069  
- pgAdmin: http://localhost:5050 (login with credentials from `.env`)

Docker Hub Automation (CI/CD)
-----------------------------

This repo includes a GitHub Actions workflow that automatically builds and pushes to Docker Hub when changes are made to `Dockerfile` or `docker-compose.yml`.

### GitHub Secrets Required

In your GitHub repository, add the following secrets:

- `DOCKERHUB_USERNAME`: your Docker Hub username
- `DOCKERHUB_TOKEN`: a [Docker Hub Access Token](https://hub.docker.com/settings/security)

To generate a Docker Hub access token:

1. Log in to Docker Hub
2. Navigate to **Account Settings > Security**
3. Click **New Access Token**
4. Name it (e.g., `github-ci`) and copy the token
5. Add it as `DOCKERHUB_TOKEN` in your GitHub repo secrets

Manual Version Bump
-------------------

Edit `VERSION.txt` with your desired tag (e.g., `1.0.1`).  
Use the provided Makefile commands:

.. code-block:: bash

    make build        # Builds Docker image
    make push         # Pushes to Docker Hub with version

License
-------

MIT License
