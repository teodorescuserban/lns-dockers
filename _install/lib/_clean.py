'''clean up the base folder; only templates, scripts and var file remain'''

# 2015 copyleft "Serban Teodorescu <teodorescu.serban@gmail.com>"

import os
import sys

sure = raw_input('\nClean up this folder! Are you sure? <y/n> ')
if sure not in ['y', 'Y']:
    print 'Canceled. Exiting...\n'
    sys.exit(1)

file_list = []
for file_name in os.listdir('.'):
    if file_name.startswith('_'):
        continue
    if file_name.endswith('.tpl'):
        continue
    file_list.append(file_name)

if not len(file_list):
    print '\nNothing to remove. Everything looks very clean already :)'
    print 'Maybe you want to run config instead?\n'
    sys.exit(1)

print '\nThe following files will be removed.\n'
print sorted(file_list)
sure = raw_input('\nAre you sure? <y/n> ')

if sure not in ['y', 'Y']:
    print 'Canceled. Exiting...\n'
    sys.exit(1)

for file_name in file_list:
    os.remove(file_name)

print 'Done.\n'
