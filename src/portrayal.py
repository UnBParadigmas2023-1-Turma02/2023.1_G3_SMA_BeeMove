from src.agents.abelhaRainha import AbelhaRainha
from src.agents.defensora import Defensora
from src.agents.operaria import Operaria
from src.agents.zangao import Zangao
from src.agents.comida import  Flor #, Comida



def agentPortrayal(agent):
    portrayal = {"Filled": "true",
                "r": 1}
    if type(agent) is AbelhaRainha: 
        portrayal['Shape'] = "src/assets/rainha.jpeg"
        portrayal['Layer'] = 2
    elif type(agent) is Zangao: 
        portrayal['Shape'] = "src/assets/zangao.jpeg"
        portrayal['Layer'] = 3
    elif type(agent) is Operaria: 
        portrayal['Shape'] = "src/assets/operaria.jpeg"
        portrayal['Layer'] = 2
    elif type(agent) is Defensora: 
        portrayal['Shape'] = "src/assets/defensora.jpeg"
        portrayal['Layer'] = 2
    elif type(agent) is Flor:
        portrayal['Shape'] = "src/assets/flor4.png"
        #portrayal['Shape'] = "circle"
        #portrayal['Color'] = "red"
        portrayal['Layer'] = 2

    portrayal['Layer'] = portrayal.get('Layer', 0)  # Verifica se 'Layer' existe no dicionário

    return portrayal
