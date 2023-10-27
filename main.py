print("Hola Mundo")
print("Hola Mundo2!!")
print("Hola Mundo3!!")

"""



"""

texto = "Repaso de Phyton con Marc"

nombre = "Marc Reylan"

altura = "187cm" # FALSO, mido 172-3 cm

year = "2006"


print(f"{texto} - {nombre} - {altura} - {str(year)}")
print(texto + " - " + nombre + " - " + altura + " - " + str(year))

# Entrada

sitioweb = input("¿Cuál es tu página web?")
print("El sitio web del usuario es:" + sitioweb)

# Condiciones

""""

altura = input("¿Cuál es tu altura?: ")

if altura >= 180:
    print=("Eres una persona alta")
else:
    print("Eres BAJITO")

"""
"""""
# Funciones
var_altura = int(input("¿Cuá es tu altura?: "))

def mostrarAltura(altura):
    resultado = ""

    if altura >= 180:
        resultado = "Eres una persona alta!!"
    else:
        resultado = "Eres BAJITO!!"
    
    return resultado

print(mostrarAltura(var_altura))
"""""

# Listas

personas = ["Tobias", "Alfredo", "All Might"]

print(personas[2])

for persona in personas:
    print("-" + persona)


