# -*- coding: utf-8 -*-
"""Mi_red

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LAiopT3sNbvzKCVDA1OBd6asaWy-MntW
"""

#Hola, para empezar con nuestro proyecto de red social, vamos a utilizar
#las herramientas que conocemos para ejecutar algunas acciones.
#
#Primero, mostraremos un mensaje en pantalla dando la bienvenida al usuario
#y escribiendo el nombre de la red.

#A continuacion preguntaremos algunos datos al usuario para poder construir su perfil,
#y guardaremos esta informacion en variables.

#Finalmente, escribiremos en pantalla todos los datos que hemos recolectado, y permitiremos
#al usuario escribir un mensaje de estado.

#Te invito a examinar el codigo, leer los comentarios y comprender los tipos de datos
#que estamos utilizando en cada caso.


#Para conocer un poco mÃ¡s del usuario, vamos a preguntarle algunos datos.
#Por ejemplo, su aÃ±o de nacimiento, y aprovecharemos este dato descubrir la edad del usuario.
#a.¿Como lo haremos?, usaremos una variable para guardar el resultado del calculo de
#la edad del usuario. Este es un dato de tipo entero.

#A continuacion le preguntaremos al usuario su estatura en metros. Este es un dato de tipo float,
#y usaremos esta informacion para calcular los centimetros

#Finalmente escribiremos en pantalla los datos que hemos recordado del usuario usando print y le solicitaremos
#que escriba un mensaje para desplegar en pantalla.

############################################################
# Lo primero que haremos sera¡ escribir un mensaje de bienvenida al usuario
# con el nombre de la red. Puedes modificar este mensajes para que represente el nombre de tu propia red
# Considera que al escribir """ tambien estamos delimitado un string, pero al hacerlo de esta manera,
# cambios de li­nea que ocurran en el codigo se consideraran como parte del string.
# Si no estas convencido, prueba el funcionamiento reemplazando los delimitadores por "

print("Bienvenido a ... ")
print("""
              _                  __
   ____ ___  (_)  ________  ____/ /
  / __ `__ \/ /  / ___/ _ \/ __  /
 / / / / / / /  / /  /  __/ /_/ /
/_/ /_/ /_/_/  /_/   \___/\__,_/

""")

#Primera interaccion. Solicitamos al usuario que ingrese su nombre,
#y lo guardamos en una variable de tipo str
nombre = input("Para empezar, dime como te llamas. ")
print()
print("Hola ", nombre, ", bienvenido a Mi Red")
print()

#Segunda interaccion. Solicitamos el ingreso del año, y utilizamos este
#dato para estimar la edad de la persona. a.¿Por que decimos que solo estamos "estimando" su edad?
#b.¿Que ocurre si eliminamos la conversion a tipo de dato 'int' de la siguiente li­nea?
agno = int(input("Para preparar tu perfil, dime en que año naciste. "))
edad = 2023-agno-1
print()

#Tercera interaccion. Solicitamos la estatura, medida en metros.
#Utilizamos la conversion a 'int', y una expresion para convertir esto
#a una medida en metros y centÃ­metros
estatura = float(input("Cuentame mas de ti, para agregarlo a tu perfil. a.¿Cuanto mides? Damelo en metros. "))
estatura_m = int(estatura)
estatura_cm = int( (estatura - estatura_m)*100 )

#Cuarta interaccion. Consultamos cuantos amigos tiene el usuario.
num_amigos = int(input("Muy bien. Finalmente, cuantame cuantos amigos tienes. "))

#Con los datos recolectados escribimos en pantalla un texto que resuma los datos que hemos obtenido
print()
print("Muy bien,", nombre, ". Entonces podemos crear un perfil con estos datos.")
print("--------------------------------------------------")
print("Nombre:  ", nombre)
print("Edad:    ", edad, "años")
print("Estatura:", estatura_m, "metros y", estatura_cm, "centi­metros")
print("Amigos:  ", num_amigos)
print("--------------------------------------------------")
print("Gracias por la informacion. Esperamos que disfrutes con Mi Red")
print()

#Finalmente, solicitamos un mensaje de prueba que sirva para publicar un estado del usuario.
mensaje = input("Ahora vamos a publicar tu primer mensaje. a.¿Que piensas hoy? ")
print()
print("--------------------------------------------------")
print(nombre, "dice:", mensaje)
print("--------------------------------------------------")

# Solicitar datos al usuario
sexo = input("Ingrese su sexo: ")
numero_telefono = input("Ingrese su número de teléfono: ")
ciudad = input("Ingrese la ciudad donde vive: ")

# Mostrar los datos ingresados por el usuario
print("Datos ingresados por el usuario:")
print("Sexo:", sexo)
print("Número de teléfono:", numero_telefono)
print("Ciudad:", ciudad)