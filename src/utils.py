from math import sqrt
from random import randint
import random

def calculate_distance(pos1, pos2):
    return sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

def random_pos(width, height):
    return (
        randint(0, width-1),
        randint(0, height-1)
    )

def random_create_bee():
    return randint(0, 100)

# Retorna o agente que se encontra na posição atual
# Baseado no exemplo sugarscape do mesa
def get_item(self, agent_type):
    for agent in self.model.grid.get_cell_list_contents([self.pos]):
        if type(agent) is agent_type and agent != self:
            return agent



# def get_all_queens(self):
#     all_queens = []
#     for agent in self.model.grid.get_cell_list_contents([self.pos]):
#         if agent.tipo == "Rainha":
#             all_queens.append(agent)
#     return all_queens


def get_group_color(groups, findPos):
    for x, y, color in groups:
        if x == findPos[0] and y == findPos[1]:
            return color

def get_random_number(start, end):
    return random.randint(start, end)