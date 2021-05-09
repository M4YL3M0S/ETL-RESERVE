class Usuarios(object):

    def __init__(self, id, matricula, nome, celular, email, perfilPolitica, perfilAcesso,
                 suspenso, ausente, departamento):
        self.id = id
        self.nome = nome
        self.email = email
        self.celular = celular
        self.matricula = matricula
        self.perfilPolitica = perfilPolitica
        self.perfilAcesso = perfilAcesso
        self.suspenso = suspenso
        self.ausente = ausente
        self.departamento = departamento

    def as_list(self):
        return [self.id, self.nome, self.email, self.celular, self.matricula,
                self.perfilPolitica, self.perfilAcesso, self.suspenso, self.ausente, self.departamento]