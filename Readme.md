ipconfig getifaddr en0


chrome://flags/#block-insecure-private-network-requests


Docker Compose File

mysql database


    docker-compose up --build


## Migrations
Before starting the project, make sure your development DB is up to date. 
Run the following command in src folder:

    flask db upgrade

If you make a change that requires a DB schema update, create a migration:

    flask db migrate -m "Short description"

If you create empty revision file, create with this command:

    flask db revision -m "Short description"

If you want to downgrade to a specific revision of a migration:

    flask db downgrade <revision_id>


## Gunicorn starter

    sudo nano /etc/systemd/system/gunicorn.service

copy the gunicorn.service here 

    sudo systemctl start gunicorn.service

    sudo systemctl enable gunicorn.service


    sudo systemctl status gunicorn.service


    sudo systemctl daemon-reload
    sudo systemctl restart gunicorn.service


