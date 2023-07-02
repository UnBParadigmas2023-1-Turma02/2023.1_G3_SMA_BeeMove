from mesa import Agent
from src.utils import random_pos

class Flor(Agent):
    def __init__(self, current_id, model, pos, flor):
        super().__init__(current_id, model)
        self.pos = pos
        self.flor = flor

    def come(self):
        self.flor.remove_flor(self)


class Comida(Agent):
    def __init__(self, current_id, model, raio_flor):
        super().__init__(current_id, model)
        self.pos = (0,0)
        self.raio = raio_flor
        self.flores = 0
        self.cria_flores()

    def step(self):
        if self.flores == 0:
            self.cria_flores()

    def remove_flor(self, flor):
        self.model.grid.remove_agent(flor)
        self.flores -= 1

    def cria_flores(self):
        xInitial, yInitial = random_pos(
            self.model.width- self.raio,
            self.model.height-self.raio
        )

        for flor_pos in self.gera_posicoes_flores(xInitial, yInitial):
            flor = Flor(self.model.next_id(), self.model, flor_pos, self)
            self.model.register(flor)
            self.flores += 1

    def gera_posicoes_flores(self, xInitial, yInitial):
        in_circle = lambda x, y: (x)**2 + (y)**2 <= self.raio**2

        for x in range(-self.raio, self.raio+1):
            for y in range(-self.raio, self.raio+1):
                if in_circle(x, y):
                    yield (x+xInitial, y+yInitial)