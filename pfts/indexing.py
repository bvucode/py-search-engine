
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
                c = self.arg.count(i)
                triallist.append((self.ind, c))
                memo[i] = triallist
        return memo
