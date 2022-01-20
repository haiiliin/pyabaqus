import os

files = os.listdir('abaqus\\DisplayGroup')
mdbString, odbString = '', ''
for file in files:
    if file.startswith('Leaf'):
        with open('abaqus\\DisplayGroup\\{}'.format(file), 'r+', encoding='utf-8') as f:
            text = f.read()
            f.close()
        if 'import displayGroupOdbToolset' in text:
            mdbString += 'from abaqus.DisplayGroup.{} import {}\n'.format(file[:-3], file[:-3])
        if 'import displayGroupMdbToolset' in text:
            odbString += 'from abaqus.DisplayGroup.{} import {}\n'.format(file[:-3], file[:-3])


print('Mdb = \n', mdbString)
print('Odb = \n', odbString)
