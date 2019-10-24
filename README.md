# Testing Get Indonesia

Result of Get Indonesia testing examp API.
Built on top of python stack using Django.

    
### Setup and installation (Docker):
    
If you are using docker, what you need to do is just build the image.
    
```
$ docker-compose build
$ docker-compose up -d
```
    
Then create the database and do a migrations.
    
```
$ docker-compose exec primary_db createdb --username=postgres postgres_db
$ docker-compose exec api python manage.py migrate
```

Reload API Service

```
$ docker-compose restart api
```
