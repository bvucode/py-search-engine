
class Ftsearch:
    """ Full search class """
    def __init__(self, xlist, xdict):
        self.xlist = xlist
        self.xdict = xdict

    def load(self):
        """ search method """
        nlist = []
        mdict = {}
        for i in self.xlist:
            if i in self.xdict.keys():
                nlist.append(self.xdict[i])

        for i in nlist:
            for j in i:
                if j[0] not in mdict.keys():
                    mdict[j[0]] = j[1]
                else:
                    mdict[j[0]] = mdict[j[0]] + j[1]
        return mdict
