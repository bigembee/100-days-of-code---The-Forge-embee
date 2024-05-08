#Caesar cipher encryption method

text = input('Enter text: ')
shift = input('Enter shift key: ')
text = text.lower()
code = ""
for char in text:
    code = ord(char) + shift
    code = chr(code)
print(code)