

class Argument:

    def __init__(self, name: str, argType: str, required: bool = True, default=None, docs: list[str] = None):
        if docs is None:
            docs = []
        self.name = name
        self.argType = argType
        self.required = required
        self.docs = docs
        self.default = default

    def __str__(self):
        return 'name: {}, type: {}, default: {}, doc string: {}'.format(
            self.name, self.argType, self.required, self.default, self.docs)

    def argString(self, typeHint: bool = True, objectName: str = '') -> str:
        argType = self.argType if not self.argType == objectName else "'{}'".format(self.argType)
        if typeHint:
            if self.required:
                return '{}: {}'.format(self.name, argType)
            else:
                return '{}: {} = {}'.format(self.name, argType, self.default)
        else:
            if self.required:
                return self.name
            else:
                return '{}={}'.format(self.name, self.default)
