
from mesa import Agent
from src import utils
from src.agents.defensora import Defensora
from src.agents.operaria import Operaria
from src.agents.zangao import Zangao


class AbelhaRainha(Agent):
    def __init__(self, current_id, model, pos):
        super().__init__(current_id, model)
        self.pos = pos
        self.home = pos
        self.tipo = "Rainha"
        self.vida_maxima = 100
        self.vida = self.vida_maxima
        self.reproduzir_intervalo = 10
        self.reproduzir_contagem = self.reproduzir_intervalo

    def step(self):
        # Verifica a vida da abelha rainha e se adiciona na lista de mortos
        if self.vida <= 0:
            pass
            # self.model.kill_agents.append(self)
        else:
            self.vida -= 1
            
        # Verificar se é hora de reproduzir
        if self.reproduzir_contagem <= 0:
            self.reproduzir(self)
            self.reproduzir_contagem = self.reproduzir_intervalo
        else:
            self.reproduzir_contagem -= 1
        
        

    def reproduzir(self, agent):
        # self.model.create_bee(self)
        # Criar novas abelhas na colmeia (modelo)
        num_filhotes = utils.get_random_number(1,4)

        for _ in range(num_filhotes):
            radius = utils.get_random_number(1, 20)
            xInitial = agent.pos[0] - (radius + utils.get_random_number(-3,3))
            yInitial = agent.pos[1] - (radius + utils.get_random_number(-3,3))
            probabilidade = utils.get_random_number(0, 100)
            
            if probabilidade <= 10:
                abelha = Zangao(self.model.next_id(), self.model, (xInitial,yInitial),  self)
            elif probabilidade <= 50:
                abelha = Defensora(self.model.next_id(), self.model,(xInitial,yInitial))
            elif probabilidade <= 100:
                abelha = Operaria(self.model.next_id(), self.model,(xInitial,yInitial))
                
            self.model.create_bee(abelha)