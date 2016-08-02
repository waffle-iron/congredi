```
Tor (controllable by Workers)
    -> nginx (forward to compose addresses)
        -> API (JWT/DB actions separate)
            -> Mongo (For initial auth query)
            -> Celery (Redis queue for Crypto, Emails, DB)
                -> Worker (send updates to API sessions)
                    -> Mongo (sync between items)
```