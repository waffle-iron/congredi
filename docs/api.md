# Cheatsheet
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
# Auth
Register, Log in, Delete account
* URL: `/api/auth/`
* Format: **POST**/**DELETE**
* Data:
* Results:

# Token
Heartbeat tokens for faster endpoints
* URL: `/api/token/`
* Format: **GET**/**DELETE**
* Data:
* Results:

# Bearing
Oauth token for longer storage
* URL: `/api/bearing/`
* Format: **GET**/**DELETE**

# Search
Data queries
* URL: `/api/search/:type?offset=0?limit=0`
* Format: **GET**
* Data: {term:"",author:""}
* Results:

# Storage
File operations (requires permissions to the object in question)
* URL: `/api/storage/:type/(new|:id)/`
* Format: **POST**/**GET**/**UPDATE**/**DELETE**
* Data:
* Results: