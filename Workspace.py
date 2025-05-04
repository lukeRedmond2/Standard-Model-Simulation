# Libraries
from BaseClasses.Interactions import BaseInteraction
from BaseClasses.Simulation import Simulation
from BaseClasses.Particle import *
from BaseClasses.Forces import Electromagnetic, StrongForce, WeakForce
import pygame
import random
import math

# Simulation 1: 
# 
# Electron-Positron Annihilation
simulation_1_particles = [
    Electron(100, 150),
    Positron(400, 150)
]
simulation_1_active_forces = [Electromagnetic(k=500)]
simulation_1 = Simulation(500, 300, simulation_1_particles, simulation_1_active_forces, 
                          name="Simulation 1: Electron-Positron Annihilation",
                          BI_threshold=25,
                          HI_strength=0.0085,
                          HI_radius=75,
                          HI_mmmulti=2)

# Simulation 2:
#
# Photon Freedom In The Higgs Field
simulation_2_particles = [
    HiggsBoson(250, 150),
    WMinusBoson(125, 75),
    WPlusBoson(375, 75),
    ZBoson(125, 225),
    Photon(375, 225)
]
simulation_2_active_forces = [Electromagnetic(k=500)]
simulation_2 = Simulation(500, 300, simulation_2_particles, simulation_2_active_forces, 
                          name="Simulation 2: Photon Freedom In The Higgs Field",
                          BI_threshold=25,
                          HI_strength=0.0085,
                          HI_radius=75,
                          HI_mmmulti=2)

# Simulation 3:
# 
# Baryon Formation
simulation_3_particles = [
    HiggsBoson(250, 125),
    UpQuark(125, 75),
    UpQuark(375, 225),
    DownQuark(125, 225),
    DownQuark(375, 75),
]
simulation_3_active_forces = [Electromagnetic(k=500), StrongForce(50, 50)]
simulation_3 = Simulation(500, 300, simulation_3_particles, simulation_3_active_forces, 
                          name="Simulation 3: Baryon Formation",
                          BI_threshold=25,
                          HI_strength=0.0085,
                          HI_radius=75,
                          HI_mmmulti=2)

# Simulation 4:
#
# Beta+ And Beta- Decay
simulation_4_particles = [
    HiggsBoson(250, 125),
    Neutron(125, 75),
    Proton(375, 225)
]
simulation_4_active_forces = [Electromagnetic(k=250), StrongForce(50, 50), WeakForce(0.001)]
simulation_4 = Simulation(500, 300, simulation_4_particles, simulation_4_active_forces, 
                          name="Simulation 4: Beta+ and Beta- Decay",
                          BI_threshold=25,
                          HI_strength=0.0085,
                          HI_radius=75,
                          HI_mmmulti=2)

# Simulation 5:
#
# Lepton Decay
simulation_5_particles = [
    HiggsBoson(250, 125),
    Muon(125, 75),
    Tau(375, 225)
]
simulation_5_active_forces = [Electromagnetic(k=500), StrongForce(50, 50), WeakForce(0.001)]
simulation_5 = Simulation(500, 300, simulation_5_particles, simulation_5_active_forces,
                          name="Simulation 5: Lepton Decay",
                          BI_threshold=25,
                          HI_strength=0.0085,
                          HI_radius=75,
                          HI_mmmulti=2)

# Simulation 6
#
# All Together
simulation_6_particles = [
    HiggsBoson(250, 125),
    DownQuark(125, 225),
    DownQuark(375, 225),
    UpQuark(125, 75),
    UpQuark(375, 75),
]
simulation_6_active_forces = [Electromagnetic(k=300), StrongForce(k=25, range_cutoff=75), WeakForce(0.001)]
simulation_6 = Simulation(500, 300, simulation_6_particles, simulation_6_active_forces, 
                          name="Simulation 6: All Together",
                          BI_threshold=25,
                          HI_strength=0.02,
                          HI_radius=75,
                          HI_mmmulti=2)


# Choose a simulation to run
simulation_1.Run()