import re

# load text
itemsfile='test\\testitems.txt'
blocklistfile = 'test\\blocklist.txt'

# write text files to lists and clean up for search
with open(blocklistfile, "r") as i:
    blockedlines = [word.strip().lower() for word in i.readlines()]
with open(itemsfile, "r") as i:
    itemlines = [word.strip().lower() for word in i.readlines()]

# determine lines with blocked words in and make list of non-blocked lines
# use break to avoid e.g. 'i had a bad bad day' appearing twice in the list
cleanlines=[]
for sentence in itemlines:
    bad_sentence = False
    for blockedword in blockedlines:
        if re.search(r"\b" + re.escape(blockedword) + r"\b", sentence):
            bad_sentence = True
            break
    if not bad_sentence:
        cleanlines.append(sentence)    

# change list to text file
with open('cleanitems.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % lines for lines in cleanlines)