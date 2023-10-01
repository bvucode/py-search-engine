import os
import sys
from pfts.indexing import Indexing
from pfts.update import Update
from pfts.ftsearch import Ftsearch
from nlp.tokenize import Tokenize

def helper():
    print("usage: main.py [-h] [file_paths file_words output_file]\nsearch engine\noptional arguments: \n-h, --help show this help message\n")

def pathwalk(listpaths):
    listfiles = []
    for i in listpaths:
        listdirs = []
        # распечатать все файлы и папки рекурсивно
        for dirpath, dirnames, filenames in os.walk(i):
            # перебрать каталоги
            for dirname in dirnames:
                listdirs.append(os.path.join(dirpath, dirname))
            # перебрать файлы
            for filename in filenames:
                listfiles.append(os.path.join(dirpath, filename))
    if len(listdirs) == 0:
        return listfiles
    return pathwalk(listdirs)

def indexer(fpaths, fwords, ofile):
    listpaths = []
    xlist = []
    memo = {}
    with open(fpaths, "r") as file:
        for line in file:
            if not line:
                continue
            else:
                listpaths.append(line.replace("\n", ""))
    directories = pathwalk(listpaths)
    for i in directories:
        with open(i, "r") as file2:
            text2 = file2.read()
            # tokenize file to words
            tokword2 = Tokenize(text2)
            tokwordload2 = tokword2.words()
            r = Indexing(tokwordload2, directories.index(i))
            l = r.load()
            if directories.index(i) == 0:
                memo = l
            else:
                u = Update(l, memo)
                memo = u.load()
    with open(fwords, "r") as file3:
        text = file3.read()
        # tokenize file to words
        tokword = Tokenize(text)
        tokwordload = tokword.words()
    for i in tokwordload:
        if i not in xlist:
            xlist.append(i)
    var = Ftsearch(xlist, memo)
    xvar = var.load()
    for k, v in xvar.items():
        with open(ofile, "a") as f:
            f.write(directories[k]+"\n")

def main():
    args = sys.argv[:]
    listfiles = []
    for arg in args:
        if len(args) == 2 and arg == "-h" or arg == "--help":
            helper()
            break
        elif len(args) == 4:
            indexer(args[1], args[2], args[3])
            break

if __name__ == "__main__":
    # calling the main function
    main()
