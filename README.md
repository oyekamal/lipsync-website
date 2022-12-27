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
deployment

apt install libgl1-mesa-glx

sudo apt update

sudo apt-get install python3.10 python3.10-dev python3.10-distutils python3.10-venv

apt install libgl1-mesa-glx

sudo apt-get install gcc

sudo apt install nginx

gunicorn --workers 3 --bind 0.0.0.0:8000 core.wsgi:application

nano /etc/nginx/sites-available/lipsync

sudo ln -s /etc/nginx/sites-available/lipsync /etc/nginx/sites-enabled


gunicorn --workers 3 --bind unix:/home/ubuntu/lipsync-website/app/core.sock core.wsgi:application

gunicorn --workers 3 --bind unix:gunicorn.sock core.wsgi:application

gunicorn --workers 3 --bind unix:/run/gunicorn.sock core.wsgi:application

sudo systemctl reload nginx

sudo systemctl restart nginx

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


digital Ocean
sudo nano /etc/systemd/system/gunicorn.socket