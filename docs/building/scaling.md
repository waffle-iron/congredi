# Starting Up


## With Docker-compose
```
docker-compose build
docker-compose up -d && docker-compose scale worker=3
```
The API/Worker subsections run different commands:

```
        command: python /code/worker.py
        command: python /code/api.py
```

## With containers:
```
docker pull ericoflondon/congredi-interface
docker pull ericoflondon/congredi-api
```




# supervisord

A valid supervisord config would daemonize each one:

```
[app]
command=python /code/worker.py
[worker]
command=python /code/api.py

```
Which could be contained in a single dockerfile, but not
scaled like docker-compose (irrelevant, as api cannot
be scaled without a cluster).

# API herds

Theoretically, you'd load balance each individual component:

* nginx files as a CDN
* Flask APIs as a service
* Mongo DB / MySQL DB on services

But I don't know how to do that, so there.