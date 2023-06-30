from mesa import Agent
from functools import singledispatch

from src.agents.abelhaRainha import AbelhaRainha


@singledispatch
def render(agent: Agent):
    return

@render.register(AbelhaRainha)
def queen(agent: AbelhaRainha):
    return {
        "Color": "#f7fb4b",
        "Shape": "rect",
        "Filled": "true",
        "Layer": 2,
        "w": 2,
        "h": 2
    }
