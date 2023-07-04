from datetime import datetime

class pessoa(object):
    "Classe pessoa"

    def __init__(self, nome, idade, pais = None):
        
        self.nome = nome
        self.idade = idade
        self.criacao = datetime.today()
        self.pais = pais
        self.filhos = []
        
        print('Criado', self.nome,'Idade', self.idade)

    def setName(self, nome):
        self.nome = nome
        print('Atualização nome ', self.nome)

    def setAge(self, idade):
        self.idade = idade
        print('Atualização idade', self.idade)

    def addChild(self, nome, idade):
        crianca = pessoa(nome, idade, pais = self)
        self.filhos.append(crianca)
        print(self.nome,'Adicionado criança', crianca.nome)

    def listChildren(self):
        
        if len(self.filhos)>0:
            print(self.nome,'Tem filhos: ')
        
            for c in self.filhos:
                print(' ',c.nome)
        
        else:
            print(self.nome,'Não tem filhos')

    def getChildren(self):
        return self.filhos