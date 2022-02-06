import os


def setAutoDocNoIndex(path: str):
    print('Processing {} package'.format(path))
    files = os.listdir(path)
    for file in files:
        filePath = '{}\\{}'.format(path, file)
        if file.startswith('__') or file.startswith('.'):
            continue
        elif os.path.isdir(filePath):
            setAutoDocNoIndex(filePath)
        elif os.path.isfile(filePath) and file.endswith('.rst'):
            with open(filePath, 'r+', encoding='utf-8') as f:
                text = f.read()
                f.close()
            lines = text.splitlines()
            for line, i in zip(lines, range(len(lines))):
                if line.startswith('.. auto'):
                    lines[i] = line + '\n    :noindex:'
                    
            with open(filePath, 'w+', encoding='utf-8') as f:
                text = f.write('\n'.join(lines))
                f.close()
                
setAutoDocNoIndex('docs\\source\\user')
            