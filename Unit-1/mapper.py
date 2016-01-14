#!/usr/bin/python
import sys
import re
count = 0
WORD_RE = re.compile(r"[\w']+")
filename = sys.argv[2]
findword = sys.argv[1]
allWords = []
with open (filename, "r") as myfile:
    allWords = WORD_RE.findall(myfile.read())
allWords = [word.lower() for word in allWords]
print allWords.count(findword.lower())