# Building
```
git clone github.com/thetoxicarcade/congredi && cd congredi
docker run -ti --rm -u $UID -v `pwd`/static/:/srv/ marmelab/bower bash -c "npm install && bower --allow-root --config.interactive install"
docker run -ti --rm -u $UID -v `pwd`/static/:/srv/ marmelab/bower bash -c "npm install -g gulp && gulp"
docker-compose build && docker-compose up
docker build -t ideas
docker run -ti --rm -e DISPLAY=$DISPLAY \
  -v /tmp/.X11-unix:/tmp/.X11-unix ideas
```