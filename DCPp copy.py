#!/usr/bin/python
# coding: utf-8

from random import randint

#DRIFT/COPY/PASTE POETIX

wordList1 = ['do']
wordList2 = ['it']
wordList3 = ['yourself']

            
wordIndex1=randint(0, len(wordList1)-1)
wordIndex2=randint(0, len(wordList2)-1)
wordIndex3=randint(0, len(wordList3)-1)

stanza = wordList1[wordIndex1] + "\n" + wordList2[wordIndex2] + "\n"
stanza = stanza + wordList3[wordIndex3] + "\n"

print "\nDRIFT/COPY/PASTE POETIX:\n\n" + (stanza)