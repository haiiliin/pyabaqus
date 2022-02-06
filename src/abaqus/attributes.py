import os
import re

from Guess import Guess


def addHyperlinkForObject(doc: str):
    objects: list[str] = re.findall('\w+\sobject', doc)
    for object in objects:
        userType = object.split()[0]
        userPath = Guess.findParentFilePath(userType, './')
        userPath = userPath[2:-3].replace('\\', '.')
        userPath += '.{}'.format(userType)
        doc = doc.replace(userType, ':py:class:`~{}`'.format(userPath))
    return doc


def addAttributesDocumentationForClass(previous: str):

    attributes = re.findall('    # [\w\W]+?\w: [\w\W]+? = [\w\W]+?\n', previous)

    doc_string = """
    Attributes
    ----------"""
    
    if len(attributes) == 0:
        return previous

    for attribute in attributes:
        lines = attribute.splitlines()
        docs, atts = [], []
        for line in lines:
            line = line.lstrip()
            if line.startswith('#'):
                docs.append(line.replace('#', '').lstrip().rstrip())
            else:
                atts.append(line.lstrip().rstrip())
        doc = '\n        '.join(docs)
        att = ' '.join(atts)
        doc = re.sub('\*(\w+)\*=(\w+)', '**\g<1>=\g<2>**', doc)
        doc = re.sub('\*(\w+)\*', '**\g<1>**', doc)
        doc = addHyperlinkForObject(doc)
        name, Type = tuple(att.split(' = ')[0].split(': '))
        doc_string += """
    {}: {}
        {}""".format(name, Type, doc)

    if 'Attributes\n    ----------' in previous:
        new = re.sub('Attributes\s+----------[\w\W]+?Notes\n\s+-----',
                     '{}\n\n    Notes\n    -----'.format(doc_string.lstrip()), previous)
    else:
        new = previous.replace('Notes\n    -----', '{}\n\n    Notes\n    -----'.format(doc_string.lstrip()))

    return new


def addAttributesDocumentationForPackage(path: str):
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
            new_class_string = addAttributesDocumentationForClass(class_string)
            if new_class_string == class_string:
                continue
            with open('{}\\{}'.format(path, module), 'w+', encoding='utf-8') as f:
                f.write(new_class_string)
                f.close()
        elif os.path.isdir('{}\\{}'.format(path, module)):
            addAttributesDocumentationForPackage('{}\\{}'.format(path, module))

packages = os.listdir('abaqus')
print(packages)

for package in packages:
    package_path = 'abaqus\\{}'.format(package)
    if not os.path.isdir(package_path) or package.startswith('__') or package.startswith('.'):
        continue
    print('Processing {} package'.format(package))
    addAttributesDocumentationForPackage(package_path)


# with open('abaqus\\PlotOptions\\DGContourOptions.py', 'r+', encoding='utf-8') as f:
#     text = f.read()
#     f.close()

# print(addAttributesDocumentationForClass(text))
