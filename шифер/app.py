from Cipher import Cipher

cip = Cipher()

key = input('Введи ключ: ')
text = input('Введи слово для шифрования: ')
key_text = input('Введи слово для расшифрования: ')

d = cip.cipher(key, text, key_text)

print(d)




