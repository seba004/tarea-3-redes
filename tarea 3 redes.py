#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      seba
#
# Created:     15-06-2014
# Copyright:   (c) seba 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

grafo_tarea=[['a','b',1],['a','g',4],['a','i',10],['b','c',9],['b','a',1],['b','e',8],['c','b',9],['c','d',2],['d','f',4],['d','e',9],['d','i',2],['e','b',8],['e','f',2],['e','i',1],['f','d',4],['f','e',2],['f','h',6],['g','a',4],['g','h',7],['h','g',7],['h','f',6],['h','i',3],['i','h',3],['i','e',1],['i','d',2],['i','a',10]]

lista_nodos=['a','b','c','d','e','f','g','h','i']




class nodo ():

    def __init__(self, nombre):
        self.nombre=nombre

        self.conexion1=[self.nombre,'a',None]
        self.conexion2=[self.nombre,'b',None]
        self.conexion3=[self.nombre,'c',None]
        self.conexion4=[self.nombre,'d',None]
        self.conexion5=[self.nombre,'e',None]
        self.conexion6=[self.nombre,'f',None]
        self.conexion7=[self.nombre,'g',None]
        self.conexion8=[self.nombre,'h',None]
        self.conexion9=[self.nombre,'i',None]


nodoa=nodo(lista_nodos[0])
nodob=nodo(lista_nodos[1])
nodoc=nodo(lista_nodos[2])
nodod=nodo(lista_nodos[3])
nodoe=nodo(lista_nodos[4])
nodof=nodo(lista_nodos[5])
nodog=nodo(lista_nodos[6])
nodoh=nodo(lista_nodos[7])
nodoi=nodo(lista_nodos[8])


def primera_asiganacion(nodo):
    for i in range(0,26):
        primer=grafo_tarea[i]#se asigna las sublista del grafo
        n_salida=primer[0]#se obtiene el nodo de salida

        if n_salida==nodo.nombre:#se iguala nodao salida grafo con nodo de tabla
            n_llegada=primer[1]#se obtien numero de llegada


            print("nombre nodo:")
            print(nodo.nombre)
            print("salida grafo")
            print(n_salida)
            print("gain")


            vector_tabla_a=nodo.conexion1#se obtiene vecor de a
            if n_llegada==vector_tabla_a[1]:#se compara  los valores
                nodo.conexion1[2]=primer[2]#se da valor a tabla

            vector_tabla_b=nodo.conexion2
            if n_llegada==vector_tabla_b[1]:
                nodo.conexion2[2]=primer[2]

            vector_tabla_c=nodo.conexion3
            if n_llegada==vector_tabla_c[1]:
                nodo.conexion3[2]=primer[2]

            vector_tabla_d=nodo.conexion4
            if n_llegada==vector_tabla_d[1]:
                nodo.conexion4[2]=primer[2]

            vector_tabla_e=nodo.conexion5
            if n_llegada==vector_tabla_e[1]:
                nodo.conexion5[2]=primer[2]

            vector_tabla_f=nodo.conexion6
            if n_llegada==vector_tabla_f[1]:
                nodo.conexion6[2]=primer[2]

            vector_tabla_g=nodo.conexion7
            if n_llegada==vector_tabla_g[1]:
                nodo.conexion7[2]=primer[2]

            vector_tabla_h=nodo.conexion8
            if n_llegada==vector_tabla_h[1]:
                nodo.conexion8[2]=primer[2]

            vector_tabla_i=nodo.conexion9
            if n_llegada==vector_tabla_i[1]:
                nodo.conexion9[2]=primer[2]

def primera_iteracion ():
    primera_asiganacion(nodoa)
    primera_asiganacion(nodob)
    primera_asiganacion(nodoc)
    primera_asiganacion(nodod)
    primera_asiganacion(nodoe)
    primera_asiganacion(nodof)
    primera_asiganacion(nodog)
    primera_asiganacion(nodoh)
    primera_asiganacion(nodoi)







