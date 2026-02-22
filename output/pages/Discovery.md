---
title: "Discovery"
categories: ["4.2", "Game_concepts", "Exploration", "Pages_with_math_errors", "Pages_with_math_render_errors"]
---

# Discovery

For the Discovery tradition tree, see Traditions page.

**Discoveries** are unusual findings that warrant additional investigation by a Scientist. The higher the scientist's level, the faster the discovery is investigated. There are two types of discoveries: anomalies and archaeological sites . The Astral Planes DLC adds a third type of discovery - astral rifts . All three come in different levels of difficulty.

A few discoveries are located in unique systems or created by origins, special projects, events or other discoveries, but the majority are randomly generated and can be found anywhere. When a science ship surveys a celestial object it may identify an anomaly or archaeological site. When the investigation of a discovery is complete, an event will pop up that can give various rewards, such as research points, resources, or even a special project which requires further research investment to unlock benefits. Certain Ethics occasionally have additional options when a discovery is investigated.

Archaeology sites are visible on the galaxy map and become grey when fully investigated. Anomalies are only visible on the system map or when hovering over the system on the galaxy map and disappear when fully investigated.

## Uncovering discoveries

Each surveyed celestial object has a 5% base chance of spawning an **anomaly** , which is incremented by 0.25%, tracked per scientist, for each consecutive surveyed planet with no anomaly before being reset. Bonuses like the Perfectionist trait, Map The Stars edict and Fear of the Dark origin then each add to a separate multiplier, which is applied to the base spawn chance. The chance to discover an anomaly rises by 50% (to 7.5% in total) by the 10th unsuccessful try with the base chance (5%), by the 7th try with the Perfectionist trait or the Map The Stars edict, and by the 5th try with both of them.

Spawn chance = (0.05 + (increment*0.0025)) * (1 + sum of multipliers)

Most **archaeological sites** are revealed by surveying, with a 1.23% chance of creating a site if the celestial object can support one. If a site is created this way, the chance to find the next one for this empire is reduced to 0.0246% for 5 years (a reduction of 80%). The AI controlled empires always have a lower chance of discovering archaeological sites (0.0246%) in comparison with the player's empire. Archaeological sites never spawn in a system with a trade value deposits (due to a workaround for a bug with minor artifact deposits).

**Astral rifts** can only appear after the mid-game year is reached. Each year there is a chance for an astral rift to spawn, and the longer it passes without one spawning the more likely it is for one to appear. Afterwards a limited number of astral rifts can also be created with the Astral Splitting astral action. Multiple empires can discover the same astral rift but if an astral rift rewarded a relic another empire cannot discover the same rift.

## Investigation

Anomalies are investigated in one sitting and do not require control of the system. The time to investigate an anomaly depends on the difference in level between the anomaly and the investigating Scientist.

| Level difference | +9 | +8 | +7 | +6 | +5 | +4 | +3 | +2 | +1 | 0 | −1 | −2 | −3 | −4 | −5 | −6 | −7 | −8 | −9 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Investigation days | 20 | 24 | 30 | 35 | 45 | 55 | 65 | 80 | 100 | 120 | 180 | 300 | 540 | 720 | 1080 | 1440 | 2160 | 2880 | 5760 |

Archaeological sites and astral rifts have 1 to 7 chapters and require ownership of the system. Investigation proceeds in phases of 90 days. At the end of each phase, a die is rolled, with a random result from 1 to 10; adding the current number of clues and the scientist's Archaeology Skill or Astral Rift Skill and subtracting the chapter's difficulty gives the total result, as in the following formula:

: Result = Die Roll + Scientist Skill + Bonus + Clues - Difficulty .

The scientist's skill is equal to the scientist's level, plus any modifiers from leader traits, including councilors and the **Curator Archaeology Lab** technology.

| Result total | Outcome | Exp |
|---|---|---|
| ≥ 14 | Completes the current chapter | 75 |
| 10/11 - 13 | Adds 2 clues for the next phase | 40 |
| 5/6 - 9/10 | Adds 1 clue for the next phase | 25 |
| 4/5 ≤ | May trigger an event, or no effect | 10 |

A result of 14 or greater completes the current chapter; a result of 11-13 adds two clues for the next phase, a result of 6-10 adds one clue, a result of 5 or less adds no clues. The thresholds for astral rifts are reduced by 1: 10-13, 5-9, and 4 or less. A result of 5 or less can also trigger various events – depending on the archaeological site and chapter. These events can be helpful: add clues, give loot, even remove the Common leader traits, Substance Abuser leader trait (5% chance); or harmful: remove clues or even kill the scientist (~2.9% chance). Astral rifts do not have random events.

Completing the chapter gives the scientist 75 experience; finding two clues gives them 40 experience, one clue 25 experience. Even when finding no clues still gives the scientist 10 experience. Clues gained from events, however, do not automatically give experience.

If all events are to be avoided from the very start of the excavation, that is, starting with zero clues, in order to minimize the chance of losing the scientist, then having:

- Archaeology Skill + Bonus - Difficulty ≥ 5 gives 0% chance of an event triggering;
- Archaeology Skill + Bonus - Difficulty = 4 gives 10% chance of an event triggering;
- Archaeology Skill + Bonus - Difficulty = 3 gives 20% chance of an event triggering;
- Archaeology Skill + Bonus - Difficulty = 2 gives 30% chance of an event triggering, and so on.

Excavation of archaeological sites can be paused and resumed at any time with no penalty. If the system with the archaeological site is gained by another empire, that empire can continue the excavation from the current chapter, but cannot gain any rewards from already completed chapters. Exploration of astral rifts cannot be stopped once started.

## Precursors

The precursors are the oldest known galactic empires, though long dead. Their ruins are scattered across the galaxy to be discovered via anomalies or archaeology sites .

Every time a celestial object that is not a star is surveyed by an empire controlled by a human player, it has a chance to start a precursor events chain. 5 days after starting the chain, a pop-up screen will inform the player which precursor has been found. Once an empire has discovered their first precursor sign, they are locked into that precursor. DLC precursors have their own conditions for what celestial objects start their chain and thus it is possible to somewhat manipulate the precursor one gets by only surveying the relevant celestial objects.

The first empire that surveys most precursor homeworlds gains a large reward. If the Ancient Relics DLC is enabled, empires that survey most precursor homeworlds, even if they weren't the first ones to do it, unlock a minor artifact action to delve into the secrets of the precursor. The action costs 750 Minor Artifacts and unlocks a special project that provides a permanent reward when completed.

Precursors from the base game are explored via anomalies which spawn special projects. Each special project grants a small amount of Engineering, Physics or Society research as well as a precursor artifact. 6 artifacts are required to reveal the location of a precursor's home system. If the Ancient Relics DLC is enabled precursor anomalies also grant a small number of Minor Artifacts and if the Grand Archive DLC is enabled half of the precursor special project will grant a specimen. After 50 years have passed, a random event can add another precursor anomaly special project on an uninhabitable planet in the empire. Another event can have AI empires "sell" a discovered artifact to non-Gestalt empires for 1000 energy. Corporate Dominion empires can counter with 500 energy. If the empire has the Warrior Culture civic, it can threaten the AI empire to surrender it for free, the success rate depending on both empires' relative fleet power . Empires that have a Protective , Friendly or Loyal attitude offer the artifact for free instead of asking for payment. Each AI Empire can offer an artifact only once.

| Precursor | Homeworld reward | Home system contains | Special project specimens | Secrets of the Precursor special project |
|---|---|---|---|---|
| **Cybrex** | - 120x unity output ( 240~9999 )<br>- 48x engineering output ( 1000~1 000 000 )<br>- 24x energy output ( 350~10 000 )<br>- large minor artifacts reward ( 750 , 1000 , or 1500 )<br>- Cybrex War Forge relic | Ruined Ringworld | - Cybrex Mining Column<br>- Derelict Cybrex Warform<br>- Kuurian Cybrex Blueprints | **12 000**<br>Engineering research cost<br>- **Cybrex Mining Hub** research option<br>- **Mega-Engineering** research option or 1000–1 000 000 Engineering if already researched<br>- Yes Secrets of the Cybrex permanent empire modifier<br>- Head of Research gains Expertise: Voidcraft or 200 xp if already has the trait at max level |
| **First League** | - 120x unity output ( 240~9999 )<br>- 48x society output ( 1000~1 000 000 )<br>- 24x influence output ( 150~300 )<br>- large minor artifacts reward ( 750 , 1000 , or 1500 ) | - Relic World (size 25)<br>- 10 Minerals<br>- 10 Energy | - First League Crew Manifest<br>- Khamdai Magil-Sha<br>- Underworld Cantina Sign | **6000**<br>Engineering research cost<br>- Weather Control Systems<br>- **First League Filing Offices** research option<br>- Anti-Gravity Engineering research option or 1000–1 000 000 Engineering if already researched<br>- Yes Secrets of the First League permanent empire modifier<br>- Head of Research gains Expertise: Industry or 200 xp if already has the trait at max level |
| **Irassian Concordat** | - 120x unity output ( 240~9999 )<br>- 48x physics output ( 1000~1 000 000 )<br>- 24x minerals output ( 350~10 000 )<br>- large minor artifacts reward ( 750 , 1000 , or 1500 )<br>- Javorian Pox Sample relic | - 10 Research<br>- 10 Minerals<br>- 5 Alloys<br>- 10 Energy<br>- 5 Exotic Gases | - Irassian Bacterium Javoria<br>- Irassian Kinder-Atlas<br>- Irassian Purge Order | **3000**<br>Society research cost<br>- Next organic pops technology or 1000–1 000 000 Society if none is available<br>- **Irassian Naval Yards** research option<br>- Yes Secrets of the Irassians permanent empire modifier<br>- Head of Research gains Expertise: Biology or 200 xp if already has the trait at max level |
| **Vultaum Star Assembly** | - 120x unity output ( 240~9999 )<br>- 24x research output ( 500~1 000 000 of each)<br>- large minor artifacts reward ( 750 , 1000 , or 1500 )<br>- Vultaum Reality Perforator relic | - 10 Research<br>- 10 Minerals<br>- 5 Alloys<br>- 10 Energy<br>- 5 Exotic Gases | - Fossilized Vultaum Remains<br>- Vultaum Religious Pamphlet<br>- Vultaum VR Video Game | **3000**<br>Physics research cost<br>- 48x physics output ( 1000~1 000 000 )<br>- Vultaum Reality Computer research option<br>- Yes Secrets of the Vultaum permanent empire modifier<br>- Head of Research gains Expertise: Computing or 200 xp if already has the trait at max level<br>- 7500 Advanced Logic if has Cosmogenesis ascension perk<br>Fanatic Materialist empires can issue an additional special project. 24x influence output ( 150~300 ) 7500 Advanced Logic with Cosmogenesis ascension perk When the additional special project is completed there are 2 options: Option 1: Unknown 15% chance Head of Research gains Hyper Focus Unknown 35% chance Head of Research gains Hyper Focus and Substance Abuser Unknown 50% chance Head of Research dies Option 2: 48x unity output ( 700~2 000 000 ) Head of Research gains 300 expenience Unknown 65% chance Head of Research gains Hyper Focus Unknown 35% chance Head of Research gains Hyper Focus and Substance Abuser Yes Deeper Secrets of the Vultaum permanent empire modifier |
| **Yuht Empire** | - 120x unity output ( 240~9999 )<br>- 24x energy output ( 350~10 000 )<br>- 24x minerals output ( 350~10 000 )<br>- large minor artifacts reward ( 750 , 1000 , or 1500 )<br>- Yuht Cryo Core relic | - 10 Research<br>- 10 Minerals<br>- 5 Alloys<br>- 10 Energy<br>- 5 Exotic Gases<br>- Ruined Hyper Relay | - Yuht Audio Console<br>- Yuht Cryo Pod<br>- Yuht Crystal Skull | **3000**<br>Society research cost<br>- Atmospheric Filtering technology<br>- **Yuht Astronomical Interferometer** research option<br>- Hostile Environment Adaptation research option or 1000–1 000 000 Society if not available<br>- Initiate Yuht Cleansing Process decision<br>- Head of Research gains Expertise: New Worlds or 200 xp if already has the trait at max level |

### Ancient Relics precursors

Rather than through anomalies, the precursors in this DLC are found exclusively via archaeological sites. Each fully excavated site will reveal the location of the next archaeological site, until all of them are completed and the event chain ends. The sites are typically available only to the empire which revealed them.

| Precursor | Homeworld reward | Home system contains | Secrets of the Precursor special project |
|---|---|---|---|
| **Baol** | The Last Baol relic Evolutionary Predators origin also gains plantoid DNA | Tomb World (size 20) | **3000**<br>Society research cost<br>- **Baol Organic Plant** research option<br>- Epigenetic Triggers or Terrestrial Sculpting tech or 1000–1 000 000 Society if already researched<br>- Yes Secrets of the Baol permanent empire modifier<br>- Head of Research gains Expertise: Biology or 200 xp if already has the trait at max level |
| **Zroni** | Psionic Archive relic | 5 Zro | **6000**<br>Society research cost<br>- **Zroni Storm Caster** research option<br>- Psionic Theory research option, or 1000–1 000 000 Society if not available<br>- Yes Secrets of the Zroni permanent empire modifier<br>- Head of Research gains Expertise: Psionics or 200 xp if already has the trait at max level |

### Cosmic Storms precursors

Unlike with other DLCs, the precursors below are spawned by completing an initial anomaly as opposed to simply finding it, and they do not alert the player via a pop-up screen, making them easier to miss if the player does not recognize the anomalies' names.

Once the initial anomaly is investigated, it will spawn an archaeological site. Each fully excavated site will reveal the location of the next archaeological site, until all of them are completed and the event chain ends. The sites are typically available only to the empire which revealed them.

| Precursor | Initial anomaly name | Homeworld reward | Home system contains | Secrets of the Precursor special project |
|---|---|---|---|---|
| **adAkkaria Convention** | Ancient Signals | Ruined habitat Either:<br>- The Tempest Invocator relic<br>- adSul I becomes a continental world | - 3 Zro<br>- 3 Physics | Time<br>**180**<br>Days research cost<br>- Yes Choice between the The True Potential of The adAkkaria permanent empire modifier or a huge amount of Unity |
| **Inetian Traders** | Ancient Shelter | The Disturbance Oppressor relic | Desert World | Time<br>**180**<br>Days research cost<br>- Hyperlane Detailer starbase building<br>- Storm Manipulation or Advanced Storm Manipulation tech or 1000–1 000 000 Engineering if already researched<br>- Yes Secrets of the Inetian Traders permanent empire modifier<br>- Head of Research gains Expertise: Statecraft or 200 xp if already has the trait at max level |