## Standard Model Particle Physics Simulation: Code Overview And Coverage

This simulation models key aspects of the Standard Model of particle physics using Python. It includes a range of fundamental and composite particles, and simulates the interactions and decays that govern their behavior. The code aims to provide a simplified but meaningful representation of how these particles might move and interact in a 2D space.

---

### Core Components

#### 1. **Particles**

The code defines a variety of particles across the main categories of the Standard Model:

* **Fermions**:

  * *Leptons*: electron, muon, tau, and their neutrinos and antiparticles.
  * *Quarks*: up, down, strange, charm, bottom, top, and corresponding antiquarks.

* **Bosons**:

  * photon, gluon, W and Z bosons, and the Higgs boson.

* **Composite Particles**:

  * protons and neutrons are modeled as bound states of quarks (e.g., uud or udd).

Each particle class includes basic properties like mass, charge, radius, and color (for visualization), as well as position and velocity.

---

### Particle Colour Coding

To visually distinguish between different particle types during the simulation. Each particle is assigned a colour based on either its type or electric charge. Certain bosons overide the default charge logic.

| Particle Category    | Colour | Visual |
| -------------------- | ------ | ------ |
| Higgs boson          | Yellow | 💛     |
| Gluon                | Grey   | 🩶     |
| Photon               | Cyan   | 🩵     |
| Positively charged   | Red    | ❤️     |
| Negatively charged   | Blue   | 💙     |
| Neutral (non-bosons) | Green  | 💚     |


---

#### 2. **Fundamental Forces**

The three fundamental forces are implemented through custom force classes:

* **Electromagnetic Force**:
  Acts on charged particles, attracting or repelling them based on Coulomb's law.

* **Strong Nuclear Force**:
  Applies at short ranges between quarks, encouraging them to bind into composite states like protons and neutrons.

* **Weak Nuclear Force**:
  Handles specific particle decay processes, such as:

  * Neutron → Proton + Electron + Electron Anti-Neutrino
  * Muon → Electron + Muon Neutrino + Electron Anti-Neutrino
  * Tau → Muon + Tau Neutrino + Muon Anti-Neutrino

---

#### 3. **Interactions and Events**

In addition to the forces, several interaction rules are defined:

* **Annihilation**:
  Particle–antiparticle pairs (such as electron–positron, muon–antimuon, quark–antiquark) annihilate when close together, producing a photon.

* **Decay**:
  The WeakForce class manages probabilistic decays of unstable particles over time.

* **Quark Binding**:
  When the strong force brings appropriate quarks together, they form baryons like protons and neutrons.

* **Higgs Interaction**:
  Assigns mass to patticles while keeping photons massless, loosely illustrating electroweak symmetry breaking.

These events are resolved per timestep and modify the list of active particles accordingly.

---

### Physical Concepts Represented

The simulation touches on many of the key ideas in particle physics:

| Concept                     | Representation                                        |
| --------------------------- | ----------------------------------------------------- |
| Electromagnetic interaction | Charged particles attract or repel                    |
| Annihilation                | Particle–antiparticle pairs produce photons           |
| Beta decay                  | Neutron decays via the weak force                     |
| Particle generations        | Higher mass leptons decay into lighter ones           |
| Composite particles         | Baryons form from quark triplets                      |
| Higgs mechanism             | W/Z bosons have mass, photon does not                 |

---

These behaviors aren't perfectly physical but aim to qualitatively mirror the correct relationships and tendencies in real systems.

---

### Simulation Mechanics

The `Simulation` class handles the update loop. It processes:

* Particle motion and velocity updates
* Application of all active forces
* Detection of collisions and interactions
* Particle creation or removal based on decay/annihilation
* Display updates (using a 2D window)

---

### Flexibility

The system allows different setups of particles and force combinations, which makes it easy to isolate and test how different processes emerge.

---

### Summary

This simulation brings together the key components of the Standard Model in a way that's computationally lightweight but still capable of showing complex behaviors. It’s useful for getting an intuitive sense of how particle interactions might play out and gives a basic but structured platform to explore ideas like decays, annihilation, and binding.

---