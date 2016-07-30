FROM nginx
MAINTAINER Cameron Whiting "thetoxicarcade@gmail.com"
ENV DEBIAN_FRONTEND noninteractive
RUN apt-get update -qq
RUN apt-get install -yqq curl nginx supervisor git 1>/dev/null
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash -
RUN apt-get install -qqy nodejs build-essential 1>/dev/null
COPY . /srv
WORKDIR /srv/
RUN mv nginx.sites /etc/nginx/conf.d/default.conf && rm -r Dockerfile
#RUN nginx -t
RUN npm install -g bower gulp-cli
RUN bower install --allow-root && rm bower.json;
RUN npm install && rm package.json
RUN gulp && rm -r node_modules gulpfile.js
#ENV DEBIAN_FRONTEND noninteractive
#RUN apt-get update && apt-get install -y apt-transport-https && apt-get upgrade -y --install-recommends
#RUN sudo apt-get install -y --install-recomends python-pip python-dev
#ADD supervisord.conf /supervisord.conf
#EXPOSE 80:400
#EXPOSE 400
#CMD ["supervisord","-c","/supervisord.conf"]
#ENTRYPOINT []
#lynis audit dockerfile <file>
