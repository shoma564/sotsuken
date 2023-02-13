FROM shomaigu/ubuntu-base
#FROM ubuntu:20.04
ADD ./sh/script.sh /etc/

RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install nmap openssh-server

RUN mkdir /etc/share/
RUN mkdir /var/run/sshd
RUN echo 'root:password' | chpasswd
RUN sed -ri 's/^#?PermitRootLogin\s+.*/PermitRootLogin yes/' /etc/ssh/sshd_config
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22


CMD /etc/script.sh
