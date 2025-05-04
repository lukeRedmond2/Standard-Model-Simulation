# Libraries
from BaseClasses.Interactions import BaseInteraction, HiggsInteraction, BaryonInteraction
from BaseClasses.Particle import *
from BaseClasses.Forces import Electromagnetic
import pygame

# Simualtion class
class Simulation():

    # Initialier
    def __init__(self, width, height, particles, forces, name, BI_threshold, HI_radius, HI_strength, HI_mmmulti):

        # Setting interaction class variables
        self.BI_threshold = BI_threshold
        self.HI_strength = HI_strength
        self.HI_mmmulti = HI_mmmulti
        self.HI_radius = HI_radius

        # Setting other important attributes
        self.base_interaction = BaseInteraction()
        self.baryon_manager = BaryonInteraction(BI_threshold)
        self.particles = particles
        self.forces = forces
        self.height = height
        self.width = width
        self.name = name

    # Method to run the simulation
    def Run(self):

        # Setting up the universe
        pygame.init()
        screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption(self.name)
        clockd = pygame.time.Clock()

        # Starting the simulation
        running = True
        while running:

            # Higgs init try block
            try:

                # Initialising the higgs field
                higgs_particle = next(p for p in self.particles if type(p) == HiggsBoson)
                higgs_interaction = HiggsInteraction(higgs_particle.x, higgs_particle.y, radius=self.HI_radius, strength=self.HI_strength, max_mass_multiplier=self.HI_mmmulti)
            
            # Handling expected error
            except Exception as e:
                if type(e) != StopIteration:
                    print("Higgs Init Exception:")
                    print(e)                

            # Setting the background
            screen.fill((0, 0, 0))

            # Event update loop
            for event in pygame.event.get():

                # Quit handling
                if event.type == pygame.QUIT:
                    running = False
            
            # Particle update loop
            for particle in self.particles:

                # Looping over forces
                for force in self.forces:
                    force.Apply(particle, self.particles)

                # Higgs application try block
                try:

                    # Applying the higgs interaction
                    higgs_interaction.Apply(particle)

                # Handling expected error
                except Exception as e:
                    if type(e) != UnboundLocalError:
                        print("Applying Higgs Exception:")
                        print(e)

                # Movement and boundary collisions
                particle.x += particle.vx
                particle.y += particle.vy
                if particle.x < 0 or particle.x > self.width:
                    particle.vx *= -1
                if particle.y < 0 or particle.y > self.height:
                    particle.vy *= -1

                # Updating the trail
                particle.UpdateTrail()

            # Handling collisions
            self.base_interaction.Apply(self.particles)

            # Baryon stuff
            self.baryon_manager.Apply(self.particles)

            # Drawing everything to the universe/screen
            for particle in self.particles:
                particle.Draw(screen)

                # Higgs drawing try block
                try:

                    # Drawing the higgs field
                    higgs_interaction.Draw(screen)

                # Handling expected error
                except Exception as e:
                    if type(e) != UnboundLocalError:
                        print("Drawing Higgs Exception")
                        print(e)

            # Updating the universe
            pygame.display.flip()
            clockd.tick(60)

        # Quitting
        pygame.quit()