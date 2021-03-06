# -*- coding: utf-8 -*-
from copy import deepcopy
from math import inf

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
                    M[k].append(0)

        if len(M) != len(V):
            raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

        for c in M:
            if len(c) != len(V):
                raise MatrizInvalidaException('A matriz passada como parâmetro não tem o tamanho correto')

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
            self.M[i_a1][i_a2] += 1
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
                self.M[i_a1][i_a2] -= 1
        else:
            raise ArestaInvalidaException('A aresta {} é inválida'.format(a))
    ##### ROTEIRO 6 ####################################################################################################

    def retira_arestas(self, Matriz):
        '''
        Retira arestas de arestas paralelas e laços
        :param Matriz: Matriz de adjacencia
        :return: nda
        '''
        for i in range(len(self.N)) :
            for j in range(len(self.N)) :
                if Matriz[i][j] > 1 :
                    Matriz[i][j] -= 1

    def max(self, Num, Num1):
        '''
        Retorna o máximo de duas arestas
        :param Num: QTde de arestas
        :param Num1: QTde de arestas
        :return: 1 para se houver arestas e 0 para quando não houver
        '''
        if Num >= 1 or Num1 >= 1 :
            return 1
        return 0

    def warshall(self) :
        '''
        Função para fazer algoritmo de warshall
        :return: Grafo em formato de matriz de alcançabilidade
        '''
        grafo = Grafo(self.N)
        List = deepcopy(self.M)
        self.retira_arestas(List)
        for i in range(len(self.N)) :
            for j in range(len(self.N)) :
                if List[j][i] >= 1:
                    for k in range(len(self.N)) :
                        List[j][k] = max(List[j][k], List[i][k])
        grafo.M = List
        return grafo

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
        while (PI[V] != inf and cond):
            print(BETA)
            print(FI)
            print(PI)
            print()
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
            if r == 0 :
                cond = False
            else :
                FI[r] = 1
                W = r
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
        # if not self.DijkstraDrone(U, V, GAS, QTDE_GAS, ESTACOES) :
        #     if not self.DijkstraDrone(V, U, GAS, QTDE_GAS, ESTACOES) :
        #         return 'Caminho não encontrado!'
        #     else :
        #         return self.DijkstraDrone(V, U, GAS, QTDE_GAS, ESTACOES)[::-1]
        # else :
        return self.DijkstraDrone(U, V, GAS, QTDE_GAS, ESTACOES)

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