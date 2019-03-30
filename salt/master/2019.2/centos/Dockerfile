FROM centos:7

ARG SALT_VERSION=2019.2

RUN yum install https://repo.saltstack.com/py3/redhat/salt-py3-repo-${SALT_VERSION}.el7.noarch.rpm -y && \
    yum clean expire-cache && \
    yum install epel-release -y && \
    yum install wget salt-master salt-api salt-minion salt-syndic virt-what -y && \
    mkdir /var/log/salt/api.d/ -p && \
    wget -O get-pip.py https://bootstrap.pypa.io/get-pip.py && python3 get-pip.py && \
    python3 -m pip install -U CherryPy pyOpenSSL pyinotify && \
    # Clean up
    python3 -m pip uninstall --yes pip && \
    yum clean all && rm -rf /var/cache/yum /tmp/* /var/tmp/*

EXPOSE 4505 4506
COPY ./app /app
CMD python3 -u /app/app.py
