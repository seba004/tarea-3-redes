

grafo_tarea=[['a','b',1],['a','g',4],['a','i',10],['b','c',9],['b','a',1],['b','e',8],['c','b',9],['c','d',2],['d','c',2],['d','f',4],['d','e',9],['d','i',2],['e','b',8],['e','f',2],['e','d',9],['e','i',1],['f','d',4],['f','e',2],['f','h',6],['g','a',4],['g','h',7],['h','g',7],['h','f',6],['h','i',3],['i','h',3],['i','e',1],['i','d',2],['i','a',10]]

lista_nodos=['a','b','c','d','e','f','g','h','i']




class nodo ():

    def __init__(self, nombre):
        self.nombre=nombre

        self.conexion1=[self.nombre,'a',0]
        self.conexion2=[self.nombre,'b',0]
        self.conexion3=[self.nombre,'c',0]
        self.conexion4=[self.nombre,'d',0]
        self.conexion5=[self.nombre,'e',0]
        self.conexion6=[self.nombre,'f',0]
        self.conexion7=[self.nombre,'g',0]
        self.conexion8=[self.nombre,'h',0]
        self.conexion9=[self.nombre,'i',0]


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
    for i in range(0,28):
        primer=grafo_tarea[i]#se asigna las sublista del grafo
        n_salida=primer[0]#se obtiene el nodo de salida

        if n_salida==nodo.nombre:#se iguala nodao salida grafo con nodo de tabla
            n_llegada=primer[1]#se obtien numero de llegada


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


def obtener_lista_conexion(nodo):
    lista_conexiones=[]
    lista_conexiones.append(nodo.conexion1)
    lista_conexiones.append(nodo.conexion2)
    lista_conexiones.append(nodo.conexion3)
    lista_conexiones.append(nodo.conexion4)
    lista_conexiones.append(nodo.conexion5)
    lista_conexiones.append(nodo.conexion6)
    lista_conexiones.append(nodo.conexion7)
    lista_conexiones.append(nodo.conexion8)
    lista_conexiones.append(nodo.conexion9)
    return lista_conexiones


def compatibilidad (lista1, lista2):
    if lista1[0]==lista2[0]:
        return False
    else:
        return True

def comprobar_peso(nodo,punto_final,suma):
    lista_nodal=obtener_lista_conexion(nodo)
    for i in range(0,9):
        lista_seleccionada=lista_nodal[i]
        if lista_seleccionada[1]==punto_final:
            suma_encontrada=lista_seleccionada[2]
            if suma_encontrada ==0:
                return True
            if suma_encontrada > suma :
                return True
            else:
                return False

def cambiar_valor(nodo, punto_final,suma):
    lista_nodal=obtener_lista_conexion(nodo)
    contador=1
    for i in range(0,9):
        lista_seleccionada=lista_nodal[i]
        if lista_seleccionada[1]==punto_final:
            if contador==1:
                nodo.conexion1[2]=suma
            if contador==2:
                nodo.conexion2[2]=suma
            if contador==3:
                nodo.conexion3[2]=suma
            if contador==4:
                nodo.conexion4[2]=suma
            if contador==5:
                nodo.conexion5[2]=suma
            if contador==6:
                nodo.conexion6[2]=suma
            if contador==7:
                nodo.conexion7[2]=suma
            if contador==8:
                nodo.conexion8[2]=suma
            if contador==9:
                nodo.conexion9[2]=suma

        contador=contador+1

def compartir(nodo,nodo2):#nodo= nodo que recbe tabla  y nodo2 el nodo que envia tabla
    lista_conexion_nodo_local=obtener_lista_conexion(nodo)

    lista_recividos=obtener_lista_conexion(nodo2)
    comp=compatibilidad(lista_conexion_nodo_local[0],lista_recividos[0])

    if comp == True:
        for i in range(0,9):
            for j in range(0,9):
                seccion_local_elegido=lista_conexion_nodo_local[i]

                seccion_visita_elegido=lista_recividos[j]

                if seccion_local_elegido[1]==seccion_visita_elegido[0] and seccion_local_elegido[2]!=0 and seccion_visita_elegido[2]!=0:
                    if seccion_local_elegido[0]!=seccion_visita_elegido[1]:
                        suma_puntos=seccion_local_elegido[2]+seccion_visita_elegido[2]
                        check=comprobar_peso(nodo,seccion_visita_elegido[1],suma_puntos)
                        if check==True:
                            cambiar_valor(nodo,seccion_visita_elegido[1],suma_puntos)





def algoritmo():
    compartir(nodoa,nodoi)
    compartir(nodoa,nodob)
    compartir(nodoa,nodog)

    compartir(nodob,nodoc)
    compartir(nodob,nodoa)
    compartir(nodob,nodoe)

    compartir(nodoc,nodod)
    compartir(nodoc,nodob)

    compartir(nodod,nodoi)
    compartir(nodod,nodoe)
    compartir(nodod,nodof)

    compartir(nodoe,nodoi)
    compartir(nodoe,nodod)
    compartir(nodoe,nodob)
    compartir(nodoe,nodof)

    compartir(nodof,nodod)
    compartir(nodof,nodoe)
    compartir(nodof,nodoh)

    compartir(nodog,nodoa)
    compartir(nodog,nodoh)

    compartir(nodoh,nodog)
    compartir(nodoh,nodoi)
    compartir(nodoh,nodof)

    compartir(nodoi,nodoa)
    compartir(nodoi,nodod)
    compartir(nodoi,nodoe)
    compartir(nodoi,nodoh)

def impresion(nodo):
    lista_a=obtener_lista_conexion(nodo)
    fichero =open('routers.txt','a')
    fichero.write("\n")
    fichero.write("----------------|\n")
    fichero.write('Nodo '+ nodo.nombre+'\t\t|\n')
    fichero.write("----------------|\n")
    for i in range(0,9):
        sublista_a=lista_a[i]
        fichero.write(sublista_a[0])
        fichero.write(" -> ")
        fichero.write(sublista_a[1])
        fichero.write(" = ")
        fichero.write(str(sublista_a[2])+"\t|\n")
    fichero.write("----------------|\n")

    fichero.close()

primera_iteracion()
for i in range (0,7):
    algoritmo()


impresion(nodoa)
impresion(nodob)
impresion(nodoc)
impresion(nodod)
impresion(nodoe)
impresion(nodof)
impresion(nodog)
impresion(nodoh)
impresion(nodoi)

