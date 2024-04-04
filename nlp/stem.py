
class Stemming:
    """ stemming class """
    def __init__(self, llist, rlist):
        self.llist = llist
        self.rlist = rlist

    def binarysearch(self, xlist, item):
        """ bynary search method """
        self.xlist = xlist
        self.item = item
        low:int = 0
        high:int = len(self.xlist)-1
        while low <= high:
            mid:int = (low + high) // 2
            if self.xlist[mid] == self.item:
                return mid
            elif self.xlist[mid] < self.item:
                low = mid + 1
            elif self.xlist[mid] > self.item:
                high = mid - 1
        return False

    def load(self, text):
        """ stemming method """
        self.text = text
        slist = []
        
        for i in self.text:
            if type(i) == int:
                slist.append(i)
            else:
                binaryr = self.binarysearch(self.llist, i)
                if binaryr != False:
                    slist.append(self.rlist[binaryr])
                else:
                    slist.append(i)
        return slist

