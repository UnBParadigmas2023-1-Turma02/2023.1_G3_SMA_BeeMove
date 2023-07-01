import mesa
from mesa.visualization.modules import ChartModule

from src.model import Colmeia
from src.render import render
from src.portrail import agentPortrayal

chart_element = ChartModule([{"Label": "Número de abelhas", "Color": "blue"},
                             {"Label": "Número de zangões", "Color": "black"},
                             {"Label": "Número de defensoras", "Color": "red"}])

canvas_element = mesa.visualization.CanvasGrid(agentPortrayal, 20, 20, 600, 600)

model_params = {
    "abelhas_iniciais": mesa.visualization.Slider(
        "População inicial de abelhas", 100, 10, 300
    ),
    "zangao_inicial": mesa.visualization.Slider(
        "População inicial de zangões", 2, 1, 10
    ),
    "colmeia_inicial": mesa.visualization.Slider(
        "Quantidade inicial de colmeias", 1, 1, 10
    ),
    "vida_adicional": mesa.visualization.Slider(
        "Vida adicional ao se alimentar", 50, 1, 100
    ),
    "quantidade_defensora": mesa.visualization.Slider(
        "Quantidade inicial de abelhas defensoras", 5, 1, 50
    ),
}


server = mesa.visualization.ModularServer(
    Colmeia, [canvas_element, chart_element], "Colmeia", model_params
)

server.port = 8521
