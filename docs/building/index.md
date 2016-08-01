# Customizing via git & docker-compose
1. Clone repo:
    `git clone github.com/thetoxicarcade/congredi && cd congredi`

2. pre-fetch npm & bower packages:
    ```docker run -ti --rm -u $UID -v `pwd`/interface/:/srv/ marmelab/bower bash -c "npm install && bower --allow-root --config.interactive install"```

3. Pre-build gulp tasks:
    ```docker run -ti --rm -u $UID -v `pwd`/interface/:/srv/ marmelab/bower bash -c "npm install -g gulp && gulp"```

4. Build, start, & scale:
    `docker-compose build && docker-compose up -d && docker-compose scale workers=2`

> docker run -ti --rm -e DISPLAY=$DISPLAY \
>  -v /tmp/.X11-unix:/tmp/.X11-unix ideas

# Optimizing Python Library

cython compiler. . .

# Edits to Angular UI js

1. run `gulp clean`
2. make edits to `/js/`
    * if you change a library call, change its `.test.js`
    * if you change a controller or otherwise, change its `view`
3. run `gulp` (should run tests as well)

# Edits to Scaling

docker-swarm scaling. . .