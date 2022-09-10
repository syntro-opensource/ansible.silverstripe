import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_hosts_file(host):
    f = host.file('/etc/hosts')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'

    f = host.file('/var/www/html/index.php')
    assert f.exists

def test_webroot(host):
    f = host.file('/var/www/html/')
    assert f.exists
    f = host.file('/var/www/html/index.php')
    assert f.exists
    f = host.file('/var/www/html/_graphql')
    assert f.exists
    f = host.file('/var/www/html/assets')
    assert f.exists
    f = host.file('/var/www/html/.htaccess')
    assert f.exists
