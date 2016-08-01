# WebLinks

> A Terrible, Digital Govermnent - [delegito.io](//delegito.io)

[![Build Status](//travis-ci.org/Thetoxicarcade/congredi.svg?branch=master)](https://travis-ci.org/Thetoxicarcade/congredi)
[![Documentation Status](//readthedocs.org/projects/congredi/badge/?version=latest)](http://congredi.readthedocs.io/en/latest/?badge=latest)
[GitHub](//github.com/thetoxicarcade/congredi)

# About

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

# Doc Specializations

## Users / Sysadmins? [User Guide](UserGuide)
Guides involved in getting up and running with Congredi instances.

## Developers / Contributors? [API](APIs) & [Build](building) docs
Guides for getting under the hood with the overlying architecture.

## Cryptographers / Skeptics? [Methodology](methodology)
Guides for working with the underlying libraries, objects, & functions.