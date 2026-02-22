---
title: "Core components"
categories: ["4.2", "Game_concepts", "Warfare"]
---

# Core components

On the right side of the designer, one can select options for different subsystems of the ship. Most of them are required and it is not possible to design a ship without some version of them, but few of them are optional, having the option to install no subsystem in its slot.

Space fauna designs can only use the starting core components until the matching bio-integration technology has been researched, at which point they can use all researched core components. Their components do not use power.

## Power generation

The power generation component provides power for the ship's other components, and a new ship design cannot be saved if it has negative power. Excess power slightly increases a ship's evasion, movement speed, and damage.

- Mechanical ships use reactors. They cost Alloys in construction and upkeep.
- Biological ships use metabolisms. They cost Food in construction and upkeep. They cost 3.5 times more than reactors. Their output is increased by 25% if the ship reaches the Mature growth stage and by 50% if the ship reaches the Elder growth stage.

| Power source | Corvette / Frigate / Mauler / Swarmer | | Destroyer / Weaver | | Cruiser / Harbinger / Escort | | Battleship / Stinger | | Titan / Enigma Battlecruiser | | Defense platform | | Juggernaut / Star-Eater / Paradox Titan | | Colossus | Required technology |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Cost | Power Power | Cost | Power Power | Cost | Power Power | Cost | Power Power | Cost | Power Power | Cost | Power Power | Cost | Power Power | Power Power | | |
| **Fission** | 10 | 75 | 20 | 140 | 40 | 280 | 80 | 550 | 160 | 1100 | 20 | 200 | 560 | 3850 | No | Fission Power |
| **Fusion** | 13 | 100 | 26 | 180 | 52 | 360 | 104 | 720 | 208 | 1450 | 26 | 260 | 730 | 5000 | No | Fusion Power |
| **Cold Fusion** | 17 | 130 | 34 | 240 | 68 | 480 | 136 | 950 | 272 | 1900 | 34 | 340 | 950 | 6500 | No | Cold Fusion Power |
| **Antimatter** | 22 | 170 | 44 | 320 | 88 | 620 | 176 | 1250 | 352 | 2500 | 44 | 440 | 1230 | 8460 | No | Antimatter Power |
| **Zero-Point** | 28 | 220 | 56 | 430 | 112 | 800 | 224 | 1550 | 448 | 3200 | 56 | 575 | 1600 | 11000 | 10000 | Zero Point Power |
| **Dark Matter** | 37 1 | 285 | 74 2 | 550 | 148 4 | 1030 | 296 8 | 2000 | 592 16 | 4200 | 74 4 | 750 | 2080 32 | 14300 | 10000 | Dark Matter Power |

## FTL

The FTL component is optional, but without one the ship is incapable of moving between systems. They cannot be reverse-engineered from ship debris.

- Mechanical ships use drives. They cost Alloys in construction and upkeep.
- Biological ships use bio-fields. They cost Food in construction and upkeep. They cost 3.5 times more than drives.
- Space fauna use bio-drives. They cost Food and Minerals in construction and upkeep. They cost 3.6 times more than drives.

Tactical jumps allow the ship to make a direct jump within a limited range, indicated by a yellow dotted circle. Initiate a jump by selecting the fleet, clicking the "Initiate Jump" button and left-clicking the target. After jumping the fleet spends 200 days recharging, during which time it suffers −50% sublight speed and weapons damage.

| FTL | Cost | Power Power | Disengagement Opportunities | Hyper jump | Tactical jump | Required technology | Crisis date |
|---|---|---|---|---|---|---|---|
| **Subspace** | 5 | 5 | 0 | No | Yes −25% Cooldown −50% Range | Subspace Drive | regular |
| **Hyper I** | 5 | 10 | 1 | Yes | No | Hyperspace Travel | regular |
| **Hyper II** | 10 | 15 | 1 | Yes −25% Charge time | No | Hyperlane Breach Points | regular |
| **Hyper III** | 15 | 20 | 1 | Yes −50% Charge time | No | Hyperspace Slipstreams | regular |
| **Jump** | 20 | 30 | 1 | Yes −70% Charge time | Yes | Jump Drive | 25 years earlier |
| **Psi Jump** | 20 | 30 | 2 | Yes −80% Charge time | Yes +50% Range | Psi Jump Drives | 25 years earlier |

## Computer system

This component predominantly improves fire-rate as well as various combat stats depending on behavior type.

- Mechanical ships use combat computers. They cost Alloys in construction and upkeep.
- Biological ships use neural implants. They cost Food in construction and upkeep. They cost 3.5 times more than combat computers.
- Space fauna use neurochips. They cost Food and Minerals in construction and upkeep. They cost 1.1 times less than combat computers.

When in combat, every military ship will advance to within a certain distance of its target and fire its weapons. The engagement range is determined by the ship's designated role and the effective range of the ship's weapons. Weapon range modifiers will also increase this range. Ships that have similar roles will typically cluster together, stay in formation with each other and attack in groups.

- **Swarm:** The ship will charge straight at enemies and try to deal as much damage as possible from the range of their shortest range weapon.
- **Torpedo:** The ship will charge straight at enemies in strafing runs.
- **Picket:** The ship will advance to medium range and attempt to intercept incoming enemies.
- **Line:** The ship will hold advance to medium range and hold formation.
- **Artillery:** The ship will stay at medium range, firing its longest range weapons on the target.
- **Carrier:** The ship will stay at the maximum engagement range of its hangars.
- **Platform:** The defensive platform will remain stationary and fire at any enemies in range.
- **Colossus:** The ship will ignore any attackers and carry on with its current task.

| Level | | Power | Effects | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Swarm | Torpedo | Picket | Line | Artillery | Carrier | Platform | Starbase | Colossus | | | |
| Basic | 0 | 0 | Default for corvette | Default for frigate | Default for destroyer | Default for cruiser Default for star-eater | Default for battleship Default for titan | Default for juggernaut | | - +5% Fire rate<br>- Tracking +10 Tracking | Only option |
| Specialized | 5 | 10 | - +5% Fire rate<br>- +5% Evasion | +5% Explosive weapons damage | - +5% Fire rate<br>- Tracking +10 Tracking | - +5% Fire rate<br>- +5% Chance to hit | - +5% Fire rate<br>- +5% Weapons range | - +25% Engagement range | - +25% Fire rate<br>- Tracking +15 Tracking | - +10% Fire rate<br>- Tracking +20 Tracking | No |
| Advanced | 10 | 15 | - +10% Fire rate<br>- +10% Evasion | +10% Explosive weapons damage | - +10% Fire rate<br>- Tracking +20 Tracking | - +10% Fire rate<br>- +10% Chance to hit | - +10% Fire rate<br>- +10% Weapons range | - +50% Engagement range | - +30% Fire rate<br>- Tracking +20 Tracking | - +15% Fire rate<br>- Tracking +30 Tracking | No |
| Sapient Autonomous | 20 | 25 | - +15% Fire rate<br>- +25% Evasion | - +10% Evasion<br>- +15% Explosive weapons damage | - +15% Fire rate<br>- Tracking +30 Tracking<br>- +10% Evasion | - +20% Fire rate<br>- +20% Chance to hit | - +20% Fire rate<br>- +20% Weapons range | - +100% Engagement range | - +35% Fire rate<br>- Tracking +25 Tracking<br>- +10% Chance to hit | No | No |
| Precognitive | 20 | 25 | - +15% Fire rate<br>- +15% Evasion<br>- +20% Sublight speed | - +15% Explosive weapons damage<br>- Tracking +10 Tracking | - +20% Fire rate<br>- Tracking +40 Tracking | - +15% Fire rate<br>- +15% Chance to hit<br>- Tracking +10 Tracking | - +15% Fire rate<br>- +15% Weapons range<br>- Tracking +10 Tracking | - +75% Engagement range<br>- Tracking +10 Tracking | - +35% Fire rate<br>- Tracking +35 Tracking | No | No |
| Allowed ship types | | | Corvette<br>- Mauler<br>- Nanite swarmer<br>- Space fauna | - Frigate<br>- Cruiser<br>- Riddle Escort<br>- Nanite swarmer<br>- Nanite interdictor<br>- Space fauna | - Corvette<br>- Destroyer<br>- Cruiser<br>- Mauler<br>- Riddle escort<br>- Nanite swarmer<br>- Space fauna | - Destroyer<br>- Cruiser<br>- Battleship<br>- Stinger<br>- Star-eater<br>- Riddle escort<br>- Enigma battlecruiser<br>- Space fauna | - Corvette<br>- Frigate<br>- Destroyer<br>- Cruiser<br>- Battleship<br>- Harbinger<br>- Stinger<br>- Titan<br>- Juggernaut<br>- Star-eater<br>- Riddle escort<br>- Enigma battlecruiser<br>- Paradox titan<br>- Nanite interdictor<br>- Space fauna | - Cruiser<br>- Battleship<br>- Harbinger<br>- Juggernaut<br>- Star-eater<br>- Enigma battlecruiser<br>- Paradox titan<br>- Nanite swarmer<br>- Nanite interdictor<br>- Space fauna | - Defense platform<br>- Ion Cannon | - Starbase<br>- Orbital Ring<br>- Citadel | Colossus |

### Weaver Neural Implants

Weavers use special neural implants. They have two designated role: Supressor or Support.

| Level | | Power | Effects | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Supressor | Support | | | | | | | | | | |
| Basic | 0 | 0 | | | | | | | | | |
| Specialized | 17.5 | 10 | - +5% Supressor Weapon Fire rate<br>- +5% Chance to hit | - +5% Support Weapon Fire rate<br>- +5% Evasion | | | | | | | |
| Advanced | 35 | 15 | - +10% Supressor Weapon Fire rate<br>- +10% Chance to hit | - +10% Support Weapon Fire rate<br>- +10% Evasion | | | | | | | |
| Sapient Autonomous | 70 | 25 | - +20% Supressor Weapon Fire rate<br>- +20% Chance to hit | - +20% Support Weapon Fire rate<br>- +20% Evasion | | | | | | | |
| Precognitive | 70 | 25 | - +15% Supressor Weapon Fire rate<br>- +15% Chance to hit<br>- Tracking +10 Tracking | - +15% Support Weapon Fire rate<br>- +15% Evasion<br>- +20% Sublight speed | | | | | | | |

## Propulsion

The propulsion component determines how fast the ship moves within a star system and increase its chance to evade weapons fire.

- Mechanical ships use thrusters. They cost Alloys in construction and upkeep.
- Biological ships use stellar motor organs. They cost Food in construction and upkeep. They cost 3.5 times more than thrusters.
- Space fauna use bio thrusters. They cost Food and Minerals in construction and upkeep. They cost 3.3 times more than thrusters.

| Propulsion | | Corvette | Destroyer | Cruiser | Battleship | Titan | Colossal ships | Sublight Speed |
|---|---|---|---|---|---|---|---|---|
| **Chemical** | Cost | 3 | 6 | 12 | 24 | 48 | 60 | |
| Power Power | 10 | 20 | 40 | 80 | 160 | 200 | | |
| Evasion Chance | | | | | | | | |
| **Ion** | Cost | 6 | 12 | 24 | 48 | 96 | 120 | +25% |
| Power Power | 15 | 30 | 60 | 120 | 240 | 300 | | |
| Evasion Chance | +5 | +4 | +3 | +2 | +1 | | | |
| **Plasma** | Cost | 9 | 18 | 36 | 72 | 144 | 180 | +50% |
| Power Power | 20 | 40 | 80 | 160 | 320 | 400 | | |
| Evasion Chance | +10 | +8 | +6 | +4 | +2 | | | |
| **Impulse** | Cost | 12 | 24 | 48 | 96 | 192 | 240 | +75% |
| Power Power | 25 | 50 | 100 | 200 | 400 | 500 | | |
| Evasion Chance | +15 | +12 | +9 | +6 | +3 | | | |
| **Dark Matter** | Cost | 12 1 | 24 2 | 48 4 | 96 8 | 192 16 | 300 32 | +125% |
| Power Power | 30 | 60 | 120 | 240 | 480 | 600 | | |
| Evasion Chance | +20 | +16 | +12 | +8 | +4 | | | |

## Sensors

The sensors components determines the ship's detection range on the galaxy map. They also increase tracking of all weapon components.

- Mechanical ships use sensors. They cost Alloys in construction and upkeep.
- Biological ships use radiosensors. They cost Food in construction and upkeep. They cost 3.5 times more than sensors.
- Space fauna use sensory organs. They cost Food and Minerals in construction and upkeep. They cost 3.3 times more than sensors.

| Sensors | Cost | Power Power | Tracking Tracking | Sensor range | Hyperlane detection range | Requirements |
|---|---|---|---|---|---|---|
| **Radar** | 2 | 5 | | 1 | 2 | |
| **Gravitic** | 4 | 10 | +5 | 2 | 3 | Gravitic Sensors |
| **Subspace** | 6 | 15 | +10 | 3 | 4 | Subspace Sensors |
| **Tachyon** | 8 | 20 | +15 | 4 | 5 | Tachyon Sensors |
| **Seer-Pattern** | | 25 | | 9 | 11 | The Pattern Maker |

## Field emitters

All field emitter components apply either a buff to allied ships (own, subjects, federation members and war time allies) or a debuff to all enemy ships that are in the system. Multiple instances of the same field emitter effect do not stack.

| Field emitter | Ship | Target | Effects | Notes |
|---|---|---|---|---|
| FTL Inhibitor | - Starbase (Starport and above)<br>- Deep Space Citadel | Hostiles | - +100% Emergency FTL Jump Cooldown<br>- Enemy ships can only leave the system via the hyperlane they arrived through | |
| Offspring Oversight | Offspring ships | Allies | - +55% Accuracy<br>- +55% Evasion<br>- +55% Ship Fire Rate<br>- +55% Sublight Speed | Time +2 Growth Progress Rate on installed ship if Biological Shipset |
| Bulwark Battlefield Repairs | Battlewright construction ship | Allies | +0.25% Daily Hull Regen | |
| Electromagnetic Disruptor | Arctrellis science ship | Hostiles | - Only applies to ships if they're owned by an empire using a Sapient or Autonomous combat computer or Machine founder species<br>- −25% Accuracy<br>- −25% Ship Fire Rate<br>- −25% Sublight Speed | |

### Titan field emitters

Titan field emitter components can only be installed on titan and paradox titan ships and tier 3 deep space citadels.

| Field emitter | Target | Effects |
|---|---|---|
| Quantum Destabilizer | Hostiles | −10% Fire Rate |
| Shield Dampener | Hostiles | −20% Shield Hit Points |
| Subspace Snare | Hostiles | - +100% Emergency FTL Jump Cooldown<br>- −20% Combat Disengagement Chance |
| Inspiring Presence | - Titan's fleet<br>- Citadel and defense platforms | +5% Fire Rate |
| Nanobot Cloud | - Titan's fleet<br>- Citadel and defense platforms | - +5% Daily Hull Regen<br>- +15% Daily Armor Regen |
| Targeting Grid | - Titan's fleet<br>- Citadel and defense platforms | +10 Tracking |
| Ancient Target Scrambler | - Titan's fleet<br>- Citadel and defense platforms | +5% Evasion Chance |

### Juggernaut field emitters

Juggernaut field emitter components can only be installed on juggernauts and tier 3 deep space citadels.

| Field emitter | Target | Effects |
|---|---|---|
| ECM Emitters | Hostiles | - −30% Point Defense Damage<br>- −30% Point Defense Firing Rate |
| Munitions Plant | Allies | +30% Orbital Bombardment Damage |
| Strike Command | Allies | - +20% Strike Craft Damage<br>- +20% Strike Craft Speed |
| Subspace Amplifier | Allies | - −40% Hyper Jump Charge Time<br>- −40% Hyper Jump Cooldown<br>- −40% Jump Drive Cooldown |
| Target Acquisition Array | Allies | +40% Ship Weapons Range |

### Deep Space Citadel field emitters

Deep Space Citadel field emitter components can only be installed on deep space citadels.

| Field emitter | Target | Effects |
|---|---|---|
| Cognition Scrambler | Hostiles | −25% Strike Craft Damage |
| Micro-Singularity Destabilizer | Hostiles | −25% Kinetic Weapon Damage |
| Multi-Target Generators | Hostiles | −25% Explosive Weapon Damage |
| Anti-Polaron Emitter | Hostiles | −25% Energy Weapon Damage |

## Supplementary organs

Supplementary organs are components available to biological ships once that ship's development technology has been researched.

BUG (v4.0.1 (1ae3)): Due to incorrect codes for supplementary organs, these supplementary organs do not have their modifiers applied correctly, excepting Metabolic Recycler and Developmental Pheromones.

| Supplementary organ | Growth stage | Effects | Cost | | | |
|---|---|---|---|---|---|---|
| Mauler | Weaver | Harbinger | Stinger | | | |
| Juvenile Growth Gland | Juvenile | Time +1 Growth Progress Rate | 21 | 43 | 86 | 171 |
| Accelerated Juvenile Growth Gland | Juvenile | Time +2 Growth Progress Rate | 21 0.5 | 43 0.5 | 86 0.5 | 171 0.5 |
| Mature Growth Gland | Mature | Time +1 Growth Progress Rate | 43 | 143 | 171 | 342 |

### Mauler supplementary organs

Mauler supplementary organs cost 16 Food. Tier 1 components require 5 power while tier 2 components require 10 power.

| Supplementary organ | Effects | Cost |
|---|---|---|
| Corrosive Fluids | - +5% Mandible Weapon Damage<br>- +5% Armor Damage | |
| Caustic Fluids | - +10% Mandible Weapon Damage<br>- +10% Armor Damage | 0.5 |
| Metabolic Recycler | - +5% Sublight Speed<br>- +2% Evasion Chance | |
| Energetic Recycler | - +10% Sublight Speed<br>- +5% Evasion Chance | 0.5 |

### Weaver supplementary organs

Weaver supplementary organs cost 16 Food. Tier 1 components require 5 power while tier 2 components require 10 power.

| Supplementary organ | Effects | Cost |
|---|---|---|
| Developmental Pheromones | - Time +1 Growth Progress Rate for Biological Ships in fleet<br>- +50% Upkeep for Biological Ships in fleet | |
| Exotic Developmental Pheromones | - Time +2 Growth Progress Rate for Biological Ships in fleet<br>- +100% Upkeep for Biological Ships in fleet | 0.5 |
| Basic Symbiotic Amplifier | - +5% Support Weapon Fire Rate<br>- +5% Suppressor Weapon Fire Rate<br>- +5% Ship Weapons Range | |
| Upgraded Symbiotic Amplifier | - +10% Support Weapon Fire Rate<br>- +10% Suppressor Weapon Fire Rate<br>- +10% Ship Weapons Range | 0.5 |

### Harbinger supplementary organs

Harbinger supplementary organs cost 16 Food. Tier 1 components require 5 power while tier 2 components require 10 power.

| Supplementary organ | Effects | Cost |
|---|---|---|
| Chitin Growth Regulators | - +5% Ship Engagement Range<br>- Armor +5 Strike Craft Armor | |
| Crystalline Growth Regulators | - +10% Ship Engagement Range<br>- Armor +10 Strike Craft Armor | 0.5 |
| Incubation Matrix | - +5% Ship Engagement Range<br>- Time −5% Strike Craft Cooldown | |
| Rapid Incubation Matrix | - +10% Ship Engagement Range<br>- Time −10% Strike Craft Cooldown | 0.5 |

### Stinger supplementary organs

Stinger supplementary organs cost 16 Food. Tier 1 components require 5 power while tier 2 components require 10 power.

| Supplementary organ | Effects | Cost |
|---|---|---|
| Rangefinder Cluster | - Tracking +5 Tracking<br>- +5% Ship Weapons Range | |
| Improved Rangefinder Cluster | - Tracking +10 Tracking<br>- +10% Ship Weapons Range | 0.5 |
| Heat Exhaust Spiracles | - Tracking +5 Tracking<br>- +5% Ship Fire Rate | |
| Volatile Spiracles | - Tracking +10 Tracking<br>- +10% Ship Fire Rate | 0.5 |