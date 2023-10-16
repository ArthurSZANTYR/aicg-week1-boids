import numpy as np
import modules.fenetre as fenetre

class Flock():

    def __init__(self) -> None:
        self.num_boids = 50
        self.boid_speed = 2

        #initialisation des positions et vitesses des Boids 
        self.positions = np.random.rand(2, self.num_boids)   #random.rand -> entre (0 et 1)     # (2, num_boids) -> 2 lignes , n colonnes
        self.positions[0, :] *= fenetre.screen_width     #([[x1, x2, x3],   -> Coordonnées x
        self.positions[1, :] *= fenetre.screen_height    #[y1, y2, y3]])    -> Coordonnées y
        
        self.velocities = np.random.rand(2, self.num_boids) * 2 - 1    # *2 -> [0.0, 2.0]    # -1 -> varie entre -1.0 et 1.0

        
        
    def update_positions(self,coeff_alignement= 1, coeff_separation= 1.5, coeff_cohesion= 1, max_speed= 2) -> None:
        """
        met a jour la matrice de postions des boids
        """
        alignement_velocities_force = self.alignement(perception_radius = 25, max_steering_force = 0.2)
        separation_velocities_force = - alignement_velocities_force
        cohesion_velocities_force = self.cohesion(perception_radius = 10, max_steering_force = 0.2)

        new_velocities = self.velocities + coeff_alignement*alignement_velocities_force + coeff_separation*separation_velocities_force + coeff_cohesion*cohesion_velocities_force + self.avoid_walls()#on fait += -> car c'est un ajout de steering force -donc la force de correction de traj

        #limitation de la vitesse des boids
        boid_speeds = np.linalg.norm(new_velocities, axis=0)  # Calcule la vitesse de chaque Boid - stocké dans une liste
        #print(speeds)
        too_fast = boid_speeds > max_speed
        new_velocities[:, too_fast] = new_velocities[:, too_fast] / boid_speeds[too_fast] * max_speed

        self.velocities = new_velocities
        self.positions += self.velocities * self.boid_speed

    def alignement(self, perception_radius, max_steering_force) -> np.array:
        """
        retourne les forces de correction necessaires - pour suivre un comportment d'alignement
        """
        aligned_velocities = np.zeros_like(self.velocities)  # matrice de zero de la meme taille que velocities

        for i in range(self.num_boids):  #pour chaque boid
            current_boid_position = self.positions[:, i]   
            current_boid_velocity = self.velocities[:, i] 
            #print(current_boid_position)     -> ex:  [162.18893711 148.80279386]


            current_boid_neighbors_velocity = []
            for j in range(self.num_boids): #on compare a chaque boid différent du boid courant i!=j
                if i != j:   
                    other_boid_position = self.positions[:, j]
                    other_boid_velocity = self.velocities[:, j]

                    distance = np.linalg.norm(other_boid_position - current_boid_position)   #np.linalg.norm -> calcule norme d'un vecteur = sa distanceentre 2 vecteurs soustrait
                    if distance < perception_radius:    #perception radius -> rayon de vision des boids
                        current_boid_neighbors_velocity.append(other_boid_velocity)

            if current_boid_neighbors_velocity: #renvoie True si la liste n'est pas vide
                average_neighbor_velocity = np.mean(current_boid_neighbors_velocity, axis=0)   #on calcule la velocity moyenne des boids voisins - axis = 0 -> pour calculer moyennes avec les elements des colonnes

                steering_force = average_neighbor_velocity - current_boid_velocity
                #steering force ex :  (2, 2) - (2, 1) = (0, 1)  -> signifie que le boid doit redresser en y de 1 pour s'aligner avec les autres - on lui applique une force de 1 en y

                steering_force = np.clip(steering_force, -max_steering_force, max_steering_force) #contient la steering force dans une plage - pour eviter les changement trop brusque de direction/comportements
                
                aligned_velocities[:, i] = steering_force

        return aligned_velocities
    
    def cohesion(self, perception_radius, max_steering_force) -> np.array:
        """
        retourne les forces de correction necesaires - pour suivre un comportement d'alignement 
        -> les boid se dirige vers la positions moyennes des boids voisins
        """

        cohesion_velocities = np.zeros_like(self.velocities)

        for i in range(self.num_boids):
            current_boid_position = self.positions[:,i]

            current_boid_neighbors_position = []
            for j in range(self.num_boids):
                if i!=j:
                    other_boid_position = self.positions[:,j]
                    distance = np.linalg.norm(current_boid_position - other_boid_position)
                    if distance < perception_radius:
                        current_boid_neighbors_position.append(other_boid_position)

            if current_boid_neighbors_position:
                average_neighbor_position = np.mean(current_boid_neighbors_position, axis=0)

                steering_force = average_neighbor_position - current_boid_position
                steering_force = np.clip(steering_force, -max_steering_force, max_steering_force)

                cohesion_velocities[:,i] = steering_force
        
        return cohesion_velocities
    
    def avoid_walls(self, wall_buffer=100, max_steering_force = 0.2):
        avoid_walls_force = np.zeros_like(self.velocities)

        for i in range(self.num_boids):
            current_boid_position = self.positions[:, i]

            # si le Boid s'approche des bords de l'écran
            if current_boid_position[0] < wall_buffer:
                avoid_walls_force[0, i] = max_steering_force  # Force pour éviter le mur gauche
            elif current_boid_position[0] > fenetre.screen_width - wall_buffer:
                avoid_walls_force[0, i] = -max_steering_force  # Force pour éviter le mur droit

            if current_boid_position[1] < wall_buffer:
                avoid_walls_force[1, i] = max_steering_force  # Force pour éviter le mur supérieur
            elif current_boid_position[1] > fenetre.screen_height - wall_buffer:
                avoid_walls_force[1, i] = -max_steering_force  # Force pour éviter le mur inférieur

        return avoid_walls_force




    



