from mesa import Agent
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
            self.model.kill_agents.append(self)
        else:
            self.vida -= 1
            
        # Verificar se é hora de reproduzir
        if self.reproduzir_contagem <= 0:
            self.reproduzir()
            self.reproduzir_contagem = self.reproduzir_intervalo
        else:
            self.reproduzir_contagem -= 1
        
        

    def reproduce(self):
        self.model.criar_abelha(self)
        # Criar novas abelhas na colmeia (modelo)
        num_filhotes = self.model.gerar_numero_aleatorio(6, 12)
        for _ in range(num_filhotes):
            probabilidade = self.model.gerar_numero_aleatorio(0, 100)
            if probabilidade <= 25:
                abelha = Zangao(self.model.next_id(), self.model)
            elif probabilidade <= 85:
                abelha = Operaria(self.model.next_id(), self.model)
            else:
                abelha = Defensora(self.model.next_id(), self.model)
            self.model.adicionar_abelha_na_colmeia(abelha)