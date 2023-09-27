
class Update:
    """класс индексации файла"""
    def __init__(self, newdict, olddict):
        self.newdict = newdict
        self.olddict = olddict

    def load(self):
        """индексация"""
        for k, v in self.newdict.items():
            if k in self.olddict.keys():
                t = []
                w = self.olddict[k]
                for i in w:
                    t.append(i)
                for i in v:
                    t.append(i)
                self.olddict[k] = t
            elif k not in self.olddict.keys():
                self.olddict[k] = v
        return self.olddict
