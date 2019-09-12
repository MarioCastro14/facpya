mensaje= (str(input("¿Que palabra deseas saber si es palidromo?:\n")))

mensajesinespacios= mensaje.replace(" ",""), mensaje.upper()


reves = mensaje[::-1]

palidromo= mensajesinespacios

print ("El mensaje al revés es:")
print(reves)

if mensajesinespacios == palidromo:
    print("La palabra si es palidromo")
else:
    print("la palabra no es palidromo")
