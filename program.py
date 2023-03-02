import fileinput

# This function reads the file and returns a list with the lines
lines = []
for line in fileinput.input():
    lines.append(line)

def determinar_tipo_numero(cadena):
    try:
        numero = int(cadena)
        return "Entero"
    except ValueError:
        try:
            numero = float(cadena)
            return "Flotante"
        except ValueError:
            return "No es un número válido"

def sumar_numeros(lista):
    suma = 0
    for numero in lista:
        if determinar_tipo_numero(numero) == "Entero":
            suma += int(numero)
        elif determinar_tipo_numero(numero) == "Flotante":
            suma += float(numero)
    return suma

print(sumar_numeros(lines))
