* [congredi] - STV server
    * `gh:thetoxicarcade/congredi` -> [delegito.io](//delegito.io) (branded hksp redirect?) -> torsite.onion
    * Flask-Mongo
    * angular app
    * [firefox extension/android app]

# congredi
congredi ([![Build Status](https://travis-ci.org/Thetoxicarcade/congredi.svg?branch=master)](https://travis-ci.org/Thetoxicarcade/congredi))
is a knowledge graph that operates based on AI and cryptographic STV.
You participate by submitting the documents, writing your proposed brains,
and voting on the final results.


congredi runs word-galaxy through an Angular user interface,
sending JSON Web Tokens to our Flask API. The server can access a Celery(Redis)
based Tensorflow/Caffe worker, and a (currently Mongo) database. Both the server,
and the clients, can execute Single Transferable Votes, and the accounts are
managed using OpenPGP and Secure Secret Sharing (possibly pulling over Tor
rendesvous from the komento project & browser implementations of Tor...).

## building
```
git clone github.com/thetoxicarcade/congredi && cd congredi
docker run -ti --rm -u $UID -v `pwd`/static/:/srv/ marmelab/bower bash -c "npm install && bower --allow-root --config.interactive install"
docker run -ti --rm -u $UID -v `pwd`/static/:/srv/ marmelab/bower bash -c "npm install -g gulp && gulp"
docker-compose build && docker-compose up
```

## Implementation

* flask api
    * [x] workable
    * [x] testable *harness is tricky about request.form*
    * [ ] finalized
* angular
    * [x] workable
    * [x] testable `jasmine` inside gulp
    * [ ] finalized
* styling, email (angular-ui, table, zurb foundation)
    * [ ] workable - [foundation scss sompile navbar/forms/pagination/progress/footer]
    * [ ] testable
    * [ ] finalized
* db (linking, queries)
    * [x] workable
    * [ ] testable
    * [ ] finalized
* queues (celery, redis)
    * [x] workable
    * [x] testable
    * [ ] finalized
* artificial intelligence (caffe, tensorflow)
    * [ ] workable
    * [ ] testable
    * [ ] finalized
* crypto (openpgp, SSS, STV hoodiecrow/mailvelope/whiteout-io)
    * [ ] workable
    * [ ] testable
    * [ ] finalized
* peer rendesvous (Tor, webrtc, /forge/sjcl/node-tor)
    * [ ] workable
    * [ ] testable
    * [ ] finalized
* point clouds
    * [ ] workable
    * [ ] testable
    * [ ] finalized
* session (JWT headers, heartbeat, sockets.io)
    * [ ] workable
    * [ ] testable `will be an e2e`
    * [ ] finalized
* angular hacks (routes /#/, modals)
    * [ ] workable
    * [ ] testable
    * [ ] finalized

## Nginx URLS
```
/                               - overview (index.html)
/api/                           - auth point
/(bower_components|static)/     - resource files
/400.html                       - internal
/50x.html                       - internal
```

## Angular URLS
```
/           - as guest/map:canvas
/auth/      - register/login:form
/settings/  - settings:form
/search/    - search:paper
/create/    - create:markdown
/edit/      - create:form
/users/:id  - users:feed
/points/:id - points:canvas
/logic/:id  - logic:sockets.io
/vote/:id   - vote:webrtc
/proxy/:id  - chat:tor
```
## Flask URLS
```
auth:
    /auth/session/  - GET/DELETE    - create JWT
    /auth/db/       - POST/DELETE   - create/delete account
search (GET):
    /api/search/users       - account info, possible to follow
    /api/search/positions   - positional logic, possible to ammend
    /api/search/records     - document contents, possible to reference
storage (GET/POST/PUT/UPDATE/DELETE):
    /api/storage/user/:id       - user information edit section
    /api/storage/position/:id   - position interaction section
    /api/storage/record/:id     - record referencing section

/api/compute/vote/:position     - push/pull election computations
/api/compute/learn/:record      - push/pull (RNN/CNN) computations
/api/compute/secure/:account    - push/pull account computations

```

# DB Links
```
users: %bio,
    users           @self

records: %content
    user            @reverse
    calculations,   -
    records         @self

calculations: %settings
    user            @reverse
    calculations    @self
    records         -

positons:   %summary
    user            @reverse
    positions       @self
    calculations    -

@self
    user, record, calculation, position

@reverse
    user <-> record,calculation,posiion

@linear
    position <-> calculation <-> record

SQL tables:

    Users
    Records
    Calculations
    Positions
    
    LinkCalculationPosition
    LinkRecordCalculation
```

# komento - destributed notes
> A note system for creating and acknowledging conclusions.

Structure-wise this is a local mongodb dataset, storing ideas
and links to ideas. To find new ones, it starts a tor client
and pulls from another's flask server within Tor. To display
them, it uses a 3d viewer (haven't decided on one).



This can be run within a docker image and still have GUI
access. Also check out subuser's github:
[http://subuser.org/](https://github.com/subuser-security/subuser)

```
docker build -t ideas
docker run -ti --rm -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix ideas
```

There's also a google cloud option (I don't know):

* [GC example code](https://github.com/GoogleCloudPlatform/getting-started-python)
* [GC post](https://cloud.google.com/python/getting-started/deploy-mongodb)

```

/*
boot-app: angular, tor, openpgpjs, scjl, weborrent
add-user: mongo, openpgp, mail
send-db
gen-ballot
display-result
*/
var world = {
    users:{
        profile:{
            links:{
                twitter:"@thetoxicarcade",
                github:"@thetoxicarcade",
            },
            location:"",
            bio:"",
            item:{}
        },
        pgppubkey:"pgppubkey",
        accountemail:"a@a.co",
        registered:{
            regid:"sig"
        },
        following:{ //P0
            userid:{
                sig:"sig", //certification
                trust:["issueid"], //whitelist
                distrust:["issueid"] //blacklist
            }
        },
        documents:{ //P1
            docid:{
                sig:"sig", //certification
                trust:["issueid"], //whitelist
                distrust:["issueid"] //blacklist
            }
        },
        calculations:{ //P2
            
        },
        issues:{ // P3
            issueid:{
                sig:"sig", //certification
                poll:"date", //proposed vote day
                open:["issueid","issueid"] //your open preference
            }
        }
    },
    records:{
        author:"",
        calculation:"@calculation @optional",
        content:"",
        signature:"",
        citations:{
            hash:{record:"recordid",user:"userid",sig:"sig"},
            hayy:{record:"recordid",user:"userid",sig:"sig"}
        }
    },
    calculations:{
        alternates:{
            
        },
        author:"",
        records:{
            hash:{record:"recordid",user:"userid",sig:"sig"},
            hayy:{record:"recordid",user:"userid",sig:"sig"}
        },
        settings:{
            inputs:         "records @ world",
            scope:          "positions @ users",
            assumptions:    "records @ user",
            bias:           "positions @ user",
            priority:       "calculations @ user"
        },
        logic:{
            bouncer:        "some calc",
            body:           "some calc",
            checker:        "some calc"
        },
        outputs:{
            models:         "@records",
            certainty:      "fairly",
            positions:      "@positions"
        }
    },
    positions:{
        author:"",
        result:"",
        calculations:{
            hash:{record:"recordid",user:"userid",sig:"sig"},
            hayy:{record:"recordid",user:"userid",sig:"sig"}
        },
        alternates:{
            hash:{record:"recordid",user:"userid",sig:"sig"},
            hayy:{record:"recordid",user:"userid",sig:"sig"}
        },
        voters:["@user"]
    },
    elections:{ // elections with participants, admins, and auditors
        registrar:"id",
        date:"date",
        admins:{
            userid:sig
        },
        participants:{
            userid:sig
        },
        auditors:{
            userid:sig
        },
        topics:{
            ballotitem:sig,
        },
        response:{
            userid:acceptordenysig
        }
    },
    registrar:{ // authenticates users for voting
        address:"addr",
        phone:"tel",
        site:"url",
        pubkey:"key",
        vetprocess:"", // description of their vetting process
        vetfamily:"", // social account, email, address, ID, membership
        admins:{
            userid:sig
        }
    }
};


```
***ORPHANED CODE: gulp, angular, scss merged with congredi***




# GoBo
> Django Experiments

1. Get to where I was with Flask on url regex / data transfers (djangobook tutorial)
2. Put django into a dockerfile (docker-compose with django tutorial)
3. place bootstrap/angular/mongo (MEAN but in python? eeeek!)
4. build a login/register
5. build live chat interface (text based)
