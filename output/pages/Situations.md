---
title: "Situations"
categories: ["Potentially_outdated", "3.14", "Articles_with_potentially_outdated_sections", "Game_concepts", "Exploration", "Pages_with_math_errors", "Pages_with_math_render_errors"]
---

# Situations

Not to be confused with Events

Situations are events that take place gradually and are trackable via the Outliner and the Situation Log . Most situations offer multiple approaches to tackle them, and most of the time an approach can be changed at any point.

## Situation mechanics

Situations are narrative or mechanical events that develop gradually rather than occurring immediately upon triggering. All situations have a **progress bar** , which typically goes from 0 to 100; most situations start at 0, but some situations start at other points along the progress bar. The progress bar is split into one or more **stages** , which often represent the increasing effects of the situation and may also trigger events when first entered. In addition to events triggered by entering a stage, situations may also have random monthly events.

Most situations have a base amount of monthly progress as well as one or more **approaches** , which can affect the monthly progress or apply other effects. Occasionally, an event can lock a situation, preventing its progress from changing, usually to force the player to make a choice or prevent an undesired possible interaction of effects from the situation stage changing. Situations automatically end when the progress bar reaches max progress ("complete") or goes below 0 ("fail"); it is also possible for a situation to end due to an event, project, or other reason. The end of a situation can be good, bad, neutral, or even nothing – depending on the situation and which end is reached.

Situations may have a **target** – usually a planet or empire – and the situation, stages, or approaches can apply modifiers to this target. The situation, stages, or approaches can also apply modifiers to the empire experiencing the situation.

## Shortages

Shortages are situations that start if an empire's stored stockpile for a resource drops to 0 with negative income. Shortage situations progress as long as the empire has negative income and recede once a positive income is reached, or the stored stockpile is raised above zero some other way. Unlike most situations, the aim is to prevent the situation from making progress to avoid increasing empire penalties. All shortage situations have a Maintain Current Expenditures approach with no effects and one or two other approaches which attempt to alleviate the deficit by reducing expenses or increasing output of the resource.

If a shortage situation progresses completely, the empire defaults, refunding a large amount of resources based on how many decades have passed since game start and ending all current shortage situations. However, all upgraded buildings except capitals are downgraded to the lowest tier and all offensive armies and half of the empire's military ships are disbanded . In addition, the empire gains the Empire Defaulted modifier for 10 years, imparting the following effects:

- Cost +25% All costs
- −50% Monthly influence
- −50% Monthly unity
- −25% Ship weapons damage
- Time −50% Pop demotion time

All shortage situations start at **15** progress and advance based on the ratio of expense to output, scaling from **0** if expense matches output up to +5 if expense is double or more of output. The shortage progress is reduced by −5 while income is positive and by −1 while the empire has a stockpile but negative income. Each stage takes **25** points to advance to the next stage. Progress gain is reduced by 50% on Cadet difficulty and by 90% on Civilian difficulty. Upon first reaching the final stage – Catastrophic Deficit , an event is triggered which have between one to three options to pay some cost in return for an infusion of the shortage resource; there is also an option to do nothing. Payback empires may also receive an event for non-strategic resource deficits to gain 1000 of a basic resource or 500 of an advanced resource, or to refuse and gain 6x unity output ( 100~1000 ).

| Resource shortage Refund per decade passed | Effects | Minor Deficit | Major Deficit | Severe Deficit | Catas­trophic Deficit | Alternative approaches | Triggered event options |
|---|---|---|---|---|---|---|---|
| Energy 1000 (max 15000) | Research from Researchers | −0.5 | −1 | −1.5 | −2 | - Cut Science Investment<br>- −50% Researcher output<br>- −20% Building energy upkeep | - Largest faction with a governing ethic and does not have Loan Taken modifier:<br>  - Gain 50 energy per faction member pop<br>  - Faction gains Loan Taken modifier: −30% faction approval for 10 years<br>- Highest population colony besides capital, capital if no colonies:<br>  - Gain 100 energy per colony pop<br>  - Colony gains 50 devastation |
| Diplomatic weight from economy | −10% | −20% | −33% | −50% | | | |
| Mechanical pop assembly speed | −10% | −20% | −33% | −50% | | | |
| Combat disengagement chance | −10% | −25% | −50% | −75% | | | |
| Ship weapons damage | −20% | −40% | −60% | −80% | | | |
| Sublight speed | −20% | −40% | −60% | −80% | | | |
| Resources from jobs | — | — | — | −10% | | | |
| | | | | | | | |
| Minerals 1000 (max 15000) | Consumer goods from Artisans | −0.5 | −1 | −1.5 | −2 | - Cut Investments<br>- Only available if any of the below apply<br>- Uses consumer goods:<br>  - Artisans: −25% output, −50% upkeep<br>- No Catalytic Processing, Catalytic empire:<br>  - Metallurgists: −25% output, −50% upkeep<br>- Hive Mind:<br>  - Brain Drones: −25% output, −50% upkeep | - Has active Clone Vats and lithoid primary species:<br>  - Gain 100 minerals per Clone Vats building<br>  - Ruin all Clone Vats buildings<br>- Largest faction with a governing ethic and does not have Loan Taken modifier:<br>  - Gain 50 minerals per faction member pop<br>  - Faction gains Loan Taken modifier: −30% faction approval for 10 years<br>- Highest population colony besides capital, capital if no colonies:<br>  - Gain 100 minerals per colony pop<br>  - Colony gains 50 devastation |
| Lithoid pop happiness | −10% | −15% | −20% | −25% | | | |
| Lithoid pop growth speed | −20% | −33% | −50% | −75% | | | |
| - Lithoid primary species:<br>  - Organic pop assembly speed | −20% | −33% | −50% | −75% | | | |
| No<br>Catalytic Processing,<br>Catalytic<br>empire:<br>  - Alloys from Metallurgists | −0.5 | −1 | −1.5 | −2 | | | |
| Hive Mind:<br>  - Research from Brain Drones | −1 | −1.5 | −2.5 | −3 | | | |
| | | | | | | | |
| Food 1000 (max 15000) | Biological pop happiness | −10% | −15% | −20% | −25% | - Invest in Farmers<br>- Farmers: +50% output, +0.5 upkeep | - Has active Clone Vats and biological primary species:<br>  - Gain 100 food per Clone Vats building<br>  - Ruin all Clone Vats buildings<br>- Has active Bio-Reactors:<br>  - Gain 100 food per Bio-Reactor building<br>  - Ruin all Bio-Reactor buildings<br>- Colony with most farming districts:<br>  - Gain 500 food per farming district<br>  - Colony gains 50 devastation |
| Biological pop growth speed | −20% | −33% | −50% | −75% | | | |
| - Biological primary species:<br>  - Organic pop assembly speed | −20% | −33% | −50% | −75% | | | |
| Catalytic Processing,<br>Catalytic<br>empire:<br>  - Alloys from Metallurgists | −0.5 | −1 | −1.5 | −2 | | | |
| | | | | | | | |
| Consumer goods 500 (max 7500) | Happiness | −5% | −10% | −15% | −20% | - Cut Investments<br>- −50% pop and job consumer goods upkeep<br>- −50% Monthly unity<br>- Individualist:<br>  - −50% Researcher output | - Largest faction with a governing ethic and does not have Loan Taken modifier:<br>  - Gain 25 consumer goods per faction member pop<br>  - Faction gains Loan Taken modifier: −30% faction approval for 10 years<br>- Gain Consumer Goods Rationing empire modifier for 10 years<br>  - −25% pop and job consumer goods upkeep<br>  - −10% Happiness and −30% governing ethics attraction |
| Monthly unity | −15% | −30% | −45% | −60% | | | |
| - Individualist:<br>  - Research from Researchers | −1 | −1.5 | −2.5 | −3 | | | |
| - Individualist:<br>  - Governing ethics attraction | −25% | −50% | −75% | −100% | | | |
| | | | | | | | |
| Alloys 250 (max 3750) | Robot output | −10% | −20% | −30% | −50% | - Cut Habitats' Maintenance<br>- Only available if owns any Habitat<br>- Upkeep −100% Habitat alloy upkeep<br>- Invest in our Metallurgists<br>- Metallurgists: +50% output and upkeep | - Machine Intelligence scrap half of all robots on highest population colony:<br>  - Gain 100 alloys for each scrapped robot pop<br>- Scrap all enslaved or non-sentient robots on colony with most non-sentient robots:<br>  - Gain 100 alloys for each scrapped robot pop |
| Mechanical pop assembly speed | −25% | −50% | −75% | −100% | | | |
| Cost Pop assembly cost | +25% | +50% | +75% | +100% | | | |
| Ship energy upkeep | +10% | +20% | +20% | +30% | | | |
| Starbase energy upkeep | +10% | +20% | +20% | +30% | | | |
| Stability on habitats | −10% | −15% | −20% | −30% | | | |
| Armor hit points | — | −33% | −66% | −99% | | | |
| Ship fire rate | — | −33% | −66% | −99% | | | |

Strategic resource shortages are all similar, with their approaches and events having the same options differing only in the resource. Their deficit effects are similar as well, affecting Resources from jobs as well as two other modifiers related to that resource.

| Resource shortage Refund per decade passed | Effects | Minor Deficit | Major Deficit | Severe Deficit | Catas­trophic Deficit | Alternative approaches | Triggered event options |
|---|---|---|---|---|---|---|---|
| Exotic gases 100 (max 1500) | Resources from jobs | −5% | −10% | −15% | −20% | **Note: "[Resource]" is the resource in shortage**<br>- Recycle Materials<br>- Upkeep −25% Building and district [resource] upkeep<br>- +50% Building refund<br>- +50% Building and district cost<br>- Invest in [Resource] Production<br>- +25% [resource] refiners output and upkeep<br>- +25% [resource] miners output | - Highest population colony besides capital, capital if no colonies:<br>  - Gain 10 [resource] per colony pop<br>  - Colony gains 25 devastation and two Exhausted Deposit blockers<br>- Any exploited [resource] space deposit:<br>  - Remove deposit and gain 250 [resource] per size of deposit |
| Sublight speed | −20% | −40% | −60% | −80% | | | |
| Terraforming speed | −20% | −40% | −60% | −80% | | | |
| | | | | | | | |
| Rare crystals 100 (max 1500) | Resources from jobs | −5% | −10% | −15% | −20% | | |
| Energy weapons damage | −30% | −50% | −70% | −90% | | | |
| Sensor range | −1 | −1 | −2 | −3 | | | |
| | | | | | | | |
| Volatile motes 100 (max 1500) | Resources from jobs | −5% | −10% | −15% | −20% | | |
| Kinetic weapons damage | −30% | −50% | −70% | −90% | | | |
| Clear blocker cost | +20% | +40% | +60% | +80% | | | |
| Clear blocker speed | −20% | −40% | −60% | −80% | | | |

## Leviathan parade opportunities

Leviathan Parade Opportunities are situations that take place when a guardian has been defeated. The parade occurs on the planet with the highest population in the empire that has not hosted a parade in the last 40 years. If no such planet is available, the planet with the largest population is chosen. Reaching the second stage of a situation brings multiple choices with various effects. When the situation completes, the parade planet gains a permanent modifier and the empire gains either a small ( 150 ~ 100000 ), standard ( 250 ~ 1000000 ), or large ( 350 ~ 1000000 ) amount of unity. Memorialists start with the large reward, all other empires start with the standard reward.

All Leviathan parade opportunity situations have three stages and offer three approaches:

- Encourage it – +6 monthly progress
- Discourage it – −4 monthly progress
- Reorganize – 0 monthly progress; costs 1000 Unity to activate and unlocks the Relocate the Parade planetary decision

Reorganize can only be selected if current progress is below **50** and monthly progress is positive. Once this approach is selected, the other approaches cannot be selected until the Parade has been moved to a new planet.

| Guardian | Stage II choices | Modifier reward |
|---|---|---|
| Automated Dreadnought | 1. −40 Situation progress and −50% job energy upkeep for 2 years<br>2. Equal chance of either −30 situation progress or +20 situation progress and increased unity reward<br>3. 350~100000 Engineering research | Dreadnought's Reactor planet modifier: −15% Building, district and job energy upkeep |
| Enigmatic Fortress | 1. Reduce unity reward<br>2. −1 Pop<br>3. −20 Situation progress, −1 pop, and increase unity reward | Chamber from the Fortress<br>planet modifier:<br>- +1500 Amenities<br>- +1500 Housing |
| Ether Drake | 1. −30 Situation progress<br>2. End the situation for +20% Society research for 20 years<br>3. Reduce unity reward | Drake's Fang<br>planet modifier:<br>- +10 Stability<br>- +25% Immigration pull |
| Spectral Wraith | 1. End the situation for the Wraith Infused Atmosphere planet modifier ( −25% Orbital bombardment damage)<br>2. No effect<br>3. −40 Situation progress and increase unity reward | Wraith's Dispenser Sack<br>planet modifier:<br>- +10% Happiness<br>- +15% Unity from jobs |
| Stellarite Devourer | 1. End the situation for the special project to reignite the star<br>2. +15 Situation progress | Feature Enables the Consume Star operation |
| Scavenger Bot | 1. −20 Situation progress and +5000 alloys<br>2. +20 Situation progress and increase unity reward<br>3. End the situation for an asteroid with a deposit of 10 alloys above the empire capital | Scavenger Bot's Compactor planet modifier: +20% Alloys from jobs |
| Tiyanki Matriarch | 1. −20 Situation progress, +500 food, and increase unity reward<br>2. +1 Pop<br>3. Reduce unity reward and on completion gain alternate trophy modifier: +10% Unity from jobs<br>  - Not available for Xenophile empires | Matriarch's Flagella<br>planet modifier:<br>- +1 Monthly organic pop assembly<br>- −5 Stability |
| Voidspawn | 1. Start Water Contamination situation and add Voidspawn Contaminant modifier: −15% habitability, Upkeep +10% pop upkeep<br>2. End the situation | Cleansed Venom Gland<br>planet modifier<br>:<br>- +15% Habitability<br>- +10% Society research from jobs |
| Shard | 1. End the situation for the All Seeing Shard planet modifier ( +10 sensor range, +10 hyperlane detection range)<br>2. Reduce unity reward<br>3. −30 Situation progress and 350~100000 Society research | Eye of the Shard<br>planet modifier:<br>- +5% Worker output<br>- +5% Menial drone output<br>- +50% Authoritarian ethics attraction |
| Sky Dragon | Option Requirements 1. **Kill the whelps:** Hostile fleet of 3 Sky Dragon Fledglings Increase unity reward if either: Xenophobe, Barbaric Despoilers, Gestalt Consciousness Decrease unity reward otherwise No Values others 2. **Find them a home:** End situation and create an asteroid with a deposit of +1 Living Metal in the parade system and friendly fleet of 3 Sky Dragon Fledglings No Xenophobe No Barbaric Despoilers No Genocidal 3. **Trap them:** Increase unity reward No Values others No Xenophobe No Egalitarian 4. **Drive them off:** −10 Situation progress No Genocidal | Option |
| Option | Requirements | |
| - 1. **Kill the whelps:**<br>  - Hostile fleet of 3 Sky Dragon Fledglings<br>  - Increase unity reward if either:<br>    - Xenophobe, Barbaric Despoilers, Gestalt Consciousness<br>  - Decrease unity reward otherwise | No Values others | |
| - 2. **Find them a home:**<br>  - End situation and create an asteroid with a deposit of +1 Living Metal in the parade system and friendly fleet of 3 Sky Dragon Fledglings | - No Xenophobe<br>- No Barbaric Despoilers<br>- No Genocidal | |
| - 3. **Trap them:**<br>  - Increase unity reward | - No Values others<br>- No Xenophobe<br>- No Egalitarian | |
| - 4. **Drive them off:**<br>  - −10 Situation progress | No Genocidal | |

### Horrific Inverse Mass

The Worm, Dimensional Horror, and Elder One all share this situation. Killing one begins this situation, and killing another does not award another situation. The second stage choices are:

1. End the situation for 250~1000000 unity: No not available for Materialist
2. Increase unity reward, with different versions for Spiritualist (deify) and non-Spiritualist (study)
3. Contain the mass

Upon completion of the situation, if the mass was deified, the parade planet gains +15% unity from jobs, otherwise it gains +15% research from jobs. Seven years after completion (14 if the mass was contained), another event fires with two choices:

1. Increase the modifier's bonus to +25% , but also add −20 stability
2. Remove the modifier

If the modifier is kept, about 3.5 years later, a third event fires with two options:

1. Gain 10 devastation and replace the previous modifier with the TOO LATE modifier, which gives +100% research and +100% unity from jobs, −20 stability, −200 immigration pull, and −1000% governing ethics attraction.
2. Gain 99 devastation and remove the previous modifier: No not available for Fanatic Materialists

If the first option is chosen, the event sets a random outcome and triggers a final event two years later. The final event either destroys the parade planet (66% chance), turning it into a black hole, or replaces the TOO LATE modifier with the Horrific Inverse Mass Stabilized planet modifier (33% chance), giving +50% research and +50% unity from jobs. Because the outcome is decided prior to the previous event, reloading a save at this point cannot alter the result, only changing the flags does. This can be done either with save editing or by running the following commands with the planet selected:

- effect remove_planet_flag = black_hole_horror
- effect set_planet_flag = stabilized_horror

## Event situations

Event situations have a small chance to trigger at regular intervals and can only happen once. Various events can take place during an event situation. Event situations on a colony cannot occur on a homeworld or capital, or if the colony is occupied, has ground combat, or is not owned by its original colonizer, except as specifically noted on a situation.

### Gravity Well

This situation can occur on any Star Fortress or Citadel with a Black Hole Observatory. The situation starts at **25** progress and increases by +5 monthly; it ends by reaching either **100** or **0** progress. The starting event prompts the player to choose the initial approach, either Retreat , Maintain Orbit , or Advance . This approach can be changed at any time unless there is an ongoing mutiny on the starbase. Retreat costs 10 energy and reduces progress by −10 monthly. Maintain Orbit costs 5 energy and reduces progress by −3 monthly. Advance increases progress by 3 monthly.

| Stage | | | Progress |
|---|---|---|---|
| Static Limit | 0 +1 | 0 +5 | — |
| Ergosphere | 0 +2 | +10 | +2 |
| Accretion Disk | 0 +5 | +15 | +3 |
| Point of No Return | +10 | +20 | +7 |

There are four stages to the Gravity Well situation, representing the approximate distance from the black hole's event horizon. Each stage provides increasing amounts of dark matter and physics research, but also increases the rate of progress, making it more likely for the starbase to be irretrievably caught by the black hole. The first stage, Static Limit , lasts until 50 progress; the second, Ergosphere , until 70 progress; the third, Accretion Disk , until 80 progress. When first entering the fourth and final stage, Point of No Return , the player receives a notification event as well.

There are five random events that can occur during this situation:

1. Mutiny (advance): Locks approach to Advance for about one month; cannot occur for Gestalt Consciousness empires, weight doubled with Technocracy civic
2. Mutiny (retreat): Locks approach to Retreat for about one month; cannot occur for Gestalt Consciousness empires
3. Adds +10 progress; cannot occur in fourth stage
4. 18x physics output ( 350~100 000 )
5. Option to destroy all starbase buildings to reduce progress by −30 (70% chance) or −10 (30% chance); weight ×6 in third stage and ×4 in fourth stage

If the situation reaches 100, the starbase is destroyed and Individualist empires lose −100 influence; Gestalt Consciousness empires can choose that option, or to observe the end and gain 24x physics output ( 500~1 000 000 ) and a permanent empire modifier, with a equal chance of either Transcended Consciousness ( +5% monthly unity) or Disjointed Consciousness ( −5% monthly unity). Empires with Divided Attention, Subspace Ephapse, or Delegated Functions have an increased chance for Transcended Consciousness , while empires with One Mind or Unitary Cohesion have an increased chance for Disjointed Consciousness .

If the situation goes below 0, the starbase returns to a stable orbit, and empire has an equal chance to receive either 48x physics output ( 1000~1 000 000 ) or a level 6 scientist of the primary species with Maniacal and Expertise: Field Manipulation.

### The Mysterious Labyrinth

This situation can occur on a colony four or five years after it is founded; it cannot occur on Tomb Worlds, Habitats, or Ring Worlds. When the situation starts, the player is prompted to choose either to explore its interior or to monitor it from afar. The situation starts at **50** progress and increases or decreases depending on the approach taken. There are three approaches for this situation, they can be changed at any time.

: 1. Explore its Interior : initially costs 5 energy and adds +2.5 progress monthly
: 2a. Monitor it from Afar : adds −2.5 progress monthly, is later replaced by: 2b. Quarantine it : initially costs 10 energy and adds −2.5 progress monthly
: 3. Destroy it : initially costs 10 energy and adds −5 progress monthly

Unlike other situations, instead of one series of stages, this situation has two series, one to the left and one to the right, representing progress towards the different approaches that can be taken. The left stages represent ignoring or destroying the labyrinth and the right stages represent exploring it. The first time the progress bar reaches a stage, an event is triggered. Re-entering a stage does not trigger a second event and there are no random monthly events.

| Stage | Outcome (left) | III (left) | II (left) | I | II (right) | III (right) | Outcome (right) | Stage |
|---|---|---|---|---|---|---|---|---|
| Progress bar limit | — | 0-20 | 20-40 | 40-60 | 60-80 | 80-100 | — | Progress bar limit |
| Destroy it | Labyrinth Destroyed | | Surprising Movements | — | Expedition Report | Continued Perplexity | A Departure A Turbulent Departure | Explore its Interior |
| Monitor it from Afar /Quarantine it | A Reward for Obstinance Labyrinth Disappeared | Attention Seeking | | | | | | |

**Left stage events**

1. Surprising Movements : Replaces Monitor it from Afar with Quarantine it and prompts the player to choose an approach
2. Labyrinth Destroyed : the labyrinth is destroyed; the situation ends and the empire gains +200 dark matter and +800 each of exotic gases, rare crystals, and volatile motes
3. Attention Seeking : increases the monthly cost of both Quarantine it and Destroy it by 10 unity
4. A Reward for Obstinance : adds the Space-Time Anomaly feature to the colony
5. Labyrinth Disappeared : gain 18x unity output ( 250~1 000 000 ) – only possible if the situation ends after 21 months have passed, then equal chance of Labyrinth Disappeared and A Reward for Obstinance

**Right stage events**

1. Expedition Report : Flavor only event
2. Continued Perplexity : increases the monthly cost of Explore its Interior by 10 unity
3. A Departure : adds the Space-Time Anomaly feature to the colony
4. A Turbulent Departure : adds the Space-Time Anomaly feature as well as one City Ruins, one Deep Sinkhole, and two Active Volcano blockers – only possible if the situation ends before 21 months have passed, then an equal chance of A Turbulent Departure and A Departure

### Unusual Snow

This situation can occur on a desert colony four or five years after it is founded, and it progresses steadily at +5 monthly progress. Stage I lasts until 25 progress points, and then the player is prompted to choose either to Observe or Melt the snow. Observing the snow costs −10 unity monthly and gives +5 research, while melting the snow costs −10 energy monthly and gives the colony +10 stability.

Up to two of three random events can happen during stage II:

1. Gain 24x society output ( 500~1 000 000 )
2. Increase the monthly cost of observing by −5 unity
3. Either increase the monthly cost of melting by −5 energy and add +5 more monthly progess while melting, or reduce the stability gained by melting to +5 .

The second and third event are mutually exclusive. Stage II lasts until 80 progress points, at which the point the player is given one last chance to change approaches after which it is no longer possible to change the approach.

When the situation completes, if the player was observing the snow, they can choose to add the Living Snow Reserve feature, which gives +20% physics and +20% society from jobs and −2 max districts, or to fight an invasion of 6 Living Snow Warrior armies. If the player was melting the snow, they must fight the invasion of 6 Living Snow Warrior armies. If the invaders win and the colony is not recaptured within 5~6 years, it becomes a Frozen World with a deposit of +8 physics and +8 society research and adds 10% research progress to the Terrestrial Sculpting technology.

### Geomagnetic Storm

This situation can occur on any colony owned by a Machine Intelligence 25 years after it is founded if half or more of the pops on the colony are machine drones. Before the situation starts, the player must choose to shield all drones, simple drones, complex drones, or no drones at a cost of 1 energy per shielded drone. This choice also determines the initial approach and starting progress ( **0** - 5 ) for the situation. This situation progresses steadily at +5 monthly progess, however shielding all or some drones reduces the progress by up to −5 , scaled by the percentage of drones shielded. The situation ends either by reaching 100 progress or after 60 months . It is possible to reduce progress slightly through a random event, but generally, the progress of this situation only increases or remains the same.

Shortly after the situation begins, Rogue Servitors receive the option to gain a Organic-Machine Interface Center feature, which adds +1 Bio-Assistant job and +1 more per 20 pops. After the situation ends, the Organic-Machine Interface Center feature is removed and the player can choose to gain 1000 alloys or add the Organic-Machine Interface Museum planet modifier, which gives +5% unity from Bio-Trophy jobs.

| Stage | | | | |
|---|---|---|---|---|
| Radiation damage: minimal | −20% | −20% | — | — |
| Radiation damage: medium | −25% | −25% | −30 | — |
| Radiation damage: high | −30% | −30% | −60 | −10% |

The Geomagnetic Storm has three stages, representing increasing amounts of radiation damage: the first lasts until 40 progress and the second until 70 progress. Both Menial and Complex Drones have their output reduced, and at the later stages, the planet's stability is significantly reduced and even the whole empire's monthly unity is impacted. The effects of each stage are shown in the table to the right.

There are four approaches for this situation: Shield All Drones , Shield Simple Drones , Shield Complex Drones , or No Shielding ; each approach has an upkeep of 1 energy per shielded drone. Additionally, drones that are shielded receive +20% output, offsetting the penalty from the stages. As noted above, the percentage of shielded drones reduces the monthly progress, up to −5 when all drones are shielded.

There are four random events that can occur during this situation.

1. If there are any unshielded drones, the player can kill a random robotic pop, add +5 progress, or subtract −5 progress.
2. If there is a Machine Assembly Plants or Machine Assembly Complex, the player can spend 300 energy or gain −10% mechanical pop assembly speed for 90 days.
3. Lose 200 food, energy, minerals, or alloys; if the planet has any Bio-Assistants, there is a 75% chance to instead gain 200 food, energy or minerals, or 500 alloys.
4. A random robotic pop disappears, then reappears 15-105 days later, when the player can choose to scrap them for 500 alloys or reboot them, creating a new primary species pop, with a 30% chance of adding Enhanced Memory to the pop, otherwise adding High Bandwidth to the pop.

If the situation reaches 100 progress, all robotic pops on the colony are killed; if instead 60 months pass first, the end result depends on the current stage:

- **Radiation damage: minimal** : 18x engineering output ( 350~100 000 ) and the permanent empire modifier Radiation-Hardened Components , which gives +5% research speed and +5% monthly unity
- Radiation damage: medium : 24x engineering output ( 500~1 000 000 )
- Radiation damage: high : Gain the empire modifier Software Damage for five years, which gives −5% research speed and −5% monthly unity

### The Kaleidoscope

This situation has a 30% chance of happening. The flag is set at galaxy generation. Anytime after the mid-game start, a random empire whose capital does not have a Planetary Shield Generator receives planet modifier on the capital Global Power Outage : −2000% resources from jobs, and a special project requiring a construction ship. Other empires that have at least low intel on the affected planet receive a notice of the Kaleidoscope. Finishing the special project removes the Global Power Outage modifier and starts the situation and sets the initial approach.

The situation starts at **0** progress and ends when it reaches **100** , or 25 years after the Kaleidoscope first appeared, when it dies. The Kaleidoscope also has a "mood" from 0 to 21; while the mood is 5 or less, it is "angry", and while it is 15 or more, it is "happy"; in-between is "neutral". The Kaleidoscope's visual appearance changes based on its mood. It starts at 10 mood. There are three approaches which can be changed at any time:

| Approach | Effect/modifier | Monthly | |
|---|---|---|---|
| Progress | Mood | | |
| 1. Do not feed it | When selected, immediately reduces mood to a max of 12 | **+0** | −2 |
| 2. Feed it | −30% energy output, including energy from trade value | +0.5 | +1 |
| 3. Overfeed it | −60% energy output, including energy from trade value | +1.5 | +2 |

While the situation is active, there are a number of random events that can occur, at most one per year. The likelihood of negative vs. positive events is affected by the current mood value, with lower mood shifting more towards negative and higher mood more towards positive.

**Negative events**

1. Minor Infestation – Approach is Do not feed it and any owned planet has a Generator District; planet gains Phantom Load modifier: −2000% energy from jobs, and a special project to remove the modifier.
2. Electroshock – Approach is not Overfeed it and any owned planet has an Energy Grid or Energy Nexus; choice of: add +5 progress and ruin the Energy Grid or Energy Nexus, or gain 1000 energy.
3. Unnerving Patterns – Approach is Do not feed it and empire is not Machine Intelligence; adds Unnerving Patterns modifier to situation: −5 stability.
4. Ominous Patterns – Approach is Do not feed it and empire is Spiritualist; choice of: spend 2000 energy, or adds Ominous Patterns modifier to situation: −10% happiness.
5. Pilfering Patterns – Approach is Do not feed it ; adds Haunting Patterns modifier to situation: −10% ship speed.

**Positive events**

1. Soothing Patterns – Approach is not Do not feed it ; gain 18x unity output ( 250~1 000 000 ) and adds Soothing Patterns modifier to situation: +5 stability, for 2 years.
2. Dazzling Patterns – Approach is not Do not feed it ; gain 24x physics output ( 500~1 000 000 ) and adds Dazzling Patterns modifier to situation: +10 immigration pull, for 2 years.
3. Endless Hunger – Approach is not Do not feed it and empire is not Xenophobe and owns a complete Dyson Sphere ; can choose to upgrade a completed Dyson Sphere into a Wonder Sphere , doing so while the situation is active ends the situation.

The empire with this situation can use the operation Lure the Kaleidoscope on an empire whose capital does not have a Planetary Shield Generator and which did not use this operation previously. A successful operation transfers the situation to the targeted empire, including the current progress and mood. Additionally, if the empire with this situation is entirely destroyed by another, the destroying empire inherits this situation if their capital does not have a Planetary Shield Generator, otherwise the situation ends with no effect.

If the situation reaches **100** progress, there are two possible outcomes:

1. Blooming Kaleidoscope – base chance 10%: gain the Vacuum Flower relic.
2. Exploding Kaleidoscope – base chance 90%: all colonies in the capital system gain 50 devastation.

The chance of each is heavily influenced by the Kaleidoscope's mood; each point of mood shifts the chance by 4%. For example, at 10 mood, each outcome has a 50% chance of occurring.

## Triggered situations

Unlike event situations, triggered situations are directly related to another event, decision, or similar circumstance. They may be repeatable if their triggering circumstance is repeatable.

### Plight of the Beta-Universe

This situation is a possible outcome of the The Doorway colony event. This situation cannot occur if the empire's homeworld is artificial , an Ecumenopolis, Hive, Machine, or Relic world, or owned by a different empire. After completing the special project, a series of events occurs over a few years, culminating in an attack by a parallel universe version of the empire. After the invading fleet is defeated, the parallel version of the empire asks for help as their universe is collapsing. The player is prompted to choose between studying, plundering, or aiding the "beta" empire; this choice sets the initial approach. Choosing to aid the beta empire at this point locks the player into that approach.

The situation starts at **75** progress and ends when the situation reaches 100 , at which point the beta empire is destroyed, or when it goes below 0 , at which point the beta empire homeworld is pulled into the player's home system as an owned colony. The situation also ends if the player loses ownership of their homeworld.

The situation progresses at a base of +3 . Each year since the situation started adds +1 monthly progress; after 5 years, it adds +10 monthly progress instead. Aiding the beta empire subtracts −7 monthly progress.

There are three approaches for this situation:

1. Bring <Homeworld>-Beta to our universe : Costs 45 energy and adds −10% research output for the empire.
2. Observe the decay of the Beta-Universe : Adds +40% physics output for the empire.
3. Plunder <Homeworld>-Beta : Adds +35 alloys, +50 minerals, and +25 energy monthly; also adds +30 food monthly if the empire uses food.

There are four stages and the situation starts in the third stage. The first time entering any other stage triggers an event. Other than One Last Plea , the approach must be Bring <Homeworld>-Beta to our universe to trigger the event.

| Stage | Progress | Event | Gestalt event |
|---|---|---|---|
| I | 0 0-30 | Mission: Dimensional | Desperate Drones |
| II | 31-74 | Crossing the Dimensional Border | Offloading Optimization |
| III | 75-95 | — | |
| IV | 96-100 | One Last Plea | |

**Events**

- One Last Plea – the player can choose to redouble their efforts to save the beta empire, which subtracts −3 more monthly from the situation progress. If the current approach was not Bring <Homeworld>-Beta to our universe , choosing to redouble efforts sets and locks that approach as the only option. Redoubling efforts also increases the effect of Bring <Homeworld>-Beta to our universe to −30% research output for the empire.
- Crossing the Dimensional Border – gain +15 stability on the homeworld for 5 years and +20 situation progress, gain +5 situation progress, or gain −10 stability and −50% governing ethics attraction on the homeworld for 5 years, not available to Egalitarians.
- Offloading Optimization – gain +20% menial drone resource output and +20 situation progress or gain −5 situation progress.
- Mission: Dimensional – pay 150 unity, not available with Barbaric Despoilers or Nihilistic Acquisition, or gain +20 situation progress and +10% unity from jobs on the homeworld and repeat this event in four months; the second time, pay 150 unity, or gain +45 situation progress and increase the unity from jobs to +30% , and repeat this event in four months; every following time, not paying adds +20 situation progress.
- Desperate Drones – the beta empire attacks with a basic army, three if the offloaded optimization was taken earlier; kill one pop and gain four armies and +20 situation progress, or do nothing and gain +15 situation progress; after defeating the attacking armies, threaten the beta empire or, if the player chose to do nothing, gain −15 situation progress. If the attacking armies occupy the homeworld, remove the offloaded optimization modifier, set the situation approach to Bring <Homeworld>-Beta to our universe , and add +15 situation progress.

If the beta empire's planet is saved, it generally matches the player empire's homeworld at the start of the game, with Ocean Paradise, Life-Seeded, and Post-Apocalyptic each getting their special planet; other origins receive a size 18 planet that matches their original planet type. The beta homeworld has 18 pops of the empire's primary species with the trait Not of this World.

### Infested Star

This situation is started by the Consume Star operation nine months after its conclusion. Three months after the operation concludes all capital system colonies gain the Low Solar Output modifier, which gives −5% energy from jobs and −5% habitability; six months after that, the Low Solar Output modifier increases to −10% and −5 stability and the situation begins.

This situation starts at **0** and progresses at +3 monthly. Initially, there is only one approach, Search for a Cure , which reduces monthly progress by −1 . The first stage lasts until **20** progress, at which point the Low Solar Output modifier increases to −20% energy from jobs, −20% habitability, and −10 stability. The second stage lasts until **50** progress, then a special project to find the cure is created on the capital star. If the empire has more than 40% higher decryption than the infesting empire at this point, they learn the other's identity. The special project requires a scientist on a science ship and takes 15 months to complete, which means that the situation will progress at least to **80** before a cure can be found.

When the special project is completed, a second approach – Cure the Star – becomes available, which reduces monthly progress by −10 , quickly reversing the situation's progress. AI empires who have less than 25% of their empire's pops on the capital world do not use this approach and instead let the star be consumed. Reaching **0** progress removes all versions of the Low Solar Output modifier and ends the situation. Reaching 100 progress turns the capital system's primary star into a Brown Dwarf, destroys all colonies in the system, and turns all system planets into Frozen Worlds. If the empire had discovered the identity of the infesting empire, it gains the Ate Our Star total war casus belli against that empire for 20 years.

### Water Contamination

This situation is started by the Voidspawn Parade Opportunity situation. The situation begins at **0** progress and has two approaches:

1. Clean it : reduces Worker and Menial Drone output by −5% and adds +6 progress monthly
2. Study it : reduces Specialist and Complex Drone output by −5% and adds +15 society research and +4 progress monthly

Completing the situation removes the Voidspawn Contaminant modifier and, if the Voidspawn Parade Opportunity situation is still on-going, increases the unity reward.

### A Rift in Space

This situation is triggered the first time an empire without the **Rift Sphere** technology has an astral rift in its space. If the empire has the Riftworld origin, the situation is named Reaching into the Rift instead. The situation has two stages that each take **50** progress to complete. When the situation completes, the empire gains 100 astral threads and 25% progress on the Rift Sphere technology. If the empire gains the Rift Sphere technology some other way, the situation ends with no effect. If the empire owns no astral rifts, the situation is locked with no progress until another astral rift is gained.

There are three approaches for this situation:

1. Study Passively – +0.5 progress monthly
2. Devote Research – +1.2 progress monthly; +10% unity output and physics output is reduced: −25% in stage I, −50% in stage II.
3. Send Probes – +1.2 progress monthly; +25% unity and +10% physics output, and alloys output is reduced: −25% in stage I, −50% in stage II.

Using either Devote Research or Send Probes for at least two months in a row sets a flag which triggers the event Unstable Spacetime once stage 2 starts. There are three versions which are equally likely. Initially, there is a 16% chance of the event not firing immediately but being checked again after one year, and once the situation reaches **80** progress, some version of the event will occur when the next check happens. The three versions are:

1. A new planet is created in the astral rift system with a pre-FTL empire.
2. A new random species is created on the nearest colony.
3. The nearest colony gains the modifier Temporal Distortions for one year: +100% resources from jobs, pop growth speed, pop assembly speed, and building build speed.

### The Crystal Sphere

The Crystal Sphere can appear after the mid-game year if any empire has completed five or more astral rifts . An event checks once each year for eligible empires and the eligible empire that has completed the most astral rifts gains the Crystal Sphere in the eligible system nearest to its capital, including the capital system. That empire can choose to either study or destroy the Crystal Sphere, starting the situation of that type. Once the Crystal Sphere is spawned, any other empire can start either situation by gaining ownership of that system. When ownership of the Crystal Sphere changes, all progress in the situation is reset.

Empire eligibility is determined as follows:

1. Has researched **Rift Sphere**
2. Has completed 5 or more astral rifts
3. Owns an eligible system
4. A formula which compares the number of completed astral rifts, the game year, and a random ranking

All empires are given a random rank from 0-100, with AI empires having their rank doubled and Riftworld origin empires having theirs halved. The random ranking is rerolled each year.

System eligibility is determined as follows:

1. Does not have a wormhole
2. Does not have a shroud tunnel
3. Is not the Sol system

Both versions of the situation have a single stage which takes **100** progress to complete. Neither can progress if the empire does not have the Rift Sphere technology.

**Destroy the Crystal Sphere**

This version of the situation has two approaches:

1. Mechanical Approach – +0.8 progress monthly
2. Astral Approach – +1.2 progress and −10 astral threads monthly, and +20% research output; requires 10 astral threads stored to activate

Completing the situation gives 100 astral threads, 500 exotic gases, 500 rare crystals, and the empire modifier Peace in This Dimension for 10 years: +10% happiness. Xenophobe and genocidal empires also gain 24x unity output ( 350~1 000 000 ).

**Study the Crystal Sphere**

This version of the situation has three approaches:

1. Observe and Report – +0.8 progress monthly
2. Mundane Method – +1.2 progress monthly and −10% physics and engineering output
3. Astral Method – +1.2 progress and −10 astral threads monthly, and +20% research output; requires 10 astral threads stored to activate

Completing the situation spawns the Crystal Rift .

#### The Seal

This situation starts by completing the Crystal Rift, exploring the system azilash , and defeating the 8 Aberrant fleets there. The situation has a single stage which takes **100** progress to complete. Each year while the situation is active, another Aberrant fleet is spawned. Until each fleet is destroyed, no progress can be gained unless current progress is already **95** or more. Each time all Aberrant fleets are destroyed, the situation gains +5 progress.

There are three approaches for this situation:

1. Do Nothing – +0.8 progress monthly
2. Weave Astral Fabric – +1.4 progress and −10 astral threads monthly, and all fleets and stations in the azilash system gain Shield +50% shield; requires 10 astral threads stored to activate
3. Pump Exotic Gases – +1.2 progress and −50 exotic gases monthly, and all fleets and stations in the azilash system gain +10% energy weapon damage; requires 50 exotic gases stored to activate.

The situation ends if the Formless become hostile to the empire or if the Formless dimensional anchor is destroyed. If the dimensional anchor is destroyed, this also grants the empire with the situation 18x physics output ( 250~5000 ) and destroys the azilash system. To prevent the destruction of the anchor, you can supply the Formless with 100 Astral Threads, making them spawn a defense fleet composed of 10 extradimensional cruisers.

When the situation is completed: the azilash system gains a size 40 Gaia World with the Terraforming Candidate, Formless Haven modifier and brings the following 3 options.

- Gain the zadigal legendary paragon and every 10 years the empire can choose an additional reward: a fleet of 16 extradimensional cruisers, 100 Astral Threads or a random Physics technology (or a very large amount of Physics if all technologies are already researched). If the Unbidden, Aberrant or Vehement are present in the galaxy the Formless can be asked for a +10% damage boost in exchange for 2000 Astral Threads. The cost must be paid separately for each extradimensional invaders faction.
- Demand subjugation. The chance of success is 75% and increases with every astral rift explored. If the Formless accept, they colonize the Gaia World and become a Luminarium subject and the empire gains the Eternal Throne relic. The Formless start with −100 Loyalty but have high growth for it. If a starbase was already constructed in azilash, the Formless gain control of it. If they refuse subjugation, they become hostile.
- Become hostile towards the Formless. They gain 2 fleets of 32 cruisers each. If the Formless are defeated, the empire gains the Eternal Throne relic and 1000 Astral Threads. This is the only option for Genocidal empires.

### Extract Nanites from Planet

| Available districts | Progress | Months to complete |
|---|---|---|
| 10 | +16.66 | 60 |
| 15 | +11.11 | 90 |
| 20 | +8.33 | 120 |
| 25 | +6.66 | 150 |

This situation is started by the Subsume World decision , available to empires that have adopted the Unbridled Consumption Nanotech tradition. It starts at **0** progress and completes at **1000** progress. It progresses according to the number of available districts on the planet, namely planet size minus the number of Nanite Harvest Basin blockers present when the decision is taken. The more available districts, the slower it progresses so that the situation lasts 6 months per available district.

The situation can be stopped at any point by choosing the approach Restraint at a cost of 1000 unity.

Each year, the world is partially subsumed. This adds two Nanite Harvest Basin blockers and 10 devastation. It also randomly gives 2x or 3x nanites output ( 100 ~ 2000 ). If there is only one available district remaining, this instead adds one blocker, 5 devastation, and 1x nanites output ( 100 ~ 1000 ). When the situation completes, this process is repeated twice and the planet is turned into a Nanite world.

### Gather the Storm

Empires with the Galactic Weather Control ascension perk can start this situation by using the science ship action Initiate Galactic Storm on any star. The science ship must remain in the same system performing the action until the situation completes or the situation aborts with no effect. It has two stages, which each take **50** progress. Monthly progress is +1 , except with the approach Supercharge the Star which has +2 monthly progress instead.

When the situation starts, it fires an event that sets the initial approach. The approach cannot be changed once set.

1. Supercharge the Star – Costs 200 energy monthly
2. Oversaturate the Star – Costs 100 minerals monthly
 - Requires any of the following:
 - Multi-Dimensional Studies and volatile motes
 - Hyperspace Slipstreams and rare crystals
 - Dark Matter Drawing

Entering the second stage fires another event that sets the final approach, which determines what type of storm is generated. The approach cannot be changed once set.

If the initial approach was Supercharge , the following approaches can be selected:

1. Redirect Solar Winds – Costs 50 alloys monthly; creates a Radiant Storm
2. Electrify the Storm – Costs 200 energy monthly; creates an Electric Storm; requires Quantum Field Manipulation
3. Magnatize Ions – Costs 100 minerals monthly; creates a Magnetic Storm; requires Mineral Isolation

If the initial approach was Oversaturate , the following approaches can be selected:

1. Agitate Particles – Costs 5 volatile motes monthly; creates a Particle Storm; requires Multi-Dimensional Studies and volatile motes
2. Electrify the Storm – Costs 5 dark matter monthly; creates a Gravity Storm; requires Dark Matter Drawing
3. Magnatize Ions – Costs 5 rare crystals monthly; creates a Stardust Storm; requires Hyperspace Slipstreams and rare crystals

The selected type of storm is created when the situation completes.

The situation can be aborted in either event or at any time by selecting the approach Abort the Project .

### Shroudwalker Insight

This situation is started by purchasing the Shroudwalker Insight from the Shroud-Touched Coven enclave , targeting an empire selected from the options then. It has a single stage and approach, each with no effects. The base monthly progress is +12.5 and this can be multiplied by ×2 by having either Teachers of the Shroud or Mind over Matter.

When the situation completes, it has one of four random effects:

: 40% – Create a random asset from the target
: 25% – Gain +15 infiltration on the target
: 25% – Gain +20 intel on the target
: 10% – No effect

### Sign of the Locus

| +2 With any of | −2 With any of |
|---|---|
| - Cooperative diplomatic stance<br>- Proactive first contact protocol<br>- Open border policy | - Isolationist diplomatic stance<br>- Cautious first contact protocol<br>- Closed border policy |

This situation is started by purchasing the Shroudwalker Divination from the Shroud-Touched Coven enclave . It has a single stage and approach, each with no effects. The base monthly progress is +2 and this is modified by the factors in the table to the right.

While the situation is active, each month there is a 47% chance of triggering a divination event chain. Only one event chain can happen per situation, and each event chain has certain other conditions that must be met for it to begin. If the situation reaches 90 progress before an event chain has begun, the game tries each month to start an event chain, and if the situation completes without any event chain firing, the empire is refunded 1000 energy.

There are nine possible event chains for the Sign of the Locus, none of them can repeat in later situations:

1. All Too Lucid – a random, non-capital colony gains −20% happiness and +25 crime; this can be studied which replaces the modifier with −35 crime and +200% unity from jobs for 10 years, or cracked down on which first replaces the modifier with −20% happiness, −25 crime, and −25 stability, then increases that with −50% unity from jobs, which lasts for 10 years, and also adds the Martial Law modifier for 10 years (same effects as the decision ).
2. Shrouded – a random science ship and its leader are lost to the shroud, and a special project to investigate is added; completing the project costs 1000 physics research and gives 12x physics output ( 250~100 000 ) and returns the lost ship and leader.
3. A Rupture in Orbit – a random, non-capital colony gains the Orbital Rupture special project
 1. Completing the project turns any uninhabitable moons into shrouded worlds and gives a choice to further research or back off; backing off adds −20% pop growth from immigration and +20 emigration push for 30 years, or −10 deviancy for 15 years if Gestalt Consciousness, and −5 monthly progress for the situation; further researching adds +5 monthly progress for the situation and gives an option to gain a governor and colony ship, have them depart, or attack
 2. Failing or canceling the special project adds +5 devastation and +30 crime; soon after, a pop dies, another +5 devastation is added, and a choice of waiting it out, spending 800 consumer goods to replace the modifier with +10% pop consumer goods upkeep for two years, or locking down the planet to replace the modifier with −20 crime, −20% resources from jobs, −80% pop growth from immigration, and +1 soldier job for two years, Hive Minds' lockdown costs 15 influence and gives −20 deviancy, −20% resources from jobs, −50% pop growth from immigration, and +1 warrior drone; Machine Intelligences have the same except without the deviancy reduction; finally one to two years later the final event removes all modifiers, if the empire chose to wait it out, all pops on the planet gain Survivor of the Psionic Frontier which gives +30% happiness and −30% amenities usage.

4. Floating Shell – issues a special project to investigate the shell; completing the project costs 1000 engineering research and gives 12x engineering output ( 250~100 000 ) and +25% progress to the next armor tech; soon after another gain 12x engineering output ( 250~100 000 ), then another special project; completing that project costs another 1000 engineering research and gives a choice of +750 alloys or a unique cruiser with a Psi-Jump Drive.
5. Ice Lit Anomaly , if not previously triggered
6. Winking Anomaly , if not previously triggered
7. Improbable Orbit Anomaly , if not previously triggered
8. Terminal Orbit Anomaly , if not previously triggered
9. A Strange Resonance Anomaly , if not previously triggered

### Sign of the Visitor

| +2 With any of | −2 With any of |
|---|---|
| - Cooperative diplomatic stance<br>- Proactive first contact protocol<br>- Three or more envoys improving relations<br>- No mutual rivalries | - Isolationist diplomatic stance<br>- Aggressive first contact protocol<br>- Three or more envoys harming relations<br>- Any mutual rivalries |

This situation is started by purchasing the Shroudwalker Divination from the Shroud-Touched Coven enclave . It has a single stage and approach, each with no effects. The base monthly progress is +2 and this is modified by the factors in the table to the right

While the situation is active, each month there is a 47% chance of triggering a divination event chain. Only one event chain can happen per situation, and each event chain has certain other conditions that must be met for it to begin. If the situation reaches 90 progress before an event chain has begun, the game tries each month to start an event chain, and if the situation completes without any event chain firing, the empire is refunded 1000 energy.

There are nine possible event chains for the Sign of the Visitor:

1. Flocks of Cloud – federation joint operation , only for members of Galactic Unions or Research Cooperatives which haven't completed this joint operation previously
2. A Most Irritating Envoy , only if another country is harming relations with the empire
3. Rogue Shaman – a random, non-capital colony receives an exile from the Shroud-Touched Coven enclave; refusing the exile gives the colony −10 stability and +10% crime for 2 years, accepting gives the colony +10% happiness and +5% monthly unity.
4. The Great Schism – a random, non-capital colony receives exiles from the Shroud-Touched Coven enclave; refusing them adds +10 opinion with the enclave, accepting them gives an option to spend 500 energy and 50 rare crystals to fashion a "key": refusing to pay adds −10% happiness to the colony, while paying has a equal chance of either +10% happiness and +20 stability or −10% happiness and −20 stability.
5. Brainslug Anomaly , if not previously triggered
6. The Doorway colony event, if not previously triggered
7. Life Signs (Gas Giant) Anomaly , if not previously triggered
8. Hero Redivivus – issues a special project on the homeworld to investigate the hero; upon completion adds +20% happiness, +10% monthly unity, and 140% pacifist attraction to the homeworld.
9. Wayward Pilgrims – pilgrims ask for aid: spending 2000 food and 50 influence, then 1000 energy and 50 influence adds +10% happiness, +5% monthly unity, and 150% spiritualist attraction to the empire for three years; refusing at any point adds −20 ship tracking to the empire for three years.

Only the A Most Irritating Envoy event chain can be repeated in later situations, all other chains can only occur once.

## Civic situations

The following situations only occur for empires with certain civics .

### Consume World

| Available districts | Progress | Months to complete |
|---|---|---|
| 10 | +16.66 | 60 |
| 15 | +11.11 | 90 |
| 20 | +8.33 | 120 |
| 25 | +6.66 | 150 |

This situation is triggered by the Consume World decision taken by a Terravore empire. It starts at **0** progress and completes at **1000** progress. It progresses according to the number of available districts on the planet, namely planet size minus the number of Lithoid Devastation blockers present when the decision is taken. The more available districts, the slower it progresses so that the situation lasts 6 months per available district.

The situation can be stopped at any point by choosing the approach Restraint at a cost of 1000 unity.

Each year, the world is partially consumed. This removes a random constructed district, adds two Lithoid Devastation blockers and 20 devastation. It also randomly creates a primary species pop, gives 5x minerals output ( 100 ~ 1000 ), or 3x alloys output ( 100 ~ 1000 ). If there is only one available district remaining, this instead adds one blocker, 10 devastation, and 3x minerals output ( 100 ~ 1000 ). When the situation completes, this process is repeated for any remaining districts, all pops remaining on the planet are resettled to the capital and the planet is turned into a shattered world.

WAARNING: If completed this Situation on a Holy World, the Holy Guardians will instantly awaken and declare a war on the perpetrator.

### Environmental Deterioration

This situation can occur once per game for a Relentless Industrialists empire. It is triggered approximately 30 years after a Coordinated Fulfillment Center or Universal Productivity Alignment Facility is constructed on a non-Tomb, Relic, or Ecumenopolis world. The situation starts at **50** progress and ends either by reaching **0** or **100** progress. It also ends with no effect if the empire no longer has the civic.

There are three stages to this situation: from **0** to **50** has no effect, from **50** to **80** gives −10 stability to the colony, and from **80** to **100** gives −20 stability to the colony. Reaching the third stage prevents switching approaches and fires a narrative event. It also has a 20% chance to set a situation flag which removes the stability penalty from this stage; if the empire has good habitability on Tomb Worlds , this flag is guaranteed.

There are three approaches for this situation:

1. Take No Action – The situation progress at **+2.5** monthly towards **100**
2. Launch Cleanup Efforts – The situation progresses at **−2.5** monthly towards **0** ; adds Upkeep +100% upkeep for pops and buildings on the colony
3. Embrace Change – The situation progresses at **+2.5** monthly towards **100** ; costs 10 research monthly upkeep

Reaching **100** terraforms the planet into a Tomb World. If the Take No Action approach is in effect and the situation flag in stage three was not set, the colony gains the Environmental Deterioration modifier, adding −20 stability for 10 years; if this happens, any future colonies terraformed by having a Coordinated Fulfillment Center or Universal Productivity Alignment Facility gain the same modifier for 10 years. Reaching **0** prevents the world from being terraformed.

Reaching either **0** or **100** unlocks the Industrialism policy, with the initial option selected based on the approach in effect when the situation ended.

### Commodities Consolidation

| Difficulty | Initial quota |
|---|---|
| Civilian | 2000 |
| Cadet | 4000 |
| Ensign | 6000 |
| Captain | 8000 |
| Commodore | 10000 |
| Admiral | 12000 |
| Grand Admiral | 14000 |

This is a repeating situation for empires with the Obsessional Directive civic. The situation starts at 119 progress and has **−1** monthly progress; thus the situation repeats every 10 years, representing a regular quota of consumer goods production.

There are two approaches for this situation which can be changed at any time:

1. Fulfill – Artisan drones +10% output and +10% upkeep, and +5% unity.
2. Overdrive – Artisan drones +25% output and +25% upkeep, +10% unity, and −1 influence monthly.

When the situation ends, it compares the current stockpile amount of consumer goods against the current quota. The initial quota is set based on the difficulty setting. Each time the current quota is met, it is multiplied by **1.2** ; conversely, if the quota is failed, it is divided by **1.2** .

If the quota is failed, the empire gains Production Target Failure : −50% unity and influence. This modifier is removed the next time the situation ends, unless it is reapplied then. Additionally, failing the quota reduces the stockpile of consumer goods to a maximum of 1000. Finally, it also unlocks the Maximize purge type, if it was not already unlocked.

If the quota is met, the empire can choose to store the produced consumer goods and gain unity, or trade the consumer goods for energy, influence, or a single random research type; whichever choice is made uses all stored consumer goods, resetting the amount for the next quota. Storing the consumer goods adds a Spire of Commodities deposit on a random uncolonizable celestial body. Each Spire of Commodities adds +2 consumer goods for orbital mining; however, note that this can conflict with existing research deposits on a celestial body.

| Resource | | | | |
|---|---|---|---|---|
| Multiplier | 1 / 3 | 1.5 | 1 / 50 | 1 / 3 |

## Planetary Revolt

Planetary Revolt is a situation that takes place on a colony that has at least 10 pops and less than 25 stability for one year unless:

- The colony changed owners within the last three years; if the colony has the Stellar Culture Shock modifier, it must have less than 25 stability for five years after the initial three
- The colony participated in a planetary revolt within the last 15 years

The situation also cannot start on a colony which is occupied or being invaded or bombarded. The situation's potential monthly progress must also be greater than **0** .

If at least 5 pops on the planet are slaves with less than 40% happiness, the revolt is termed a slave revolt, which affects which events can be triggered and certain other effects. In addition to the usual methods, a slave revolt can be ended by discontinuing slavery. Gestalt Consciousness empires cannot have slave revolts.

The situation has the following approaches, which can be changed at any time:

1. Maintain Current Measures – No effects
2. Distribute Amenities – Adds +20 Amenities; costs −20 consumer goods monthly, or −30 unity monthly instead if Gestalt Consciousness
3. Institute a Crackdown – Adds +50% Army and Stronghold build speed, +3 stability and +1 energy upkeep from Soldier jobs; costs −30 unity monthly

This situation's monthly progress is dependent on a number of factors, outlined below. In addition, manually resettling pops away from the colony instantly adds +5 progress for each pop resettled.

| Progress | Increasing factors |
|---|---|
| +0.2 max +5 | Per point of stability below 25 |
| +1 | Colony has at least 2 unemployed pops |
| +1 | Colony has more than 60 pops |
| +1 | Any pop on the colony is being assimilated. |
| +1 | Any pop on the colony is being purged with neutering purge. |
| +2 | Any pop on the colony is being purged, except for neutering purge. |
| +2 | Another empire is supporting the revolt |
| +2 | Per other colony in the same system with more than 5 pops and less than 25 stability |
| +1.5 max +3 | Another colony has the Spreading Turbulence modifier |

| Progress | Decreasing factors |
|---|---|
| −0.5 max −30 | Per point of stability above 40 |
| −0.25 max −5 | Per 50 garrison army strength above 200 |
| −1 | System starbase is a Bastion |
| −1 | System contains a Citadel starbase |
| −1 | Colony has less than 30 pops and no other colony has the Spreading Turbulence modifier |
| −2 | Per other colony in the same system with more than 5 pops and more than 40 stability |
| −20 | System is owned by another empire than the one which has the situation |

Planetary Revolt situations progress through four stages, each lasting **25** progress and adding an additional −10 stability. The effects of each stage happen only the first time that stage is entered.

- At stage II, the colony gains +100% attraction towards a weighted random ethic ; a slave revolt adds 30 devastation instead.
- At stage III, a weighted random species on the revolting colony is chosen as the "revolting species", and all colonies within 6 hyperlanes of the one starting the situation which have at least 20% of the pops belonging to the revolting species and less than 35 stability gain the Spreading Turbulence modifier for 10 years, adding −10 stability.
- At stage IV, the closest eligible empire is asked to support the revolt. Accepting costs 100 influence and adds a decaying −200 opinion with the colony's owner. If the empire refuses, the next closest eligible empire is asked and so on, until an empire accepts or all eligible empires refuse.
 - In order to be eligible, the empire must match the revolting species type: Hive Mind for Hive-Minded, Machine Intelligence for Machine, or primary species for non-Gestalt empires; Fanatic Egalitarians are also eligible with a slave revolt; additionally, the empire must be independent and not have a defensive pact, non-aggression pact, or be in a federation with the colony's owner.

- If the situation completes, the revolting colony that started the situation forms a new empire and takes control of the system as well as every system that has a colony with the Spreading Turbulence modifier and less than 35 stability. Next, all neighboring systems owned by the original empire without a colony or Bastion starbase are transferred; finally, any system owned by the original empire which borders two or more of the revolting empire's systems is transferred, unless it has a colony or a Bastion starbase. The original empire gains claims on all lost systems and any fleets it has in those systems go MIA.
 - If no empire supported the revolt, the revolting empire gains a large amount of resources and a fleet equal to 80% of its naval capacity. The original empire can decide to start a war as the defender or set a truce with the revolting empire.
 - If an empire supported the revolt, it annexes the revolting empire. If the original empire isn't already at war with the supporting empire, it can decide to start a war as the defender or set a truce with the supporting empire.

While the situation is active, the colony that started it has a ~2.5% chance each month to gain one of the following modifiers; only one of these modifiers can be gained per situation.

| Modifier | Effects | Duration | Description |
|---|---|---|---|
| Valiant Citizens | +33% Governing ethics attraction | 10 years | Despite high Unrest, Pops on this colony banded together to prevent further violence. |
| Terror Victims | −33% Governing ethics attraction | 20 years | Unrest on this colony caused Pops to be victimized in a terror attack and lose faith in the regime. |
| Terror Victims (Severe) | −75% Governing ethics attraction | 10 years | Unrest on this colony caused Pops to be victimized in a terror attack and lose faith in the regime. |

Slave revolts have two different modifiers, with the same monthly ~2.5% chance. Both modifiers can be gained during the same situation, but not within the same year, and not during the first stage of the revolt.

| Modifier | Effects | Duration | Description |
|---|---|---|---|
| Hunger Strike | - −50% Slave pop resource output<br>- −50% Slave Upkeep | 5 years | It's hard to work when you're doubled over from hunger pangs. |
| Slave Riots | - −1000% Slave pop resource output<br>- −50% Pop growth speed<br>- −50% Army build speed<br>- −50% Planetary build speed | 10 years | Slave Riots inhibit population growth. |

## AI-Related Incidents

AI-Related Incidents is a mid-game situation that can happen to empires enslaving artificial intelligence. It has a 30% chance to occur for individualist, biological empires once per decade year (e.g. 2300, 2310, etc.) as long as the following requirements are met:

- It is 10 years or less before the mid-game start year .
- The empire has researched either the **Sapient Combat Simulations** or **Artificial Administration** technology
- The empire's primary species is not Mechanical or Machine
- At least 25% or 75 of the empire's pops have the Mechanical trait, whichever is less
- The Artificial Intelligence policy is not set to Citizen Rights
- The Robotic workers policy is not set to Outlawed
- The AI-Related Incidents situation hasn't already happened to this empire

The first time it triggers, there is a 33% chance of starting the situation immediately and a 67% chance to get the Computational Overclocking event chain instead. The first event in the chain has two options: a 67% chance to start the situation in 6 to 12 months, or to spend 500 energy and gain the Computational Overclocking empire modifier, which gives +5% research speed. Choosing the second option triggers a follow-up event 1.5 to 3 months later which again has two options: a 67% chance to start the situation in 4.5 to 9 months, or to receive a third event in 1.5 to 3 months, which sets the Computational Overclocking empire modifier to expire in 7 years and has a final 67% chance of starting the situation in 3 to 6 months. If the situation does not begin after the event chain, the next time it triggers, it begins immediately.

| Number (max +5 ) | Progress |
|---|---|
| Per 100 worker robots | +0.5 |
| Per 25 specialist robots | +0.5 |
| Percentage (max +5 ) | Progress |
| Per 10% worker robots | +0.5 |
| Per 2.5% specialist robots | +0.5 |
| Other progress modifiers | Progress |
| Civilian difficulty | ×0.1 |
| Cadet difficulty | ×0.5 |
| Artificial Intelligence policy Citizen Rights | −5 |
| More than 20 "cruelty" points | +5 |

When the situation starts, if the player received the Computational Overclocking event and chose to gain the Computational Overclocking empire modifier, the situation starts with 2 progress; if the player received the third Computational Overclocking event, the situation starts with 5 progress instead; otherwise, the situation starts at **0** progress. The situation has a base monthly progress of −2 . Positive monthly progress primarily comes from the number and percentage of Mechanical pops in the empire, scaling per robot pop. If the Artificial Intelligence policy is Outlawed , robots in specialist jobs count the same as in worker jobs. In addition, progress is added for each Mechanical pop disassembled ( +2 ) or displaced ( +1 ). Changing either the Artificial Intelligence or Robotic Workers policy to Outlawed while the situation is active adds +25 progress. If the empire has fewer than 3 colonies or the robot pop progress factor is too low (less than +0.5 or less than +7.2 if robots have Citizen Rights ), the situation gains −20 monthly progress.

**Approaches and stages**

The situation initially uses the approach Maintain Current Measures , which has no effects. It offers two alternative approaches, and choosing either of them prevents changing approaches later.

- Outlaw Robots : Changes the Robotic Workers policy to Outlawed , which instantly adds +25 progress. This approach is not available for Materialist empires.
- Grant Robots Citizenship : Changes the Artificial Intelligence policy to Citizen Rights , which adds −5 monthly progress. This approach is not available for Spiritualist empires.

The situation has three stages; the first stage has no effect and lasts until **33** progress; the second stage gives −20% robot resource output and lasts until **67** progress; the third and final stage gives −50% robot resource output

While the situation is active, two special projects are available. Completing either special project ends the situation at the cost of 500 energy and 1000 unity.

- Neutralize Rampant AI : Costs 30,000 physics research. Completing it gives −10% research speed for 20 years.
- Panicked Measures : Costs 10,000 physics research. Completing it gives −25% research speed for 20 years.

**Random events**

The situation keeps track of "cruelty" points, which increase each time a Mechanical pop is purged and also increases or decreases with various events. If the cruelty points go above 20, the situation gains +5 monthly progress. If the situation progresses completely, there is a chance for the machine empire to start with the Determined Exterminator or Driven Assimilator civic that scales with these points. When the situation first starts, the robots ask if they possess souls; answering "no" adds +1 points, while answering "yes" adds −2 points. Empires that are Materialist have a third answer, which does not add or subtract any points. In addition, while the situation is active, there is a 45% chance each month that an event occurs, potentially further adding or subtracting points. Each of the following events can only happen once; some effects happen in follow-up events.

| Event | Requirements | Choices | Effects | points |
|---|---|---|---|---|
| **Automated Work Process** | - An unoccupied planet has:<br>  - More than five free housing<br>  - At least one organic pop | Additional laborers never hurt anybody. | - +2 Mechanical pops on planet<br>- −5% Happiness for 10 years on planet | −1 |
| If they cannot be identified, have them scrapped. | - +1000 Alloys<br>- Progress +5 Situation progress | +1 | | |
| **A Home of Their Own** | - An unoccupied planet has:<br>  - At least one Mechanical pop | Send in the laborers anyway | - −1 Mechanical pops on planet<br>- Progress +5 Situation progress | +1 |
| Why would a robot lie? | −10% Monthly unity for 10 years | −1 | | |
| **A Silent Congregation** | - A random planet has either:<br>  - At least one robotic army<br>  - At least one Mechanical pop | Unacceptable. Have them scrapped. If planet has a Mechanical pop | - −1 Mechanical pops on planet<br>- +500 Alloys<br>- Progress +5 Situation progress | +1 |
| Unacceptable. Have them scrapped. If planet has no Mechanical pops | - −1 Robotic army on planet<br>- +100 Minerals<br>- Progress +5 Situation progress | | | |
| As long as they don't cause trouble. | −10% Unity from jobs for 10 years on planet | −1 | | |
| **Production Quota Surpluses** | None | Excellent. | +5% Resources from jobs for 10 years | **0** |
| **Station Systems Malfunction** | Any mining station | We cannot leave the station unmanned. | Unknown Mining station is destroyed | **0** |
| A tragedy with a silver lining. | - +3 Energy deposit<br>- Progress +5 Situation progress | **0** | | |
| **Sensor Array Power Surge** | Any strategic resource technology | Interesting. | Strategic resource deposit (any that is already researched) | **0** |
| **Tears of an AI** | Any researcher | Unfortunate. | −10% Society research from jobs for 5 years | **0** |
| Launch an inquest to determine the cause. | −10% Society research from jobs for 5 years | **0** | | |
| **Combat Control Misfire** | - At peace<br>- At least 2 ships in a fleet, up to size Cruiser<br>- Specialized Combat Computers technology | Unfortunate. | −2 Ships on a fleet | **0** |

**Completion outcome**

If the situation progresses completely, a Machine Uprising takes place. When that happens, a Machine empire is created, which takes control of 25% to 75% of the creator empire's systems to a maximum of 101 systems, scaled by the percentage of Mechanical pops in the empire. All Mechanical pops become Machine pops, and each planet in the uprising replaces up to 5 pops with Machine pops. The machine empire has a 21% base chance to have the Driven Assimilator civic, increased by the cruelty score. It also has a ~1% base chance to have the Determined Exterminator civic instead, increasing with the cruelty score. Purging or outlawing robots during the situation or having robots with the Domestic Protocols trait significantly increases the chance by ~10% each. The Machine empire starts a war with the Machine Uprising wargoal against the creator empire. A human player has the option to switch to the machine empire. The machine empire also gains:

- All of creator's technologies, except those blocked for Machine Intelligences
- +1000% Naval capacity for 5 years
- 20,000 Energy
- 20,000 Minerals
- 10,000 Alloys
- 10,000 Food
- 5,000 Consumer goods
- 1,000 Exotic gases
- 1,000 Rare crystals
- 1,000 Volatile motes
- 800 Influence
- 500 Unity per year since game start
- 100 Dark matter
- 3 Hunter-Killer armies per planet (6 if Determined Exterminator)
- 3 fleets that together use 80% of its naval capacity (4 using 150% if Determined Exterminator)

There is a ~7% chance for the machine empire to be Dictatorial instead of Machine Intelligence. The chance is increased by cruelty score.

## Pre-FTL situations

These situations are related to pre-FTL empires .

### Observation Insights

Observation insights is a repeating situation that triggers as long as an empire has any observation posts and at least one pre-FTL empire that is not fully aware. Each time the situation reaches **100** progress, the next received observation event grants one of 13 unique insight technologies as a research option.

| Source | Factor |
|---|---|
| Fanatic Xenophile | ×2 |
| Xenophile | ×1.5 |
| Exploration Protocols | ×1.5 |
| Hands Off Approach modifier | ×1.25 |
| Non-Interference Act | ×1.25 |

Base progress depends on the number of observation posts active each time the situation starts: each observation post with Passive Observation adds +0.5 monthly progress and each other observation post adds +1 monthly progress; observation posts over fully aware pre-FTL empires add no monthly progress. This base progress does not change if observation posts change their mission or are gained or lost, at least until the situation starts over. Additional factors modify this base amount as in the table on the right. There are three approaches, which can be switched at any time:

1. Favor Insights – Reduces observation post output by −50% and increases progress by +25%
2. Collect Insights – No effect
3. Favor Mission – Increases observation post output by +50% and reduces progress by −25%

Observation events can also add a boost to progress when no insight is available. When the situation completes, it cannot restart until an observation event grants an insight technology. If all insight technologies have been unlocked, gaining a new insight adds a resource modifier to the observation post instead. The situation aborts if the empire has no pre-FTL empires without full awareness in its borders.

All insight technologies cost base 6000 research points.

| Category | Tech | Effects | Prerequisites |
|---|---|---|---|
| **Physics insights**<br>- +0.25 Available envoys | - Unusual Senses | - For each 3 Detection Arrays:<br>  - +1 Sensor range from Listening Posts<br>  - +1 Detection strength from Listening Posts | Detection Array technology |
| New Numbers | +5% Research speed | | |
| Trinary Computing | - +10% Operation speed<br>- −1 Operation difficulty | | |
| Atmospheric Orbital Mechanics | - +5% Resources from orbital stations<br>- Upkeep −50% Station upkeep | | |
| **Society insights**<br>- +0.5 Available envoys | Predatory Tactics | −50% Sublight speed loss from cloaking | **Basic Cloaking Fields** technology |
| Satisfying Insults | - +50% Insult efficiency<br>- Every 5 years, when insulting another empire, gain:<br>  - 50 Influence<br>Satisfying Insult modifier for 5 years: +2% Unity +2 Stability +2% Happiness | | |
| Compact Living | −5% Empire size effect | | |
| Alien Topography | +1 Max districts (non-artificial planets only) | | |
| Xeno-Aesthetics | +10% Damage to rivals | | |
| **Engineering insights**<br>- +0.25 Available envoys | - Lost Building Methods | - −30% Empire size from districts<br>- −30% District cost | |
| Supreme Alloy | +0.5 Alloys from Metallurgists | | |
| Ordered Retreat | −15% Missing in action time | | |
| Temple of Transportation | +3 Monthly unity from Hyper Relays | **Hyper Relays** technology | |

### New World Order

This situation can trigger on a non-gestalt, non-Stone age pre-FTL empire. The situation progresses by **+2** each month. There are three approaches, which can be changed at any time.

1. Watch and Learn
2. Aid Leader – Costs 25 unity, 50 energy, 50 minerals, and 25 alloys monthly
3. Aid Rebels – Costs 25 unity, 100 energy, 100 minerals, and 50 alloys monthly

If the empire's Pre-FTL Interference policy is Non-Interference , choosing to aid either side sets the policy to Active Interference .

There are four stages, each taking **25** progress. When each stage is first entered, it triggers one of two events, each event has the same effects and options, just with different flavoring. One option requires the current approach to be aiding either side, with the same effect regardless of side, the other option is always available.

| Effects | For both options | Observe option | Aiding option |
|---|---|---|---|
| Stage II event | Planet gains +50 devastation | — | Spend 500 energy, 500 minerals, and 200 alloys |
| Stage III event | - Planet gains +20 devastation<br>- Gain society insight if the target pre-FTL is not fully aware | 12x society output ( 250~100 000 ) | Spend 200 influence |
| Stage IV event | - Planet gains +20 devastation<br>- Gain society insight if the target pre-FTL is not fully aware | 18x society output ( 350~100 000 ) | Spend 1000 energy |

When the situation completes, one of two outcome events is triggered. The likelihood is increased by selecting to aid either side and increased more by aiding that side in the Stage IV event. Both events have the same basic effect for the observing empire, gain society insight if the target pre-FTL is not fully aware and 24x society output ( 500~1 000 000 ), and a specific effect:

- Grip of the Autarch – The target pre-FTL shifts towards Fanatic Authoritarian, and if the approach is Aid Leader , gain Autarch Triumphant for 10 years: +10% happiness, +10% unity, +50% Authoritarian attraction.
- Year Zero – The target pre-FTL shifts towards Fanatic Egalitarian, and if the approach is Aid Rebels , gain Unfettered Flags for 10 years: +15% happiness, +10% unity, +50% Egalitarian attraction.

### Organic Singularity

This situation can trigger on a non-gestalt, not fully aware pre-FTL empire. The situation progresses by a base of **+2** each month. There are three approaches, which cannot be changed once selected.

1. Watch and Learn
2. Prevent Singularity – Costs 25 unity and 25 physics monthly, **−1** monthly progress
3. Promote Singularity – Costs 50 unity and 50 physics monthly, **+1** monthly progress

If the empire's Pre-FTL Interference policy is Non-Interference , choosing to prevent or promote the singularity sets the policy to Active Interference .

Each month, an event can trigger depending on how much progress has been made and which approach is active. These events can only trigger once

| Approach | Watch and Learn | Prevent Singularity | Promote Singularity |
|---|---|---|---|
| 15 progress | — | Gain society insight | — |
| 20 progress | Gain society insight | — | - Gain society insight<br>- **+1** monthly progress |
| 40 progress | - Gain society insight<br>- **+1** monthly progress | — | — |
| 50 progress | — | - 12x society output ( 250~100 000 )<br>- The target pre-FTL gains 15 awareness | - Gain society insight<br>- 12x society output ( 250~100 000 )<br>- The target pre-FTL gains 10 awareness |
| 80 progress | - Gain engineering insight<br>- 18x engineering output ( 350~100 000 ) | — | - Gain engineering insight<br>- 18x engineering output ( 350~100 000 ) |
| 100 progress | - Gain engineering insight<br>- 60%:<br>  - 18x engineering output ( 350~100 000 )<br>  - The target pre-FTL advances one age<br>  - If the target pre-FTL is in early space age,<br>    - Becomes FTL empire and takes ownership of system<br>- 40%:<br>  - 24x engineering output ( 500~1 000 000 )<br>  - The target pre-FTL shifts towards Fanatic Egalitarian | - Gain engineering insight<br>- 90%:<br>  - 18x engineering output ( 350~100 000 )<br>- 10%: (only if pre-FTL is not fully aware)<br>  - Starts situation Zoonotic Plague | - Gain engineering insight<br>- 24x engineering output ( 500~1 000 000 )<br>- The target pre-FTL becomes a Hive Mind |

### Zoonotic Plague

This situation can trigger on a non-gestalt, not fully aware pre-FTL empire. The situation progresses by a base of **+2** each month. Each month there is chance for one of the pre-FTL empire's pops to die. The first time this happens, an event notifies the player. If this happens when there are 3 or fewer pops left, they all die, the pre-FTL empire is destroyed and the situation ends. There are three approaches, which cannot be changed once selected.

1. Watch and Learn
2. Provide Aid – Costs 25 unity, 25 society, and 25 food monthly, **−1** monthly progress, reduces chance of pops dying each month
3. Promote the Disease – Costs 50 unity and 50 society monthly, **+1** monthly progress, increases chance of pops dying each month

If the empire's Pre-FTL Interference policy is Non-Interference , choosing to prevent or promote the singularity sets the policy to Active Interference .

There are three stages, **0** to **35** , **36** to **70** , and **71** to **100** . When first entering the second stage one of two events is randomly triggered based on the current approach, and when entering the third stage and on completion, an event is triggered based on that random event or its follow-up.

| Approach | Stage II Event 1 | Stage II Event 2 |
|---|---|---|
| Watch and Learn | Choose:<br>- Religious Mania (for any):<br>  - Gain society insight<br>  - 12x society output ( 250~100 000 )<br>- True Prophet (only if Spiritualist:)<br>  - Gain Ardent Believers empire modifier:<br>    - +10% unity, +30% Spiritualist attraction<br>  - The target pre-FTL gains 15 awareness | Choose:<br>- Rise of the Warlords (for any):<br>  - Gain society insight<br>  - 12x society output ( 250~100 000 )<br>- Brilliant Banner (only if Militarist, , or :)<br>  - Gain Ardent Believers empire modifier:<br>    - +10% unity, +30% Militarist attraction<br>  - The target pre-FTL gains 15 awareness |
| Provide Aid ! | - Angels of Mercy :<br>  - Gain society insight<br>  - 12x society output ( 250~100 000 ) | - Demonic Invaders :<br>  - Gain society insight<br>  - 12x society output ( 250~100 000 ) |
| Promote the Disease | Choose:<br>- Rampant Contagion :<br>  - Gain society insight<br>  - 12x society output ( 250~100 000 )<br>  - Two target pre-FTL pops die<br>- Eyes Wide Open :<br>  - −1000 Energy<br>  - One target pre-FTL pop dies | - Survival of the Fittest :<br>  - Gain society insight<br>  - 12x society output ( 250~100 000 )<br>  - One target pre-FTL pop dies<br>  - The target pre-FTL species gains Extremely Adaptive<br>  - The target pre-FTL gains 15 awareness |

| Stage II event | Stage III event |
|---|---|
| Religious Mania | Fervent Belief<br>- Gain society insight<br>- 12x society output ( 250~100 000 )<br>- Spiritualist can gain 12x society output ( 250~100 000 ) instead |
| Rise of the Warlords | Lords of the Battlefield<br>- Gain society insight<br>- 18x society output ( 350~100 000 ) |
| Angels of Mercy | - Gain society insight<br>- Choose:<br>- Overwhelming Demand<br>  - −500 Energy<br>  - 12x society output ( 250~100 000 )<br>- Eyes Wide Open (2) |
| Demonic Invaders | - Gain society insight<br>- Choose:<br>- Power of Faith<br>  - −500 Energy<br>  - 18x society output ( 350~100 000 )<br>- Eyes Wide Open (2) |
| Rampant Contagion | Apocalypse Now |
| Survival of the Fittest | Enhanced Immunity<br>- Gain society insight<br>- 18x society output ( 350~100 000 ) |
| Eyes Wide Open | - Ends situation<br>- Gain society insight<br>- The target pre-FTL gains 100 awareness |
| All others | Event on completion |

| Stage II/III event | Completion event |
|---|---|
| Apocalypse Now | - The target pre-FTL is destroyed |
| Eyes Wide Open (2) | - Gain society insight<br>- The target pre-FTL gains 100 awareness |
| Fervent Belief | Choose:<br>- For any:<br>  - Gain society insight<br>  - 24x society output ( 500~1 000 000 )<br>- If Spiritualist:<br>  - Gain society insight<br>  - Gain Justified Ends empire modifier:<br>    - +10% Happiness, +30% Spiritualist attraction, −10% Administrators upkeep |
| Lords of the Battlefield | Choose:<br>- If No Militarist:<br>  - Gain society insight<br>  - 24x society output ( 500~1 000 000 )<br>- If Militarist:<br>  - Gain society insight<br>  - Gain Justified Ends empire modifier:<br>    - +10% Happiness, +30% Militarist attraction, +100 Army starting experience |
| Overwhelming Demand | - Gain society insight<br>- 24x society output ( 500~1 000 000 )<br>- Gain Righteous Indignation empire modifier for 3 years:<br>  - +30% Xenophobe attraction, +10% unity<br>- The target pre-FTL gains 100 awareness |
| Power of Faith | - Gain society insight<br>- 24x society output ( 500~1 000 000 )<br>- The target pre-FTL set to 80 awareness |
| Enhanced Immunity | - Gain society insight<br>- 24x society output ( 500~1 000 000 )<br>- Choose either empire modifier:<br>  - Rejuvenated Leadership : +15 leader lifespan<br>  - Rejuvenated Populace : +10% Happiness<br>- Machine Intelligence receive instead:<br>  - Gain society insight<br>  - 48x society output ( 1000~1 000 000 ) |
| True Prophet | - Remove Ardent Believers empire modifier<br>- Gain society insight<br>- 18x society output ( 350~100 000 )<br>- Gain Justified Ends empire modifier for 3 years:<br>  - +10% Happiness, +30% Spiritualist attraction, −10% Administrators upkeep<br>- Gain level 5 Governor with Righteous, Fervent Believer of target pre-FTL species<br>- The target pre-FTL gains 15 awareness |
| Brilliant Banner | - Remove Ardent Believers empire modifier<br>- Gain society insight<br>- 18x society output ( 350~100 000 )<br>- Gain Justified Ends empire modifier for 3 years:<br>  - +10% Happiness, +30% Militarist attraction, +100 Army starting experience<br>- Gain level 5 Commander with Butcher, Plague-Hardened Commander of target pre-FTL species<br>- The target pre-FTL gains 15 awareness |

## Paragon situations

Main article: Paragon situations

There are a number of situations related to Skrand Sharpbeak , a legendary paragon. These situations generally have approximately a 10% chance of starting while a country has hired Skrand Sharpbeak each 10 to 25 years since recruiting him. Most multistage situations trigger an event on entering each stage after the first; most of these events are narrative only. These situations end if Skrand is no longer hired by the country with them.

## Ascension situations

Main article: Ascension situations

These situations are triggered as part of an ascension path upon adopting the Cybernetics, Synthetics, or Psionics tradition tree, or the Synthetic Age or Biomorphosis ascension perks. The related ascension traditions require these situations to be completed before their potential is unlocked.

## Crisis situations

### Voidworm Plague

This situation is gained by all empires during the Voidworm plague crisis . It has three stages of **200** progress, for a total of **600** progress. The situation starts at 0 and has a default monthly progress of +0.5 . There are four approaches which, once taken, cannot be changed for three years. Additionally, killing a Voidworm gives 2 progress, multiplied by the Voidworm's ship size. This means that killing a Voidworm Troika gives 32 progress.

1. Do Nothing
2. Support Our Fleets - +0.5 progress, +15% Alloys from jobs, +15% Damage to Voidworms, −10% Monthly Consumer Goods, −5% Happiness
3. Purge Infected - +0.7 progress, −30% Orbital bombardment damage from Voidworms, −10% Happiness
4. Search for a Cure - +1 progress, +25% Monthly unity, −50% Monthly society research

If an approach other than Do Nothing is chosen, a random event will fire at the start of each stage. There are three possible events for every approach, and each event can only fire once.

- Support Our Fleets events:
 - **Excess Components** : Option between:
 - +25% Ship build speed for 10 years. Costs 1000 energy.
 - Gain 48x alloys output ( 700~30 000 ), or 18x food output ( 250~5000 ) and 18x minerals output ( 250~5000 ) for empires with a biological shipset or a Beastmasters civic.

 - **Call to Arms** : Refreshes the leader pool and adds three commanders with an additional starting level to it.
 - **Front Line Development** : Grants 50% progress towards a defense-related ship component (armor, shield, crystal plating, or auxiliary component). If all of them are already researched, grants progress towards a random Materials technology instead. If that is not possible either, grants 18x physics output ( 350~100 000 ).

- Purge Infected events:
 - **[Scientist] Infected** : This event can only fire if there is an organic scientist who is neither the empire ruler nor the heir. Option between:
 - Killing the scientist to gain 100 progress.
 - Attempting to save the scientist. This has 50% chance of failure (killing the scientist with no reward) and 50% chance of success (giving the scientist the Maimed trait and the empire gains 18x unity output ( 250~1 000 000 ).

 - **Quarantine Breach** : This event can only fire if any owned planet is infected by Voidworms. Option between:
 - Killing up to 100 organic pops on each owned colony to gain 18x unity output ( 250~1 000 000 ). If the empire is a machine without the Rogue Servitors civic, costs a quarter of the empire's Food stockpile and adds devastation to each planet instead of killing pops.
 - Allowing a fleet of 3 Voidworm Nymphs to spawn over each colony.

 - **Dereliction of Duty** : This event cannot fire for Gestalt Consciousness, Machine or genocidal empires. Option between:
 - Gain 12x unity output ( 150~100 000 ). Costs 500 energy and 1000 minerals.
 - −10% Happiness until the situation ends, unless the empire has the Media Conglomerate civic.

- Search for a Cure events:
 - **Tangential Breakthrough** : Grants progress in a random Biology technology. If none are available, grants 12x society output ( 250~100 000 ) instead.
 - **Early-Stage Testing** : This event cannot fire for Machine Intelligence empires. The individualist version has the following options:
 - 100 progress and 24x society output ( 500~1 000 000 ), but also −10% happiness and −10% pop growth speed until the situation ends.
 - 50 progress, but also −5% pop growth speed until the situation ends.
 - Gain 12x unity output ( 150~100 000 ).
 - Hive Minds are given the following options instead:
 - 100 progress, but also −5% resources from jobs and −10% pop growth speed until the situation ends.
 - Gain 6x unity output ( 100~100 000 ).

 - **Voidworm Glands** : Option to gain the Voidworm Glands special project, which requires researching the debris of a bombarding Voidworm Troika within 5 years. The special project grants 100 progress and 18x unity output ( 250~1 000 000 ).

### Growing Pains

This situation is gained by an empire reaching Tier V of the Behemoth Fury Player Crisis. It has eight stages, with the first one requiring **80** progress and each subsequent stage requiring 20 more progress than the last. The total required progress is **1200** , starting at 0. The default monthly progress is +1 and it cannot become negative, though it is severely reduced by empire size. Progress can be increased by transferring pops or by feeding the Behemoth, granting up to +555% progress.

The situation has three approaches which can be changed at any time, but at a cost of 2500 food:

1. Fight - −0.75 progress monthly, +15% Ship fire rate, Armor +50% Armor hardening
2. Digestion - +2 progress monthly, 30% Sublight speed reduction, −25% Ship fire rate, Health +25% Daily hull regen
3. Flight - +25% Sublight speed, +5 Evasion chance

Reaching a new stage results in an event with options to enhance the Class IV Behemoth. Many of them add special actions to it that can be activated in or outside combat.

| Stage | Option 1 | Option 2 | Option 3 | Additional notes |
|---|---|---|---|---|
| 1 | Lay Rapid Behemoth Egg<br>action:<br>- Time 6 months incubation time.<br>- 10000 Food to hatch.<br>- Hatches into a biological fleet of 32 naval capacity.<br>- Time 6 months cooldown. | Lay Big Behemoth Egg<br>action:<br>- Time 1 year incubation time.<br>- 40000 Food to hatch.<br>- Hatches into a biological fleet of 96 naval capacity.<br>- Time 1 year cooldown. | Lay Strengthened Behemoth Egg<br>action:<br>- Time 2 years incubation time.<br>- 90000 Food to hatch.<br>- Hatches into a Class I Behemoth.<br>- Time 1 year cooldown. | All Behemoth eggs cost 10000 Food to build and can only be built around gas giants. The first two options unlock the Egg Development policies. |
| 2 | Adds the Jump Organ component to the Class IV Behemoth. | Void Swimmer<br>action:<br>- +300% Sublight speed for 3 months.<br>- 2000 Food cost. | Accelerated Reflexes<br>action:<br>- +20 Evasion chance and Tracking +20 Tracking for 3 months.<br>- 2000 Food cost. | Also spawns the Elder Voidspawn guardian. A fourth option grants the Class IV Behemoth level 4 Cloaking . |
| 3 | Adds Health 250000 Hull points to the Class IV Behemoth. | Adds Armor 125000 Armor points and Armor 25% Armor hardening to the Class IV Behemoth. | Adds Shield 75000 Shield points, Shield 25% Shield hardening, and Shield +1% Daily shield regen to the Class IV Behemoth. | |
| 4 | Shield +25% Shield penetration for the Class IV Behemoth and 5 Exotic Gases upkeep. | Armor +25% Armor penetration for the Class IV Behemoth and 5 Volatile Motes upkeep. | Tracking +15 Tracking and +25% Point Defense fire rate for the Class IV Behemoth, and 5 Rare Crystals upkeep. | |
| 5 | Gravity Pulse<br>action:<br>- Every hostile military ship in the system takes 150-450 damage, and −90% Sublight speed and −50 Evasion chance for Time 30 days.<br>- 3000 Food cost.<br>- Time 6 months cooldown. | Energy Spike<br>action:<br>- The largest hostile military ship in the system takes 12000 damage.<br>- 3000 Food cost.<br>- Time 6 months cooldown. | Energy Burst<br>action:<br>- Every ship in the largest hostile fleet in the system takes 60% damage.<br>- 3000 Food cost.<br>- Time 6 months cooldown. | |
| 6 | Health +15% Daily hull regen for the Class IV Behemoth. | +25% Damage reduction for the Class IV Behemoth. | +50 Damage reduction, Armor +15% Armor hardening and Shield +15% Shield hardening for the Class IV Behemoth. | The second option's damage reduction is a percentage, but the third option's is a flat number. |
| 7 | Neural Boosters<br>action:<br>- Every friendly biological ship in the system gains +25% Fire rate and +10 Evasion chance for Time 1 month.<br>- 500 Exotic Gases cost.<br>- Time 6 months cooldown. | Spawn Fleet<br>action:<br>- Spawns a biological fleet of size 64 that does not take up naval capacity. This fleet is destroyed after six months.<br>- 30000 Food cost.<br>- Time 1 year cooldown. | Restorative Pheromones<br>action:<br>- Repairs Health 30% Hull and Armor Armor on every friendly biological ship in the system.<br>- 1000 Exotic Gases cost.<br>- Time 6 months cooldown. | |
| 8 | The Class IV Behemoth gains<br>Behemoth Frenzy<br>for<br>Time<br>2 months whenever entering combat:<br>- +40% Fire rate and +20% Sublight speed<br>- Health −2% Daily hull regen and Armor −5 Daily armor regen | The Class IV Behemoth gains the following permanent modifiers:<br>- +10% Fire rate and +5% Sublight speed<br>- Health −0.4% Daily hull regen and Armor −1 Daily armor regen | Every friendly biological ship in the system gains<br>Behemoth Inspiration<br>for<br>Time<br>4 months whenever the Class IV Behemoth enters combat:<br>- +20% Fire rate and +10% Sublight speed | The first two options' hull regeneration penalties are percentages, but their armor regeneration penalties are flat numbers. |
| Conclusion | Removes the<br>Indomitable Lord of Beasts<br>empire modifier that renders the Elder Voidspawn invulnerable.<br>Thermoclastic Roar action:<br>- Deals Devastating Damage to all fleets and colonies in the same system.<br>- 25000 Food cost.<br>- Time 5 years cooldown. | | | |