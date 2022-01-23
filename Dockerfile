FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8
RUN apt-get update 2>/dev/null
RUN apt-get -y install openssh-server
RUN mkdir /run/sshd
RUN echo PermitRootLogin yes >> /etc/ssh/sshd_config
RUN echo PermitEmptyPasswords yes >> /etc/ssh/sshd_config
RUN sed -i s/:x:/::/g /etc/passwd
RUN sed -i '3i/usr/sbin/sshd' /start.sh
COPY ./app /app
EXPOSE 80/tcp
EXPOSE 22/tcp
