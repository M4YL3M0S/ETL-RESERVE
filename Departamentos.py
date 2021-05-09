class Departamentos (object):

    def __init__(self,id, nome, empresa, grupo):
        self.id = id
        self.nome = nome
        self.nome = nome
        self.empresa = empresa
        self.grupo = grupo


    def as_list(self):
        return [self.id, self.nome, self.empresa, self.grupo]