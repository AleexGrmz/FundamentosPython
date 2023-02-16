def nuevoTema ( tema ):
    print (" \n------ ", tema, " ------\n ")
    #segmento de bloque vacio = pass 

nuevoTema ("OPERADORES ARITMETICOS")
print (" Operador division entera ( 10 // 3 ): ", 10 // 3 )
print (" Operador potencia ( 5 ** 3 ): ", 5 ** 3 )

#  **ACTIVIDAD**
# Imprimir la tabla de verdad de los operadores logicos.

nuevoTema ("OPERADORES lOGICOS")
nuevoTema("Operador and")
print ("Operador and ( True and True ): ", True and True )
print ("Operador and ( True and False ): ", True and False )
print ("Operador and ( False and True ): ", False and True )
print ("Operador and ( False and False ): ", False and False )

nuevoTema("Operador not")
print ("Operador not ( not False = True ): ", not False )
print ("Operador not ( not True = False ): ", not True )

nuevoTema("Operador or")
print ("Operador or ( True or True ): ", True or True )
print ("Operador or ( True or False ): ", True or False )
print ("Operador or ( False or True ): ", False or True )
print ("Operador or ( False or False ): ", False or False )

nuevoTema ("OPERADORES DE COMPARACION")
print (" 2 == 3: ", 2 == 3 )
print (" 2 < 3: ", 2 < 3 )
print (" 2 > 3: ", 2 > 3 )
print (" 2 <= 3: ", 2 <= 3 )
print (" 2 >= 3: ", 2 >= 3 )
print (" 2 != 3: ", 2 != 3 )

nuevoTema ("VARIABLES")
variable1 = 10
_variable2 = 6.2
dosPalabras = "Hello"
a, b, c = 10, 5.5, "palabra"
print ( variable1, _variable2, dosPalabras)
print(a, b, c)

nuevoTema("ENTEROS")
z = 12
y = 123456789
x = -11
w = 0b1010101
v = 0xffa
print ( z, type(z) )
print ( y, type(y) )
print ( x, type(x) )
print ( w, type(w) )
print ( v, type(v) )

nuevoTema("FLOTANTES")
x = 12.12
y = 0.01
print ( x, type(x) )
print ( y, type(y) )

nuevoTema("NUMEROS COMPLEJOS")
x = -11j
y = 1j
z = 1+1j
print ( x, type(x) )
print ( y, type(y) )
print ( z, type(z) )

nuevoTema("BOOLEANO")
lis = [8]
t = ()
num = 77
# val = none     <- none = null
print (lis, "es", bool(lis))
print (t, "es", bool(t))
print (num, "es", bool(num))
# print (val, "es", bool(val))

nuevoTema("LISTAS")  #no son array's
a = [10, 10.5, "python list"]
print (a)
print (a[1])
a[0] = "Hola" # <- para cambiar valor en una lista

nuevoTema("TUPLA")  # <- Protegidos. no se pueden modificar
t = (11, "tupla", 1+1j)
print (t)
print (t[1])
print ("t[0:2]", t[0:2]) 

nuevoTema("SETS")
x = {50, 40, 30, 20, 10, 10}
print ("Conjunto x: ", x, type(x))

nuevoTema("DICCIONARIO")
d = {1: "Valor1", "Valor2" :2j }
print (d, type(d))
print ("d:[valor2]:", d["Valor2"])

nuevoTema("CADENAS")
cadena1 = "cadena con comillas dobles"
cadena2 = 'cadena con comillas simples'
cadenaMultilinea = ''' Esta cadena es de varias
lineas,  tabulares    y   saltos'''

print (cadena1, type(cadena1))
print (cadena2, type(cadena2))
print (cadenaMultilinea, type(cadenaMultilinea))
print ("Segmentacion de cadena")
print (cadena1[5:11]) 
print (cadena1[:5])
print (cadena1[7:])
print (cadena1[-8:-1])
print (cadena1[0:18:1])
print (cadena1[0:18:2])
print (cadena1[0:18:3])

cadena1 = "Hello"
cadena4 =  (cadena1 + " ") * 5
print (cadena4)
cadena5 = cadena4.upper()
print (cadena5)

