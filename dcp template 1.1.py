#! /usr/bin/pythonw
# coding: utf-8

import random, textwrap
from random import randint

"""
Cut-up
"""

text = ['do', 'it', 'yourself']

while len(text) > 3:
    text.remove(random.choice(text))
print "\nDRIFT/COPY/PASTE POETIX:\n\n" + \
    textwrap.fill(" ".join(text), 40) + random.choice(['']) + '\n'

