import string
import random
print ("probando!!")
print ("generador de claves")
chars = string.ascii_letters + string.digits + string.punctuation
password = ""
length = 10

for c in range(length):
    password = password + random.choice(chars)

print ("contraseña generada: " + password)