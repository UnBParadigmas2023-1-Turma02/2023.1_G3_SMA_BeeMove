from random import randint
import mesa
from src.agents.defensora import Defensora
from src.agents.operaria import Operaria
from src.agents.zangao import Zangao
from src.globals import Globals
import src.utils as utils
from mesa import Model, Agent
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid
from src.agents.abelhaRainha import AbelhaRainha
from src.agents.comida import Flor
import random


class Colmeia(Model):

    def __init__(
        self,
        abelhas_iniciais,
        zangao_inicial,
        colmeia_inicial,
        vida_adicional,
        quantidade_defensora,
        quantidade_flores
        #raio_flor,
    ):

        self.current_id = 1
        self.width = 20
        self.height = 20

        self.schedule = SimultaneousActivation(self)
        self.grid = MultiGrid(self.width, self.height, torus=True)

        self.colmeia_inicial = colmeia_inicial
        self.vida_adicional = vida_adicional
        # self.raio_flor = raio_flor
    
        self.glob = Globals()
        self.qtd_abelhas = 0
        self.qtd_defensoras = 0
        self.qtd_zangoes = 0
        self.qtd_operarias = 0
        self.atualiza_qtds()

        self.kill_list = []

        # Esses valores devem ser integrados ao código depois, para atualizar constantemente os seus valores
        self.quantidade_abelha = [1, 2, 3, 4]
        self.quantidade_zangao = [1, 2, 3]
        self.quantidade_flores = quantidade_flores
        self.quantidade_defensora = quantidade_defensora

        # Inicialização das colmeias
        self.groups = []
        for group in range(self.colmeia_inicial):
            self.groups.append((
                self.random.randrange(self.width),
                self.random.randrange(self.height),
                [self.random.randint(0, 125) for _ in range(3)]
            ))

        # Inicialização da rainha
        rainhas = []
        for abelha in range(self.colmeia_inicial):
            x, y, _ = self.groups[abelha % self.colmeia_inicial]
            q = AbelhaRainha(self.next_id(),self, (x, y))
            rainhas.append(q)
            self.register(q)
        
        # Iniciar flor
        for _ in range(self.quantidade_flores):
            comida = Flor(self.next_id(),
                          self, 
                          (self.random.randint(0, (self.grid.width - 1)), 
                          self.random.randint(0, (self.grid.height - 1))), 
                          1000, "Flor")
            self.register(comida)
            
        # Inicializar Zangao
        for abelha in range(self.colmeia_inicial):
            x, y, _ = self.groups[abelha % self.colmeia_inicial]
            m = Zangao(self.next_id(), self, utils.random_pos(self.width-1, self.height-1), rainhas[0])
            self.register(m)

        # Iniciar Operaria
        # operaria = []
        # for abelha in range(self.colmeia_inicial):
        #     x, y, _ = self.groups[abelha % self.colmeia_inicial]
        #     m = Operaria(self.next_id(), self, utils.random_pos(self.width, self.height), rainhas[0])
        #     self.register(m)

        self.datacollector = mesa.DataCollector(model_reporters={"Número de abelhas": lambda m: m.qtd_abelhas,
                                                                 "Número de zangões": lambda m: m.qtd_zangoes,
                                                                 "Número de defensoras": lambda m: m.qtd_defensoras,
                                                                 "Número de operárias": lambda m: m.qtd_operarias
                                                                 })
       
    # Código para o gráfico
    def collect_abelha(self):
        return len(self.quantidade_abelha)

    def collect_zangao(self):
        return len(self.quantidade_zangao)

    def collect_defensora(self):
        # Esse retorno deve seguir o padrão das funções anteriores
        # Está assim apenas para testes!!!!!!!!!!!!!!!!!!!!!!!!
        return self.quantidade_defensora
    
    def atualiza_qtds(self):
        self.qtd_abelhas = self.glob.get_qtd_abelhas()
        self.qtd_defensoras = self.glob.get_qtd_defensoras()
        self.qtd_zangoes = self.glob.get_qtd_zangoes()
        self.qtd_operarias = self.glob.get_qtd_operarias()


    def step(self):
        self.schedule.step()
        self.atualiza_qtds()
        self.datacollector.collect(self)
        #print(self.kill_list)
        for x in self.kill_list:
            #print(self.kill_list)
            self.grid.remove_agent(x)
            self.schedule.remove(x)
            if type(x) is Defensora:
                self.glob.set_qtd_defensoras(True)
            elif type(x) is Zangao:
                self.glob.set_qtd_zangoes(True)
            elif type(x) is Operaria:
                self.glob.set_qtd_operarias(True)
        self.kill_list = []

    def create_bee(self, agent):
            queen_group_color = utils.get_group_color(self.groups, (agent.pos[0], agent.pos[1]))
            new_ant = agent
            self.register(new_ant)

    def register(self, agent: Agent):
        if agent.pos:
            self.grid.place_agent(agent, agent.pos)

        self.schedule.add(agent)
