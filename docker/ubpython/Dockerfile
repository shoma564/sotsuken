FROM ubuntu:20.04
USER root

ADD ./python_hon/ /root/


RUN apt-get update && apt-get install -y --no-install-recommends wget build-essential libreadline-dev libncursesw5-dev libssl-dev libsqlite3-dev libgdbm-dev libbz2-dev liblzma-dev zlib1g-dev uuid-dev libffi-dev libdb-dev vim less openssh-server
RUN apt-get -y install locales && localedef -f UTF-8 -i ja_JP ja_JP.UTF-8
ENV LANG ja_JP.UTF-8
ENV LANGUAGE ja_JP:ja
ENV LC_ALL ja_JP.UTF-8
ENV TZ JST-9
ENV TERM xterm
RUN wget --no-check-certificate https://www.python.org/ftp/python/3.9.5/Python-3.9.5.tgz && tar -xf Python-3.9.5.tgz && cd Python-3.9.5 && ./configure --enable-optimizations && make && make install

RUN apt-get autoremove -y


RUN pip3 install paramiko
RUN pip3 install --upgrade pip
RUN pip3 install --upgrade setuptools
RUN pip3 install paramiko



CMD ["python3", "/root/sc.py"]
