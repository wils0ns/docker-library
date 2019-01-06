def preseed_master_minion_key():
    hostname = str(subprocess.Popen(['hostname'], stdout=subprocess.PIPE).communicate()[0]).strip()

    process = subprocess.Popen(['salt-key', '--gen-keys={}'.format(hostname)])
    process.wait()

    process = subprocess.Popen(['mkdir', '/etc/salt/pki/master/minions', '-p'])
    process.wait()

    process = subprocess.Popen([
        'cp', '{}.pub'.format(hostname), '/etc/salt/pki/master/minions/{}'.format(hostname)
    ])
    process.wait()

    process = subprocess.Popen(['mkdir', '/etc/salt/pki/minion', '-p'])
    process.wait()

    process = subprocess.Popen([
        'mv', '{}.pub'.format(hostname), '/etc/salt/pki/minion/minion.pub'
    ])
    process.wait()
    process = subprocess.Popen([
        'mv', '{}.pem'.format(hostname), '/etc/salt/pki/minion/minion.pem'
    ])
    process.wait()
