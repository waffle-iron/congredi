[![Stories in Ready](https://badge.waffle.io/Thetoxicarcade/congredi.png?label=ready&title=Ready)](https://waffle.io/Thetoxicarcade/congredi)
# Congredi

Congredi is a digital political engine for speciallized STV elections.
This allows you to conduct experiments on forms of voting, issue debates,
coalitions, & practical government improvements.

It is made available in several formats:

* a staticly served Nginx Angular app (& docker image)
* a Firefox extension
* a JSON Web Token authorized Flask API, Celery Queue, & Mongo DB (& docker image)
* a python library for Pip

The crypto involves:

* threshold-signature OpenPGP for jurisdiction appointments
* threshold-encrypted Secure Secret Sharing for jurisdiction admin
* Shuffle-Sum for private vote results
* OpenPGP signatures for public polls
* OpenPGP Key Signing & keyservers for authorizations
* Tor & WebRTC for peer communications


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


> Helping out? Check out the github [issues](//github.com/thetoxicarcade/congredi/issues)