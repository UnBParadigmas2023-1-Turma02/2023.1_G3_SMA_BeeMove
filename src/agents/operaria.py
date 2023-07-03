from mesa import Agent, Model

from src.agents.comida import Flor
from src.utils import calculate_distance


class Operaria(Agent):
    def __init__(self, current_id, model: Model, pos, posRainha):
        super().__init__(current_id, model)
        self.tipo = "Operaria"
        self.alimento = 0
        self.vida_maxima = 80
        self.pos = pos
        self.polen = 0
        self.posRainha = posRainha
        self.vida = self.vida_maxima
        self.raio = 10
        self.nearby_flowers: list[Agent] = []

    def goto_rainha(self):

        if self.posRainha:
            dx = self.posRainha.pos[0] - self.pos[0]    
            dy = self.posRainha.pos[1] - self.pos[1]

            xAtual = self.pos[0]
            yAtual = self.pos[1]

            if dx > 0:
               xAtual += 1
            elif dx < 0:                      
                xAtual -= 1
            
            if dy > 0:
                yAtual += 1
            elif dy < 0:                      
                yAtual -= 1
            
            self.model.grid.move_agent(self, (xAtual, yAtual))
 

    def move(self):
        x, y = self.pos
        # cellmates = self.model.grid.iter_neighborhood(self.pos, True, False,  math.inf)
        for agent in self.model.schedule.agent_buffer():
            if isinstance(agent, Flor):
                if self.model.grid.get_neighborhood(self.pos, True, False, self.raio): # calculate_distance((x, y), agent.pos) <= self.raio:
                    self.nearby_flowers.append(agent)
                    # print(len self.self.nearby_flowers)
        if self.alimento > 0:
            self.goto_rainha()

        elif self.nearby_flowers:
            # Ordena as flores com base na distância da abelha operária
            self.nearby_flowers.sort(key=lambda flower: calculate_distance((x, y), flower.pos))

            # Obtém a posição da flor mais próxima
            if not self.nearby_flowers[0].pos is None:
                target_x = self.nearby_flowers[0].pos[0]
                target_y = self.nearby_flowers[0].pos[1]

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
        self.verificaRainha()
        self.vida -= 1
        # self.alimentaRainha(self.model.get_agent_by_type(AbelhaRainha))  # Substitua 'Rainha' pelo nome da classe da rainha

    def verificaRainha(self):
        agents = self.model.grid.get_cell_list_contents(self.pos)
        for a in agents:
            if a.tipo == 'Rainha':
                self.alimentaRainha(a)                 

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
            agentes: list[Flor] = self.model.grid.get_cell_list_contents((x, y))
            for agente in agentes:
                # Se o agente econtrado for uma flor, ela é coletada pela operaria

                if isinstance(agente, Flor):
                    if self.polen > 3 and agente.pos:
                        print("Creating flower")
                        flor = Flor(
                                self.model.next_id(), 
                                self.model, 
                                (self.random.randint(0, agente.pos[0] + 7 % self.model.grid.width), 
                                self.random.randint(0, (agente.pos[1] + 7) % self.model.grid.height )), 
                                self.random.randint(1, 5), "Flor")
                        self.polen = 0
                        self.model.register(flor)

                    else: self.polen += 1

                    self.vida -= 2
                    self.alimento += 1
                    agente.come()


    def alimentaRainha(self, agent):
        if agent.tipo == "Rainha":
            agent.alimentar_rainha(self)
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
