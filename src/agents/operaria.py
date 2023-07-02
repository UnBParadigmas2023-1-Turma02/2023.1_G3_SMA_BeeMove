from mesa import Agent



class Operaria(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.tipo = "Operaria"
        self.vida_maxima = 80
        self.vida = self.vida_maxima