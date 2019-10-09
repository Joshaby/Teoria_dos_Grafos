from grafo import *
import time

#g_p = Grafo(['J', 'C', 'E', 'P'], {'a1':'J-C', 'a3':'E-J', 'a4':'J-P', 'a6':'E-C', 'a7':'C-P', 'a8':'P-E'})

g_p = Grafo(['A', 'B', 'C', 'D', 'E', 'F', 'H', 'G'], {'a1':'A-E', 'a2' : 'A-F', 'a3':'F-H', 'a4':'H-G', 'a5' : 'G-F', 'a6':'A-B', 'a7':'B-C', 'a8':'B-D'})

print(g_p.startHACILO())

ex_vertices = ['A', 'B', 'C', 'D', 'E',
               'F', 'G', 'H', 'I', 'J',
               'K']
ex_arestas = {
    '1': 'A-B', '2': 'A-G', '3': 'A-J', '4': 'G-K',
    '5': 'K-J', '6': 'J-G', '7': 'J-I', '8': 'I-G',
    '9': 'G-H', '10': 'H-F', '11': 'F-B', '12': 'G-B',
    '13': 'B-C', '14': 'C-D', '15': 'E-D', '16': 'B-D',
    '17': 'B-E'
}

grafo_ex = Grafo(ex_vertices, ex_arestas)
