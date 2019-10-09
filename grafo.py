class VerticeInvalidoException(Exception):
    pass


class ArestaInvalidaException(Exception):
    pass


class Grafo:
    QTDE_MAX_SEPARADOR = 1
    SEPARADOR_ARESTA = '-'

    def __init__(self, N=[], A={}):
        '''
        Constrói um objeto do tipo Grafo. Se nenhum parâmetro for passado, cria um Grafo vazio.
        Se houver alguma aresta ou algum vértice inválido, uma exceção é lançada.
        :param N: Uma lista dos vértices (ou nodos) do grafo.
        :param V: Uma dicionário que guarda as arestas do grafo. A chave representa o nome da aresta e o valor é uma string que contém dois vértices separados por um traço.
        '''
        for v in N:
            if not (Grafo.verticeValido(v)):
                raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

        self.N = N

        for a in A:
            if not (self.arestaValida(A[a])):
                raise ArestaInvalidaException('A aresta ' + A[a] + ' é inválida')

        self.A = A

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

        # Verifica se as arestas antes de depois do elemento separador existem no Grafo
        if not (self.existeVertice(aresta[:i_traco])) or not (self.existeVertice(aresta[i_traco + 1:])):
            return False

        return True

    @classmethod
    def verticeValido(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro está dentro do padrão estabelecido.
        Um vértice é um string qualquer que não pode ser vazio e nem conter o caractere separador.
        :param vertice: Um string que representa o vértice a ser analisado.
        :return: Um valor booleano que indica se o vértice está no formato correto.
        '''
        return vertice != '' and vertice.count(Grafo.SEPARADOR_ARESTA) == 0

    def existeVertice(self, vertice=''):
        '''
        Verifica se um vértice passado como parâmetro pertence ao grafo.
        :param vertice: O vértice que deve ser verificado.
        :return: Um valor booleano que indica se o vértice existe no grafo.
        '''
        return Grafo.verticeValido(vertice) and self.N.count(vertice) > 0

    def existeAresta(self, aresta=''):
        '''
        Verifica se uma aresta passada como parâmetro pertence ao grafo.
        :param aresta: A aresta a ser verificada
        :return: Um valor booleano que indica se a aresta existe no grafo.
        '''
        existe = False
        if Grafo.arestaValida(self, aresta):
            for k in self.A:
                if aresta == self.A[k]:
                    existe = True

        return existe

    def adicionaVertice(self, v):
        '''
        Adiciona um vértice no Grafo caso o vértice seja válido e não exista outro vértice com o mesmo nome
        :param v: O vértice a ser adicionado
        :raises: VerticeInvalidoException se o vértice passado como parâmetro não puder ser adicionado
        '''
        if self.verticeValido(v) and not self.existeVertice(v):
            self.N.append(v)
        else:
            raise VerticeInvalidoException('O vértice ' + v + ' é inválido')

    def adicionaAresta(self, nome, a):
        '''
        Adiciona uma aresta no Grafo caso a aresta seja válida e não exista outra aresta com o mesmo nome
        :param v: A aresta a ser adicionada
        :raises: ArestaInvalidaException se a aresta passada como parâmetro não puder ser adicionada
        '''
        if self.arestaValida(a):
            self.A[nome] = a
        else:
            ArestaInvalidaException('A aresta ' + self.A[a] + ' é inválida')

#### ROTEIRO 1 #########################################################################################################

    def vertices_nao_adjacentes(self):
        '''
        Acha os vértices não adjacentes de um determinado grafo
        :return: Lista com os possíveis vértices não adjacentes
        '''
        vertices = list()
        for i in self.N:
            for j in self.N:
                v = i + self.SEPARADOR_ARESTA + j
                if v not in self.A.values() and v[::-1] not in self.A.values():
                    vertices.append(v)
        return vertices

    def ha_laco(self):
        '''
        Verifica se um grafo possui um laço
        :return: True para a existência de um laço, e False para o contrário
        '''
        for i in self.N:
            v = i + self.SEPARADOR_ARESTA + i
            if v in self.A.values():
                return True
        return False

    def ha_paralelas(self):
        '''
        Verifica se um grafo possui um arestas paralelas
        :return: True para a existência de uma aresta paralela, e False para o contrário
        '''
        for i in self.N:
            for j in self.N:
                v = i + self.SEPARADOR_ARESTA + j
                cont = 0
                for k in self.A.values():
                    if k == v:
                        cont += 1
                if cont > 1:
                    return True
        return False

    def grau(self, v):
        '''
        Conta quantas arestas incidem em um determinado vértice, ou seja, verifica seu grau
        :return: grau do vértice
        '''
        cont = 0
        for i in self.A.values():
            if v in i:
                cont += 1
        return cont

    def arestas_sobre_vertice(self, v):
        '''
        Adiciona a arestas que incidem em um dado vértice
        :return: lista de arestas
        '''
        arestas = list()
        for i in self.A.keys():
            if v in self.A[i]:
                arestas.append(i)
        return arestas

    def eh_completo(self):
        '''
        Verifica se um grafo é completo
        :return: True para se ele for completo, False para o contrário
        '''
        cond = True
        contM = 0
        if len(self.N) == 1:
            return True
        else:
            while cond:
                for i in self.N:
                    cont = 0
                    for j in self.N:
                        if i != j:
                            if self.existeAresta(i + '-' + j) or self.existeAresta(j + '-' + i):
                                cond = True
                                cont += 1
                            else:
                                return False
                            if cont == (len(self.N) - 1):
                                contM += 1
                    if contM == len(self.N):
                        return True

#### ROTEIRO 2 #########################################################################################################

    def __arestas_e_vertices_adjacentes(self, VerticeEntrada):
        '''
        Descobre quais vértices estam ligados em VerticeEntrada e quais arestas incidem em VerEntrada
        A ordenação das arestas é de acordo com a ligação de VerticeEntrada com os vertices adjacentes
        :param VerticeEntrada: um vértice de entrada
        :return: lista de vértices e arestas
        '''
        VerticesAdjacentes, ArestasAdjacentes = list(), list()
        for i in self.N:
            Ver1 = VerticeEntrada + self.SEPARADOR_ARESTA + i
            for j in self.A.keys():
                if self.A[j] == Ver1 or self.A[j] == Ver1[::-1] and VerticeEntrada != i:
                    VerticesAdjacentes.append(Ver1[-1])
                    ArestasAdjacentes.append(j)
        return VerticesAdjacentes, ArestasAdjacentes

    def __RETIRA(self, Vertice, ListaVertice, ListaAresta):
        '''
        Remove um dado Vertice se ele estiver em ListaVertice, é removido também uma aresta
        de acordo com a posição do Vertice
        :param Vertice: Vertice para verificação
        :param ListaVertice: Lista de vértices
        :param ListaAresta: Lista de arestas
        :return: Lista de vértices e arestas com modificações
        '''
        for i in range(len(ListaVertice)) :
            if Vertice == ListaVertice[i] :
                ListaVertice.remove(ListaVertice[i])
                ListaAresta.remove(ListaAresta[i])
                break
        return ListaVertice, ListaAresta

    def __DFS(self, VerticesVisitados, ArestasPercorridas, VerticeAtual):
        '''
        Recursão para perrcorrer um grafo não-direcionado e adicionando vértices e arestas visitados em lista
        :param VerticesVisitados: lista com vértices visitados
        :param ArestasPercorridas: lista com arestas percoridas
        :param VerticeAtual: Vértice de entrada
        :return: recursão
        '''
        if VerticeAtual in VerticesVisitados:
            return
        else:
            VerticesVisitados.append(VerticeAtual)
            VerticesAdjacentes, ArestasAdjacentes = self.__arestas_e_vertices_adjacentes(VerticeAtual)
            while True:
                if len(VerticesAdjacentes) == 0 or len(VerticesVisitados) == len(self.N):
                    return
                else:
                    for i in range(len(VerticesVisitados)):
                        for j in range(len(VerticesVisitados)):
                            VerticesAdjacentes, ArestasAdjacentes = self.__RETIRA(VerticesVisitados[j], VerticesAdjacentes, ArestasAdjacentes)
                    if len(VerticesAdjacentes) > 0 and len(ArestasAdjacentes) > 0:
                        Aux1 = VerticesAdjacentes[0]
                        Aux2 = ArestasAdjacentes[0]
                        if Aux1 not in VerticesVisitados:
                            ArestasPercorridas.append(Aux2)
                        VerticesAdjacentes.remove(Aux1)
                        ArestasAdjacentes.remove(Aux2)
                        self.__DFS(VerticesVisitados, ArestasPercorridas, Aux1)
                    else :
                        return

    def startDFS(self):
        '''
        Função para starta a funçâo DFS! Contêm listas para ir adicionando vértices e arestas!
        :return: um grafo direcionando do tipo list
        '''
        VerticesVisitados = list()
        ArestasPercorridas = list()
        self.__DFS(VerticesVisitados, ArestasPercorridas, self.N[0])
        ArvoreDFS = list()
        for i, j in zip(VerticesVisitados, ArestasPercorridas):
            if VerticesVisitados != []:
                ArvoreDFS.append(i)
            if ArestasPercorridas != []:
                ArvoreDFS.append(j)
        ArvoreDFS.append(VerticesVisitados[-1])
        return ArvoreDFS

#### ROTEIRO 3 #########################################################################################################

    def eh_conexo(self):
        '''
        Função para saber se um grafo é conexo
        :return:
        '''
        cond = True
        List = self.startDFS();
        for i in self.N :
            if i not in List :
                cond = False
                break
        return cond

    def __CAMINHO(self, VerticesVisitados, ArestasPercorridas, VerticeAtual, Comprimento, Vertices):
        '''
        Função para percorrer um grafo de acordo com um comprimento!
        :param VerticesVisitados: Lista onde seram adicionados os vertices visitados
        :param ArestasPercorridas: Lista onde seram adicionados os arestas percorridas
        :param VerticeAtual: Vertice atual
        :param Comprimento: Comprimento para percorrer o grafo
        :param Vertices: Lista com todos os vertices visitados! Possui função diferente do VerticeVisitados
        :return: True se achar um caminho ou False se percorrer o grafo todo e não achar um caminho
        '''
        if VerticeAtual in VerticesVisitados:
            return
        else:
            VerticesVisitados.append(VerticeAtual)
            if VerticeAtual not in Vertices :
                Vertices.append(VerticeAtual)
            Tam = len(VerticesVisitados)
            if Tam - 1 == Comprimento:
                Vertices = []
                return True
            if len(Vertices) == len(self.N):
                return False
            VerticesAdjacentes, ArestasAdjacentes = self.__arestas_e_vertices_adjacentes(VerticeAtual)
            while True:
                for i in range(len(VerticesVisitados)) :
                    for j in range(len(VerticesVisitados)):
                        VerticesAdjacentes, ArestasAdjacentes = self.__RETIRA(VerticesVisitados[j], VerticesAdjacentes, ArestasAdjacentes)
                if len(VerticesAdjacentes) > 0 and len(ArestasAdjacentes) > 0:
                    Aux1 = VerticesAdjacentes[0]
                    Aux2 = ArestasAdjacentes[0]
                    if Aux1 not in VerticesVisitados:
                        ArestasPercorridas.append(Aux2)
                    VerticesAdjacentes.remove(Aux1)
                    ArestasAdjacentes.remove(Aux2)
                    self.__CAMINHO(VerticesVisitados, ArestasPercorridas, Aux1, Comprimento, Vertices)
                    Tam = len(VerticesVisitados)
                    if Tam - 1 == Comprimento:
                        return True
                    if len(Vertices) == len(self.N) :
                        return False
                    VerticesVisitados.remove(VerticesVisitados[-1])
                    ArestasPercorridas.remove(ArestasPercorridas[-1])
                    Tam -= 1
                else :
                    return

    def startCAMINHO(self, Comprimento):
        '''
        Dado um comprimento, a função tenta achar um caminho com o comprimeto dado!
        :param Comprimento: Comprimento para achar um caminho
        :return: Um caminho ou False
        '''
        Caminhos = []
        for k in self.N :
            VerticesVisitados = list()
            ArestasPercorridas = list()
            Vertices = []
            cond = self.__CAMINHO(VerticesVisitados, ArestasPercorridas, k, Comprimento, Vertices)
            caminho = list()
            if cond :
                for i, j in zip(VerticesVisitados, ArestasPercorridas):
                    if VerticesVisitados != []:
                        caminho.append(i)
                    if ArestasPercorridas != []:
                        caminho.append(j)
                caminho.append(VerticesVisitados[-1])
                return caminho
        return False

    def __ha_ciclo(self, VerticeAtual, VerticesG, Ciclo, VerticesAnterior):
        '''
        Função recursiva para achar um ciclo! Sua parada é quando o ultimo vértice de Ciclo, estiver em Ciclo[:-1],
        ou seja, é "excluido" o ultímo termo para não fazer comparação com ele mesmo!
        :param VerticeAtual: vertice atual
        :param VerticesG: Vertices percorridos
        :param Ciclo: Provável ciclo da grafo
        :param VerticesAnterior: Vértice anterior para remoção do mesmo em lista posteriores
        :return:Um Ciclo ou None
        '''
        if Ciclo != [] and VerticeAtual == Ciclo[-1]:
            return
        else:
            Ciclo.append(VerticeAtual)
            if VerticeAtual not in VerticesG :
                VerticesG.append(VerticeAtual)
            if Ciclo[-1] in Ciclo[:-1] :
                return Ciclo
            VerticesAdjacentes, ArestasAdjacentes = self.__arestas_e_vertices_adjacentes(VerticeAtual)
            while True:
                if len(VerticesAdjacentes) == 0 :
                    return
                else:
                    for i in range(len(VerticesAdjacentes)) :
                        if VerticesAdjacentes[i] == VerticesAnterior :
                            VerticesAdjacentes.remove(VerticesAdjacentes[i])
                            ArestasAdjacentes.remove(ArestasAdjacentes[i])
                            break
                    if len(VerticesAdjacentes) > 0 and len(ArestasAdjacentes) > 0:
                        Aux1 = VerticesAdjacentes[0]
                        Aux2 = ArestasAdjacentes[0]
                        for i in range(len(VerticesAdjacentes)) :
                            if VerticesAdjacentes[i] in Ciclo[:-1] :
                                Aux1 = VerticesAdjacentes[i]
                                Aux2 = ArestasAdjacentes[i]
                                break
                        Ciclo.append(Aux2)
                        VerticesAdjacentes.remove(Aux1)
                        ArestasAdjacentes.remove(Aux2)
                        VerticesAnterior = VerticeAtual
                        self.__ha_ciclo(Aux1, VerticesG, Ciclo, VerticesAnterior)
                        if Ciclo[-1] in Ciclo[:-1]:
                            return Ciclo
                        for i in range(2) :
                            Ciclo.remove(Ciclo[-1])
                    else :
                        return

    def startHACILO(self):
        '''
        Função para starta o ha_ciclo! Só retorna False quando nada é retornado na repetição
        :return: Um ciclo ou False
        '''
        for i in range(len(self.N)) :
            VerticesG = []
            Ciclo = []
            cond = (self.__ha_ciclo(self.N[i], VerticesG, Ciclo, '0'))
            if cond != None :
                if cond[0] == cond[-1] :
                    return cond
                else :
                    while cond[0] != cond[-1] :
                        cond.remove(cond[0])
                    return cond
        return False

########################################################################################################################

    def __str__(self):
        '''
        Fornece uma representação do tipo String do grafo.
        O String contém um sequência dos vértices separados por vírgula, seguido de uma sequência das arestas no formato padrão.
        :return: Uma string que representa o grafo
        '''
        grafo_str = ''

        for v in range(len(self.N)):
            grafo_str += self.N[v]
            if v < (len(self.N) - 1):  # Só coloca a vírgula se não for o último vértice
                grafo_str += ", "

        grafo_str += '\n'

        for i, a in enumerate(self.A):
            grafo_str += self.A[a]
            if not (i == len(self.A) - 1):  # Só coloca a vírgula se não for a última aresta
                grafo_str += ", "

        return grafo_str