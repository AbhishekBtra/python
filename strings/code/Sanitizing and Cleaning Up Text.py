text = 'Java is\tawesome and python is\fcool\r\n'

remap = {
    ord('\t') : '   ',
    ord('\f') :' ',
    ord('\r') :None
}

translated_text = text.translate(remap)

print(text)
print(translated_text)