
import fnmatch
import re
import os
import sys


DOMAIN = os.getenv('DOMAIN')
KEY = os.getenv('SSL_KEY')
CRT = os.getenv('SSL_CRT')
KEY_FILE = '/etc/nginx/ssl.key'
CRT_FILE = '/etc/nginx/ssl.crt'


def transform_env_to_str(env_var):
    s = env_var.replace('"', '').split(":::")
    return '\n'.join(s)


def find_templates(path):

    templates = []

    for root, dirs, files in os.walk(path):
        for file_name in files:
            if file_name.endswith('.tpl'):
                templates.append(os.path.join(root, file_name))

    return templates


def create_config_files():
    '''creates config files from templates and env vars'''
    for template_file in find_templates('/etc/nginx'):
        # if not template_file.endswith('.tpl'):
        #     continue
        file_name = re.sub(r'\.tpl$', '', template_file)
        with open(template_file) as t:
            template = t.readlines()

        if os.path.isfile(file_name):
            print file_name, 'already created. Remove it to refresh.'
            print 'Skipping.'
            continue

        print 'writing', file_name, '...'
        with open(file_name, 'w') as f:
            for line in template:
                sub_vars = re.findall(r'\$\{([0-9a-zA-Z_]+)\}', line)
                for var_name in sub_vars:
                    if var_name not in os.environ:
                        print var_name, 'not found in env!!!'
                        print 'Quitting'
                        sys.exit(1)
                    line = line.replace('${' + var_name + '}', os.getenv(var_name))
                line = line.replace('%', '$')
                f.write(line)


def main():
    # construct crt and key
    with open(CRT_FILE, 'w') as f:
        for line in transform_env_to_str(os.getenv('SSL_CRT')):
            f.write(line)
        f.write('\n')
    with open(KEY_FILE, 'w') as f:
        for line in transform_env_to_str(os.getenv('SSL_KEY')):
            f.write(line)
        f.write('\n')

    create_config_files()


if __name__ == '__main__':
    main()
