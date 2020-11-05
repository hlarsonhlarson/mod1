import pygame
import os
import sys
import tkinter as tk
import math
import numpy as np

from Reader import read_map

points = read_map('resources/demo5.mod1')

x = [x.x for x in points]
y = [y.y for y in points]
z = [z.z for z in points]

matrix = np.array([x, y, z])
print(matrix)

WIDTH = 1280
HEIGHT = 720
GRAY = (125, 125, 125)
WHITE = (255, 255, 255)
'''
os.environ['SDL_VIDEO_WINDOW_POS'] = f'{(tk.Tk().winfo_screenwidth() - WIDTH) // 2},' \
                                         f'{(tk.Tk().winfo_screenheight() - HEIGHT) // 4}'
pygame.init()
pygame.display.set_caption('Ray marching')
sc = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.mouse.set_visible(True)
game = True
ans = []
for i in range(len(x)):
    ans.append([x[i]/z[i], y[i]/z[i]])
print(x, y)
while game:
    for event in pygame.event.get():
        # pygame.draw.aalines(sc, WHITE, False, ans)
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                game = False
        pygame.draw.aalines(sc, WHITE, False, ans)
        pygame.display.flip()

'''