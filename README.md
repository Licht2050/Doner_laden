# Doner_laden
Doner_laden source code

To execute a running doccker for example mysql
find out the name of running docker: #docker ps
then execute: docker exec -it "docker name without cotation" bash
now mysql command: # mysql - u "username" -p

create django project using docker:
  sudo docker-compose run web django-admin startproject DonerLaden .
  
 docker-compose run web python3 manage.py showmigrations
 
 Update an existing Image
 
 sudo docker-compose up --force-recreate --build -d
 sudo docker image prune -f
 
 create user by django admin
 docker-compose run web python3 manage.py createsuperuser
 
 to go mysql
 docker-compose exec web sh
 
 docker exec -it doner_laden_backend_db_1 bash
 
 AFTER PULLING FROM GITHUB CREATE A DOCKER BUILD USING:
 sudo docker-compose up --force-recreate --build -d
 
 LINKS TO OPEN THE PROJECT:
 http://127.0.0.1:8000/benutzerSicht/home
 
 &
 
 https://127.0.0.1:8000/mitarbeiterSicht
 
 LOGIN: acc: root, pass: 12345 -> SHOULD BE LOGGED IN TO ACCESS MITARBEITER SICHT!!!
 
 another user acc: hjouel pass: 12345678H!
