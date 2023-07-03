from mesa import Agent
from src.agents.zangao import Zangao

class Defensora(Agent):
    def __init__(self, unique_id, model, pos):
        super().__init__(unique_id, model)
        self.tipo = "Defensora"
        self.vida_maxima = 120
        self.vida = self.vida_maxima
        self.poder_ataque = 10
        self.pos = pos

    def step(self):
        self.vida -= 1

    def detecta_ameaca(self):
        neighbors = self.model.grid.get_neighbors(self.pos, moore=True)
        for neighbor in neighbors:
            if isinstance(neighbor, Zangao):
                # Verifica se o zangão pertence à mesma colmeia
                if neighbor.colmeia == self.colmeia:
                    continue
                print("Ameaça detectada!")  # Adiciona o print para verificar se a função é chamada
                return True
        return False

    def attack(self):
        if self.detecta_ameaca():
            neighbors = self.model.grid.get_neighbors(self.pos, moore=True)
            for neighbor in neighbors:
                if isinstance(neighbor, Zangao):
                    # Verifica se o zangão pertence à mesma colmeia
                    if neighbor.colmeia == self.colmeia:
                        continue
                    self.model.kill_list.append(neighbor)
