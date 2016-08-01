# Mongo db

This is a quick fix until using valid SQL linker tables.

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