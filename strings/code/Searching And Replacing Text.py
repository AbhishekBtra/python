import re

text = 'Hello, this text should be replaced'

replaced_text = text.replace('this text should be','the text is ')

print(text) #Hello, this text should be replaced
print(replaced_text) #Hello, the text is  replaced

## OR we could use sub() for complex patterns
print('-'*50+'sub()'+'-'*50)
text = 'Hello, today is 17th Aug'

re_subbed = re.sub('\s[0-9]+',' 18',text)

print(text) #Hello, today is 17th Aug
print(re_subbed) #Hello, today is 18th Aug