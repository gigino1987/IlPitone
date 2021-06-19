# coding: utf-8
# This script provides automatically upgrade all packages of Python via PIP utility

import os
from sys import exit

print('PIP Upgrade all packages, by Luigi Russo')
try:
    input('Press ENTER to continue, CTRL+C to stop.')
except KeyboardInterrupt:
    print('Exiting...')
    exit()
# create a packages list file

os.system("pip list > pip-packages.txt")

f = open("pip-packages.txt").read()
f = f.split("\n")
del(f[0:2])
buffer = ""

for i in f:
    j = i.split(' ')
    buffer+=j[0]+" "
print(buffer)
os.system("pip install --upgrade "+buffer)
os.unlink("pip-packages.txt")
input('Done. Press ENTER to finish.')