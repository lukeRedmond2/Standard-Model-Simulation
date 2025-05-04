# Libraries
from BaseClasses.Particle import *
import random
import math

# Base class for forces
class Force:

    # Empty method to be overridden by subclasses
    def Apply(self, particle, others):
        raise NotImplementedError

# Electromagnetic force class
class Electromagnetic(Force):

    # Initialiser
    def __init__(self, k=500):

        # Setting k force / constant
        self.k = k

    # Applying the force
    def Apply(self, particle, others):

        if type(particle) == Photon or type(particle) == Gluon:
            return

        # Looping over other particles
        for other in others:

            # Skip if the same particle to avoid self-interaction
            if other == particle:
                continue
            
            # Calculating the distances between particles
            dx = other.x - particle.x
            dy = other.y - particle.y
            dist = math.hypot(dx, dy)

            # Avoiding division by zero
            if dist == 0:
                continue

            # Calculating the force using coulomb's law
            force = self.k * (particle.charge * other.charge) / (dist ** 2 + 1)
            fx = -force * dx / dist
            fy = -force * dy / dist

            # Updating the particle's velocity based on the force
            particle.vx += fx / particle.mass
            particle.vy += fy / particle.mass

# Strong nuclear force
class StrongForce(Force):

    # Initialiser
    def __init__(self, k=300, range_cutoff=120):

        # Setting important attributes
        self.range_cutoff = range_cutoff
        self.k = k

    # Applying the force
    def Apply(self, particle, others):

        # Filtering out non-quark particles
        if "Quark" not in particle.name:
            return

        # Looping over other particles
        for other in others:

            # Filtering out original and non quarks
            if other == particle or "Quark" not in other.name:
                continue

            # Calculating distances
            dx = other.x - particle.x
            dy = other.y - particle.y
            dist = math.hypot(dx, dy)

            # Avoiding division by zero and out of range interactions
            if dist == 0 or dist > self.range_cutoff:
                continue

            # Strong attractive force only at close range
            force = self.k / (dist + 1)
            fx = force * dx / dist
            fy = force * dy / dist

            # Updating velocities
            particle.vx += fx / particle.mass
            particle.vy += fy / particle.mass

# Weak nuclear force
class WeakForce(Force):

    # Initialiser
    def __init__(self, decay_chance=0.002):

        # Important attribute
        self.decay_chance = decay_chance

    # Applying the force
    def Apply(self, particle, particles):

        # Force applies to the neutron
        if type(particle) == Neutron:

            # Generating chance
            if random.random() < self.decay_chance:

                # Updating user
                print("Neutron decayed via weak force!")

                # Removing the neutron
                x, y = particle.x, particle.y
                particles.remove(particle)

                # Adding the decay products
                particles.append(Proton(x, y))
                particles.append(Electron(x, y))
                particles.append(ElectronAntiNeutrino(x, y))

    # Applying the force
    def Apply(self, particle, particles):

        # Chance to trigger any decay
        if random.random() >= self.decay_chance:
            return
        
        # Setting coordinates of particle
        x, y = particle.x, particle.y

        # Neutron case (Beta-minus decay)
        if type(particle) == Neutron:

            # Informing user
            print("Neutron decayed via weak force!")

            # Removing neutron and adding products
            particles.remove(particle)
            particles.extend([
                Proton(x, y),
                Electron(x, y),
                ElectronAntiNeutrino(x, y)
            ])

        # Proton case (Beta-plus decay)
        elif type(particle) == Proton:

            # Informing user
            print("Proton decayed via weak force!")

            # Removing proton and adding products
            particles.remove(particle)
            particles.extend([
                Neutron(x, y),
                Positron(x, y),
                ElectronNeutrino(x, y)
            ])
        
        # Muon case (Muon decay)
        elif type(particle) == Muon:

            # Informing user
            print("Muon decayed via weak force!")

            # Removing proton and adding products
            particles.remove(particle)
            particles.extend([
                Electron(x, y),
                ElectronAntiNeutrino(x, y),
                MuonNeutrino(x, y)
            ])
            
        # Anti muon case (Muon decay)
        elif type(particle) == AntiMuon:

            # Informing user
            print("Anti Muon decayed via weak force!")

            # Removing proton and adding products
            particles.remove(particle)
            particles.extend([
                Positron(x, y),
                ElectronNeutrino(x, y),
                MuonAntiNeutrino(x, y)
            ])

        # Tau case (Tau decay)
        elif type(particle) == Tau:

            # Informing user
            print("Tau decayed via weak force!")

            # Removing proton and adding products
            particles.remove(particle)
            particles.extend([
                Muon(x, y),
                TauNeutrino(x, y),
                MuonAntiNeutrino(x, y)
            ])
            
        # Anti Tau case (Tau decay)
        elif type(particle) == AntiTau:

            # Informing user
            print("Anti Tau decayed via weak force!")

            # Removing proton and adding products
            particles.remove(particle)
            particles.extend([
                AntiMuon(x, y),
                TauAntiNeutrino(x, y),
                MuonNeutrino(x, y)
            ])
