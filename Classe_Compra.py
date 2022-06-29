from Classe_Estoque import *

class Compra:
    def __init__(self):
        self.entrada = Estoque()

    def comprar(self):
        prod = 0
        entrada = input('Informe o codigo do Produto: ')
        for i in range(len(self.entrada.listaProd)):
            if entrada == self.entrada.listaProd[i].cod:
                self.entrada.listaProd[i].quat += int(input('Informe a quantidade comprada: '))
            else:
                prod += 1
                if prod == len(self.entrada.listaProd):
                    print('Codigo não cadastrado!')