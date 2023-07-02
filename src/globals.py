class Globals:

    def __init__(self):
        self.qtd_abelhas = 0
        self.qtd_defensoras = 0
        self.qtd_zangoes = 0
        self.qtd_operarias = 0
    
    def get_qtd_abelhas(self):
        return self.qtd_defensoras + self.qtd_zangoes + self.qtd_operarias

    def get_qtd_defensoras(self):
        return self.qtd_defensoras

    def get_qtd_zangoes(self):
        return self.qtd_zangoes
    
    def get_qtd_operarias(self):
        return self.qtd_operarias

    def set_qtd_abelhas(self):
        self.qtd_abelhas += 1

    def set_qtd_defensoras(self):
        self.qtd_defensoras += 1

    def set_qtd_zangoes(self):
        self.qtd_zangoes += 1

    def set_qtd_operarias(self):
        self.qtd_operarias += 1