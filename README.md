# Exchange test API
For run following this steps:

* Clone project
```shell script
git clone https://github.com/kouhkan/exchange-test.git
```

* Go to project directory:
```shell script
cd exchange-test
``` 
* Change .env.sample to .env


* Execute compose:
```shell script
docker-compose up
``` 

* Now, You must **kill** compose and follow this steps:
```shell script
docker-compose run --rm python bash
```
* After that, migrate db:
```shell script
python manage.py migrate
```
Note: if you got DB error, you must run postgres container in another teminal.

* And collectstatic:
```shell script
 python manage.py collectstatic
```

* Load DB:
```shell script
 python manage.py loaddata db.json
```

* And exit:

```shell script
exit
```

* Now, run compose again:
```shell script
 docker-compose up 
```
Note: if you got error, It's may because of drf-yasg! for that you must install it manually.
```shell script
docker-compose run --rm python bash 
pip install drf-yasg
```

username: amir

password: amir

```djangourlpath
Admin panel: /admin
```

```djangourlpath
Swagger Doc: /swagger/ui/ 
```
