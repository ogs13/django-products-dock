
## Django admin panel

   `http://127.0.0.1:8000/admin/`

### Categories page
-   `http://127.0.0.1:8000/categories/`

### commands
- `docker-compose exec django python3 manage.py generate_products 100 100`

- `docker-compose exec django python3 manage.py set_product_values`


## Installation process

### Install the system dependencies
-   **Docker**
-   **Docker-compose**

## Get the code

Clone the repository `https://github.com/ogs13/drf-todoapp.git`

## Run the command to run app

`docker-compose up -d`

#### to create first user (admin):
`docker-compose exec django python3 manage.py createsuperuser`
