import copy
import os
from collections import deque


packages = os.listdir('abaqus')

def addClass(name, path, headerLabel='~'):
    string = ''
    string += '{}\n'.format(name)
    string += '{}\n\n'.format(headerLabel * len(name))
    string += '.. autoclass:: {}\n    :members:\n\n'.format(path)
    return string


def addPackage(packagePath, h, hs):
    string = '\n'
    files = os.listdir(packagePath)
    hs1 = copy.deepcopy(hs)
    for file in files:
        hs1 = copy.deepcopy(hs)
        if file.startswith('__'):
            continue
        if os.path.isdir('{}\\{}'.format(packagePath, file)):
            h = hs1.popleft()
            string += addPackage('{}\\{}'.format(packagePath, file), h, hs1)
        elif os.path.isfile('{}\\{}'.format(packagePath, file)):
            path = '{}\\{}\\{}'.format(packagePath, file[:-3], file[:-3]).replace('\\', '.')
            string += addClass(file[:-3], path, h)
    hs = hs1
    return string


for package in packages:
    if not os.path.isdir('abaqus\\{}'.format(package)):
        continue

    text = ''
    text += '{}\n'.format('=' * len(package))
    text += '{}\n'.format(package)
    text += '{}\n\n'.format('=' * len(package))
    text += 'Object features\n---------------\n'
    modules = os.listdir('abaqus\\{}'.format(package))

    headers = deque(['~', '*', '\'', '`', '.', '*', '+'])
    header = headers.popleft()
    text += addPackage('abaqus\\{}'.format(package), header, headers)

    rstPath = 'docs\\rsts\\{}.rst'.format(package.lower())
    with open(rstPath, 'w+') as f:
        f.write(text)
        f.close()
