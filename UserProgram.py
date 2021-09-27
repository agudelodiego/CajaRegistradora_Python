'''Este archivo estara dedicado a la escritura del codigo del programa de usuario, el cual se encargara de intuar con el usuario, ademas de que sera el que creara y manipulara las instancias de clases, en pocas palabras, es el puente entre el usuario y los modulos del programa

REALIZADP POR: Diego Alexander Agudelo Garcia'''


#Importacion de modulos necesario
from io import open_code
from Producto import *
from Orden import *


lista_prodcutos=[]
#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
#FUNCION ENCARGADA DE INSTACIAR LOS PRODUCTOS AGREGADOR POR EL USUAIRO
def instanciar(producto):

    instancia_producto=nuevo_producto(producto)
    return instancia_producto.producto

#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
#FUNCION ENCARGADA DE CREAR UNA LISTA DE PRODUCTOS
def agregar(producto):

    global lista_prodcutos
    lista_prodcutos.append(producto)
    print('')
    print(f'Producto {producto} fue agregado con exito')

#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
#FUNCION ENCARGADA DE EFECTUAR LA COMPRAR
def terminar():

    if len(lista_prodcutos) > 0:

        factura=nueva_orden(lista_prodcutos)
        factura.info()

    else:

        print('Compra finalizada, gracias por utilizar nuestro sistema')

#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################


#PROGRAMA DE USUAIRO 
while True:

    pregunta=input('Bienvenido a la caja registradora, que accion desea ejecutar ? comprar o salir: ')

    if pregunta == 'salir':

        break

    elif pregunta == 'comprar':

        print('''
        ***************Bienvenido al programa de caja resigtradora***************
        ''')

        while True:

            UsrData=input('Introduzca el ID del producto selccionado: ')

            #Instanciamos el producto
            producto=instanciar(UsrData)

            if producto == False:

                continue
            
            else:

                opcion=input('Que desea hacer ?. agregar y continuar(A), continuar sin agregar(B), agregar y terminar compra(C), terminar sin agregar(D): ')

                if opcion == 'B':

                    continue

                elif opcion == 'A':

                    agregar(producto)
                
                elif opcion == 'C':
                    
                    agregar(producto)
                    terminar()
                    lista_prodcutos.clear()
                    break
                    
                elif opcion == 'D':

                    terminar()
                    lista_prodcutos.clear()
                    break

    else:

        print('El programa no reconoce el comando ingresado, por favor vuelca a intentarlo')


print('''
GRACIAS POR UTILZAR NUESTRO PROGRAMA
''')