 class Rule:
    def __init__(self, *args, **kwargs):
        self.Read = kwargs.get('read', False)
        self.Write = kwargs.get('write', False)
        self.Edit = kwargs.get('edit', False)
        self.Delete = kwargs.get('delete', False)
        self.Name = kwargs.get('name', False)
        self.Manage = kwargs.get('manage', False)
        self.Share = kwargs.get('share', False)
    def Parse(self, s):
        for c in s:
            if c == 'r':
                self.Read = True
            elif c == 'w':
                self.Write = True
            elif c == 'e':
                self.Edit = True
            elif c == 'd':
                self.Delete = True
            elif c == 'n':
                self.Name = True
            elif c == 'm':
                self.Manage = True
            elif c == 's':
                self.Share = True
        return self
    def __iter__(self):
        yield ('r', self.Read)
        yield ('w', self.Write)
        yield ('e', self.Edit)
        yield ('d', self.Delete)
        yield ('n', self.Name)
        yield ('m', self.Manage)
        yield ('s', self.Share)
    def __str__(self):
        return ''.join([c if v else '' for c, v in self])

class Directive:
    def __init__(self, *args, **kwargs):
        self.Rule = kwargs.get('rule', '')
        self.Space = kwargs.get('space', '')
    def Parse(self, s):
        elements = s.split(' ')
        self.Rule = Rule().Parse(elements[0])
        self.Space = ' '.join(elements[1:])
        return self
    def __str__(self):
        return str(self.Rule) + ' ' + str(self.Space)