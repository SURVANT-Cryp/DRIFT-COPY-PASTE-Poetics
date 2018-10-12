#! /usr/bin/pythonw
# coding: utf-8

"""
cut-up
"""

import random, textwrap
from random import randint

text = ['do', 'it', 'yourself']

while len(text) > 3:
    text.remove(random.choice(text))
print "\noutput:\n\n" + \
    textwrap.fill(" ".join(text), 40) + random.choice(['']) + '\n'

