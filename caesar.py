#Caesar cipher encryption method

text = input('Enter text: ')
shift = int(input('Enter shift key: '))
text = text.lower()
result = ""

for char in text:
    #check for non-alphabets.
    if char.isalpha():
        code = ord(char) 
        char_code = code + shift

        if char_code > 121:
            char_code -= 26

        newcode = chr(char_code)
        result += newcode
        #print (char, code, char_code, newcode)
    else:
        result +=char
print(f'here is your code: {result}')