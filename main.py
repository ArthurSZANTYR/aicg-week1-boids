import pygame
import numpy as np


import modules.flock as flock
import modules.render as render

render = render.Render()
flock = flock.Flock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    flock.update_positions()
    render.update_render(flock)

pygame.quit()
