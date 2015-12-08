'''setup and configure a docker-compose stack'''

# 2015 copyleft "Serban Teodorescu <teodorescu.serban@gmail.com>"


import os
import subprocess
import sys

from distutils.spawn import find_executable

import _doin


# variables file location
VARS_FILE = '_VARS'

# custom variables file location
CUSTOM_VAR_FILE = '_CUSTOM_VARS'
CUSTOM_VARS = {
    'HDX_PREFIX': ('HDX_SHORT_PREFIX', r'-$', ''),
    'DOMAIN': ('DOMAIN_LABEL', r'\.ro$', 'ro'),
}

# private files names file location
PRIVATE_FILES_FILE = '_PRIVATE_FILES'
PRIVATE_FILES = {
    'SSL_CRT': '_example_crt.pem',
    'SSL_KEY': '_example_key.pem',
    # 'SSH_PUB_KEY': 'ssh.pub',
    # 'SSH_KEY': 'ssh.key',
}


def yes_no():
    intro = raw_input('Press y or Y to continue: ')
    if intro not in ['y', 'Y']:
        print '\nCanceled.\n'
        sys.exit(1)
    return True


def execute_cmd(cmd, err):
    exit_code = subprocess.call(cmd)
    if exit_code:
        print err
        sys.exit(exit_code)


def choose_editor():
    if 'EDITOR' in os.environ:
        editor = os.getenv('EDITOR')
    else:
        mcedit = find_executable('mcedit')
        vi = find_executable('vi')
        nano = find_executable('nano')
        if mcedit:
            editor = mcedit
        elif vi:
            editor = vi
        elif nano:
            editor = nano
        else:
            raise Exception("Can't find any editor.")
    return editor


def process_config():
    '''do all the work, basically:)'''
    c = _doin.Doin(vars_file=VARS_FILE)
    c.custom_vars = CUSTOM_VARS
    c.private_files = PRIVATE_FILES
    c.import_private_files()
    c.import_vars()
    c.create_config_files()


def main():
    '''entrypoint to the configurator'''

    print '\nWelcome to docker configuration tool!'
    print 'This dialog will guide you through'
    print 'to successfully install this docker stack.\n'
    print 'First step: edit file vars (I will open the editor).'
    yes_no()
    cmd = [choose_editor(), VARS_FILE]
    execute_cmd(cmd, '\nEdit variables canceled. Quiting the config as well...')

    # print '\nDone. Ready to edit custom variables'
    # yes_no()
    # cmd = [choose_editor(), CUSTOM_VAR_FILE]
    # execute_cmd(cmd, '\nEdit custom variables canceled. Quiting the config as well...')
    # time.sleep(2)
    # execfile('_CUSTOM_VARS')
    # print CUSTOM_VARS

    # print '\nDone. Ready to edit private files names'
    # yes_no()
    # cmd = [choose_editor(), PRIVATE_FILES_FILE]
    # execute_cmd(cmd, '\nEdit private files names canceled. Quiting the config as well...')
    # execfile('_PRIVATE_FILES')
    # print PRIVATE_FILES

    print '\nDone. Ready to edit templates and replace with your defined variables'
    yes_no()
    process_config()
    print '\nDone. You are ready to use your stack!'

    print 'You will most likely want to execute:\n'
    print '    docker-compose pull\n'
    print 'then\n'
    print '    docker-compose up -d\n'
    print 'Enjoy!\n'


if __name__ == '__main__':
    sys.exit(main())
