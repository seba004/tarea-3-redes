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

grafo_tarea=[['a','b',1],['a','g',4],['a','i',10],['b','c',9],['b','a',1],['b','e',8],['c','b',9],['c','d',2],['d','f',4],['d','e',9],['d','i',2],['e','b',8],['e','f',2],['e','i',1],['f','d',4],['f','e',2],['f','h',6],['g','a',],['g','h',7],['h','g',7],['h','f',6],['h','i',3],['i','h',3],['i','e',1],['i','d',2],['i','a',10]]

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
nodoc=nodo(lista_nodos[3])
nodod=nodo(lista_nodos[3])
nodoe=nodo(lista_nodos[4])
nodof=nodo(lista_nodos[5])
nodog=nodo(lista_nodos[6])
nodoh=nodo(lista_nodos[7])
nodoi=nodo(lista_nodos[8])









