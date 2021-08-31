from fnmatch import fnmatch, fnmatchcase

is_a_match = fnmatch('foo.txt','*.txt')
print(is_a_match) #True
is_a_match = fnmatchcase('foo.txt','*.TXT')
print(is_a_match) #false
