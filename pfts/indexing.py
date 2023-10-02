
class Indexing:
    """класс индексации файла"""
    def __init__(self, arg, ind):
        self.arg = arg
        self.ind = ind

    def load(self):
        """индексация"""
        memo = {}

        for i in self.arg:
            if i not in memo.keys():
                triallist = []
                #c = self.arg.count(i)
                triallist.append((self.ind, 1))
                memo[i] = triallist
        return memo
