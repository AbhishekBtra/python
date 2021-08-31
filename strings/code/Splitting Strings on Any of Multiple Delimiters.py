import re

line = 'asdf    , ghj; 12; open   ;  ,  jkl '

list_of_words = re.split('[\s,;]\s*',line)

print(list_of_words) #['asdf', '', 'ghj', '12', 'open', '', '', 'jkl', '']