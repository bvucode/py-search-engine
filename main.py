import os
import sys
import re
from pfts.indexing import Indexing
from pfts.update import Update
from nlp.tokenize import Tokenize

def helper():
    print("usage: main.py [-h] [file_paths file_words output_file]\nsearch engine\noptional arguments: \n-h, --help show this help message")

def pathwalk(listpaths):
    listfiles = []
    for i in listpaths:
        listdirs = []
        for dirpath, dirnames, filenames in os.walk(i):
            for dirname in dirnames:
                listdirs.append(os.path.join(dirpath, dirname))
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
        text = file.read()
        listpaths = re.split(" ", text.replace("\n", ""))
    directories = pathwalk(listpaths)
    for i in directories:
        with open(i, "r") as file2:
            try:
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
            except:
                continue
    with open(fwords, "r") as file3:
        text = file3.read()
        # tokenize file to words
        tokword = Tokenize(text)
        tokwordload = tokword.words()
    for i in tokwordload:
        if i not in xlist:
            xlist.append(i)
    for i in xlist:
        if i in memo.keys():
            for j in memo[i]:
                with open(ofile, "a") as f:
                    f.write(directories[j[0]] + " - " + i + "\n")
def main():
    args = sys.argv[:]
    for arg in args:
        if len(args) == 2 and arg == "-h" or len(args) == 2 and arg == "--help":
            helper()
            break
        elif len(args) == 4:
            indexer(args[1], args[2], args[3])
            break

if __name__ == "__main__":
    # calling the main function
    main()
