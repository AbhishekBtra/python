from operator import itemgetter
from pprint import pprint

rows = [
{'fname': 'Abhishek', 'lname': 'Batra', 'uid': 1003},
{'fname': 'Rachit', 'lname': 'Kumar', 'uid': 1002},
{'fname': 'Ajit', 'lname': 'Waikar', 'uid': 1001},
{'fname': 'Neal', 'lname': 'Jones', 'uid': 1004}
]

rows_by_fname =  sorted(rows,key= itemgetter('fname'))
rows_by_uid =  sorted(rows,key= itemgetter('uid'))

pprint(rows_by_fname)
print('-'*100)
pprint(rows_by_uid)
print('-'*100)

#OR we can use a lamda with sorted, however itemgetter is faster

rows_by_fname_lambda = sorted(rows,key= lambda x: x['fname'])

pprint(rows_by_fname_lambda)

# remember that we can use itemgetter with other functions such as min, max....

max_by_uid = max(rows, key= itemgetter('uid'))
print('-'*100)
print('max row => ',max_by_uid) #max row =>  {'fname': 'Neal', 'lname': 'Jones', 'uid': 1004}