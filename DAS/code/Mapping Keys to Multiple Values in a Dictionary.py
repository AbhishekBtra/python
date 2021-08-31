from collections import defaultdict

dictionary = {}

dictionary['influence'] = 'effect'

dictionary['influence'] = 'impact'

print(dictionary['influence'])  # prints impact

def_dict = defaultdict(list)

def_dict['influence'].append('effect')
def_dict['influence'].append('impact')

print(def_dict['influence'])  # prints effect , impact
