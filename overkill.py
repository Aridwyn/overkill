from Crypto.Cipher import AES
import hashlib
import numpy as geek
import re

BS = AES.block_size
number = geek.arange(100,1000,1)

# print('введите cipher_text')
# hex_string = str(input())
hex_string = "5d9906f1bfa9506698152ba36b2fe14674ea4043e70f01b7f76ef8509718ce54b819dc8c3c9dc28cb0be9314f66c1054"
sample_string = hex_string.encode("ascii")
bytearray_string = bytearray.fromhex(hex_string)
# print(bytearray_string)

def overkill(key):
    key = key
    unpad = lambda s : s[:-ord(s[len(s)-1:])]
    cipher_text = bytearray_string
    iv = cipher_text[:BS]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plain_text_byt = unpad(cipher.decrypt(cipher_text[BS:]))
    plain_text_string = str(plain_text_byt)
    if (len(plain_text_byt)) != 0:
        return(plain_text_string)

def remove_hex_codes(text):
    pattern = r"\\x[0-9a-fA-F]{2}"
    filtered_text = re.sub(pattern, "", text)
    if filtered_text == text:
        return text
# text = "Пример строки с шестнадцатеричным кодом: \\x8b\\xf5\\xfd\\xed"

for i in number: 
    key_N = str(i)
    # print(key_N)
    key = hashlib.sha256(key_N.encode('ASCII')).digest()
    overkill(key)

    if str(overkill(key)) != str('None'): 
        if str(remove_hex_codes(overkill(key))) != str('None'):
            print(remove_hex_codes(overkill(key)))