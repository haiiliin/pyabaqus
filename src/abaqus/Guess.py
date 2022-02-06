import os


class Guess:

    @staticmethod
    def findParentFilePath(userDefinedType: str, searchDir: str):
        if not os.path.isdir(searchDir):
            return ''

        files = os.listdir(searchDir)
        for file in files:

            if os.path.isdir(os.path.join(searchDir, file)):
                foundDir = Guess.findParentFilePath(userDefinedType, os.path.join(searchDir, file))
                if not foundDir == '':
                    return foundDir
            elif os.path.isfile(os.path.join(searchDir, file)) and file.endswith('.py'):
                filePath = os.path.join(searchDir, file)
                with open(filePath, 'r+', encoding='utf-8') as f:
                    text = f.read()
                    if 'class {}:'.format(userDefinedType) in text or 'class {}('.format(userDefinedType) in text:
                        return filePath
                    f.close()
        return ''
