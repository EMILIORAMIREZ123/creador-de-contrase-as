import random

patron = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
longitud = int(input("de cuantos caracteres quieres que sea la contraseña:  "))
contraseña = ""

for i in range(longitud):
    contraseña += random.choice(patron)
print(contraseña)