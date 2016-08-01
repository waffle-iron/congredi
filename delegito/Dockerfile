FROM python:2.7
MAINTAINER Cameron Whiting "thetoxicarcade@gmail.com"
RUN apt-get update -qq
RUN apt-get install -qqy build-essential libssl-dev libffi-dev python-dev 1>/dev/null
RUN bash -c "pip install flask redis pymongo nose2 PGPy pyjwt celery stem" 1>/dev/null
ADD . /code/delegito
WORKDIR /code
RUN mv delegito/setup.py setup.py
RUN python setup.py build && python setup.py test && python setup.py install
#ENV DEBIAN_FRONTEND noninteractive
#RUN apt-get update && apt-get install -y apt-transport-https && apt-get upgrade -y --install-recommends
#RUN sudo apt-get install -y --install-recomends python-pip python-dev
#ADD supervisord.conf /supervisord.conf
#EXPOSE 80:400
#EXPOSE 400
#CMD ["supervisord","-c","/supervisord.conf"]
#ENTRYPOINT []
#lynis audit dockerfile <file>
