import mesa
from src.agents.zangao import Zangao
import src.utils as utils
from mesa import Model, Agent
from mesa.time import SimultaneousActivation
from mesa.space import MultiGrid
from src.agents.abelhaRainha import AbelhaRainha

class Colmeia(Model):

    def __init__(
        self,
        abelhas_iniciais,
        zangao_inicial,
        colmeia_inicial,
        vida_adicional,
        quantidade_defensora,
    ):

        self.current_id = 1
        self.width = 20
        self.height = 20

        self.schedule = SimultaneousActivation(self)
        self.grid = MultiGrid(self.width, self.height, torus=True)

        self.abelhas_iniciais = abelhas_iniciais
        self.zangao_inicial = zangao_inicial
        self.colmeia_inicial = colmeia_inicial
        self.vida_adicional = vida_adicional
        self.quantidade_defensora = quantidade_defensora

        self.kill_list = []
        # Esses valores devem ser integrados ao código depois, para atualizar constantemente os seus valores
        self.quantidade_abelha = [1, 2, 3, 4]
        self.quantidade_zangao = [1, 2, 3]

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
            
            
        # Inicializar Zangao
        for abelha in range(self.colmeia_inicial):
            x, y, _ = self.groups[abelha % self.colmeia_inicial]
            m = Zangao(self.next_id(), self, utils.random_pos(self.width, self.height), rainhas[0])
            self.register(m)

        self.datacollector = mesa.DataCollector(model_reporters={"Número de abelhas": self.collect_abelha,
                                                                 "Número de zangões": self.collect_zangao,
                                                                 "Número de defensoras": self.collect_defensora})

    # Código para o gráfico
    def collect_abelha(self):
        return len(self.quantidade_abelha)

    def collect_zangao(self):
        return len(self.quantidade_zangao)

    def collect_defensora(self):
        # Esse retorno deve seguir o padrão das funções anteriores
        # Está assim apenas para testes!!!!!!!!!!!!!!!!!!!!!!!!
        return self.quantidade_defensora


    def step(self):
        self.schedule.step()
        self.datacollector.collect(self)
        print(self.kill_list)
        for x in self.kill_list:
            print(self.kill_list)
            self.grid.remove_agent(x)
            self.schedule.remove(x)
        self.kill_list = []


    def register(self, agent: Agent):
        self.grid.place_agent(agent, agent.pos)
        self.schedule.add(agent)
