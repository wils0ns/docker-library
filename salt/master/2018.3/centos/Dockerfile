FROM centos:7

ARG SALT_VERSION=2018.3
# ENV DEBIAN_FRONTEND noninteractive

RUN yum install https://repo.saltstack.com/yum/redhat/salt-repo-${SALT_VERSION}-1.el7.noarch.rpm -y && \
    yum clean expire-cache && \
    yum install wget salt-master salt-api salt-minion salt-syndic virt-what -y && \
    mkdir /var/log/salt/api.d/ -p && \
    wget -O get-pip.py https://bootstrap.pypa.io/get-pip.py && python get-pip.py && \
    pip install -U CherryPy pyOpenSSL pyinotify && \
    # Clean up
    python -m pip uninstall --yes pip && \
    yum clean all && rm -rf /var/cache/yum /tmp/* /var/tmp/*
    # apt-get remove --purge wget python-pip -y && apt-get autoremove -y && apt-get clean && rm -rf /tmp/* /var/tmp/*

EXPOSE 4505 4506
COPY ./app /app
CMD python -u /app/app.py
