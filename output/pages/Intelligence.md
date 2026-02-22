---
title: "Intelligence"
categories: ["4.2", "Game_concepts"]
---

# Intelligence

**Intelligence** and espionage are two important factors in gaining the upper hand over other empires . While an empire can only be defeated militarily, espionage can be used to significantly weaken it or gain substantial advantages over it.

## Intel

Intel is a value between **0** and **100** that represents how much information an empire has about another empire. Intel automatically increases or decreases towards the intel cap for the target empire. Some intelligence on systems, including fleets and colonies, can also be gained via sensors (fleets, starbases, or colonies).

### Intel level

There are 5 categories of intelligence, and 5 intel levels for each category: No None, Low, Medium, High, and Full. Every 10 points of intel increases the intel level in at least one category of intelligence, revealing additional information about the target empire.

| Category | Intel | | | | | | | | | | |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 0-9 | 10-19 | 20-29 | 30-39 | 40-49 | 50-59 | 60-69 | 70-79 | 80-89 | 90-99 | 100 | |
| Government | No | Intel level low | Intel level low | Intel level low | Intel level mid | Intel level mid | Intel level mid | Intel level high | Intel level high | Intel level high | Intel level full |
| Diplomacy | No | No | Intel level low | Intel level low | Intel level low | Intel level mid | Intel level mid | Intel level mid | Intel level high | Intel level high | Intel level full |
| Economy Technology Military | No | No | No | Intel level low | Intel level low | Intel level low | Intel level mid | Intel level mid | Intel level mid | Intel level high | Intel level full |

Besides increasing intel, intel levels can be gained temporarily via intel reports from operations. Each intel level reveals the following information:

| Category | Low intel | Medium intel | High intel | Full intel |
|---|---|---|---|---|
| Government | - Authority<br>- Ethics<br>- Capital location<br>- Ruler | - Civics<br>- Origin<br>- Number of owned relics<br>- Governors | - Empire size | |
| Diplomacy | - Casus belli<br>- Relative power<br>- Rivalries<br>- Federation names | - Opinion breakdown<br>- Diplomatic pacts<br>- Galactic community vote rationale | - Specialist tier | - Secret diplomatic pacts |
| Economy | - Owned inhabited systems<br>- Relative economic power | - Owned systems<br>- Number of colonies<br>- Location of colonies<br>- Planet class of colonies<br>- Location of civilian ships | - Planet class of owned planets<br>- All information about colonies (districts, population, etc)<br>- Current orders of civilian ships<br>- Subject resource production | - Surveyed celestial objects in owned systems |
| Technology | - Relative technological power<br>- Number of researched technologies | | | |
| Military | - Casus belli<br>- Relative fleet power<br>- Location of starbases<br>- Imminent invasion plans | - Ship details | - Location of military fleets | - Current orders of military fleets<br>- Cloaked fleets |

If an intel level is reduced, all information from the previous level is lost. Information about relative power will remain displayed but will be marked as Stale and no longer update.

### Intel cap

Intel cap is determined by base intel level, diplomatic pacts , trust, or infiltration, whichever is the highest. If current intel is below the intel cap, it increases by +1 per month. If current intel is above the intel cap, it decreases by −1 per year. Intel cap from trust is equal to half the trust amount, while intel cap from infiltration is equal to the infiltration level.

The following are used to determine intel cap from diplomatic pacts. They do not stack unless specified otherwise. Some of them can also be increased by the following:

- Establishing an Embassy between empires increases all of the below intel caps by +20 , and gives information about the empire's diplomatic pacts.
- Federation centralization increases federation intel caps by +10 per federation centralization level.

| Relationship | Information Gained | | | Intel Cap |
|---|---|---|---|---|
| Intel on Systems | Relative Power | Other information | | |
| First Contact | | | | 10 |
| Commercial Pact | Medium Intel on Systems High Intel on Colonies | Relative Economic Power | | 20 |
| Guarantee Independence | | | | 20 |
| Non-Aggression Pact | | | | 20 |
| Secret Fealty | | | | 20 |
| Galactic Community member | | | | 30 |
| Migration Treaty | Low Intel on Systems | | | 30 |
| Research Agreement | | Relative Technological Power | | 30 |
| Overlord empire (as their subject) | | | | 30 |
| Subject empire (as their overlord) | Low Intel on Systems Low Intel on Colonies | | Specialist Subject Tier Resource Production | 40 |
| Defensive Pact | Low Intel on Systems | Relative Fleet Power | | 40 |
| Federation Associate | Low Intel on Systems | | | 40 |
| Hegemony federation | Low Intel on Systems | | | 40 |
| Martial Alliance federation | Low Intel on Systems | Relative Fleet Power | | 50 |
| Research Cooperative federation | Low Intel on Systems | Relative Technological Power | | 50 |
| Trade League federation | Low Intel on Systems | Relative Economic Power | | 50 |
| Galactic Union federation | Low Intel on Systems | | | 60 |
| Galactic Community member<br>  - (as Galactic Custodian) | | Relative Fleet Power | | 45 |
| Galactic Imperium member<br>  - (as Galactic Emperor) | High Intel on Systems High Intel on Colonies | Relative Fleet Power | | 65 |
| Galactic Imperium member<br>  - (as Galactic Emperor with Imperial Security Directorate) | High Intel on Systems High Intel on Colonies | Relative Fleet Power | | 80 |

#### Base intel level

Base intel level grants a minimum on intel cap towards every empire. Base intel starts at 10 and can be increased by the following:

| Base intel level 0 | |
|---|---|
| Source | Effect |
| Tactical Algorithms civic | +20 |
| Blabbermouth III councilor trait | +20 |
| Bureau of Espionage edict | +10 |
| Covert Analysis Algorithm edict | +10 |
| Observation Instinct edict | +10 |
| Blabbermouth II councilor trait | +10 |
| Colonial Bureaucracy technology | +10 |
| Galactic Bureaucracy technology | +10 |
| Mind Readers tradition | +10 |
| Blabbermouth I councilor trait | +5 |
| Uncover Secrets agenda | +5 |

## Spy networks

| Infiltration | Growth | Max. |
|---|---|---|
| Relative codebreaking and encryption Maximum 4 point difference | ±10% | ±10 |
| Criminal Heritage civic | +20% | — |
| Shadow Recruits tradition | +50% | — |
| Double Agents tradition | — | +10 |
| Bureau of Espionage edict | — | +10 |
| Per asset | — | +5 |
| Per Disinformation Center holding | — | +5 |
| Per Science Ship on Active Reconnaissance | +10% | — |
| Prepare for War | +33% | — |

Spy networks are created by assigning an envoy to build one in a target empire via the diplomacy or espionage menu. Creating a spy network allows an empire to launch various operations once they have a sufficient infiltration level. Infiltration level grows over time as long as an envoy is assigned to the spy network and the current level is below the maximum level. Each day the spy network gains +1 point, plus an additional +0.0025 for each point of empire size in the target empire (i.e +1 per 400 ). Overlords and their subjects gain an additional +1 points daily when building a network on each other. Each infiltration level requires 5 points plus 5 points times the current level. For example, to increase from level 49 to level 50 requires 5 + (5 * 49) = 250 points . Spy network growth is multiplied by various factors, as shown in the table on the right. If the envoy is removed or the maximum infiltration level drops below the current infiltration level, the current infiltration level falls by −1 each month unless a Prepare Sleeper Cells operation was completed.

The current infiltration level is visible on the diplomacy screen to the right of the intel level along with an arrow showing the current trend. Hovering over the infiltration icon displays the maximum as well as the current infiltration growth. The current and maximum infiltration can also be seen in the espionage screen. The base maximum infiltration level is **50** . Maximum infiltration can also be increased by various factors, as shown in the table on the right, as well as the Gather Information operation, which temporarily raises the maximum infiltration level by +5 (stackable to a maximum of +20 ).

### Codebreaking and Encryption

**Codebreaking** represents the ability to effectively infiltrate another empire, while **Encryption** represents an empire's defense against foreign infiltration. When an operation takes place, the infiltrating empire's codebreaking is pitted against the infiltrated empire's encryption to determine the modified difficulty of the operation. Each can be increased by various factors listed below. Only the relative value of codebreaking and encryption matters, and the various benefits (or penalties) are capped at 4 points above (or below) the other empire.

| Codebreaking 0 | |
|---|---|
| Source | Effect |
| The Pattern Maker relic | +4 |
| Bureau of Espionage edict | +2 |
| Observation Instinct edict | +2 |
| Covert Analysis Algorithm edict | +2 |
| Quantum Hacking technology | +2 |
| Simulated Social Engineering technology | +2 |
| Quasi-Dimensional Reflection technology | +2 |
| Virtuality tradition tree | +2 |
| Shrouded Communications tradition | +2 |
| Imperial Security Directorate resolution | +2 |
| Uncover Secrets agenda | +2 |
| The Passenger ruler trait | +2 |
| Ever Vigilant III ruler trait | +2 |
| Ever Vigilant II ruler trait | +2 |
| Blorg Insight councillor trait | +2 |
| Shadow Broker II councillor trait | +2 |
| Sentry Array Stage IV | +2 |
| Unknown Whisperers in the Void covenant (50 favor) | +2 |
| Unknown Whisperers in the Void covenant | +1 |
| Corporate Recollection authority | +1 |
| Cutthroat Politics civic | +1 |
| Shadow Council civic | +1 |
| Static Research Analysis civic | +1 |
| Spyware Directives civic | +1 |
| Criminal Heritage civic | +1 |
| Ruthless Competition civic | +1 |
| Subterfuge tradition tree | +1 |
| Operational Security tradition | +1 |
| Shadow Matrix edict | +1 |
| Rolling Updates edict | +1 |
| Unknown Defeated Absurdism empire modifier | +1 |
| Unknown Rock Brain Linguistics empire modifier | +1 |
| Unknown Mycelial Network empire modifier | +1 |
| Inward Perfection civic | −1 |
| Optimized Network agenda launch effect | +1 |
| Ever Vigilant ruler trait | +1 |
| Shadow Broker councillor trait | +1 |
| Sentry Array Stage III | +1 |
| Sentry Array Stage II | +1 |

| Encryption 0 | |
|---|---|
| Source | Effect |
| Imperial Security Directorate resolution | +4 |
| Ever Vigilant III ruler trait | +4 |
| Ever Vigilant II ruler trait | +2 |
| Common leader traits, The Passenger ruler trait | +2 |
| Shady Contacts II councillor trait | +2 |
| Gestalt Consciousness ethic | +2 |
| Enigmatic Engineering ascension perk | +2 |
| Virtuality tradition tree | +2 |
| Strong on our Own agenda launch effect | +2 |
| Shrouded Communications tradition | +2 |
| Quantum Firewalls technology | +2 |
| Simultaneous-Collapse Storage technology | +2 |
| Negative-Time Keys technology | +2 |
| Unknown Closed Society empire modifier | +2 |
| Unknown Asteroid Encryption empire modifier | +1 |
| Unknown Disinformation Protocols empire modifier | +1 |
| Inward Perfection civic | +1 |
| Genetic Identification civic | +1 |
| Pooled Knowledge civic | +1 |
| Introspective civic | +1 |
| Tracking Implants edict | +1 |
| Thought Enforcement edict | +1 |
| Enhanced Surveillance edict | +1 |
| Shadow Matrix edict | +1 |
| Rolling Updates edict | +1 |
| Information Security tradition | +1 |
| Virtual Leader ruler trait | +1 |
| Chosen of the Whisperers ruler trait | +1 |
| Ever Vigilant I ruler trait | +1 |
| Shady Contacts I councillor trait | +1 |
| Optimized Network agenda launch effect | +1 |

### Operations

| Operation difficulty modifiers | |
|---|---|
| Relative codebreaking and encryption Maximum 4 point difference | ±4 |
| Operational Security tradition | −2 |
| Target has Non-Disclosure Agreement tradition | +1 |
| Per matching category of assigned asset | −4 |
| Subject or overlord of target | −2 |
| Successful Prepare Sleeper Cells operation | −1 |

Operations are targeted events that can be triggered within a specific empire. To run an operation, an empire must have an envoy assigned to build a spy network in the target empire. All operations have an infiltration level requirement and influence cost as well as an an ongoing energy upkeep until they are completed. The Non-Disclosure Agreement tradition increases the required infiltration level for hostile operations by +20% .

Operations progress similarly to the archeology mechanic, with each preparation phase advancing by rolling a die every 30 days and eventually overcoming the required difficulty check. Each operation has a base difficulty which is modified by the factors in the table on the right. Operation events may occur during the preparation of an operation, possibly modifying the difficulty, influencing the outcome, or requiring the sacrifice of an asset to avoid a negative effect. Most operations reduce the spy network's current infiltration level upon completion. If the Subterfuge is completed, successful operations refund half of the spent infiltration on completion.

#### Operations targeting pre-FTL civilizations

The following operations can only be undertaken towards pre-FTL civilizations. They are riskier and more expensive if the Gene Tailoring technology hasn't been researched and are not available if the Pre-FTL Interference policy is set to Non-Interference.

| Operation | Intel category | Phases | | Costs | | | Requirements | | | Effects | DLC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Launch | Upkeep | Finish | Infilitration | Civilization | Empire | | | | | | |
| **Plant Advanced Knowledge** | Technology | Espionage chapter | 6 | - 30<br>- 20 with | −7 | −20 | 20 | | - No Aggressive Interference policy<br>- No Prohibited Enlightenment policy | Time Increases progress towards the next age | |
| **Infiltrate Government** | Government | Espionage chapter | 7 | - 60<br>- 40 with | −8 | −40 | 40 | - No Hive Mind<br>- Early Space Age | - No Gestalt Consciousness<br>- No Subtle Interference policy<br>- No Inward Perfection | - Yes Civilization is annexed<br>- Yes Civilization's homeworld buildings are upgraded to tier 1<br>- Civilization's homeworld gains +30% Happiness for 20 years | |
| **Indoctrinate Society** | Government | Espionage chapter | 5 | - 55<br>- 40 with | −7 | −30 | 30 | - No Hive Mind<br>- No Same ethics as empire | No Gestalt Consciousness | Yes Civilization shifts ethics towards the empire's | |
| **Infiltrate Hive** | Government | Espionage chapter | 7 | - 60<br>- 40 with | −8 | −40 | 40 | - Hive Mind<br>- Early Space Age | - Gestalt Consciousness<br>- No Subtle Interference policy | - Yes Civilization is annexed<br>- Yes Civilization's homeworld buildings are upgraded to tier 1 | |
| **Increase Awareness** | Diplomacy | Espionage chapter | 5 | - 45<br>- 25 with | −6 | −15 | 15 | No Fully Aware | No Aggressive Interference policy | - +15-20 Awareness<br>- No Awareness cannot decay for 5 years | |
| **Spread Disinformation** | Diplomacy | Espionage chapter | 7 | - 45<br>- 25 with | −6 | −15 | 15 | No Fully Aware | | −20 Awareness | |
| **Procure DNA** | Government | Espionage chapter | 5 | 45 | −6 | None | 30 | | Evolutionary Predators origin | - Yes Gain the DNA of the civilization's phenotype<br>- Gain progress for the Adaptive Evolution situation | |
| **Smuggle Population** | Government | Espionage chapter | 7 | 120 | −10 | −50 | 55 | - 500+ pops<br>- No Both are Fanatic Egalitarian | No Both are Fanatic Egalitarian | Steal 100-200 pops from the civilization | |

#### Operations targeting empires

The following operations can only be undertaken towards spacefaring empires.

| Operation | Operation category | Intel category | Phases | | Costs | | | Requirements | | Effects | DLC |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Launch | Upkeep | Finish | | Others | | | | | | | |
| **Gather Information** | Subterfuge | None | Espionage chapter | 4 | 20 | −4 | −5 | 10 | None | - +5 Maximum infiltration Level for 10 years. Stacks to a maximum of +20 , after which further operations only reset the duration.<br>Randomly receive one of:<br>4.5% per intel category to gain an intel report one level above current (19.2% with an asset of that category). 45.5% to gain +5 intel. 22.7% to gain +10 intel (12.8% if already have 40 intel or more). 9.1% to gain +15 intel (2.4% if already have 50 intel or more). | |
| **Spark Diplomatic Incident** | Manipulation | Diplomacy | Espionage chapter | 5 | 30 | −5 | −10 | 25 | - Communications with 4+ empires<br>- No Gestalt Consciousness target<br>- No Fanatic Purifiers target | - Target suffers a diplomatic event or envoy event | |
| **Prepare Sleeper Cells** | Subterfuge | Government | Espionage chapter | 6 | 45 | −6 | None | 30 | No Wilderness | - +1 Operation Skill and no Spy Network Decay for 15 years<br>- Can sacrifice an asset to double the duration | |
| **Embed Planetary Roots** | Subterfuge | Military | Espionage chapter | 6 | 45 | −6 | None | 30 | Wilderness | - +1 Operation Skill and no Spy Network Decay for 15 years<br>- Can sacrifice an asset to double the duration | |
| **Acquire Asset** | Subterfuge | Government | Espionage chapter | 5 | 45 | −6 | −15 | 30 | None | - Acquires a random asset against the target empire | |
| **Extort Favors** | Manipulation | Diplomacy | Espionage chapter | 6 | 60 | −7 | −20 | 35 | - No Genocidal empire or target | - 80% chance to gain +1 favor from the target<br>- 20% chance to gain +2 favors from the target | |
| **Smear Campaign** | Manipulation | Diplomacy | Espionage chapter | 7 | 60 | −7 | −20 | 35 | Communications with 4+ empires | - Target's Federation loses −20 cohesion<br>- If target is not part of a Federation, it loses −100 opinion with a random empire | |
| **Steal Technology** | Subterfuge | Technology | Espionage chapter | 8 | 80 | −8 | Either:<br>- −20<br>- −30 | 40 | - No Enigmatic Engineering target<br>- Time At least 6 years since the last Steal Technology operation | - +30% Research progress in a random technology<br>- If target has no technology you don't have, gain +1000 research in each category instead<br>- With a Hacker or Memory Cache asset, can give the target −10% research speed for one year at the cost of 10 infiltration and 25 influence<br>Additional options on superior codebreaking:<br>**Research backdoor** Requirements: Relative codebreaking/encryption > 1.4, Subterfuge asset or Technology asset Cost: −1 Technology asset, or −1 Subterfuge asset if you don't have a Technology asset Effect: +10% Research Speed for two years. **Steal extra technology** Requirements: Smooth exit, Subterfuge asset and Technology asset, 16.7% chance (or 37.5% with relative codebreaking/encryption > 1.6) Cost: −1 Technology asset, −10 infiltration Effect: Gain 10% progress in a random technology the target has and you don't. | |
| **Sabotage Starbase Facility** | Sabotage | Military | Espionage chapter | 9 | 100 | −9 | Either:<br>- −30<br>- −45 | 45 | Target has a Starbase or Orbital Ring with a non-Shipyard module or building | If any non-shipyard modules are present, destroys a random non-shipyard module, otherwise destroys a random building.<br>Additional options on success:<br>**Collateral Damage (Module)** Requirements: Sabotage asset and starbase has at least 2 non-shipyard modules, base 16.7% chance (50% with a technology asset, no Military asset, and relative codebreaking/encryption > 0.6) Cost: −1 Technology asset Effect: Target starbase loses random non-shipyard module. **Collateral Damage (Platform)** Requirements: Sabotage asset, at least 2 volatile motes and starbase has a defense platform, base 16.7% chance (50% with a Military asset, no technology asset, and relative codebreaking/encryption > 0.6) Cost: −2 volatile motes Effect: Target starbase loses a random defense platform | |
| **Arm Privateers** | Provocation | Economy | Espionage chapter | 10 | 180 | −12 | −60 | 60 | Time At least 3 years since any empire successfully armed privateers in this empire | A scaling pirate fleet attacks one of the target's systems Target's fleet power Ships 0-299 1 300-599 2 600-999 6 1000-1999 7 2000-3999 11 4000-7999 14 8000-11999 20 12000-19999 26 20000-29999 34 30000+ 38 | Target's fleet power |
| Target's fleet power | Ships | | | | | | | | | | |
| 0-299 | 1 | | | | | | | | | | |
| 300-599 | 2 | | | | | | | | | | |
| 600-999 | 6 | | | | | | | | | | |
| 1000-1999 | 7 | | | | | | | | | | |
| 2000-3999 | 11 | | | | | | | | | | |
| 4000-7999 | 14 | | | | | | | | | | |
| 8000-11999 | 20 | | | | | | | | | | |
| 12000-19999 | 26 | | | | | | | | | | |
| 20000-29999 | 34 | | | | | | | | | | |
| 30000+ | 38 | | | | | | | | | | |
| **Crisis Beacon** | Provocation | Technology | Espionage chapter | 12 | 320 | −16 | −80 | 80 | - Unknown Endgame crisis , Gray Tempest or Great Khan<br>- Time 4 years cooldown | - The nearest crisis fleet attacks the target's closest system | |
| **Imperium: Weaken Imperial Authority** | Subterfuge | Technology | Espionage chapter | 7 | 60 | −7 | −15 | 35 | - Galactic Imperium member<br>- Galactic Emperor target | - Galactic Imperium loses −20 Imperial Authority | |
| **Imperium: Target Seditionists** | Subterfuge | Technology | Espionage chapter | 7 | 60 | −7 | None | 35 | - Galactic Emperor<br>- Galactic Imperium member target<br>- Target is a rival or undermining Imperial Authority | - Target empire cannot undermine Imperial Authority for 5 years | |
| **Imperium: Spark Rebellion** | Subterfuge | Technology | Espionage chapter | 11 | 250 | −14 | −50 | 70 | - Galactic Imperium member<br>- Galactic Emperor target<br>- Imperial authority 50 or less | - Declares war against the Galactic Emperor with the Restore Community casus belli<br>- Every member of the Galactic Imperium will be asked to join either side<br>- This operation will be terminated if imperial authority is 80 or higher when a phase concludes | |
| **Lure the Kaleidoscope** | Sabotage | Economy | Espionage chapter | 4 | 20 | −5 | None | 10 | - The Kaleidoscope situation<br>- Target's empire capital does not have a Planetary Shield Generator | The Kaleidoscope situation is moved to the targeted empire's capital | |
| **Procure DNA** | Subterfuge | Government | Espionage chapter | 5 | 45 | −6 | −5 | 30 | - Evolutionary Predators origin<br>- No Machine target<br>- No Same founder species | - Gain the DNA of the target's founder species phenotype<br>- Gain progress for the Adaptive Evolution situation | |
| **Smuggle Population** | Provocation | Government | Espionage chapter | 7 | 120 | −10 | −50 | 55 | - Target has 500+ pops without the Wilderness trait<br>- No Both empires are Fanatic Egalitarian | - Steal 100-800 pops from the target depending on their Empire Size<br>- Empires with the Bodysnatcher civic steal 200 more | |
| **Prepare Invasion** | Sabotage | Military | Espionage chapter | 5 | 180 | −12 | −80 | 100 | - Bodysnatcher civic<br>- No Machine target<br>- No Target has the Non-Disclosure Agreement tradition | - If the empires go to war within the next 10 years their closest starbases will be occupied and any worlds in those systems will be invaded by 5 Assault Armies each<br>- At least one system will always be targeted<br>- Can pay Pops to increase the number of systems targeted<br>Pops paid Systems targeted 0 5% 100 10% 300 15% 500 25% 2000 50% | Pops paid |
| Pops paid | Systems targeted | | | | | | | | | | |
| 0 | 5% | | | | | | | | | | |
| 100 | 10% | | | | | | | | | | |
| 300 | 15% | | | | | | | | | | |
| 500 | 25% | | | | | | | | | | |
| 2000 | 50% | | | | | | | | | | |
| **Consume Star** | Sabotage | Military | Espionage chapter | 11 | 250 | −9 | None | 60 | - Devourer's Egg Sac modifier<br>- No Target's capital star is a Black hole<br>- No Target's capital system has a Dyson Sphere<br>- No Operation already used on target | - Target gains a special project that if not completes in time, all colonies in the target's capital system will be destroyed | |

### Assets

Assets are characters gained from the Acquire Asset operation and can be assigned to improve the skill of any operation. Each asset grants +4 skill bonus per category that matches with the operation. Some operations allow for sacrificing an asset to obtain a greater reward. Each asset also increases the maximum infiltration the spy network can reach by +5 .

An asset that is assigned to a Gather Information operation gives a 50% chance that the intel gained matches the asset's intel category.

| Operation category | Intel category | Individualist asset | Hive Mind asset | Machine Intelligence asset |
|---|---|---|---|---|
| Subterfuge | Diplomacy | Clerk | Ephapse Relay | Engagement Protocol |
| Subterfuge | Economy | Economist | Labor Drone | Logistics System |
| Subterfuge | Government | Bureaucrat | Synapse Drone | Coordination System |
| Subterfuge | Military | Junior Officer | Warrior Drone | War Algorithm |
| Subterfuge | Technology | Scientist | Research Drone | Research Database |
| Manipulation | Diplomacy | Newscaster | Pheromone Emitter | No |
| Manipulation | Economy | Pop Icon | Resource Distribution Node | No |
| Manipulation | Government | Agitator | Behavioral Regulator | No |
| Manipulation | Military | Veteran | Subspace Tendril | No |
| Manipulation | Technology | Academic | Cortex Node | No |
| Sabotage | Diplomacy | Attache | No | Dispatch Uplink |
| Sabotage | Economy | Laborer | No | Resource Pylon |
| Sabotage | Government | Criminal Underling | No | Command Relay |
| Sabotage | Military | Arms Smuggler | No | Weapons Platform |
| Sabotage | Technology | Hacker | No | Memory Cache |

#### Internal Organs

Internal Organs are a unique asset that can only be obtained by vivisection during an aggressive first contact . Unlike other assets, it provides a bonus to two operation categories: Subterfuge and Manipulation.