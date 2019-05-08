FROM ubuntu:18.04

ARG SALT_VERSION=2019.2
ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && apt-get install wget gnupg -y && \
    wget -O salt-gpg-key.pub https://repo.saltstack.com/py3/ubuntu/18.04/amd64/${SALT_VERSION}/SALTSTACK-GPG-KEY.pub && \
    apt-key add salt-gpg-key.pub && rm salt-gpg-key.pub && \
    echo "deb http://repo.saltstack.com/py3/ubuntu/18.04/amd64/${SALT_VERSION} bionic main" > /etc/apt/sources.list.d/saltstack.list && \
    apt-get update && apt-get install python3-distutils salt-minion virt-what -y && \
    wget -O get-pip.py https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && \
    python3 -m pip install -U CherryPy pyOpenSSL pyinotify && \
    # Clean up
    python3 -m pip uninstall --yes pip && \
    apt-get remove --purge wget python-pip -y && apt-get autoremove -y && apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

COPY ./app /app
CMD python3 -u /app/app.py
