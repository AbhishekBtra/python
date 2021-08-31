import re

text = 'Python is a FleXIBLe language'

case_insensitive_subbed_text = re.sub('flexible','structured',text,flags=re.IGNORECASE)

print(text) #Python is a FleXIBLe language
print(case_insensitive_subbed_text) #Python is a structured language