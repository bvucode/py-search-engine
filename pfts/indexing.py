
class Indexing:
    """ indexing class """
    def __init__(self, arg, ind):
        self.arg = arg
        self.ind = ind

    def load(self):
        """ indexing method """
        memo = {}

        for i in self.arg:
            if i not in memo.keys():
                triallist = []
                triallist.append((self.ind, 1))
                memo[i] = triallist
            else:
                triallist = []
                w = memo[i]
                triallist.append((self.ind, w[0][1] + 1))
                memo[i] = triallist
        return memo
