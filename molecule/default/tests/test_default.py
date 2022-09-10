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
    assert os.path.exists('/var/www/html/')
    assert os.path.exists('/var/www/html/index.php')
    assert os.path.exists('/var/www/html/_graphql')
    assert os.path.exists('/var/www/html/assets')
    assert os.path.exists('/var/www/html/.htaccess')
