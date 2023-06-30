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
        self.width = 100
        self.height = 100

        self.schedule = SimultaneousActivation(self)
        self.grid = MultiGrid(self.width, self.height, torus=True)

        self.abelhas_iniciais = abelhas_iniciais
        self.zangao_inicial = zangao_inicial
        self.colmeia_inicial = colmeia_inicial
        self.vida_adicional = vida_adicional
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
        for abelha in range(self.colmeia_inicial):
            x, y, _ = self.groups[abelha % self.colmeia_inicial]
            q = AbelhaRainha(self.next_id(),self, (x, y))
            self.register(q)


    def step(self):
        self.schedule.step()
        for x in self.kill_agents:
            self.grid.remove_agent(x)
            self.schedule.remove(x)
        self.kill_agents = []


    def register(self, agent: Agent):
        self.grid.place_agent(agent, agent.pos)
        self.schedule.add(agent)
