FROM ubuntu:20.04
ADD ./sh/script.sh /etc/
RUN apt-get -y update && apt-get -y upgrade
RUN apt-get -y install nmap openssh-server
CMD /etc/script.sh
