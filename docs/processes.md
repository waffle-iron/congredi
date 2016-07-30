# Processes

Within docker-compose.yml each process is separate, but a valid single Dockerfile
could use supervisord to run individual daemons in the same container.


The API/Worker subsections are run using the command operation in `docker-compose`:

```
        command: python /code/worker.py
        command: python /code/api.py
```