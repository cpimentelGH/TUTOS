## 01. Imprimir un texto en pantalla ##
>>> print("Hello World")
Hello World
>>> print('Hello World')
Hello World
>>> print('She said "Hello World"')
She said "Hello World"

>>> ## 02. Almacenamiento de secuencias en variables ##
>>> ## guarda una secuencia corta de DNA en la variable my_dna ##
>>> my_dna = "ATGCGTA"
>>> print (my_dna)
ATGCGTA
>>> my_dna
'ATGCGTA'

>>> ## 03. Herramientas para manipular cadenas ##
>>> # Concatenación #
>>> my_dna2 = "AATT" + "GGCC"
>>> print my_dna2
AATTGGCC

>>> # Ahora juntemos variables que contienen una cadena y cadenas que no están en una variable #
>>> upstream = "AAA"
>>> downstream = "GGG"
>>> my_dna3 = upstream + "ATGC" + downstream
>>> # Now the DNA string has to be AAA ATGC GGG all together. #
>>> print(my_dna3)
AAAATGCGGG

# Encontrar la longitud de una secuencia #
>>> dna_lenght = len("AGTC")
>>> print(dna_lenght)
4
>>> len("AGTC")
4

## Ejercicio para poner en práctica lo leído hasta el momento ##
>>> # Guarda la secuencia en una variable #
>>> my_dna = "ATGCGAGT"
>>> # Calcula la longitud de la secuencia y guárdala como una variable #
>>> dna_lenght = len(my_dna)
>>> # Imprime un mensaje que diga cuál es la longitud de la secuencia de DNA #
>>> print("La longitud de la secuencia de DNA es" + dna_length)
# Te habrás dado cuénta que arroja un error y eso es porque secuencias de letras, símbolos y espacios no pueden ir unidas con <+> a números por lo que necesitarás la función <str()> dentro de la función <print()>
print('La longitud de la secuencia de DNA es ' + str(dna_lenght))
La longitud de la secuencia de DNA es 8
# Poner a prueba la función int( ) #
>>> número = 3 +int('4')
>>> print(número)
7

# Reemplazamiento #

#

