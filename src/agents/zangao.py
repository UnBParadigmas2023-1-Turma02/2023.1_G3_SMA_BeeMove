from mesa import Agent
from src.agents.operaria import Operaria


class Zangao(Agent):
    def __init__(self, current_id, model, pos, origin):
        super().__init__(current_id, model)
        self.tipo = "Macho"
        self.vida_maxima = 50
        self.vida = self.vida_maxima
        self.pos = pos

    def step(self):
        # Encontra abelha rainha para reproduzir
        rainhas = self.model.encontrar_abelhas_por_tipo("Rainha")
        if rainhas:
            rainha = self.model.escolher_abelha_aleatoria(rainhas)
            if rainha.unique_id != self.unique_id:
                self.reproduzir_com_rainha(rainha)

    def reproduzir_com_rainha(self, rainha):
        # Verifica se a reprodução é bem-sucedida
        probabilidade = self.model.gerar_numero_aleatorio(0, 100)
        if probabilidade <= 50:
            # Reprodução bem-sucedida, cria nova abelha
            abelha = Operaria(self.model.next_id(), self.model)
            self.model.adicionar_abelha_na_colmeia(abelha)
            self.vida = -1 # Se bem sucedida, o macho morre
            
    def revoada(self): # caçada de acasalamento
        if self.origin == -1:
            return (lambda ovario: (ovario[0], ovario[1]))(self.random.choice(self.model.groups))
        else:
            return self.random.choice(
                list(set([(x, y) for x, y,  in self.model.groups]).difference([self.origin]))
            )
