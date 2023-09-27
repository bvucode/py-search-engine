
def stopwords(chlang):
    stoplist = []
    if chlang == "ru":
        with open("./data/stopwordsru.txt", "r") as file:
            stoplist = file.read().split("\n")

    if chlang == "eng":
        with open("./data/stopwordsru.txt", "r") as file:
            stoplist = file.read().split("\n")
    return stoplist

def stemming():
    llist = []
    rlist = []
    with open("./data/stem.txt", "r") as file:
        for line in file:
            if not line:
                continue
            else:
                left, right, *res = line.split(":")
                llist.append(left)
                rlist.append(right.replace("\n", ""))
    return llist, rlist
