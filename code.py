Coding:
  
import re
from collections import Counter
sentence = input()
a=input()
counter = len(re.findall(a, sentence))
print(counter)
