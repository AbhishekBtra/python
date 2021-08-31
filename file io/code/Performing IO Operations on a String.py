from io import StringIO

"""Use StringIO to create a file-like object containing 
test data that’s fed into a function that would otherwise
work with a normal file."""

s = StringIO()
print('Unit test case 1',file=s)
print('Unit test case 2',file=s)
print('Unit test case 3',file=s)

print(s.getvalue()) #Unit test case 1 ...