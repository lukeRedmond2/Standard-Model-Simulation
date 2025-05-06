# Libraries
from BaseClasses.Interactions import BaseInteraction
from BaseClasses.Simulation import Simulation
from BaseClasses.Particle import *
from BaseClasses.Forces import Electromagnetic, StrongForce, WeakForce
import pygame
import random
import math

# Screen dimensions
width = 500
height = 300

# Simulation 1: 
# 
# Electron-Positron Annihilation
simulation_1_particles = [
    Electron(random.randrange(0, width), random.randrange(0, height)),
    Electron(random.randrange(0, width), random.randrange(0, height)),
    Positron(random.randrange(0, width), random.randrange(0, height)),
    Positron(random.randrange(0, width), random.randrange(0, height)),
    Positron(random.randrange(0, width), random.randrange(0, height))
]
simulation_1_active_forces = [Electromagnetic(k=500)]
simulation_1 = Simulation(width, height, simulation_1_particles, simulation_1_active_forces, 
                          name="Simulation 1: Electron-Positron Annihilation",
                          BI_threshold=25,
                          HI_strength=0.0085,
                          HI_radius=75,
                          HI_mmmulti=2)

# Simulation 2:
#
# Photon Freedom In The Higgs Field
simulation_2_particles = [
    HiggsBoson(random.randrange(0, width), random.randrange(0, height)),
    WMinusBoson(random.randrange(0, width), random.randrange(0, height)),
    WPlusBoson(random.randrange(0, width), random.randrange(0, height)),
    ZBoson(random.randrange(0, width), random.randrange(0, height)),
    Photon(random.randrange(0, width), random.randrange(0, height))
]
simulation_2_active_forces = [Electromagnetic(k=500)]
simulation_2 = Simulation(width, height, simulation_2_particles, simulation_2_active_forces, 
                          name="Simulation 2: Photon Freedom In The Higgs Field",
                          BI_threshold=25,
                          HI_strength=0.0085,
                          HI_radius=100,
                          HI_mmmulti=2)

# Simulation 3:
# 
# Baryon Formation
simulation_3_particles = [
    HiggsBoson(random.randrange(0, width), random.randrange(0, height)),
    UpQuark(random.randrange(0, width), random.randrange(0, height)),
    UpQuark(random.randrange(0, width), random.randrange(0, height)),
    DownQuark(random.randrange(0, width), random.randrange(0, height)),
    DownQuark(random.randrange(0, width), random.randrange(0, height)),
]
simulation_3_active_forces = [Electromagnetic(k=500), StrongForce(50, 50)]
simulation_3 = Simulation(width, height, simulation_3_particles, simulation_3_active_forces, 
                          name="Simulation 3: Baryon Formation",
                          BI_threshold=25,
                          HI_strength=0.0085,
                          HI_radius=75,
                          HI_mmmulti=2)

# Simulation 4:
#
# Beta+ And Beta- Decay
simulation_4_particles = [
    HiggsBoson(random.randrange(0, width), random.randrange(0, height)),
    Neutron(random.randrange(0, width), random.randrange(0, height)),
    Proton(random.randrange(0, width), random.randrange(0, height))
]
simulation_4_active_forces = [Electromagnetic(k=250), StrongForce(50, 50), WeakForce(0.001)]
simulation_4 = Simulation(width, height, simulation_4_particles, simulation_4_active_forces, 
                          name="Simulation 4: Beta+ and Beta- Decay",
                          BI_threshold=25,
                          HI_strength=0.0085,
                          HI_radius=75,
                          HI_mmmulti=2)

# Simulation 5:
#
# Lepton Decay
simulation_5_particles = [
    HiggsBoson(random.randrange(0, width), random.randrange(0, height)),
    Muon(random.randrange(0, width), random.randrange(0, height)),
    Tau(random.randrange(0, width), random.randrange(0, height))
]
simulation_5_active_forces = [Electromagnetic(k=500), StrongForce(50, 50), WeakForce(0.001)]
simulation_5 = Simulation(width, height, simulation_5_particles, simulation_5_active_forces,
                          name="Simulation 5: Lepton Decay",
                          BI_threshold=25,
                          HI_strength=0.0085,
                          HI_radius=75,
                          HI_mmmulti=2)

# Simulation 6
#
# All Together
simulation_6_particles = [
    HiggsBoson(random.randrange(0, width), random.randrange(0, height)),
    DownQuark(random.randrange(0, width), random.randrange(0, height)),
    DownQuark(random.randrange(0, width), random.randrange(0, height)),
    UpQuark(random.randrange(0, width), random.randrange(0, height)),
    UpQuark(random.randrange(0, width), random.randrange(0, height)),
]
simulation_6_active_forces = [Electromagnetic(k=300), StrongForce(k=25, range_cutoff=75), WeakForce(0.001)]
simulation_6 = Simulation(width, height, simulation_6_particles, simulation_6_active_forces, 
                          name="Simulation 6: All Together",
                          BI_threshold=25,
                          HI_strength=0.02,
                          HI_radius=75,
                          HI_mmmulti=2)


# Choose a simulation to run
simulation_3.Run()