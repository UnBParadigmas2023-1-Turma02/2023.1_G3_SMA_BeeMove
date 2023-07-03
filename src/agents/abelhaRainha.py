from mesa import Agent
from src import utils
from src.agents.defensora import Defensora
from src.agents.operaria import Operaria
from src.agents.zangao import Zangao
from src.globals import Globals


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
        # # Verifica a vida da abelha rainha e se adiciona na lista de mortos
        if self.vida <= 0:
            self.model.kill_list.append(self)
        else:
            self.vida -= 1
            
        # # Verificar se é hora de reproduzir
        # if self.reproduzir_contagem <= 0:
        #     self.reproduzir()
        #     self.reproduzir_contagem = self.reproduzir_intervalo
        # else:
        #     self.reproduzir_contagem -= 1
        
    def alimentar_rainha(self, agent):
        self.vida = min(self.vida + agent.alimento, self.vida_maxima)
        print(f'alimentando - vida: {self.vida}')

    def reproduzir(self, agent):
        # self.model.create_bee(self)
        # Criar novas abelhas na colmeia (modelo)
        num_filhotes = utils.get_random_number(5,8)
        cria_zangao = False
        zangoes_mortos = 0

        #laço para saber a quantidade de zangões que estão na lista para morrerem (já procriaram)
        for i in range(len(self.model.kill_list)):
            agent = self.model.kill_list[i]
            if type(agent) is Zangao:
                zangoes_mortos += 1

        for i in range(num_filhotes):
            xInitial = utils.get_random_number(0,19)
            yInitial = utils.get_random_number(0,19)
            probabilidade = utils.get_random_number(0, 100)

            if self.model.glob.get_qtd_zangoes() - zangoes_mortos <= 1:
                    cria_zangao = True
                    abelha = Zangao(self.model.next_id(), self.model, (xInitial,yInitial),  self)
                    self.model.glob.set_qtd_zangoes(False)
            elif probabilidade <= 30 and cria_zangao == True:
                abelha = Zangao(self.model.next_id(), self.model, (xInitial,yInitial),  self)
                self.model.glob.set_qtd_zangoes(False)
            elif probabilidade <= 40:
                abelha = Defensora(self.model.next_id(), self.model,(xInitial,yInitial))
                self.model.glob.set_qtd_defensoras(False)
            elif probabilidade <= 100:
                abelha = Operaria(self.model.next_id(), self.model,(xInitial,yInitial), self)
                self.model.glob.set_qtd_operarias(False)
                
            self.model.create_bee(abelha)
