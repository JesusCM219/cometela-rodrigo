from Funciones import nuevo_Tema, nuevo_subtema

print("hola mundo mi nombre es 'David'")
print('saludos') 

def error():
    fjvbjebfvuisdngvkjnskjbgttr

def factorial(n):
    if (n == 0 or n == 1):
         return 1
    else:
        return n *  factorial(n - 1)
numero = 500
print ("factorial de", numero, "es", factorial(numero))


nuevo_Tema("variables")
edad = 27
print("edad:", edad)

Altura = 1.70
print("Altura:", Altura)

nombre = "Jesus"
print("nombre:", nombre)

es_trabajador = True
print("es_trabajador:", es_trabajador)

nuevo_Tema("listas")

frutas = ["manzanas", "peras", "piñas","naranjas", "guayabas", "papayas"]
print("frutas:", frutas)

varias_cosas = ["Escuela", 23, True, frutas]
print("varias_cosas:", varias_cosas)

"""
   Seleccionando un elemento
   Comentario de multiples lineas
"""
print("frutas[2]: ", frutas[2])

print("frutas[-1]: ", frutas[-1])
print("frutas[-2]: ", frutas[-2])

print("frutas[1:5]: ", frutas[1:5])
print("frutas[1:5:2]: ", frutas[1:5:2])

# agregando un elemento al final
frutas.append("fresas")
print("frutas:", frutas)
# quitando un elemnto
frutas.remove("naranjas")
print("frutas", frutas)
# insertando un elemnto en la posicion descrita
frutas.insert(1, "kiwi")
print("frutas", frutas)

# creando una lista vacia
calificaciones = []
libros = []
print("calificaciones: ", calificaciones)
print("libros: ", libros)

frutas.reverse()
print("frutas: ", frutas)

frutas.sort()
print("frutas: ", frutas)

nuevo_Tema("diccionarios")
persona={"nombre":"pedro", "apellido":"perez","edad":48, "estatura":1.70,"hijos":["casimira", "bryan","eliud"]}

print('persona:', persona)

print("persona.keys():" , persona.keys())
print("persona.values():" , persona.values())

print('persona.get("nombre):', persona.get("nombre"))
print('persona.get("estatura"):' , persona.get("estatura")) 

print("persona.items():" , persona.items())

nuevo_Tema("Ciclos")
nuevo_subtema("for")
for i in range(10):
    print(i)
    
print("########")
for i in range(3,10):
    print(i)
    
print("########")
for i in range(3,10,2):
    print(i)
    
print("len(frutas):", len(frutas))

for f in frutas:
    print(f)
    
for indice in range(len(frutas)):
    print("indice", indice, frutas[indice])
        
for key, value in persona.items():
    print(key,value)
    
