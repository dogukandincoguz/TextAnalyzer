from collections import Counter
from sys import argv
import re
import locale
locale.setlocale(locale.LC_ALL, "en_US")

#2.1
text = open(argv[1] , "r")
sent = re.split(r'[.]', text)