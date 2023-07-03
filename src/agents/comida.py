from mesa import Agent
from src.utils import random_pos
import random

class Flor(Agent):
    def __init__(self, current_id, model, pos, nectar, tipo):
        super().__init__(current_id, model)
        self.pos = pos
        self.nectar = nectar
        self.tipo = "Flor"
        
        print(f'Nectar: {self.nectar}')

    def step(self):
        # if self.nectar <= 0 # if self.flores <= 0:
        #     self.cria_flores()
        if self.nectar <= 0:
            self.remove_flor()

    def remove_flor(self):
        # self.flores -= 1
        if not self.pos is None: 
            self.model.grid.remove_agent(self)

    def come(self):
        if self.nectar > 0:
            self.nectar -= 1


# class Comida(Agent):
#     def __init__(self, current_id, model, raio_flor):
#         super().__init__(current_id, model)
#         self.pos = (0,0)
#         self.raio = raio_flor
#         self.flores = 0
#         self.cria_flores()

#     def cria_flores(self):
#         xInitial, yInitial = random_pos(
#             self.model.width- self.raio,
#             self.model.height-self.raio
#         )

#         for flor_pos in self.gera_posicoes_flores(xInitial, yInitial):
#             flor = Flor(self.model.next_id(), self.model, flor_pos, self, random.randint(1, 25))
#             self.model.register(flor)
#             self.flores += 1

#     def gera_posicoes_flores(self, xInitial, yInitial):
#         in_circle = lambda x, y: (x)**2 + (y)**2 <= 20**2 # test self.raio**2
#         posis = []
#         #for x in range(-self.raio, self.raio+1):
#         #test
#         for x in range(-5, 5):
#             for y in range(-5, 5):
#                 if in_circle(x, y):
#                     posis.append((x+xInitial, y+yInitial))
        
#         return posis
