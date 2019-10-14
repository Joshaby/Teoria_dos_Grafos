import string as str

from grafo_adj_nao_dir import Grafo

g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'])

g_p.adicionaAresta('J-C')
g_p.adicionaAresta('C-E')
g_p.adicionaAresta('C-E')
g_p.adicionaAresta('C-P')
g_p.adicionaAresta('C-P')
g_p.adicionaAresta('C-M')
g_p.adicionaAresta('C-T')
g_p.adicionaAresta('M-T')
g_p.adicionaAresta('T-Z')

g_c = Grafo(['J', 'C', 'E', 'F'])
g_c.adicionaAresta('J-C')
g_c.adicionaAresta('F-E')
g_c.adicionaAresta('F-J')

g_p1 = Grafo(['J', 'C', 'T', 'P', 'A', 'Z', 'E', 'M'])

g_p1.adicionaAresta('J-C')
g_p1.adicionaAresta('C-E')
g_p1.adicionaAresta('E-A')
g_p1.adicionaAresta('A-P')
g_p1.adicionaAresta('E-P')
g_p1.adicionaAresta('P-M')
g_p1.adicionaAresta('M-T')
g_p1.adicionaAresta('T-Z')
g_p1.adicionaAresta('T-C')
g_p1.adicionaAresta('Z-J')

g_p2 = Grafo(['A', 'C', 'B', 'E', 'D', 'H', 'G', 'F'])
g_p2.adicionaAresta('A-B')
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
g_p2.adicionaAresta('D-D')
g_p2.adicionaAresta('F-F')
g_p2.adicionaAresta('D-F')
g_p2.adicionaAresta('F-F')

print(g_c.ha_ciclo_hamiltoniano())

# a = str.ascii_uppercase
# a = a[:-20]
#
# grafo1 = Grafo(a)
# cont = 0
#     for i in range(len(a)) :
#         for j in range(len(a)) :
#             if a[i] != a[j] :
#                 grafo1.adicionaAresta(a[i] + grafo1.SEPARADOR_ARESTA + a[j])
#     cont += 1
#
# # Vertices = []
# # grafo1.DFS(Vertices,'C')
# # print(Vertices)
# grafo = Grafo()
#
# Grafo.adicionaVertice(grafo,"A")
# Grafo.adicionaVertice(grafo,"B")
# Grafo.adicionaVertice(grafo,"C")
# Grafo.adicionaVertice(grafo,"D")
# Grafo.adicionaVertice(grafo,"E")
# Grafo.adicionaVertice(grafo,"F")
# Grafo.adicionaVertice(grafo,"G")
# Grafo.adicionaVertice(grafo,"H")
# Grafo.adicionaVertice(grafo,"I")
# Grafo.adicionaVertice(grafo,"J")
# Grafo.adicionaVertice(grafo,"K")
# Grafo.adicionaVertice(grafo,"L")
# Grafo.adicionaVertice(grafo,"M")
# Grafo.adicionaVertice(grafo,"N")
# Grafo.adicionaVertice(grafo,"O")
# Grafo.adicionaVertice(grafo,"P")
# Grafo.adicionaVertice(grafo,"Q")
# Grafo.adicionaVertice(grafo,"R")
# Grafo.adicionaVertice(grafo,"S")
# Grafo.adicionaVertice(grafo,"T")
#
# Grafo.adicionaAresta(grafo, "A-B")
# Grafo.adicionaAresta(grafo, "A-C")
# Grafo.adicionaAresta(grafo, "B-C")
# Grafo.adicionaAresta(grafo, "B-D")
# Grafo.adicionaAresta(grafo, "C-E")
# Grafo.adicionaAresta(grafo, "D-E")
# Grafo.adicionaAresta(grafo, "D-F")
# Grafo.adicionaAresta(grafo, "E-F")
# Grafo.adicionaAresta(grafo, "G-H")
# Grafo.adicionaAresta(grafo, "H-I")
# Grafo.adicionaAresta(grafo, "I-J")
# Grafo.adicionaAresta(grafo, "J-K")
# Grafo.adicionaAresta(grafo, "G-L")
# Grafo.adicionaAresta(grafo, "H-M")
# Grafo.adicionaAresta(grafo, "O-J")
# Grafo.adicionaAresta(grafo, "L-M")
# Grafo.adicionaAresta(grafo, "M-N")
# Grafo.adicionaAresta(grafo, "N-O")
# Grafo.adicionaAresta(grafo, "O-L")
# Grafo.adicionaAresta(grafo, "B-G")
# Grafo.adicionaAresta(grafo, "D-K")
# Grafo.adicionaAresta(grafo, "F-J")
# Grafo.adicionaAresta(grafo, "E-I")
# Grafo.adicionaAresta(grafo, "T-P")
# Grafo.adicionaAresta(grafo, "P-Q")
# Grafo.adicionaAresta(grafo, "Q-R")
# Grafo.adicionaAresta(grafo, "R-S")
# Grafo.adicionaAresta(grafo, "S-P")
# Grafo.adicionaAresta(grafo, "S-T")
# Grafo.adicionaAresta(grafo, "R-T")
# Grafo.adicionaAresta(grafo, "T-C")
# Grafo.adicionaAresta(grafo, "Q-D")
#
#
# print(grafo1)
# print(grafo1.ha_caminho_euleriano())