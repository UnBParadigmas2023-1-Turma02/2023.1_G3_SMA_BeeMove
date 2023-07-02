#from asyncio.windows_events import INFINITE
from mesa import Agent
from src.utils import calculate_distance, get_random_number
import math


class Zangao(Agent):
    def __init__(self, current_id, model, pos, posRainha):
        super().__init__(current_id, model)
        self.tipo = "Macho"
        self.vida_maxima = 50
        self.vida = self.vida_maxima
        self.pos = pos
        self.posRainha = posRainha

    def step(self):
        # Encontra abelha rainha para reproduzir
        # rainhas = self.get_all_queens()
        # print(rainhas)
        # escolhida = None
        # menor = math.inf
        # if rainhas:
        #     for queen in rainhas:
        #         if calculate_distance(self.pos, queen.pos) < menor:
        #             escolhida = queen 

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
            if self.pos == self.posRainha.pos:
                self.model.kill_list.append(self)
                self.reproduzir_com_rainha(self.posRainha)

    def reproduzir_com_rainha(self, rainha):
        # Verifica se a reprodução é bem-sucedida
        if rainha.tipo == "Rainha" and self.vida > 0:
            if self.model.glob.get_qtd_zangoes() == 1:
                probabilidade = 1
            else:
                probabilidade = get_random_number(0, 100)
            if probabilidade <= 80:
                # Reprodução bem-sucedida, cria nova abelha
                #print(self)
                rainha.reproduzir(rainha)
                 # Se bem sucedida, o macho morre
        else: pass

    def revoada(self): # caçada de acasalamento
        if self.origin == -1:
            return (lambda ovario: (ovario[0], ovario[1]))(self.random.choice(self.model.groups))
        else:
            return self.random.choice(
                list(set([(x, y) for x, y,  in self.model.groups]).difference([self.origin]))
            )

    def get_all_queens(self):
        all_queens = []
        for agent in self.model.grid.iter_neighborhood(self.pos, True, False,  math.inf):
            if agent.tipo == "Rainha":
                all_queens.append(agent)
        return all_queens