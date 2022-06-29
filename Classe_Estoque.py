from Classe_Produtos import *

class Estoque:
    def __init__(self):
        self.listaProd = []

    def salvar_cadastro(self):
        entrada_cod = input('Informe o codigo: ')
        entrada_nome = input('Informe o nome: ')
        entrada_fabt = input('Informe o fabricante: ')
        self.listaProd.append(Produtos(entrada_cod, entrada_nome, entrada_fabt))
        print('Cadastro realizado com sucesso!')

    def lista_codp(self):
        prod = 0
        entrada = input('Informe o codigo do Produto: ')
        for i in range(len(self.listaProd)):
            if entrada == self.listaProd[i].cod:
                print('Codigo:', self.listaProd[i].cod,
                      '- Nome:', self.listaProd[i].nome,
                      '- Fabricante', self.listaProd[i].fabt,
                      '- Quantidade:', self.listaProd[i].quat)
            elif prod == '':
                print('Codigo:', self.listaProd[i].cod,
                      '- Nome:', self.listaProd[i].nome,
                      '- Fabricante', self.listaProd[i].fabt,
                      '- Quantidade:', self.listaProd[i].quat)
            else:
                prod += 1
                if prod == len(self.listaProd):
                    print('Codigo não cadastrado!')

    def lista_produtos(self):
        for i in range(len(self.listaProd)):
            print('Codigo:', self.listaProd[i].cod,
                  '- Nome:', self.listaProd[i].nome,
                  '- Fabricante:', self.listaProd[i].fabt,
                  '- Quantidade:', self.listaProd[i].quat)

    def alterar_nome(self):
        prod = 0
        entrada = input('Informe o codigo do Produto: ')
        for i in range(len(self.listaProd)):
            if entrada == self.listaProd[i].cod:
                self.listaProd[i].nome = input('Alterar Nome: ')
            else:
                prod += 1
                if prod == len(self.listaProd):
                    print('Codigo não cadastrado!')