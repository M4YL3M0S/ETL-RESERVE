class Centro_de_custo (object):

    def __init__(self, id, name):
        self.id = id
        self.name = name


    def as_list(self):
        return [self.id,
                self.name]
