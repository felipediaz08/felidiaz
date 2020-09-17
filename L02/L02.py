#!/usr/bin/env python
# coding: utf-8

# In[149]:



def numero_espadas(mapa):
    mapa = mapa.lower()
    cantidad = len(mapa)
    impares = 1
    pares = 0
    contador = 0
    for letra in mapa:
        stack.append(letra)
    while impares < cantidad:
        bestias.append(stack[impares])
        impares += 2
    while pares < cantidad:
        espadas.append(stack[pares])
        pares += 2
    for bestia in bestias:
        if bestia in espadas and espadas.index(bestia) <= bestias.index(bestia):
            espadas.insert(espadas.index(bestia),"")
            espadas.remove(bestia)
            bestias.insert(bestias.index(bestia),"")
            bestias.remove(bestia)
            
        else:
            contador += 1 
            bestias.insert(bestias.index(bestia),"")
            bestias.remove(bestia)
    return contador


# In[192]:



class Node:                                        ##clase obtenida de https://medium.com/@nicholas.w.swift/easy-a-star-pathfinding-7e6689c7f7b2

    def __init__(self, parent, posicion):          #funcion de inicializacion, donde le da atributo padre, de donde
        self.parent = parent                         #proviene, y posicion
        self.posicion = posicion
        
        self.g = 0                                 #tambien los valores para usar el A*
        self.h = 0
        self.f = self.g + self.h
        self.altura = 0

    
def encontrar_vecinos(mapa, actual, padre):
    lista_vecinos = []
    for mov in [(0, -1), (0, 1), (-1, 0), (1, 0), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
        pos_vecino = (actual[0] + mov[0], actual[1] + mov[1])
        if  pos_vecino[0] in range(0,len(mapa)-1) and pos_vecino[1] in range(0,len(mapa[0])-1) and pos_vecino != padre:
            lista_vecinos.append(pos_vecino)        
    return lista_vecinos

def min_f(lista):
    f_min = lista[0]
    for i in range(1,len(lista)):
        if lista[i] < f_min:
            f_min = lista[i]
    return f_min

def min_g(lista):
    g_min = lista[0]
    for i in range(1,len(lista)):
        if lista[i] < g_min:
            g_min = lista[i]
    return g_min

##Algortimo A* hecho a base del pseudocodigo del syllabus
def AStar(inicio, fin, mapa):
    
    origen = Node(None, inicio)
    origen.g = origen.h = origen.f = 0  
    origen.altura = mapa[origen.posicion[0]][origen.posicion[1]]
    destino = Node(None, fin)
    destino.altura = mapa[destino.posicion[0]][destino.posicion[1]]
    destino.f = 0
    lista_abierta = []
    lista_cerrada = []
    nodo_actual = origen
    lista_abierta.append(nodo_actual)
    lista_efes = []
    
    while nodo_actual.posicion != destino.posicion:
        
        lista_efes = []
        if len(lista_abierta) > 0:
            for feli in lista_abierta:
                lista_efes.append(feli.f)
            f_maschico = min_f(lista_efes)
            lugar = lista_efes.index(f_maschico)
        
            nodo_actual = lista_abierta[lugar]
            lista_abierta.remove(nodo_actual)                                                    #se elimina el nodo actual para añadirlo a la lista con nodos ya     
        
        if nodo_actual.posicion == destino.posicion:                   #pseudocodigo syllabus
            return lista_cerrada
        
        else:
            if nodo_actual.posicion not in lista_cerrada:
                lista_cerrada.append(nodo_actual.posicion)
            nodos_vecinos = []
            papito = nodo_actual.parent
            if nodo_actual.parent != None:
                antecesor = papito.posicion
            else:
                antecesor = ()
            vecinos = encontrar_vecinos(mapa,nodo_actual.posicion, antecesor)      #####
            for hermano in vecinos:
                if hermano == destino.posicion:
                    lista_cerrada.append(hermano)
                    return lista_cerrada
                
                elif hermano not in lista_cerrada:
                    hermano = Node(nodo_actual,hermano)
                    hermano.altura = mapa[hermano.posicion[0]][hermano.posicion[1]]
                    
                    if hermano.altura > nodo_actual.altura:
                        hermano.g = nodo_actual.g + hermano.altura - nodo_actual.altura + 1
                    else:
                        hermano.g = nodo_actual.g + 1
            
                    hermano.h = ((hermano.posicion[0] - destino.posicion[0]) ** 2) + ((hermano.posicion[1] - destino.posicion[1]) ** 2)
                    hermano.f = hermano.g + hermano.h
                    if hermano.posicion not in lista_cerrada:
                        nodos_vecinos.append(hermano)
                        
                    if len(nodos_vecinos) > 0:    
                        ges_vecinos = []
                        for gino in nodos_vecinos:
                            ges_vecinos.append(gino.g)
                        g_maschico = min_g(ges_vecinos)
                
            for vecino in nodos_vecinos:
                
                if vecino.g < nodo_actual.g and vecino.posicion in lista_cerrada:
                    vecino.g = g_maschico
                    vecino.parent = nodo_actual
                    
                elif nodo_actual.g < vecino.g and vecino in lista_abierta:
                    vecino.g = g_maschico
                    vecino.parent = nodo_actual
                    if vecino not in lista_abierta:
                        lista_abierta.append(vecino)
                else:
                    lista_abierta.append(vecino)


def ruta_de_jaime(inicio,fin,mapa):
    comienzo = Node(None,inicio)
    termino = Node(None,fin)
    mapa = mapa
    ruta_minima = AStar(comienzo.posicion,termino.posicion,mapa)
    return ruta_minima


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




