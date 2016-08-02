FROM python:2.7
MAINTAINER Cameron Whiting "thetoxicarcade@gmail.com"
RUN apt-get update -qq && \
    apt-get install -qqy build-essential libssl-dev libffi-dev python-dev tor 1>/dev/null
ADD requirements.txt /
RUN pip install -r requirements.txt 1>/dev/null && \
    pip install nose2 setuptools-lint 1>/dev/null
ADD . /code/delegito
WORKDIR /code
RUN mv delegito/setup.py setup.py && \
    mv delegito/.pylintrc .pylintrc && \
    python setup.py build && \
    python setup.py test && \
    python setup.py install && \
    python setup.py lint || echo "Lint failing..."
#ENV DEBIAN_FRONTEND noninteractive
#RUN apt-get update && apt-get install -y apt-transport-https && apt-get upgrade -y --install-recommends
#RUN sudo apt-get install -y --install-recomends python-pip python-dev
#ADD supervisord.conf /supervisord.conf
#EXPOSE 80:400
#EXPOSE 400
#CMD ["supervisord","-c","/supervisord.conf"]
#ENTRYPOINT []
#lynis audit dockerfile <file>
