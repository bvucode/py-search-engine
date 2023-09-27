import os
from pfts.indexing import Indexing
from pfts.update import Update
from pfts.ftsearch import Ftsearch
from nlp.tokenize import Tokenize

dlist = []
memo = {}

path = "./my_folder/"
directory = os.listdir(path)
for f in directory:
    with open(path + f, "r") as file:
        text = file.read()
        # tokenize file to words
        tokword = Tokenize(text)
        tokwordload = tokword.words()
        dlist.append(tokwordload)

for c, i in enumerate(dlist):
    r = Indexing(i, c)
    l = r.load()
    if c == 0:
        memo = l
    else:
        u = Update(l, memo)
        memo = u.load()

while True:
    xlist = []
    inp = input(">> ")
    word = Tokenize(inp)
    wordload = word.words()
    for i in wordload:
        if i not in xlist:
            xlist.append(i)
    var = Ftsearch(xlist, memo)
    xvar = var.load()
    print(xvar)
