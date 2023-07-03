from mesa import Agent
from src.agents.comida import Flor
import math
from src.utils import calculate_distance

class Operaria(Agent):
    def __init__(self, current_id, model, pos, posRainha):
        super().__init__(current_id, model)
        self.tipo = "Operaria"
        self.alimento = 0
        self.vida_maxima = 80
        self.pos = pos
        self.posRainha = posRainha
        self.vida = self.vida_maxima
        self.raio = 10
        # self.posComida = posComida

    def move(self):
        x, y = self.pos
        nearby_flowers = []
        # cellmates = self.model.grid.iter_neighborhood(self.pos, True, False,  math.inf)
        for agent in self.model.schedule.agents:
            if isinstance(agent, Flor):
                if calculate_distance((x, y), agent.pos) <= self.raio:
                    nearby_flowers.append(agent)
                    print(len(nearby_flowers))

        if nearby_flowers:
            # Ordena as flores com base na distância da abelha operária
            nearby_flowers.sort(key=lambda flower: calculate_distance((x, y), flower.pos))

            # Obtém a posição da flor mais próxima
            target_x, target_y = nearby_flowers[0].pos

            # Move-se na direção da flor mais próxima
            if target_x < x:
                x -= 1
            elif target_x > x:
                x += 1

            if target_y < y:
                y -= 1
            elif target_y > y:
                y += 1

            self.model.grid.move_agent(self, (x, y))  # Move a abelha operária para a nova posição

    def step(self):
        self.move()
        self.coletarComida()
        # self.alimentaRainha(self.model.get_agent_by_type(AbelhaRainha))  # Substitua 'Rainha' pelo nome da classe da rainha


    # def step(self):
    #     # Sai da comeia atras de comida
    #     # Depois volta para a comeia

    #         dx = self.posComida.pos[0] - self.pos[0]    
    #         dy = self.posComida.pos[1] - self.pos[1]

    #         xAtual = self.pos[0]
    #         yAtual = self.pos[1]
    #         if dx > 0:
    #            xAtual += 1
    #         elif dx < 0:                      
    #             xAtual -= 1
            
    #         if dy > 0:
    #             yAtual += 1
    #         elif dy < 0:                      
    #             yAtual -= 1

    #         self.model.grid.move_agent(self, (xAtual, yAtual))
    #         if self.pos == self.posComida.pos: #comida

    #             self.vida = -1 #Perde vida quando sai da colmeia
    #             self.coletarComida(self.posComida)
    #             self.vida = -1 #Perde quando volta pra colmeia

    #             if self.vida <= 0:
    #                 self.model.kill_list.append(self)
            
    def coletarComida(self):
            x, y = self.pos
            # Recupera os agentes presente na celula passada
            agentes = self.model.grid.get_cell_list_contents((x, y))
            for agente in agentes:
                # Se o agente econtrado for uma flor, ela é coletada pela operaria
                if isinstance(agente, Flor):
                    self.alimento += 1

    def alimentaRainha(self, agent):
        if agent.tipo == "Rainha":
            agent.alimentar_rainha(self.alimento)
            self.alimento = 0
            

    # def irColmeia(self):
    #         # A posicao da colmeia eh onde ta a rainha, ela nao sai
    #         dx_c = self. self.posRainha.pos[0] - self.pos[0]    
    #         dy_c = self. self.posRainha.pos[1] - self.pos[1]

    #         xAtual_c = self.pos[0]
    #         yAtual_c = self.pos[1]

    #         if dx_c > 0:
    #            xAtual_c += 1
    #         elif dx_c < 0:                      
    #             xAtual_c -= 1
            
    #         if dy_c > 0:
    #             yAtual_c += 1
    #         elif dy_c < 0:                      
    #             yAtual_c -= 1
