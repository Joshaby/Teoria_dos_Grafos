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

# print(g_p.Dijkstra('J', 'Z'))

# g_c = Grafo(['J', 'C', 'E', 'F'])
# g_c.adicionaAresta('J-C')
# g_c.adicionaAresta('F-E')
# g_c.adicionaAresta('F-J')
#
g_p1 = Grafo(['J', 'C', 'A', 'P', 'Z', 'T', 'E', 'M'])
#
g_p1.adicionaAresta('J-C')
g_p1.adicionaAresta('C-E')
g_p1.adicionaAresta('E-A')
g_p1.adicionaAresta('E-P')
g_p1.adicionaAresta('P-M')
g_p1.adicionaAresta('M-T')
g_p1.adicionaAresta('T-Z')
g_p1.adicionaAresta('T-C')
g_p1.adicionaAresta('Z-J')
g_p1.adicionaAresta('A-Z')
g_p1.adicionaAresta('A-C')
#
# g_p2 = Grafo(['A', 'C', 'B', 'E', 'D', 'H', 'G', 'F'])
# g_p2.adicionaAresta('A-B')
# g_p2.adicionaAresta('A-H')
# g_p2.adicionaAresta('H-B')
# g_p2.adicionaAresta('H-F')
# g_p2.adicionaAresta('H-G')
# g_p2.adicionaAresta('D-B')
# g_p2.adicionaAresta('B-C')
# g_p2.adicionaAresta('D-C')
# g_p2.adicionaAresta('D-F')
# g_p2.adicionaAresta('D-E')
# g_p2.adicionaAresta('F-G')
# g_p2.adicionaAresta('F-E')
# g_p2.adicionaAresta('D-D')
# g_p2.adicionaAresta('F-F')
# g_p2.adicionaAresta('D-F')
# g_p2.adicionaAresta('F-F')

grafo = Grafo(['A', 'B', 'C', 'D', 'E', 'H', 'F', 'G', 'I', 'J'])
grafo.adicionaAresta('A-H')
grafo.adicionaAresta('I-H')
grafo.adicionaAresta('I-G')
grafo.adicionaAresta('I-F')
grafo.adicionaAresta('H-F')
grafo.adicionaAresta('H-C')
grafo.adicionaAresta('G-F')
grafo.adicionaAresta('G-C')
grafo.adicionaAresta('D-C')
grafo.adicionaAresta('D-E')
grafo.adicionaAresta('D-B')
grafo.adicionaAresta('E-B')
grafo.adicionaAresta('F-B')
grafo.adicionaAresta('F-E')
grafo.adicionaAresta('J-B')

# print(grafo.DijkstraDrone('A', 'J', 2, 3, ['C']))

grafo1 = Grafo(
    ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'X',
     'W', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g'])
grafo1.adicionaAresta('A-B')
grafo1.adicionaAresta('A-C')
grafo1.adicionaAresta('A-D')
grafo1.adicionaAresta('B-C')
grafo1.adicionaAresta('B-E')
grafo1.adicionaAresta('C-F')
grafo1.adicionaAresta('D-H')
grafo1.adicionaAresta('D-L')
grafo1.adicionaAresta('E-I')
grafo1.adicionaAresta('E-F')
grafo1.adicionaAresta('F-G')
grafo1.adicionaAresta('F-J')
grafo1.adicionaAresta('F-K')
grafo1.adicionaAresta('G-K')
grafo1.adicionaAresta('G-D')
grafo1.adicionaAresta('H-G')
grafo1.adicionaAresta('I-M')
grafo1.adicionaAresta('J-N')
grafo1.adicionaAresta('K-L')
grafo1.adicionaAresta('K-O')
grafo1.adicionaAresta('L-P')
grafo1.adicionaAresta('M-Q')
grafo1.adicionaAresta('N-R')
grafo1.adicionaAresta('O-R')
grafo1.adicionaAresta('Q-R')
grafo1.adicionaAresta('O-Q')
grafo1.adicionaAresta('O-S')
grafo1.adicionaAresta('P-R')
grafo1.adicionaAresta('P-T')
grafo1.adicionaAresta('R-U')
grafo1.adicionaAresta('R-S')
grafo1.adicionaAresta('S-W')
grafo1.adicionaAresta('S-T')
grafo1.adicionaAresta('T-X')
grafo1.adicionaAresta('U-Y')
grafo1.adicionaAresta('U-Z')
grafo1.adicionaAresta('V-R')
grafo1.adicionaAresta('W-V')
grafo1.adicionaAresta('W-a')
grafo1.adicionaAresta('W-b')
grafo1.adicionaAresta('X-b')
grafo1.adicionaAresta('X-c')
grafo1.adicionaAresta('Z-e')
grafo1.adicionaAresta('c-f')
grafo1.adicionaAresta('f-e')
grafo1.adicionaAresta('e-d')
grafo1.adicionaAresta('e-g')

# print(grafo1.startDijkstraDrone('A', 'd', 3, 4, ['I', 'R', 'X', 'f']))
print(grafo1.Kruskall({}))
#
# print(grafo.DFS_Dijkstra(Ver, 'J', 'A', 3, 3, ['C'], BETA, FI, PI))
#
#
# grafo1 = Grafo(a)
# cont = 0
# for i in range(len(a)) :
#     for j in range(len(a)) :
#         if a[i] != a[j] :
#             grafo1.adicionaAresta(a[i] + grafo1.SEPARADOR_ARESTA + a[j])
# cont += 1
# Vertices = []
# grafo1.DFS(Vertices,'C')
# print(grafo1)
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
