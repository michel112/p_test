FROM python:3
RUN apt-get update && apt-get -y install libxml2-dev libxslt1-dev libxslt-dev python-lxml
RUN pip install lxml

ADD valid.xml /
ADD main.py /
ADD unit_test.py /
ADD invalid_pom.xml /
ADD pom.xml /

CMD [ "python", "-u", "./main.py" ]
CMD [ "python", "-u", "./unit_test.py" ]
