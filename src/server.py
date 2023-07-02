import mesa
from mesa.visualization.modules import ChartModule

from src.model import Colmeia
from src.portrayal import agentPortrayal

chart_element = ChartModule([{"Label": "Número de abelhas", "Color": "blue"},
                             {"Label": "Número de zangões", "Color": "black"},
                             {"Label": "Número de defensoras", "Color": "red"},
                             {"Label": "Número de operárias", "Color": "green"},
                             ])

canvas_element = mesa.visualization.CanvasGrid(agentPortrayal, 20, 20, 600, 600)

model_params = {
    "abelhas_iniciais": mesa.visualization.Slider(
        "População inicial de abelhas", 100, 10, 300
    ),
    "zangao_inicial": mesa.visualization.Slider(
        "População inicial de zangões", 2, 1, 10
    ),
    "colmeia_inicial": mesa.visualization.Slider(
        "Quantidade inicial de colmeias", 1, 1, 3
    ),
    "vida_adicional": mesa.visualization.Slider(
        "Vida adicional ao se alimentar", 50, 1, 100
    ),
      "quantidade_defensora": mesa.visualization.Slider(
        "Vida adicional ao se alimentar", 50, 1, 100
    ),
    "quantidade_flores": mesa.visualization.Slider(
        "Quantidade de flores", 1, 1, 2
    ),

}


server = mesa.visualization.ModularServer(
    Colmeia, [canvas_element, chart_element], "Colmeia", model_params
)

server.port = 8521
