import numpy as np
import modules.fenetre as fenetre

class Flock():

    def __init__(self) -> None:
        self.num_boids = 100
        self.boid_speed = 2

        #initialisation des positions et vitesses des Boids 
        self.positions = np.random.rand(2, self.num_boids)   #random.rand -> entre (0 et 1)     # (2, num_boids) -> 2 lignes , n colonnes
        self.positions[0, :] *= fenetre.screen_width     #([[x1, x2, x3],   -> Coordonnées x
        self.positions[1, :] *= fenetre.screen_height    #[y1, y2, y3]])    -> Coordonnées y
        
        self.velocities = np.random.rand(2, self.num_boids) * 2 - 1    # *2 -> [0.0, 2.0]    # -1 -> varie entre -1.0 et 1.0

        
        
    def update_positions(self) -> None:
        """
        met a jour la matrice de postions des boids
        """
        self.positions += self.velocities * self.boid_speed


