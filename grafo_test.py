import unittest
from grafo import *

class TestGrafo(unittest.TestCase):

    def setUp(self):
        # Grafo da Paraíba
        self.g_p = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1':'J-C', 'a2':'C-E', 'a3':'C-E', 'a4':'P-C', 'a5':'C-P', 'a6':'C-M','a7': 'C-T', 'a8':'M-T', 'a9':'T-Z'})

        # Grafo da Paraíba sem arestas paralelas
        self.g_p_sem_paralelas = Grafo(['J', 'C', 'E', 'P', 'M', 'T', 'Z'], {'a1': 'J-C', 'a3': 'C-E', 'a4': 'C-P', 'a6': 'C-M', 'a7': 'C-T', 'a8': 'M-T', 'a9': 'T-Z'})

        # Grafos completos
        self.g_c = Grafo(['J', 'C', 'E', 'P'], {'a1':'J-C', 'a3':'J-E', 'a4':'J-P', 'a6':'C-E', 'a7':'C-P', 'a8':'E-P'})
        self.g_c2 = Grafo(['J', 'C', 'E', 'P'], {'a1':'J-C', 'a3':'E-J', 'a4':'J-P', 'a6':'E-C', 'a7':'C-P', 'a8':'P-E'})
        self.g_c3 = Grafo(['J'])
        self.g_c4 = Grafo(['J', 'C', 'E'], {'a1' : 'J-C', 'a2' : 'E-J', 'a3' : 'J-E', 'a4' : 'E-C'})

        # Grafos com laco
        self.g_l1 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-A', 'a2':'B-A', 'a3':'A-A'})
        self.g_l2 = Grafo(['A', 'B', 'C', 'D'], {'a1':'A-B', 'a2':'B-B', 'a3':'B-A'})
        self.g_l3 = Grafo(['A', 'B', 'C', 'D'], {'a1':'C-A', 'a2':'C-C', 'a3':'D-D'})
        self.g_l4 = Grafo(['D'], {'a2':'D-D'})
        self.g_l5 = Grafo(['C', 'D'], {'a2':'D-C', 'a3':'C-C'})

    def test_vertices_nao_adjacentes(self):
        self.assertEqual(self.g_p.vertices_nao_adjacentes(), ['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-C', 'C-Z', 'E-J', 'E-E', 'E-P', 'E-M', 'E-T', 'E-Z', 'P-J', 'P-E', 'P-P', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-M', 'M-Z', 'T-J', 'T-E', 'T-P', 'T-T', 'Z-J', 'Z-C', 'Z-E', 'Z-P', 'Z-M', 'Z-Z'])

        self.assertEqual(self.g_p.vertices_nao_adjacentes(),
                         ['J-J', 'J-E', 'J-P', 'J-M', 'J-T', 'J-Z', 'C-C', 'C-Z', 'E-J', 'E-E', 'E-P', 'E-M', 'E-T',
                          'E-Z', 'P-J', 'P-E',
                          'P-P', 'P-M', 'P-T', 'P-Z', 'M-J', 'M-E', 'M-P', 'M-M', 'M-Z', 'T-J', 'T-E', 'T-P', 'T-T',
                          'Z-J', 'Z-C', 'Z-E',
                          'Z-P', 'Z-M', 'Z-Z'])

        self.assertEqual(self.g_c.vertices_nao_adjacentes(), ['J-J', 'C-C', 'E-E', 'P-P'])

        self.assertEqual(self.g_c2.vertices_nao_adjacentes(), ['J-J', 'C-C', 'E-E', 'P-P'])

        self.assertEqual(self.g_c3.vertices_nao_adjacentes(), ['J-J'])

    def test_ha_laco(self):
        self.assertFalse(self.g_p.ha_laco())
        self.assertFalse(self.g_p_sem_paralelas.ha_laco())
        self.assertTrue(self.g_l1.ha_laco())
        self.assertTrue(self.g_l2.ha_laco())
        self.assertTrue(self.g_l3.ha_laco())
        self.assertTrue(self.g_l4.ha_laco())
        self.assertTrue(self.g_l5.ha_laco())

    def test_grau(self):
        # Paraíba
        self.assertEqual(self.g_p.grau('J'), 1)
        self.assertEqual(self.g_p.grau('C'), 7)
        self.assertEqual(self.g_p.grau('E'), 2)
        self.assertEqual(self.g_p.grau('P'), 2)
        self.assertEqual(self.g_p.grau('M'), 2)
        self.assertEqual(self.g_p.grau('T'), 3)
        self.assertEqual(self.g_p.grau('Z'), 1)

        # Completos
        self.assertEqual(self.g_c.grau('J'), 3)
        self.assertEqual(self.g_c.grau('C'), 3)
        self.assertEqual(self.g_c.grau('E'), 3)
        self.assertEqual(self.g_c.grau('P'), 3)
        self.assertEqual(self.g_c4.grau('J'), 3)

        # Com laço. Lembrando que cada laço conta uma única vez por vértice para cálculo do grau
        self.assertEqual(self.g_l1.grau('A'), 3)
        self.assertEqual(self.g_l2.grau('B'), 3)
        self.assertEqual(self.g_l4.grau('D'), 1)

    def test_arestas_ha_paralelas(self):
        self.assertTrue(self.g_p.ha_paralelas())
        self.assertFalse(self.g_p_sem_paralelas.ha_paralelas())
        self.assertFalse(self.g_c.ha_paralelas())
        self.assertFalse(self.g_c2.ha_paralelas())
        self.assertFalse(self.g_c3.ha_paralelas())
        self.assertFalse(self.g_c4.ha_paralelas())
        self.assertTrue((self.g_c4.eh_completo()))
        self.assertTrue(self.g_l1.ha_paralelas())

    def test_arestas_sobre_vertice(self):
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('J')), set(['a1']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('C')), set(['a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7']))
        self.assertEqual(set(self.g_p.arestas_sobre_vertice('M')), set(['a6', 'a8']))

    def test_eh_completo(self):
        self.assertFalse(self.g_p.eh_completo())
        self.assertFalse((self.g_p_sem_paralelas.eh_completo()))
        self.assertTrue((self.g_c.eh_completo()))
        self.assertTrue((self.g_c2.eh_completo()))
        self.assertTrue((self.g_c3.eh_completo()))
        self.assertTrue((self.g_c4.eh_completo()))
        self.assertFalse((self.g_l1.eh_completo()))
        self.assertFalse((self.g_l2.eh_completo()))
        self.assertFalse((self.g_l3.eh_completo()))
        self.assertTrue((self.g_l4.eh_completo()))
        self.assertTrue((self.g_l5.eh_completo()))

    def __ha_ciclo(self, VerticeAtual, Aux = ['0'], Ciclo = []):
        Ciclo.append(VerticeAtual)
        if len(Ciclo) == (2 * len(self.N)) - 1 and Ciclo[0] != Ciclo[-1]:
            return False
        if len(Ciclo) > 3 and Ciclo[0] == Ciclo[-1]:
            return Ciclo
        else:
            VerticesAdjacentes, ArestasAdjacentes = self.__arestas_e_vertices_adjacentes1(VerticeAtual)
            while True:
                cond = True
                for i in range(len(VerticesAdjacentes)):
                    if VerticesAdjacentes[i] == Aux[0] :
                        VerticesAdjacentes.remove(VerticesAdjacentes[i])
                        ArestasAdjacentes.remove(ArestasAdjacentes[i])
                        break
                if len(VerticesAdjacentes) > 0 and len(ArestasAdjacentes) > 0:
                    Aux1 = VerticesAdjacentes[0]
                    Aux2 = ArestasAdjacentes[0]
                    for i in range(len(VerticesAdjacentes)) :
                        if Ciclo != [] and (Ciclo[0] == VerticesAdjacentes[i]) :
                            Aux1 = VerticesAdjacentes[i]
                            Aux2 = ArestasAdjacentes[i]
                    Ciclo.append(Aux2)
                    VerticesAdjacentes.remove(Aux1)
                    ArestasAdjacentes.remove(Aux2)
                    Aux[0] = VerticeAtual
                    self.__ha_ciclo(Aux1)
                    if len(Ciclo) >= (2 * len(self.N)) - 1 and Ciclo[0] != Ciclo[-1]:
                        return False
                    if len(Ciclo) > 3 and Ciclo[0] == Ciclo[-1]:
                        return Ciclo
                    if Ciclo != [] and len(Ciclo) > 3 :
                        Ciclo.remove(Ciclo[-1])
                        Ciclo.remove(Ciclo[-2])
                else:
                    return

    def __ha_ciclo(self, VerticeAtual, Vertices, Arestas, Aux = ["0"]):
        Vertices.append(VerticeAtual)
        if len(Vertices) >= len(self.N) and Vertices[0] != Vertices[-1]:
            return
        if len(Vertices) > 3 and Vertices[0] == Vertices[-1]:
            return
        else:
            VerticesAdjacentes, ArestasAdjacentes = self.__arestas_e_vertices_adjacentes1(VerticeAtual)
            while True :
                if Vertices != [] :
                    cond = True
                    for i in range(len(VerticesAdjacentes)):
                        if cond == True:
                            if VerticesAdjacentes[i] == Aux[0]:
                                VerticesAdjacentes.remove(VerticesAdjacentes[i])
                                ArestasAdjacentes.remove(ArestasAdjacentes[i])
                                cond = False
                                break
                if len(VerticesAdjacentes) > 0 and len(ArestasAdjacentes) > 0:
                    Aux1 = VerticesAdjacentes[0]
                    Aux2 = ArestasAdjacentes[0]
                    cond1 = True
                    for i in range(len(VerticesAdjacentes)):
                        if cond1 :
                            for j in Vertices[:-1] :
                                if VerticesAdjacentes[i] == j :
                                    Aux1 = VerticesAdjacentes[i]
                                    Aux2 = ArestasAdjacentes[i]
                                    cond1 = False
                                    break
                    Arestas.append(Aux2)
                    VerticesAdjacentes.remove(Aux1)
                    ArestasAdjacentes.remove(Aux2)
                    Aux[0] = VerticeAtual
                    self.__ha_ciclo(Aux1, Vertices, Arestas)
                else :
                    return
    def __CAMINHO(self, VerticesVisitados, ArestasPercorridas, VerticeAtual, Comprimento, Vertices = []):
        if VerticeAtual in VerticesVisitados:
            return
        else:
            VerticesVisitados.append(VerticeAtual)
            Vertices.append(VerticeAtual)
            VerticesAdjacentes, ArestasAdjacentes = self.__arestas_e_vertices_adjacentes(VerticeAtual)
            while True:
                if len(VerticesAdjacentes) == 0 or len(VerticesVisitados) == len(self.N):
                    return
                else:
                    cond = True
                    for i in range(len(VerticesAdjacentes)):
                        if cond :
                            for j in VerticesVisitados:
                                if VerticesAdjacentes[i] == j:
                                    VerticesAdjacentes.remove(VerticesAdjacentes[i])
                                    ArestasAdjacentes.remove(ArestasAdjacentes[i])
                                    cond = False
                                    break
                    if len(VerticesAdjacentes) > 0 and len(ArestasAdjacentes) > 0:
                        Aux1 = VerticesAdjacentes[0]
                        Aux2 = ArestasAdjacentes[0]
                        if Aux1 not in VerticesVisitados:
                            ArestasPercorridas.append(Aux2)
                        VerticesAdjacentes.remove(Aux1)
                        ArestasAdjacentes.remove(Aux2)
                        self.__CAMINHO(VerticesVisitados, ArestasPercorridas, Aux1, Comprimento)
                        Tam = len(VerticesVisitados)
                        if Tam - 1 == Comprimento:
                            return True
                        if len(Vertices) == len(self.N) :
                            return False
                        VerticesVisitados.remove(VerticesVisitados[-1])
                        ArestasPercorridas.remove(ArestasPercorridas[-1])
                        Tam -= 1
                    else:
                        return

