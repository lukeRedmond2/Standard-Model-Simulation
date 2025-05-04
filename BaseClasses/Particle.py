# Libraries
import random
import pygame

# Global colour variables
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
PURPLE = (180, 100, 255)
ORANGE = (255, 165, 0)
CYAN = (0, 255, 255)
GREY = (180, 180, 180)

# Particle Masterclass
class Particle():

    # Initialiser
    def __init__(self, x, y, charge, mass, name):

        # Setting the position attributes
        self.vx = random.uniform(-2, 2)
        self.vy = random.uniform(-2, 2)
        self.x = x
        self.y = y

        # Information attributes
        self.trail = []
        self.name = name
        self.mass = mass
        self.charge = charge
        self.in_higgs = False
        self.radius = int(mass)
        self.colour = self.GetColour()
        self.original_mass = mass

    # Method determining the colour
    def GetColour(self):

        # Boson colourings
        if "Higgs" in self.name:
            return YELLOW
        if "Gluon" in self.name:
            return GREY
        if "Photon" in self.name:
            return CYAN
        
        # Charge cases
        if self.charge > 0:
            return RED
        elif self.charge < 0:
            return BLUE
        elif self.charge == 0:
            return GREEN
        
    # Method for updating the particle's trail
    def UpdateTrail(self):

        # Adding the current position to the trail
        self.trail.append((self.x, self.y))

        # Removing the oldest position if the trail is too long
        if len(self.trail) > 50:
            self.trail.pop(0)

    # Method for drawing the particles
    def Draw(self, surface):

        # Drawing the trail
        if len(self.trail) > 1:
            pygame.draw.lines(surface, self.colour, False, [(int(x), int(y)) for x, y in self.trail], 2)

        current_radius = int(self.mass)

        # Drawing the particle
        pygame.draw.circle(surface, self.colour, (int(self.x), int(self.y)), current_radius)
        font = pygame.font.SysFont(None, 18)
        img = font.render(self.name, True, WHITE)
        surface.blit(img, (self.x - self.radius, self.y - self.radius - 10))

    # Method for confirming antiparticles
    def IsAntiparticle(self, other):

        # Returning boolean answer
        return getattr(self, "antiparticle_of", None) == type(other)

# ----------------------------------------------------------------
# -----------------------LEPTON SUBCLASSES------------------------
# ----------------------------------------------------------------

# Electron Subclass
class Electron(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Electron"
        self.mass = 8
        self.charge = -1
        self.antiparticle_of = Positron
        super().__init__(x, y, self.charge, self.mass, self.name)

# Muon Subclass
class Muon(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Muon"
        self.mass = 8
        self.charge = -1
        self.antiparticle_of = AntiMuon
        super().__init__(x, y, self.charge, self.mass, self.name)

# Tau Subclass
class Tau(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Tau"
        self.mass = 8
        self.charge = -1
        self.antiparticle_of = AntiTau
        super().__init__(x, y, self.charge, self.mass, self.name)

# Electron Neutrino Subclass
class ElectronNeutrino(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Electron Neutrino"
        self.mass = 4
        self.charge = 0
        self.antiparticle_of = ElectronAntiNeutrino
        super().__init__(x, y, self.charge, self.mass, self.name)

# Muon Neutrino Subclass
class MuonNeutrino(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Muon Neutrino"
        self.mass = 4
        self.charge = 0
        self.antiparticle_of = MuonAntiNeutrino
        super().__init__(x, y, self.charge, self.mass, self.name)

# Tau Neutrino Subclass
class TauNeutrino(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Tau Neutrino"
        self.mass = 4
        self.charge = 0
        self.antiparticle_of = TauAntiNeutrino
        super().__init__(x, y, self.charge, self.mass, self.name)

# ---------------------------------------------------------------
# -----------------------QUARK SUBCLASSES------------------------
# ---------------------------------------------------------------

# Up Quark Subclass
class UpQuark(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Up Quark"
        self.mass = 7
        self.charge = 2/3
        super().__init__(x, y, self.charge, self.mass, self.name)

# Down Quark Subclass
class DownQuark(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Down Quark"
        self.mass = 7
        self.charge = -1/3
        super().__init__(x, y, self.charge, self.mass, self.name)

# Charm Quark Subclass
class CharmQuark(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Charm Quark"
        self.mass = 8
        self.charge = 2/3
        super().__init__(x, y, self.charge, self.mass, self.name)

# Strange Quark Subclass
class StrangeQuark(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Strange Quark"
        self.mass = 8
        self.charge = -1/3
        super().__init__(x, y, self.charge, self.mass, self.name)

# Top Quark Subclass
class TopQuark(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Top Quark"
        self.mass = 10
        self.charge = 2/3
        super().__init__(x, y, self.charge, self.mass, self.name)

# Bottom Quark Subclass
class BottomQuark(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Bottom Quark"
        self.mass = 10
        self.charge = -1/3
        super().__init__(x, y, self.charge, self.mass, self.name)
        
# ---------------------------------------------------------------
# -----------------------BOSON SUBCLASSES------------------------
# ---------------------------------------------------------------

# Photon Subclass
class Photon(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Photon"
        self.mass = 0
        self.charge = 0
        super().__init__(x, y, self.charge, self.mass, self.name)

# Gluon Subclass
class Gluon(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Gluon"
        self.mass = 0
        self.charge = 0
        super().__init__(x, y, self.charge, self.mass, self.name)

# W+ Boson Subclass
class WPlusBoson(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "W+ Boson"
        self.mass = 9
        self.charge = 1
        super().__init__(x, y, self.charge, self.mass, self.name)

# W- Boson Subclass
class WMinusBoson(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "W- Boson"
        self.mass = 9
        self.charge = -1
        super().__init__(x, y, self.charge, self.mass, self.name)

# Z Boson Subclass
class ZBoson(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Z Boson"
        self.mass = 9
        self.charge = 0
        super().__init__(x, y, self.charge, self.mass, self.name)

# Higgs Boson Subclass
class HiggsBoson(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Higgs Boson"
        self.mass = 11
        self.charge = 0
        super().__init__(x, y, self.charge, self.mass, self.name)

# ----------------------------------------------------------------
# -----------------------BARYON SUBCLASSES------------------------
# ----------------------------------------------------------------

# Proton Subclass
class Proton(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Proton"
        self.mass = 15
        self.charge = 1
        super().__init__(x, y, self.charge, self.mass, self.name)

# Neutron Subclass
class Neutron(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Neutron"
        self.mass = 15
        self.charge = 0
        super().__init__(x, y, self.charge, self.mass, self.name)

# ----------------------------------------------------------------
# --------------------ANTIPARTICLE SUBCLASSES---------------------
# ----------------------------------------------------------------

# Positron subclass
class Positron(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Positron"
        self.mass = 8
        self.charge = 1
        self.antiparticle_of = Electron
        super().__init__(x, y, self.charge, self.mass, self.name)

# Anti Muon subclass
class AntiMuon(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Anti Muon"
        self.mass = 8
        self.charge = 1
        self.antiparticle_of = Muon
        super().__init__(x, y, self.charge, self.mass, self.name)

# Anti Tau Subclass
class AntiTau(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Anti Tau"
        self.mass = 8
        self.charge = 1
        self.antiparticle_of = Tau
        super().__init__(x, y, self.charge, self.mass, self.name)

# Electron Anti Neutrino Subclass
class ElectronAntiNeutrino(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Electron Anti Neutrino"
        self.mass = 4
        self.charge = 0
        self.antiparticle_of = ElectronNeutrino
        super().__init__(x, y, self.charge, self.mass, self.name)

# Muon Anti Neutrino Subclass
class MuonAntiNeutrino(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Muon Anti Neutrino"
        self.mass = 4
        self.charge = 0
        self.antiparticle_of = MuonNeutrino
        super().__init__(x, y, self.charge, self.mass, self.name)

# Tau Anti Neutrino Subclass
class TauAntiNeutrino(Particle):

    # Initialiser
    def __init__(self, x, y):

        # Setting attributes
        self.name = "Tau Anti Neutrino"
        self.mass = 4
        self.charge = 0
        self.antiparticle_of = TauNeutrino
        super().__init__(x, y, self.charge, self.mass, self.name)