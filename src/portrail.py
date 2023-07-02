from src.agents.abelhaRainha import AbelhaRainha

def agentPortrayal(agent):
    portrayal = {"Filled": "true",
                "r": 1}
    if type(agent) is AbelhaRainha: 
        portrayal['Shape'] = "src/assets/rainha.jpeg"
        portrayal['Layer'] = 2
    # elif type(agent) is Zangao: 
    #     portrayal['Shape'] = "src/assets/zangao.jpeg"
    #     portrayal['Layer'] = 2
    # elif type(agent) is Operaria: 
    #     portrayal['Shape'] = "src/assets/operaria.jpeg"
    #     portrayal['Layer'] = 2
    # elif type(agent) is Defensora: 
    #     portrayal['Shape'] = "src/assets/defensora.jpeg"
    #     portrayal['Layer'] = 2
    return portrayal