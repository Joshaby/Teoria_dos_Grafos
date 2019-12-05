# -*- coding: utf-8 -*-
from math import inf
from random import choice, randint

class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class MatrizInvalidaException(Exception):
    pass


class Grafo:
    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'
    __maior_vertice = 0

    def __init__(self, V=None, M=None):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param V: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma matriz de adjacência que guarda as arestas do grafo. Cada entrada da matriz tem um inteiro que indica a quantidade de arestas que ligam aqueles vértices
        '''

        if V == None:
            V = list()
        if M == None:
            M = list()

        for v in V:
            if not (Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

        self.N = list(V)

        if M == []:
            for k in range(len(V)):
                M.append(list())
                for l in range(len(V)):
                    if k > l:
                        M[k].append('-')
                    else:
                        M[k].append(0)

        if len(M) != len(V):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(V):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for i in range(len(V)):
            for j in range(len(V)):
                '''
                Verifica se os índices passados como parâmetro representam um elemento da matriz abaixo da diagonal principal.
                Além disso, verifica se o referido elemento é um traço "-". Isso indica que a matriz é não direcionada e foi construída corretamente.
                '''
                if i > j and not (M[i][j] == '-'):
                    raise MatrizInvalidaException('A matriz não representa uma matriz não direcionada')

                aresta = V[i] + Grafo.SEPARADOR_ARESTA + V[j]
                if not (self.arestaValida(aresta)):
                    raise ArestaInvalidaException('A aresta ' + aresta + ' é inválida')

        self.M = list(M)

    def arestaValida(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro está dentro do padrão estabelecido.
        Uma aresta é representada por um string com o formato a-b, onde:
        a é um substring de aresta que é o nome de um vértice adjacente à aresta.
        - é um caractere separador. Uma aresta só pode ter um único caractere como esse.
        b é um substring de aresta que é o nome do outro vértice adjacente à aresta.
        Além disso, uma aresta só é válida se conectar dois vértices existentes no grafo.
        :param aresta: A aresta que se quer verificar se está no formato correto.
        :return: Um valor booleano que indica se a aresta está no formato correto.
        '''

        # Não pode haver mais de um caractere separador
        if aresta.count(Grafo.SEPARADOR_ARESTA) != Grafo.QTDE_MAX_SEPARADOR:
            return False

        # Índice do elemento separador
        i_traco = aresta.index(Grafo.SEPARADOR_ARESTA)

        # O caractere separador não pode ser o primeiro ou o último caractere da aresta
        if i_traco == 0 or aresta[-1] == Grafo.SEPARADOR_ARESTA:
            return False

        if not (self.existeVertice(aresta[:i_traco])) or not (self.existeVertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice: str):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def __primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice X
        :param a: a aresta a ser analisada
        :return: O primeiro vértice da aresta
        '''
        return a[0:a.index(Grafo.SEPARADOR_ARESTA)]

    def __segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o vértice Y
        :param a: A aresta a ser analisada
        :return: O segundo vértice da aresta
        '''
        return a[a.index(Grafo.SEPARADOR_ARESTA) + 1:]

    def __indice_primeiro_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice X na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do primeiro vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__primeiro_vertice_aresta(a))

    def __indice_segundo_vertice_aresta(self, a: str):
        '''
        Dada uma aresta no formato X-Y, retorna o índice do vértice Y na lista de vértices
        :param a: A aresta a ser analisada
        :return: O índice do segundo vértice da aresta na lista de vértices
        '''
        return self.N.index(self.__segundo_vertice_aresta(a))

    def existeAresta(self, a: str):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, a):
            for i in range(len(self.M)):
                for j in range(len(self.M)):
                    if self.M[self.__indice_primeiro_vertice_aresta(a)][self.__indice_segundo_vertice_aresta(a)]:
                        existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Inclui um vértice no grafo se ele estiver no formato correto.
        :param v: O vértice a ser incluído no grafo.
        :raises VerticeInvalidoException se o vértice já existe ou se ele não estiver no formato válido.
        '''
        if v in self.N:
            raise VerticeInvalidoException('O vértice {} já existe'.format(v))

        if self.verticeValido(v):
            if len(v) > self.__maior_vertice:
                self.__maior_vertice = len(v)

            self.N.append(v)  # Adiciona vértice na lista de vértices
            self.M.append([])  # Adiciona a linha

            for k in range(len(self.N)):
                if k != len(self.N) - 1:
                    self.M[k].append(0)  # adiciona os elementos da coluna do vértice
                    self.M[self.N.index(v)].append('-')  # adiciona os elementos da linha do vértice
                else:
                    self.M[self.N.index(v)].append(0)  # adiciona um zero no último elemento da linha
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, a):
        '''
        Adiciona uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            i_a1 = self.__indice_primeiro_vertice_aresta(a)
            i_a2 = self.__indice_segundo_vertice_aresta(a)
            if i_a1 < i_a2:
                self.M[i_a1][i_a2] += 1
            else:
                self.M[i_a2][i_a1] += 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    def remove_aresta(self, a):
        '''
        Remove uma aresta ao grafo no formato X-Y, onde X é o primeiro vértice e Y é o segundo vértice
        :param a: a aresta no formato correto
        :raise: lança uma exceção caso a aresta não estiver em um formato válido
        '''
        if self.arestaValida(a):
            if self.existeAresta(a):
                i_a1 = self.__indice_primeiro_vertice_aresta(a)
                i_a2 = self.__indice_segundo_vertice_aresta(a)
                if i_a1 < i_a2:
                    self.M[i_a1][i_a2] -= 1
                else:
                    self.M[i_a2][i_a1] -= 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))

    #### ROTEIRO 4 #####################################################################################################

    def vertices_nao_adjacentes(self):
        '''
        Acha os vértices não adjacentes de um determinado grafo
        :return: Lista com os possíveis vértices não adjacentes
        '''
        List = list()
        for i in range(len(self.N)):
            for j in range(i, len(self.N)):
                if self.M[i][j] == 0:
                    List.append(self.N[i] + self.SEPARADOR_ARESTA + self.N[j])
        return List

    def ha_laco(self):
        '''
        Verifica se um grafo possui um arestas paralelas
        :return: True para a existência de uma aresta paralela, e False para o contrário
        '''
        List = list()
        for i in range(len(self.N)):
            if self.M[i][i] >= 1:
                return True
        return False

    def ha_paralelas(self):
        '''
        Verifica se um grafo possui um arestas paralelas
        :return: True para a existência de uma aresta paralela, e False para o contrário
        '''
        List = list()
        for i in range(len(self.N)):
            for j in range(i, len(self.N)):
                if self.M[i][j] > 1:
                    return True
        return False

    def grau(self, v):
        '''
        Conta quantas arestas incidem em um determinado vértice, ou seja, verifica seu grau
        :return: grau do vértice
        '''
        for i in range(len(self.N)):
            cont = 0
            if self.N[i] == v:
                if self.M[i][i] >= 1:
                    cont += self.M[i][i]
                for k in range(len(self.N)):
                    for j in range(k, len(self.N)):
                        if k == i or j == i:
                            cont += self.M[k][j]
                return cont

    def arestas_sobre_vertice(self, v):
        '''
        Adiciona a arestas que incidem em um dado vértice
        :return: lista de arestas
        '''
        for i in range(len(self.N)):
            List = list()
            if self.N[i] == v:
                for k in range(len(self.N)):
                    for j in range(k, len(self.N)):
                        if self.M[k][j] != 0:
                            for m in range(self.M[k][j]):
                                if j == i or k == i:
                                    List.append(self.N[k] + self.SEPARADOR_ARESTA + self.N[j])
                return List

    def eh_completo(self):
        '''
        Verifica se um grafo é completo
        :return: True para se ele for completo, False para o contrário
        '''
        for i in range(len(self.N)):
            for j in range(i + 1, len(self.N)):
                if self.M[i][j] == 0:
                    return False
        return True

    #### ROTEIRO 5 #####################################################################################################

    def __retira_vertices(self, Caminho, ListaVertice, Tipo):
        '''
        Retira vertices já percorridos de um Grafo
        :param Caminho: caminho qualquer de vertice, podendo ser propriamente um caminho ou um ciclo
        :param ListaVertice: Lista com vertice para retirada dos mesmos
        :param Tipo: Tipo da função que usa esta função
        :return: ListaVertice com possiveis mudanças
        '''
        for i in range(len(ListaVertice)):
            if Tipo == 'HAMILTON':
                if ListaVertice[i] in Caminho and (ListaVertice[i] != Caminho[0] or len(Caminho) != len(self.N)):
                    ListaVertice.remove(ListaVertice[i])
                    break
            if Tipo == 'DFS':
                if ListaVertice[i] in Caminho:
                    ListaVertice.remove(ListaVertice[i])
                    break
        return ListaVertice

    def __vertices_adjacentes(self, VerticeEntrada):
        '''
        Descobre quais são os vertices adjacentes de VerticeEntrada
        :param VerticeEntrada: Um vertice qualquer
        :return: Lista com os vertices adjacentes de VerticeEntrada
        '''
        List = self.arestas_sobre_vertice(VerticeEntrada)
        for i in range(len(List)):
            if List[i][-1] == VerticeEntrada:
                List[i] = List[i][::-1]
            List[i] = List[i][-1]
        return List

    def __hamilton(self, VerticeAtual, Ciclo):
        '''
        Percorrer um Grafo para tentar saber se ele possui um ciclo hamiltoniano
        :param VerticeAtual: Um vertice qualquer
        :param Ciclo: Lista onde sera colocado ciclo
        :return: Possivel ciclo hamiltoniano
        '''
        Ciclo.append(VerticeAtual)
        if Ciclo != [] and Ciclo[0] == Ciclo[-1] and len(Ciclo) == (len(self.N) + 1):
            return Ciclo
        VerticesAdjacentes = self.__vertices_adjacentes(VerticeAtual)
        while True:
            if len(VerticesAdjacentes) == 0 or len(Ciclo) == (len(self.N) + 1):
                return
            for i in range(len(VerticesAdjacentes)):
                VerticesAdjacentes = self.__retira_vertices(Ciclo, VerticesAdjacentes, 'HAMILTON')
            if len(VerticesAdjacentes) > 0:
                Aux = VerticesAdjacentes[0]
                VerticesAdjacentes.remove(Aux)
                self.__hamilton(Aux, Ciclo)
                if Ciclo != [] and Ciclo[0] == Ciclo[-1] and len(Ciclo) == (len(self.N) + 1):
                    return Ciclo
                del Ciclo[-1]
            else:
                return

    def ha_ciclo_hamiltoniano(self):
        '''
        Função iniciar o __hamilton
        A função roda enquanto não achar um ciclo ou até o range de self.N
        :return:
        '''
        cond = None
        for i in self.N:
            Ciclo = []
            VerticeG = []
            cond = self.__hamilton(i, Ciclo)
            if cond != None:
                return cond
        return False

    def DFS(self, VerticesVisitados, VerticeAtual):
        '''
        Recursão para perrcorrer um grafo não-direcionado e adicionando vértices e arestas visitados em lista
        :param VerticesVisitados: lista com vértices visitados
        :param VerticeAtual: Vértice de entrada
        :return: recursão
        '''
        if VerticeAtual in VerticesVisitados:
            return
        else:
            VerticesVisitados.append(VerticeAtual)
            VerticesAdjacentes = self.__vertices_adjacentes(VerticeAtual)
            while True:
                if len(VerticesAdjacentes) == 0 or len(VerticesVisitados) == len(self.N):
                    return
                else:
                    for i in range(len(VerticesVisitados)):
                        for j in range(len(VerticesVisitados)):
                            VerticesAdjacentes = self.__retira_vertices(VerticesVisitados, VerticesAdjacentes, 'DFS')
                    if len(VerticesAdjacentes) > 0:
                        Aux = VerticesAdjacentes[0]
                        VerticesAdjacentes.remove(Aux)
                        self.DFS(VerticesVisitados, Aux)
                    else:
                        return

    def arestas(self):
        '''
        Função para percorrer um Grafo e saber quais as arestas existentes nele
        :return: Retorna as arestas existentes de um grafo
        '''
        List = list()
        for i in range(len(self.N)):
            for j in range(i, len(self.N)):
                for k in range(self.M[i][j]):
                    List.append(self.N[i] + self.SEPARADOR_ARESTA + self.N[j])
        return List

    def vertices_e_arestas_adjacentes(self, Vertice, Arestas):
        '''
        Nessa função, tem função como saber quais vertices e arestas são adjacentes a Vertice. É dado nomes a arestas
        para ajudar a percorrer o Grafo e achar um caminho euleriano
        :param Vertice: Vertice para saber quais vertices esta ligados com ele
        :param Arestas: Arestas ligadas ao Vertice
        :return: Lista de vertices e arestas a adjacentes a Vertice
        '''
        NewArestas = Arestas[:]
        VerticesAdjacentes = self.__vertices_adjacentes(Vertice)
        ArestasAdjacentes = list()
        NomesVertices = [str('a' + str(i)) for i in range(1, len(Arestas) + 1)]
        for i in VerticesAdjacentes:
            Aresta = Vertice + self.SEPARADOR_ARESTA + i
            for j in range(len(NewArestas)):
                if Aresta == NewArestas[j] or Aresta[::-1] == NewArestas[j]:
                    ArestasAdjacentes.append(NomesVertices[j])
                    del NewArestas[j]
                    del NomesVertices[j]
                    break
        return VerticesAdjacentes, ArestasAdjacentes

    def eh_conexo(self):
        '''
        Função para percorrer um Lista oriunda de função função DFS para saber se o Grafo é conexo
        :return: True para conexo e False para não conexo
        '''
        Vertices = []
        self.DFS(Vertices, self.N[0])
        for i in self.N:
            if not i in Vertices:
                return False
        return True

    def __retira_vertice_e_arestas(self, Vertice, VerticesAdjacentes, ArestasAdjacentes, ArestasPercorridas):
        '''
        :param Vertice: Verice base para retirar vertice e arestas adjacentes
        :param VerticesAdjacentes: Vertices adjacentes a Vertice
        :param ArestasAdjacentes: Arestas adjacentes a Vertice
        :param ArestasPercorridas: Lista de arestas que foram percorridas
        '''
        for i in ArestasPercorridas:
            for j in range(len(VerticesAdjacentes)):
                if ArestasAdjacentes[j] in ArestasPercorridas:
                    del ArestasAdjacentes[j];
                    del VerticesAdjacentes[j]
                    break

    def __euler(self, VerticeAtual, VerticeFinal, Caminho, ArestasPercorridas, Arestas):
        '''
        Função recursiva para percorrer Grafo e achar um possivel caminho euleriano
        :param VerticeAtual: Um vertice qualquer
        :param VerticeFinal: Vertice do final do caminho de euler
        :param Caminho: Possivel caminho de euler, que é modificado ao longo das chamadas recursivas
        :param ArestasPercorridas: Lista de arestas que foram percorridas
        :param Arestas: Arestas que o Grafo possui
        :return:possivel caminho euleriano
        '''
        Caminho.append(VerticeAtual)
        if len(ArestasPercorridas) == len(Arestas) and Caminho[-1] == VerticeFinal:
            return Caminho
        VerticesAdjacentes, ArestasAdjacentes = self.vertices_e_arestas_adjacentes(VerticeAtual, Arestas)
        while True:
            self.__retira_vertice_e_arestas(VerticeAtual, VerticesAdjacentes, ArestasAdjacentes, ArestasPercorridas)
            if len(VerticesAdjacentes) > 0 and len(ArestasAdjacentes) > 0:
                Aux, Aux1 = VerticesAdjacentes[0], ArestasAdjacentes[0]
                VerticesAdjacentes.remove(Aux);
                ArestasAdjacentes.remove(Aux1)
                ArestasPercorridas.append(Aux1)
                VerticeAnterior = VerticeAtual
                self.__euler(Aux, VerticeFinal, Caminho, ArestasPercorridas, Arestas)
                if len(ArestasPercorridas) == len(Arestas) and Caminho[-1] == VerticeFinal:
                    return Caminho
                del Caminho[-1];
                del ArestasPercorridas[-1]
            else:
                return

    def ha_caminho_euleriano(self):
        '''
        Função para saber se um Grafo obedece as regras de euler, se sim tenta fazer um caminho
        :return: Caminho euleriano ou False para se o Grafo não for conexo e não obdecer as regras de euler
        '''
        if self.eh_conexo():
            Arestas = self.arestas()
            contGrau = []
            contPar = []
            for i in self.N:
                if self.grau(i) % 2 != 0:
                    contGrau.append(i)
                if self.grau(i) % 2 == 0:
                    contPar.append(i)
            if len(contGrau) == 2 or len(contPar) == len(self.N):
                if len(contPar) == len(self.N):
                    for i in self.N:
                        Caminho = []
                        ArestasPercorridas = []
                        cond = self.__euler(i, i, Caminho, ArestasPercorridas, Arestas)
                        if cond != None:
                            return cond
                if len(contGrau) == 2:
                    Caminho = []
                    ArestasPercorridas = []
                    cond = self.__euler(contGrau[-1], contGrau[0], Caminho, ArestasPercorridas, Arestas)
                    if cond != None:
                        return cond
            return False

    #### ROTEIRO 7 #####################################################################################################

    def __retira_vertice(self, Vertice, Vertices):
        '''

        :param Vertice: Vértice a ser tirado
        :param Vertices: Lista de vértices
        :return: nda
        '''
        if Vertice in Vertices:
            Vertices.remove(Vertice)

    def __retira_arestas(self):
        '''
        retira arestas paralelas e laços
        :return:
        '''
        for i in range(len(self.N)):
            for j in range(i, len(self.N)):
                if self.M[i][j] > 1:
                    self.M[i][j] = 1

    def inicia_vertices(self, U):
        '''
        Calcula o BETA, FI e Pi dos vértices
        :param U: Vértice de início
        :return: BETA, FI, PI
        '''
        BETA = dict()
        FI = dict()
        PI = dict()
        for i in self.N:
            PI[i] = 0
            if i == U:
                BETA[i] = 0
                FI[i] = 1
            else:
                BETA[i] = inf
                FI[i] = 0
        return BETA, FI, PI

    def Dijkstra(self, U, V):
        '''
        Implementação do algoritmo de Dijkstra
        :param U: Vértice inicial
        :param V: Vértice final
        :return: Um caminho do tipo String
        '''
        self.__retira_arestas()
        BETA, FI, PI = self.inicia_vertices(U)
        W = U
        while (W != V):
            Vertices, AUX = self.vertices_e_arestas_adjacentes(W, self.arestas())
            self.__retira_vertice(PI[W], Vertices)
            for i in Vertices:
                if BETA[i] > BETA[W] + 1 and FI[i] == 0:
                    BETA[i] = BETA[W] + 1
                    PI[i] = W
            AUX1 = inf
            r = 0
            for i in self.N:
                if FI[i] == 0 and BETA[i] < AUX1:
                    r = i
                    AUX1 = BETA[i]
            FI[r] = 1
            W = r
        AUX = PI[V]
        CAMINHO = V + ' - '
        while (AUX != 0):
            CAMINHO += (AUX + ' - ')
            AUX = PI[AUX]
        CAMINHO = CAMINHO[::-1]
        return CAMINHO[3:]

    def DijkstraDrone(self, U, V, GAS, QTDE_GAS, ESTACOES):
        '''
        Implementação do algoritmo de Dijkstra para achar menor caminho para um drone percorrer
        :param U: Vértice inicial
        :param V: Vértice final
        :return: Um caminho do tipo String
        '''
        self.__retira_arestas()
        BETA, FI, PI = self.inicia_vertices(U)
        W = U
        cond = True
        while (W != V and cond):
            if W in ESTACOES :
                GAS += QTDE_GAS
            Vertices, AUX = self.vertices_e_arestas_adjacentes(W, self.arestas())
            self.__retira_vertice(PI[W], Vertices)
            for i in Vertices:
                if BETA[i] > BETA[W] + 1 and FI[i] == 0 and BETA[W] < GAS:
                    BETA[i] = BETA[W] + 1
                    PI[i] = W
            AUX1 = inf
            r = 0
            for i in self.N:
                if FI[i] == 0 and BETA[i] < AUX1 :
                    r = i
                    AUX1 = BETA[i]
            if r == 0 :
                cond = False
            else :
                FI[r] = 1
                W = r
        if not cond :
            return False
        AUX = PI[V]
        CAMINHO = V + ' - '
        while (AUX != 0):
            CAMINHO += (AUX + ' - ')
            AUX = PI[AUX]
        CAMINHO = CAMINHO[::-1]
        return CAMINHO[3:]

    def startDijkstraDrone(self, U, V, GAS, QTDE_GAS, ESTACOES) :
        '''
        É chamada a função DijkstraDrone, por algum motivo, poder ser que não seja encontrado um caminho que comece de X e vai até Y,
        no caso X é o inicial e Y p final, mas, segundo alguns testes, é possível achar um caminho começando de Y até X, nesse caso,
        a String é invertida, caso seja um caminho
        :param U: Vértice inicial
        :param V: Vértice final
        :param GAS: Gasolina
        :param QTDE_GAS: Qtde de gasolina que o drone pode abastecer num posto
        :param ESTACOES: posto de gasolinas
        :return: um caminho ou uma mensagem
        '''
        return self.DijkstraDrone(U, V, GAS, QTDE_GAS, ESTACOES)

    # Tentativa de Dijkstra com DFS, acha um caminho, mas as vezes não é o menor
    # def DFS_Dijkstra(self, Ver, V, W, GAS, QTDE_GAS, ESTACOES, BETA, FI, PI) :
    #     Ver.append(W)
    #     GAS -= 1
    #     if W in ESTACOES :
    #         GAS = QTDE_GAS
    #     if Ver[-1] == V or GAS == 0 :
    #         return
    #     else :
    #         Vertices = self.__vertices_adjacentes(W)
    #         while True :
    #             for i in Vertices :
    #                 if BETA[i] > BETA[W] + 1 and FI[i] == 0 :
    #                     BETA[i] = BETA[W] + 1
    #                     PI[i] = W
    #             AUX1 = inf
    #             R = 0
    #             for i in Vertices:
    #                 if FI[i] == 0 and BETA[i] < AUX1 :
    #                     R = i
    #             if R == 0 :
    #                 return
    #             FI[R] = 1
    #             W = R
    #             Vertices.remove(R)
    #             self.DFS_Dijkstra(Ver, V, W, GAS, QTDE_GAS, ESTACOES, BETA, FI, PI)
    #             if Ver[-1] == V or GAS == 0 :
    #                 return
    #             FI[Ver[-1]] = 0
    #             del Ver[-1]
    #
    # def start_DFS_Dijkstra(self, V, U, GAS, QTDE_GAS, ESTACOES) :
    #     BETA, FI, PI = self.inicia_vertices(U)
    #     Vertices = []
    #     self.DFS_Dijkstra(Vertices, V, U, GAS + 1, QTDE_GAS, ESTACOES, BETA, FI, PI)
    #     return Vertices

    #### ROTEIRO 8 #####################################################################################################

    def __EscolheVerticeSemPeso(self, V, G):
        Vertices = self.__vertices_adjacentes(V)
        for i in Vertices :
            if i not in G.N :
                return i
        return 0

    def PrimSemPeso(self) :
        VerticeIni = choice(self.N)
        G = Grafo(VerticeIni)
        while(len(self.N) != len(G.N)) :
            i = choice(G.N)
            VerticeEscolhido = self.__EscolheVerticeSemPeso(i, G)
            if VerticeEscolhido != 0 :
                G.adicionaVertice(VerticeEscolhido)
                G.adicionaAresta(i + self.SEPARADOR_ARESTA + VerticeEscolhido)
        return G.N

    def __EscolheVertice(self, V, G, DicionarioArestas) :
        Vertices = self.__vertices_adjacentes(V)
        AUX = inf
        AUX1 = '0'
        for i in Vertices :
            if (V + self.SEPARADOR_ARESTA + i) in DicionarioArestas and (DicionarioArestas[V + self.SEPARADOR_ARESTA + i] < AUX) and i not in G.N :
                AUX = DicionarioArestas[V + self.SEPARADOR_ARESTA + i]
                AUX1 = i
            if (i + self.SEPARADOR_ARESTA + V) in DicionarioArestas and (DicionarioArestas[i + self.SEPARADOR_ARESTA + V] < AUX) and i not in G.N :
                AUX = DicionarioArestas[i + self.SEPARADOR_ARESTA + V]
                AUX1 = i
        if AUX1 != '0' :
            return AUX1, AUX
        else :
            return 0, 0

    def Prim(self, DicionarioArestas) :
        VerticeIni = choice(self.N)
        G = Grafo(VerticeIni)
        self.__setPesos(DicionarioArestas)
        while(len(self.N) != len(G.N)) :
            AUX = inf
            AUX1 = '0'
            VerticeEscolhido1 = '0'
            for i in G.N :
                VerticeEscolhido, Peso = self.__EscolheVertice(i, G, DicionarioArestas)
                if VerticeEscolhido != 0 and Peso != 0 :
                    if Peso < AUX :
                        AUX = Peso
                        AUX1 = i
                        VerticeEscolhido1 = VerticeEscolhido
            G.adicionaVertice(VerticeEscolhido1)
            G.adicionaAresta(AUX1 + self.SEPARADOR_ARESTA + VerticeEscolhido1)
        return G

    def __EscolheVerticeModificado1(self, V, G, DicionarioArestas) :
        AUX = inf
        AUX1 = '0'
        for i in self.__vertices_adjacentes(V) :
            if ((V + self.SEPARADOR_ARESTA + i) in DicionarioArestas or (i + self.SEPARADOR_ARESTA + V) in DicionarioArestas) and i not in G.N :
                PesosSobreVertice = 0
                for j in DicionarioArestas :
                    if i in j:
                        PesosSobreVertice += DicionarioArestas[j]
                if PesosSobreVertice < AUX :
                    AUX = PesosSobreVertice
                    AUX1 = i
        if AUX1 != '0':
            return AUX1, AUX
        else:
            return 0, 0

    def __EscolheVerticeModificado2(self, DicionarioArestas, Vertices) :
        AUX = inf
        AUX1 = '0'
        AUX3 = 0
        if Vertices == [] :
            AUX3 = self.N
        else :
            AUX3 = Vertices
        for i in AUX3 :
            PesosSobreVertice = 0
            for j in DicionarioArestas:
                if i in j:
                    PesosSobreVertice += DicionarioArestas[j]
            if PesosSobreVertice < AUX:
                AUX = PesosSobreVertice
                AUX1 = i
        if AUX1 != '0':
            return AUX1
        else:
            return 0

    def PrimModificado(self, DicionarioArestas) :
        self.__setPesos(DicionarioArestas)
        VerticeIni = self.__EscolheVerticeModificado2(DicionarioArestas, [])
        G = Grafo(VerticeIni)
        while(len(self.N) != len(G.N)) :
            AUX = inf
            AUX1 = '0'
            VerticeEscolhido1 = '0'
            for j in G.N :
                VerticeEscolhido, Peso = self.__EscolheVerticeModificado1(j, G, DicionarioArestas)
                if VerticeEscolhido != 0 and Peso != 0 :
                    if Peso < AUX :
                        AUX = Peso
                        AUX1 = j
                        VerticeEscolhido1 = VerticeEscolhido
            G.adicionaVertice(VerticeEscolhido1)
            G.adicionaAresta(AUX1 + self.SEPARADOR_ARESTA + VerticeEscolhido1)
        return G

    def __setPesos(self, DicionarioArestas) :
        if DicionarioArestas == {} :
            for i in self.arestas() :
                DicionarioArestas[i] = randint(1, len(self.N))
        else :
            return DicionarioArestas

    def __MenorAresta(self, DicionarioArestas) :
        AUX = inf
        AUX1 = '0'
        for i in DicionarioArestas :
            if DicionarioArestas[i] < AUX:
                AUX = DicionarioArestas[i]
                AUX1 = i
        if AUX1 != '0' :
            return AUX1
        else :
            return 0

    def __AdicionaAresta(self, Aresta, ArvoresArestas) :
        for i in ArvoresArestas :
            if Aresta[0] in ArvoresArestas[i].N :
                if Aresta[2] not in ArvoresArestas[i].N :
                    for j in ArvoresArestas :
                        if Aresta[2] in ArvoresArestas[j].N :
                            if Aresta[0] not in ArvoresArestas[j].N :
                                if len(ArvoresArestas[i].N) > len(ArvoresArestas[j].N) :
                                    for k in ArvoresArestas[j].N :
                                        ArvoresArestas[i].adicionaVertice(k)
                                    for k in ArvoresArestas[j].arestas() :
                                        ArvoresArestas[i].adicionaAresta(k)
                                    ArvoresArestas[i].adicionaAresta(Aresta)
                                    del ArvoresArestas[j]
                                    break
                                else :
                                    for k in ArvoresArestas[i].N :
                                        ArvoresArestas[j].adicionaVertice(k)
                                    for k in ArvoresArestas[i].arestas() :
                                        ArvoresArestas[j].adicionaAresta(k)
                                    ArvoresArestas[j].adicionaAresta(Aresta)
                                    del ArvoresArestas[i]
                                    break
                            else :
                                break
                else :
                    break
                break

    def Kruskall(self, DicionarioArestas) :
        ArvoresArestas = {}
        for i in self.N :
            ArvoresArestas[i] = Grafo(i)
        self.__setPesos(DicionarioArestas)
        while(len(ArvoresArestas) != 1) :
            MenorAresta = self.__MenorAresta(DicionarioArestas)
            self.__AdicionaAresta(MenorAresta, ArvoresArestas)
            del DicionarioArestas[MenorAresta]
        AUX = list(ArvoresArestas.keys())
        return ArvoresArestas[AUX[0]]

    def __min(self, DicionarioArestas) :
        AUX = list(DicionarioArestas.values())
        Menor = AUX[0]
        for i in range(1, len(AUX) - 1) :
            if AUX[i] < Menor :
                Menor = AUX[i]
        return Menor

    def __max(self, DicionarioArestas) :
        AUX = list(DicionarioArestas.values())
        Maior = AUX[0]
        for i in range(len(AUX)) :
            if AUX[i] > Maior :
                Maior = AUX[i]
        return Maior

    def __BucketSort(self, DicionarioArestas) :
        BucketsPesos = []
        BucketsArestas = []
        QtdeBuckets = 5
        for i in range(QtdeBuckets) :
            BucketsPesos.append([])
        for i in range(QtdeBuckets) :
            BucketsArestas.append([])
        MAX = self.__max(DicionarioArestas)
        MIN = self.__min(DicionarioArestas)
        for i in DicionarioArestas :
            AUX = (((DicionarioArestas[i] - MIN) / (MAX - MIN)) * (QtdeBuckets - 1)) + 1
            if AUX >= QtdeBuckets :
                AUX -= 1
            BucketsArestas[int(AUX)].append(i)
            BucketsPesos[int(AUX)].append(DicionarioArestas[i])
        for i in range(len(BucketsPesos)) :
            cond = True
            while cond :
                cond = False
                for k in range(len(BucketsPesos[i]) - 1) :
                    if BucketsPesos[i][k] > BucketsPesos[i][k + 1] :
                        AUX = BucketsPesos[i][k]
                        AUX1 = BucketsArestas[i][k]
                        BucketsPesos[i][k] = BucketsPesos[i][k + 1]
                        BucketsArestas[i][k] = BucketsArestas[i][k + 1]
                        BucketsPesos[i][k + 1] = AUX
                        BucketsArestas[i][k + 1] = AUX1
                        cond = True
        PesosOrdenados = []
        ArestasOrdenadas = []
        for i in BucketsPesos :
            for k in i :
                PesosOrdenados.append(k)
        for i in BucketsArestas :
            for k in i :
                ArestasOrdenadas.append(k)
        return PesosOrdenados, ArestasOrdenadas

    def KruskallModificado(self, DicionarioArestas) :
        self.__setPesos(DicionarioArestas)
        PesosOrdenados, ArestasOrdenadas = self.__BucketSort(DicionarioArestas)
        ArvoresArestas = {}
        for i in self.N :
            ArvoresArestas[i] = Grafo(i)
        while (len(ArestasOrdenadas) != 0) :
            MenorAresta = ArestasOrdenadas[0]
            self.__AdicionaAresta(MenorAresta, ArvoresArestas)
            del ArestasOrdenadas[0]
        AUX = list(ArvoresArestas.keys())
        return ArvoresArestas[AUX[0]]


    ####################################################################################################################

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''

        # Dá o espaçamento correto de acordo com o tamanho do string do maior vértice
        espaco = ' ' * (self.__maior_vertice)

        grafo_str = espaco + ' '

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca o espaço se não for o último vértice
                grafo_str += ' '

        grafo_str += '\n'

        for l in range(len(self.M)):
            grafo_str += self.N[l] + ' '
            for c in range(len(self.M)):
                grafo_str += str(self.M[l][c]) + ' '
            grafo_str += '\n'

        return grafo_str