# Libraries
from BaseClasses.Particle import *
import pygame
import math

# Base interaction class
class BaseInteraction():

    # Method to handle collisions
    def Apply(self, particles):

        # # Function for finding annihilation pairs
        # def IsPair(p1, p2):

        #     # Return logic
        #     return (

        #         # Electron-positron pair
        #         (type(p1) == Electron and type(p2) == Positron) or
        #         (type(p1) == Positron and type(p2) == Electron)
        #     )

        # Storage variables
        to_add = []
        to_remove = set()

        # Primary loop over particles
        for i, p1 in enumerate(particles):

            # Secondary loop over particles
            for j, p2 in enumerate(particles):

                # Checking for particles that will raise errors
                if i >= j or p1 in to_remove or p2 in to_remove:
                    continue

                # Calculating the distance between two particles
                dx = p1.x - p2.x
                dy = p1.y - p2.y
                dist = math.hypot(dx, dy)

                # If particles are close enough
                if dist < (p1.radius + p2.radius) * 0.8:

                    # If a pair is found
                    if p1.IsAntiparticle(p2):

                        # Annihilating the particles
                        print(f"{p1.name} and {p2.name} annihilated!")
                        x_mid = (p1.x + p2.x) / 2
                        y_mid = (p1.y + p2.y) / 2

                        # Adding product particle and removing originals
                        to_add.append(Photon(x_mid, y_mid))
                        to_remove.update([p1, p2])

        # Removing and adding said particles
        for p in to_remove:
            particles.remove(p)
        particles.extend(to_add)

# Higgs field interaction class
class HiggsInteraction():

    # Initialiser
    def __init__(self, x, y, radius=150, strength=0.1, max_mass_multiplier=2):

        # Setting important attributes
        self.x = x
        self.y = y
        self.radius = radius
        self.strength = strength
        self.max_mass_multiplier = max_mass_multiplier

    # Applying the higgs field to particles
    def Apply(self, particle):

        # Filtering out paraticles that can't be affected by the field
        if type(particle) == Photon or type(particle) == Gluon or type(particle) == HiggsBoson:
            return

        # Calculating the distance
        dx = self.x - particle.x
        dy = self.y - particle.y
        dist = math.hypot(dx, dy)

        # Setting target mass if particle in range of the field
        inside = dist < self.radius
        target_mass = particle.original_mass * self.max_mass_multiplier if inside else particle.original_mass

        # Setting the rate of change and new mass
        change_rate = 0.5
        particle.mass += (target_mass - particle.mass) * change_rate * 0.05

        # If the particle is in the field
        if inside:
            
            # Applying drag due to the increased mass
            particle.vx *= (1 - self.strength)
            particle.vy *= (1 - self.strength)

    # Method to draw the field
    def Draw(self, surface):

        # Draw the field zone
        pygame.draw.circle(surface, (255, 255, 100), (int(self.x), int(self.y)), self.radius, 1)
        font = pygame.font.SysFont(None, 18)
        label = font.render("Higgs Field", True, (255, 255, 100))
        surface.blit(label, (self.x - self.radius, self.y - self.radius - 20))

# Baryon interaction class
class BaryonInteraction():

    # Initialiser
    def __init__(self, threshold=25):

        # Setting important attributes
        self.threshold = threshold

    # Applying the logic to the particles
    def Apply(self, particles):

        # Storage variables
        to_add = []
        used = set()
        to_remove = set()

        # Get all quarks
        quarks = [p for p in particles if type(p) == UpQuark or type(p) == DownQuark]

        # Primary loop of quarks
        for i, p1 in enumerate(quarks):

            # Ignoreing used quarks
            if p1 in used:
                continue

            # Secondary loop of quarks
            for j, p2 in enumerate(quarks):

                # Ignoreing used quarks
                if p2 in used or p2 == p1:
                    continue

                # Tertiary loop of quarks
                for k, p3 in enumerate(quarks):

                    # Ignoreing used quarks
                    if p3 in used or p3 == p1 or p3 == p2:
                        continue

                    # Calculating the distances
                    d12 = math.hypot(p1.x - p2.x, p1.y - p2.y)
                    d13 = math.hypot(p1.x - p3.x, p1.y - p3.y)
                    d23 = math.hypot(p2.x - p3.x, p2.y - p3.y)

                    # If the quarks are close enough, initialise reaction
                    if d12 < self.threshold and d13 < self.threshold and d23 < self.threshold:

                        # Splitting up up and down quarks
                        three = [p1, p2, p3]
                        ups = [p for p in three if type(p) == UpQuark]
                        downs = [p for p in three if type(p) == DownQuark]

                        # The proton case
                        if len(ups) == 2 and len(downs) == 1:

                            # Updating user
                            print("Proton formed!")

                            # Adding the proton
                            to_add.append(Proton(x=(p1.x + p2.x + p3.x) / 3,
                                                 y=(p1.y + p2.y + p3.y) / 3))
                            
                            # Removing the quarks
                            to_remove.update(three)
                            used.update(three)

                        # The Neutron case
                        elif len(ups) == 1 and len(downs) == 2:

                            # Updating user
                            print("Neutron formed!")

                            # Adding the neutron
                            to_add.append(Neutron(x=(p1.x + p2.x + p3.x) / 3,
                                                  y=(p1.y + p2.y + p3.y) / 3))
                            
                            # Removing the quarks
                            to_remove.update(three)
                            used.update(three)

        # Removing the particles
        for p in to_remove:
            particles.remove(p)
        particles.extend(to_add)
