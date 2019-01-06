FROM ubuntu:18.04

ARG SALT_VERSION=2017.7
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install wget gnupg -y && \
    wget -O salt-gpg-key.pub https://repo.saltstack.com/apt/ubuntu/18.04/amd64/${SALT_VERSION}/SALTSTACK-GPG-KEY.pub && \
    apt-key add salt-gpg-key.pub && rm salt-gpg-key.pub && \
    echo "deb http://repo.saltstack.com/apt/ubuntu/18.04/amd64/${SALT_VERSION} bionic main" > /etc/apt/sources.list.d/saltstack.list && \
    apt-get update && apt-get install salt-master salt-api salt-minion salt-syndic virt-what -y && \
    mkdir /var/log/salt/api.d/ -p && \
    wget -O get-pip.py https://bootstrap.pypa.io/get-pip.py && python get-pip.py && \
    pip install -U CherryPy pyOpenSSL pyinotify && \
    # Clean up
    python -m pip uninstall --yes pip && \
    apt-get remove --purge wget python-pip -y && apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

EXPOSE 4505 4506
COPY ./app /app
CMD python -u /app/app.py
