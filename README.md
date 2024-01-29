# Hogwarts Docker Compose Setup

This repository provides a Docker Compose setup for running MySQL and MongoDB containers for a Hogwarts project.



how and what to do:


Commands for docker compose

```
docker-compose build
docker-compose up
docker-compose down
```
Steps to check mysql container

```
docker ps
docker exec -it mysql-container bash
mysql -u admin -padmin
USE hogwarts;
show tables;
SELECT * FROM Characters;
SELECT * FROM Spells;
```
Steps to check mongodb container

```
docker ps
docker exec -it mongodb-container mongosh
show dbs
use hogwarts 
db.Spells.find()
db.Characters.find()
db.Spells.countDocuments()      #77 docs expected
db.Characters.countDocuments()  #25 docs expected
```