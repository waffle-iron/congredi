# Congredi

Congredi is an STV service, built into a PyPI package, Docker Image, & Mozilla extension.

It involves providing a secure interface for experiments on forms of government.

The library caters to providing a threshold-signature, single-transferable-vote system.
The interface & accompanying infrastructure are for anonymity & censorship-proofing.

Around the web:

* Travis [![Build Status](https://travis-ci.org/Thetoxicarcade/congredi.svg?branch=master)](https://travis-ci.org/Thetoxicarcade/congredi) - Automated commit tests.
* RTFD [![Documentation Status](https://readthedocs.org/projects/congredi/badge/?version=latest)](http://congredi.readthedocs.io/en/latest/?badge=latest) - Spec & explainations.
* PyPI [![PyPI version](https://badge.fury.io/py/delegito.svg)](https://badge.fury.io/py/delegito) - The base library (& api).
* Mozilla Extension [not yet]() - signed js is safer for crypto.
* dockerhub
    * `congredi-interface` [![Docker Pulls](https://img.shields.io/docker/pulls/ericoflondon/congredi-interface.svg?maxAge=2592000)](https://hub.docker.com/r/ericoflondon/congredi-interface/) the interface containers.
    * `congredi-api` [![Docker Pulls](https://img.shields.io/docker/pulls/ericoflondon/congredi-api.svg?maxAge=2592000)](https://hub.docker.com/r/ericoflondon/congredi-api/) the api containers.
* [Website](//delegito.io) - ***Not currently/usually running***
* [Onion](//aldskfj.onion) - ***Not currently/usually running***


## Starting Up

With compose:
```
docker-compose build
docker-compose up -d && docker-compose scale worker=3
```

With containers:
```
docker pull ericoflondon/congredi-interface
docker pull ericoflondon/congredi-api
```

For the library: `pip install delegito`


## Helping out

* document scaling api clusters?
* css styling within interface?
* the [todo](docs/todo) section
