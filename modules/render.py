import pygame
import modules.fenetre as fenetre

class Render():

    def __init__(self) -> None:
        self.boid_color = (0, 0, 255)
        self.boid_size = 5

        pygame.init()
        self.screen = pygame.display.set_mode((fenetre.screen_width, fenetre.screen_height))
        pygame.display.set_caption("Simulation de Boids")

        self.clock = pygame.time.Clock() #pour controller fps

    def update_render(self, f: "Flock") -> None:
        self.screen.fill((255, 255, 255))
        for i in range(f.num_boids):
            pygame.draw.circle(self.screen, self.boid_color, (int(f.positions[0, i]), int(f.positions[1, i])), self.boid_size)

        pygame.display.update()
        self.clock.tick(60)   #60 fps