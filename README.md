"# lipsync-website" 




This Project is deprecated on

docker run -p 49153:8765 -d lowerquality/gentle


important

https://github.com/khabdrick/django-job-queue-article/tree/main/project

https://www.honeybadger.io/blog/job-queues-workers-django/

docker run -d -p 6379:6379 --name myredis redis

formating the code use
isort .

python -m black .

flake8 --ignore=E501,F401 .




setup docker

docker-compose build 

docker-compose up

docker-compose exec web python manage.py migrate 

docker-compose down -v {for removeing the volumes}

docker-compose exec db psql --username=hello_django --dbname=hello_django_dev

$ docker-compose exec web python manage.py flush --no-input

$ docker-compose exec web python manage.py migrate

docker-compose -f docker-compose.prod.yml down -v

$ docker-compose -f docker-compose.prod.yml up -d --build

$ docker-compose -f docker-compose.prod.yml exec web python manage.py migrate --noinput

 docker-compose -f docker-compose.prod.yml logs -f