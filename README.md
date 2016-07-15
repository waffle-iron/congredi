# Congredi - A Terrible, Digital Govermnent [delegito.io](//delegito.io)
[![Build Status](https://travis-ci.org/Thetoxicarcade/congredi.svg?branch=master)](https://travis-ci.org/Thetoxicarcade/congredi)

Congredi is a digital politics experiment, using cryptographic STV and
social profiles to debate issues, form coalitions, and run "governments".

It's an Nginx served Angular UI Pointcloud, & JWT Flask API to mongo DB.

Crypto involves OpenPGP, Secure Secret Sharing, Shuffle-Sum, Tor, & WebRTC.

## fixes / tests / functionality
* [ ] request.form in test harness
* [ ] jasmine inside gulp
* [ ] foundation emails
* [ ] db structure (linking, queries, objects)
* [ ] openpgp plugin
* [ ] webtorrent streaming
* [ ] mail server
* [ ] secure secret sharing plugin (webrtc-openpgp)
* [ ] Tor-webrtc rendesvous (forge/sjcl/node-tor)
* [ ] UI (hoodiecrow/mailvelope/whiteout-io/mailpile)
* [ ] JWT-heartbeat e2e
* [ ] angular /#/ hacks, modals
* [ ] point clouds
* [ ] STV shuffle-sum

```
/auth/session/ [GET|DELETE] - JWT
/auth/db/ [POST|DELETE] - account
/api/search/?offset=0?limit=0 {term:"",author:""} - search
/api/storage/(user|district|election)/(new|<id>)/ [POST|GET|UPDATE|DELETE]

/#/(auth|settings|create)/
/#/user/(follow|<issues>)/
/#/<district>/(admin|join|<election>/(register|vote|audit))/
```


```
git clone github.com/thetoxicarcade/congredi && cd congredi
docker run -ti --rm -u $UID -v `pwd`/static/:/srv/ marmelab/bower bash -c "npm install && bower --allow-root --config.interactive install"
docker run -ti --rm -u $UID -v `pwd`/static/:/srv/ marmelab/bower bash -c "npm install -g gulp && gulp"
docker-compose build && docker-compose up
docker build -t ideas
docker run -ti --rm -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix ideas
```


```
var user = {
    profile:{
        links:{twitter:""},
        location:"",
        bio:"",
        other:{},
        },
    publicKey:"",
    email:"",
    organiations:{regid:"sig"},
    following:{
        user:{
            sig:"sig", //certification
            trust:["issueid"], //whitelist
            distrust:["issueid"] //blacklist
            }
        },
    opinions:{
        opinion:{
            sig:"sig", //certification
            trust:["issueid"], //whitelist
            distrust:["issueid"], //blacklist
            poll:"date", //proposed vote day
            open:["issueid","issueid"] //your open preference, your actual vote is private
            }
        }
    };
var opinion = { // can be sub-items as well
    author:"", // org/user
    sig:"sig",
    trust:["trust"], // whitelist
    distrust:["distrust"], // blacklist
    opinionCascade:["opinionid","opinionid"], // components of proposed ballot choice
    content:"",
    citations:{
        hash:{record:"recordid",user:"userid",sig:"sig",relation:"disent"},
        hayy:{record:"recordid",user:"userid",sig:"sig",relation:""}
        }
    };
var organization = { // parliment, district, party, registrar, auditor, etc
    bio:{ address:"addr", phone:"tel", site:"url"},
    pubkey:"key",
    vetting:{process:"",type:""},
    staff:{ id:sig },
    issues:{ id:sig }, //opinions
    voters:{
        pub:{ id:sig },
        priv:{ token:taken }
        }
    };
var election = {
    district:"", // managing org
    date:"",
    ballot:{ item:sig },
    status:{ user:"ready-fail-success" },
    poll:{ user:position },
    result:["stv-item"]
    };
```