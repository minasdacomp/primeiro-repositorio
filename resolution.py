#GABRIELA MARCULINO
#HOW TO COMPILE ON LINUX/WINDOWS: nome da pasta/python3 resolution.py
#PYTHON VERSION: 3.10.2 64-bit
#COMPLEXITY: O(N+M)

# A classe “ReqList” é a classe principal do programa e é responsável por criar a lista de
# requisitos e gerenciar as operações relacionadas a ela. Na inicialização da classe, o usuário é
# solicitado a inserir a quantidade de requisitos a serem criados, bem como os nomes de cada
# requisito. Para cada requisito, um objeto da classe Requirement é criado e adicionado à lista
# de requisitos. Em seguida, é exibido um menu de opções para o usuário escolher o que fazer:
# adicionar pré-requisitos a um determinado requisito, exibir a lista de requisitos com
# informações sobre as dependências de cada requisito ou exibir a ordem ideal de instalação
# dos requisitos.
class ReqList:
    def __init__(self):
        self.reqsList = []
        reqAmount = int(input('Requirement amount: '))
        for i in range(reqAmount):
            reqName = input(f'  Requirement {i+1}: ')
            req = Requirement(reqName)
            self.reqsList.append(
                [req, reqName, req.pointed_by, req.pointing_to])

        self.menu()

    def menu(self):
        print('\n\t#### MENU ####')
        print('\t1 - Add pre-reqs')
        print('\t2 - Show list')
        print('\t3 - Show best order to install')
        option = int(input('Option: '))
        if (option == 1):
            self.addPreReqs()
        elif (option == 2):
            self.showList()
        elif (option == 3):
            self.showBestOrder()
            return
        else:
            print('Invalid option')

        self.menu()

    # função “getReqByName” da classe “ReqList” é responsável por buscar um determinado
    # requisito na lista de requisitos pelo nome e retornar o objeto Requirement correspondente. A
    # função “reqListLen” retorna o tamanho atual da lista de requisitos'''
    def getReqByName(self, name):
        for req in self.reqsList:
            if req[1] == name:  # req[1] is the name of the requirement
                return req[0]  # req[0] is the object address

        return None  # if the requirement is not found

    def reqListLen(self):
        return len(self.reqsList) #return the list's length

    # A função “addPreReqs” permite ao usuário adicionar pré-requisitos a um determinado
    # requisito, atualizando a lista de requisitos que o requisito atual aponta e a lista de requisitos
    # que apontam para ele, bem como as contagens correspondentes.
    def addPreReqs(self):
        to_add = input('Requirement to add pre-reqs:')
        req = self.getReqByName(to_add)
        if req is None:
            print('Requirement not found')
            return

        pre_reqs = input('Pre-reqs (separated by space):').split(' ')
        for pre_req in pre_reqs:
            pre_req = self.getReqByName(pre_req)
            if pre_req is None:
                print(f'Requirement {pre_req} not found')
                return

            if pre_req in req.points_to_list:
                print(f'Requirement {pre_req} already in pre-reqs')
                return

            req.points_to_list.append(pre_req)
            pre_req.pointed_by_list.append(req)
            pre_req.pointed_by += 1
            req.pointing_to += 1

    # A função "show List" exibe a lista de requisitos atual com informações sobre as dependências
    # de cada requisito.
    def showList(self):
        for req in self.reqsList:
            print(
                f'{req[1]}: Pointed by {req[0].pointed_by} | Points to {req[0].pointing_to}')
    
    # A função “showBestOrder” exibe a ordem ideal de instalação dos requisitos. Essa função foi
    # implementada usando um algoritmo de ordenação, que funciona removendo iterativamente os
    # requisitos que não têm dependências, adicionando-os à ordem ideal e atualizando as
    # dependências dos requisitos restantes na lista. O resultado é uma lista ordenada dos requisitos
    # que atende a todas as dependências'''
    def showBestOrder(self):
        bestOrder = []
        while (self.reqListLen() > 0):
            tempLen = self.reqListLen()
            for req in self.reqsList:
                if req[0].pointing_to == 0:
                    for pre_req in req[0].pointed_by_list:
                        pre_req.points_to_list.remove(req[0])
                        pre_req.pointing_to -= 1

                    bestOrder.append(req[1])
                    self.reqsList.remove(req)

        print((' ').join(bestOrder))

# A classe “Requirement” é uma classe simples que tem como objetivo armazenar informações
# sobre um determinado requisito, tais como os requisitos que ele aponta e os requisitos que
# apontam para ele, além do nome do requisito em si. Os requisitos seriam os termos A, B, C,
# D, E… e assim sucessivamente.
class Requirement:
    def __init__(self, name):
        self.points_to_list = []
        self.pointed_by_list = []
        self.pointed_by = 0
        self.pointing_to = 0
        self.name = name


projectX = ReqList()
