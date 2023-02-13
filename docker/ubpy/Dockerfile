#FROM ubuntu:20.04
FROM shomaigu/ubuntu-base
ADD ./sh/script.sh /etc/
ADD ./python_hon /etc/

RUN apt-get -y update
RUN apt-get -y install software-properties-common && add-apt-repository ppa:deadsnakes/ppa && apt-get -y install python3.9 python3-pip
RUN apt-get -y install openssh-server

RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install paramiko

RUN mkdir -p /etc/share/
RUN mkdir -p /var/run/sshd
RUN mkdir -p /run/sshd

RUN ssh-keygen -A
RUN echo 'root:password' | chpasswd
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd


ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22


CMD ["/etc/script.sh"]
