import os
import re


def convertCodeBlockForClass(previous: str):
    code_block: list[str] = re.findall('Notes\s+-----\s+This object can be accessed by:[\w\W]+?\n\n', previous)
    if len(code_block) == 0:
        return previous
    
    code_block_string = '    This object can be accessed by:\n\n    .. code-block:: python\n\n'
    code_block_string += '\n'.join(code_block[0].splitlines()[3:]).replace('- ', '')
    
    new = re.sub('Notes\s+-----\s+This object can be accessed by:[\w\W]+?\n\n',
           'Notes\n    -----\n{}\n'.format(code_block_string), previous)
    
    code_block: list[str] = re.findall('Notes\s+-----\s+This function can be accessed by:[\w\W]+?\n\n', previous)
    if len(code_block) == 0:
        return previous
    
    code_block_string = '        This function can be accessed by:\n\n        .. code-block:: python\n\n'
    code_block_string += '\n'.join(code_block[0].splitlines()[3:]).replace('- ', '')
    
    new = re.sub('Notes\s+-----\s+This function can be accessed by:[\w\W]+?\n\n',
           'Notes\n        -----\n{}\n'.format(code_block_string), new)
    
    return new

def convertCodeBlockForPackage(path: str):
    modules = os.listdir(path)
    for module in modules:
        if not module.endswith('.py') or module.startswith('__init__'):
            continue
        if os.path.isfile('{}\\{}'.format(path, module)):
            print('    Processing {} module'.format(module))
            with open('{}\\{}'.format(path, module), 'r+', encoding='utf-8') as f:
                class_string = f.read()
                f.close()
            if len(re.findall('class \w+', class_string)) == 0:
                continue
            new_class_string = convertCodeBlockForClass(class_string)
            if new_class_string == class_string:
                continue
            with open('{}\\{}'.format(path, module), 'w+', encoding='utf-8') as f:
                f.write(new_class_string)
                f.close()
        elif os.path.isdir('{}\\{}'.format(path, module)):
            convertCodeBlockForPackage('{}\\{}'.format(path, module))
   
packages = os.listdir('abaqus')
print(packages)

for package in packages:
    package_path = 'abaqus\\{}'.format(package)
    if not os.path.isdir(package_path) or package.startswith('__') or package.startswith('.'):
        continue
    print('Processing {} package'.format(package))
    convertCodeBlockForPackage(package_path) 
    
# with open('abaqus\\Adaptivity\\AdaptiveMeshConstraint.py', 'r+', encoding='utf-8') as f:
#     text = f.read()
#     f.close()
    
# print(convertCodeBlockForClass(text))
