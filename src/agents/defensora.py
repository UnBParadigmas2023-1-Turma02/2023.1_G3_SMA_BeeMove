from mesa import Agent


class Defensora(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.tipo = "Defensora"
        self.vida_maxima = 120
        self.vida = self.vida_maxima
        self.poder_ataque = 10
        self.pos = pos