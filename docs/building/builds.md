# Travis-CI - [file](//github.com/Thetoxicarcade/congredi/blob/master/.travis.yml)

Build process:
1. install nose2, setuptools-lint, mkdocs, requirements.txt
2. docker builds
3. setup.py builds & lints
4. mkdocs builds

# Docker Hub

## congredi-interface
1. install npm env, nginx
2. run npm, bower, & gulp

## congredi-api
1. install extra python-dev
2. install listed requirements
3. setup.py build, test, install lint

# PyPI

1. setup.py build test install
2. setup.py metadata sdist upload

# Firefox Extension