'''El presente archivo esta dedicado para el desarrollo de una parte del codigo de un programa de caja registradora y generadora de facturas, mas concretamente, en este archivo se encuentra el diseño de la clase nuevo_producto. A la hora de realizar el instanciamiento de la clase se le debe de pasar como parametro el ID del producto dentro de la base de datos, la cual se encuentra simlada como un simple diccionario de python. Una vez realizdo ello, la clase misma se encargara de verificar si el producto existe dentro de la base de dato o no, si el producto existe se creara una variable cuyo valor sera un diccionario con el nombre del producto y su precio correspondiente


CODIGO REALIZADO POR: Diego Alexander Agudelo Garcia
'''


#BASE DE DATOS PRODUCTO
PRODUCTOS={
    'a01' : {'nombre':'papas fritas','precio':1200},
    'bj2' : {'nombre':'doritos pequeños','precio':1200},
    'j45' : {'nombre':'jugo de mango','precio':2000},
    'a45' : {'nombre':'hamburguesa','precio':25000},
    'm23' : {'nombre':'pizza de peperoni','precio':19000},
    'k2f' : {'nombre':'guaro(tapetusa)','precio':50000},
    't32' : {'nombre':'frijoles con cilantro salvaje','precio':40000}
}


#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
#CLASE PRODCUTOS
class nuevo_producto:

    #*************CONSTRUCTOR*****************
    def __init__(self,id):
        self._id=id
        self._producto=self.verificar()
    #*****************************************


    #*************VERIFICAR_ID*************
    def verificar(self):

        Coincidencias = False

        if self._id in PRODUCTOS.keys():

            #Actualizamos el valor de la variable coincidencias
            Coincidencias=True

            #Almacenamos el producto en un diccionario de manera temporal
            Contenedor=dict(PRODUCTOS[self._id])

            #Mostrar la coincidencia
            print(f'''
                ******************INFORMACION DEL PRODUCTO*******************
                Producto encontrado en la base de datos
                ------------------------------------------
                NOMBRE: {Contenedor['nombre']}
                PRECIIO: {Contenedor['precio']} $
                *************************************************************
            ''')
            return Contenedor

        else:
            
            #Actualizamos coincidencias
            Coincidencias=False

            #Mostrar mensaje de error
            print('''
                *************************************************************
                El producto especificado no fue encontrado en l base de datos
                por favor intentelo de nuevo
                *************************************************************
            ''')
            return Coincidencias
    #**************************************


    #**************GET ID******************
    @property
    def id(self):
        return self._id
    #**************************************


    #************GET PRODUCTO*************
    @property
    def producto(self):
        return self._producto
    #************************************
#####################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################


#! Enntorno de pruebas de clase
if __name__ == '__main__':

    #COMO INSTANCIAR CLASES:
    #nombreObjeto = nuevo_producto(parametros)
    #Como parametro se le debe de pasar el identifador del producto dentro de la base de datos
    ejemplo = nuevo_producto('a45')



    #ACCESO AL ID DEL PRODUCTO
    #Se logra mediante el metodo .id el cual devuelve el id del prodcuto dentro de la base de datos 
    #!  EL ID DE UN PRODUCTO ES UNA PROPIEDAD DE SOLO LECTURA
    idProducto = ejemplo.id
    print("     El id del producto es -->",idProducto)

    
    #ACCEDER A LA INFORMACION DE UN PRODUCTO
    #Se logra usando el metodo .producto, el cual devuelve una lista con el nombre y el precio del producto en caso de que este exista. Si el producto no se encuenctra registrado en la base de datos este metodo retornara un False
    #!  TAMBIEN ES UN ATRIBUTO DE SOLO LECTURA
    infoProducto = ejemplo.producto
    print("     Informacion del producto",infoProducto)