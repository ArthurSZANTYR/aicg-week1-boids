import pygame
import numpy as np

pygame.init()
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Simulation de Boids")

num_boids = 100
boid_speed = 2
boid_size = 5
boid_color = (0, 0, 255)

#initialisation des positions et vitesses des Boids 
positions = np.random.rand(2, num_boids)   #random.rand -> entre (0 et 1)     # (2, num_boids) -> 2 lignes , n colonnes
positions[0, :] *= screen_width     #([[x1, x2, x3],   -> Coordonnées x
positions[1, :] *= screen_height    #[y1, y2, y3]])    -> Coordonnées y

velocities = np.random.rand(2, num_boids) * 2 - 1    # *2 -> [0.0, 2.0]    # -1 -> varie entre -1.0 et 1.0

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    positions += velocities * boid_speed

    screen.fill((255, 255, 255))
    for i in range(num_boids):
        pygame.draw.circle(screen, boid_color, (int(positions[0, i]), int(positions[1, i])), boid_size)

    pygame.display.update()
    clock.tick(60)   #60 fps

pygame.quit()
