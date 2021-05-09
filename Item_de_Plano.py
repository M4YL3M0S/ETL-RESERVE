class Item_de_Plano (object):

    def __init__(self,id, nome, categoria, classe, duracao, permiteDataForaVigencia, valorUnitario,
                 unidade, tipoVeiculo):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.classe = classe
        self.datafim = datafim
        self.duracao = duracao
        self.permiteDataForaVigencia = permiteDataForaVigencia
        self.valorUnitario = valorUnitario
        self.unidade = unidade
        self.tipoVeiculo = tipoVeiculo

    def as_list(self):
        return [self.id, self.nome, self.categoria, self.classe, self.duracao,
                self.permiteDataForaVigencia, self.valorUnitario, self.unidade, self.tipoVeiculo]