FROM nginx
MAINTAINER Cameron Whiting "thetoxicarcade@gmail.com"
ENV DEBIAN_FRONTEND noninteractive
#RUN apt-get update && apt-get install -y apt-transport-https && apt-get upgrade -y --install-recommends
RUN apt-get update -qq && \
    apt-get install -yqq curl nginx supervisor git 1>/dev/null && \
    curl -sL https://deb.nodesource.com/setup_4.x | bash - 1>/dev/null && \
    apt-get install -qqy nodejs build-essential 1>/dev/null
COPY . /srv
WORKDIR /srv/
RUN mv nginx.sites /etc/nginx/conf.d/default.conf && \
    rm -r Dockerfile && \
    nginx -t || echo "nginx-compose bug..."
RUN npm install -g bower gulp-cli 1>/dev/null && \
    npm install 1>/dev/null && \
    rm package.json
RUN bower install --allow-root 1>/dev/null && \
    rm bower.json && \
    gulp 1>/dev/null && \
    rm -r node_modules gulpfile.js
#ADD supervisord.conf /supervisord.conf
#EXPOSE 80:400
#EXPOSE 400
#CMD ["supervisord","-c","/supervisord.conf"]
#ENTRYPOINT []
#lynis audit dockerfile <file>
