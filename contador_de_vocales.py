palabra = input("ingrese una palabra: ").lower()
contador_vocales = 0
for letra in palabra:
    if letra == "a" or letra == "e" or letra == "i" or letra == "o" or letra == "u":
        contador_vocales += 1
print("la cantidad de vocales en la palabra es:", contador_vocales)