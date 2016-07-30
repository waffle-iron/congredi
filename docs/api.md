# API endpoints
```
/api/
    /auth/          [POST|DELETE] - db
    /token/         [GET|DELETE] - JWT
    /bearing/       [GET|DELETE] - JWT (longer time)
    /search/:type
        ?offset=0?limit=0 {term:"",author:""} - search
    /storage/:type
        /(new|:id)/ [POST|GET|UPDATE|DELETE]
```