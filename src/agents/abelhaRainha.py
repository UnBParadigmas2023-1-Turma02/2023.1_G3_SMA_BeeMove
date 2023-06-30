from mesa import Agent

from mesa import Agent

class AbelhaRainha(Agent):
    def __init__(self, current_id, model, pos):
        super().__init__(current_id, model)
        self.pos = pos
        self.home = pos

    def reproduce(self):
        self.model.criar_abelha(self)