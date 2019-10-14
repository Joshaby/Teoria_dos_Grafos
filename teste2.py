from grafo_adj_dir import *

g_p2 = Grafo(['A', 'B', 'C', 'E', 'D', 'H', 'G', 'F'])
g_p2.adicionaAresta('B-A')
g_p2.adicionaAresta('A-H')
g_p2.adicionaAresta('H-B')
g_p2.adicionaAresta('H-F')
g_p2.adicionaAresta('H-G')
g_p2.adicionaAresta('D-B')
g_p2.adicionaAresta('B-C')
g_p2.adicionaAresta('D-C')
g_p2.adicionaAresta('D-F')
g_p2.adicionaAresta('D-E')
g_p2.adicionaAresta('F-G')
g_p2.adicionaAresta('F-E')

print(g_p2)