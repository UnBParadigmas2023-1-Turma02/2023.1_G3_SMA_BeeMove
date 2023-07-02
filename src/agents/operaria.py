from mesa import Agent

class Operaria(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.tipo = "Operaria"
        self.vida_maxima = 80
        self.vida = self.vida_maxima

    def step(self):
        # Sai da comeia atras de comida
        # Depois volta para a comeia

            dx = self.posComida.pos[0] - self.pos[0]    
            dy = self.posComida.pos[1] - self.pos[1]

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
            if self.pos == self.posComida.pos: #comida

                self.vida = -1 #Perde vida qnd sai
                self.coletarComida(self.posComida)
                self.vida = -1 #Perde qnd volta p colmeia

                if self.vida <= 0:
                    self.model.kill_list.append(self)
            
    def coletarComida(self):
        # Conseguiu pegar comida
        probabilidade = get_random_number(0, 100) # de encontrar comida
        if probabilidade <= self.prob_comida:
            self.prob_comida -= 5 # Decrementa se achar comida
            # Se achar comida volta pra colmeia
            self.irColmeia(self.pos, self. self.posRainha)

    def irColmeia(self):
            # A posicao da colmeia eh onde ta a rainha, ela n sai
            dx_c = self. self.posRainha.pos[0] - self.pos[0]    
            dy_c = self. self.posRainha.pos[1] - self.pos[1]

            xAtual_c = self.pos[0]
            yAtual_c = self.pos[1]

            if dx_c > 0:
               xAtual_c += 1
            elif dx_c < 0:                      
                xAtual_c -= 1
            
            if dy_c > 0:
                yAtual_c += 1
            elif dy_c < 0:                      
                yAtual_c -= 1

    def get_all_food(self): # get all comidas
        all_food = []
        for agent in self.model.grid.iter_neighborhood(self.pos, True, False,  math.inf): # que isso
            if agent.tipo == "Operaria":
                all_food.append(agent)
        return all_food