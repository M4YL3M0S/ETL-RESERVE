class Despesa (object):

    def __init__(self, id, formaPagto, nomeDespesa, tipoDeDespesa, categoriaDeDespesa, data,
                 reembolsavel, moeda, idSolicitante, territorio, status, idPlano, dataCriacao):
        self.id = id
        self.formaPagto = formaPagto
        self.nomeDespesa = nomeDespesa
        self.tipoDeDespesa = tipoDeDespesa
        self.categoriaDeDespesa = categoriaDeDespesa
        self.data = data
        self.reembolsavel = reembolsavel
        self.moeda = moeda
        self.idSolicitante = idSolicitante
        self.territorio = territorio
        self.status = status
        self.idPlano = idPlano
        self.dataCriacao = dataCriacao

    def as_list(self):
        return [self.id, self.formaPagto, self.nomeDespesa, self.tipoDeDespesa,
                self.categoriaDeDespesa, self.data, self.reembolsavel, self.moeda,
                self.idSolicitante, self.territorio, self.status, self.idPlano, self.dataCriacao]