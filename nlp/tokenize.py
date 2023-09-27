import re

class Tokenize:
    """ класс делает токинезацию по словам """
    def __init__(self, text):
        self.text = text

    def words(self):
        """ токенизация по словам """
        self.lowertext = self.text.lower()
        self.clearstring = re.sub("[\t\r\n\f\v]", " ", self.lowertext)
        self.onestring = re.sub("[ё]", "е", self.clearstring)
        self.twostring = re.sub("\—|\]|\[|\.|\!|\,|\:|\;|\)|\(|\&|\#|\"|\?|\»|\«|\/", " ", self.onestring)
        self.wordslist = list(map(lambda x: int(x) if x.isdigit() else x, re.split("\s", self.twostring)))
        self.filtered = [x for x in self.wordslist if str(x) not in ""]
        return self.filtered

    def sentences(self):
        """ токенизация по предложениям """
        self.lowertext = self.text.lower()
        self.clearstring = re.sub("[\t\r\n\f\v]", "", self.lowertext)
        self.onestring = re.sub("[ё]", "е", self.clearstring)
        self.sentlist = re.split("(?<!\w\.\w)(?<![a-z]\.\s)(?<=\.)(\s|[a-z].*)", self.onestring)
        self.filtered = [x for x in self.sentlist if x not in " "]
        return self.filtered
