'''setup and configure a docker-compose stack'''

# 2015 copyleft "Serban Teodorescu <teodorescu.serban@gmail.com>"

import fcntl
import re
import os
import pprint
import socket
import struct
import sys


def get_filename(label):
    file_name = raw_input(label)
    if not os.path.isfile(file_name):
        print 'File', file_name, 'does not exists.'
        return False
    return file_name


def transform_file_to_string(file_name):
    return_list = []
    with file(file_name) as f:
        for line in f.readlines():
            if '-----' in line:
                continue
            return_list.append(line.rstrip())
    return '"' + ' '.join(return_list) + '"'


def get_ip_address(ifname):
    '''copy paste from python cookbook.'''
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


def import_ssl_files_as_env_vars():
    '''asks about the ssl key and certificate files location;
    imports them as strings and returns a dict containing both'''
    print 'Do you want to autocomplete ssl certificate and ssl key env vars?'
    run_or_not = raw_input('You will need the crt and key files (y/n/t): ')
    key = ''
    crt = ''
    if run_or_not.lower() == 'y':
        key_fh = get_filename('SSL Key filename (full path): ')
        if key_fh:
            key = transform_file_to_string(key_fh)
            # print key
        crt_fh = get_filename('SSL Certificates filename (full path): ')
        if crt_fh:
            crt = transform_file_to_string(crt_fh)
            # print crt
    elif run_or_not.lower() == 't':
        key = transform_file_to_string('_example_key.pem')
        crt = transform_file_to_string('_example_crt.pem')
    else:
        print 'Ok. Skipping.'

    return {'SSL_KEY': key, 'SSL_CRT': crt}


def import_vars_as_env_vars():
    '''creates a dict containing the env vars read from
    vars file, all substitution made'''
    env = {}
    env['DOCKER0_ADDR'] = get_ip_address('docker0')
    with file('vars') as f:
        for l in f.readlines():
            l = l.rstrip()
            if (len(l) < 2) or ('=' not in l) or (l.startswith('#')):
                continue
            label, value = l.split('=')
            # print label, '-->', value
            sub_vars = re.findall(r'\$\{(.*)\}', value)  # try to substitute variable

            for i in sub_vars:
                value = value.replace('${' + i + '}', env[i])
            env[label] = value
            if label == 'DOMAIN':
                env['DOMAIN_LABEL'] = re.sub(r'\.ro$', 'ro', value)
    return env


def create_config_files(env):
    '''creates config files from templates and env dict'''
    for template_file in os.listdir('.'):
        if not template_file.endswith('.tpl'):
            continue
        file_name = re.sub(r'\.tpl$', '', template_file)
        with open(template_file) as t:
            template = t.readlines()

        print 'writing', file_name, '...'
        with open(file_name, 'w') as f:
            for line in template:
                sub_vars = re.findall(r'\$\{([0-9a-zA-Z_]+)\}', line)
                for var_name in sub_vars:
                    line = line.replace('${' + var_name + '}', env[var_name])
                f.write(line)


def main():
    env = {}
    env.update(import_vars_as_env_vars())
    env.update(import_ssl_files_as_env_vars())

    # pprint.pprint(env)
    create_config_files(env)

    # for l, v in os.environ.items():
    # for l in sorted(os.environ.keys()):
    #     print l, '-->', os.environ[l]


if __name__ == '__main__':
    sys.exit(main())
