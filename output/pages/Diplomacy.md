---
title: "Diplomacy"
categories: ["Potentially_outdated", "4.1", "Articles_with_potentially_outdated_sections", "Pages_with_unrecognized_icon_strings", "Game_concepts", "Diplomacy"]
---

# Diplomacy

For the Diplomacy tradition tree, see Traditions page.

**Diplomacy** comprises the actions and agreements that empires can take with and against each other. Most diplomatic actions and agreements are mutually beneficial.

Empires with the Pompous Purists civic can send but not receive diplomatic propositions. This includes border access, so whether an empire has borders open or close towards them is decided solely by the Initial Border Status policy. It also means that if two empires have the civic they cannot conduct diplomacy with each other.

## Envoys

Envoys are minor leaders that can be assigned to perform various diplomatic tasks. Once an envoy is assigned to a task, it cannot be reassigned again for a year. Envoys can be assigned to the following tasks:

- Improve Relations with another empire, which grants +0.25 opinion per month to and from the target empire (up to +150 ) and removes the embassy requirement for certain diplomatic actions
- Harm Relations with another empire, which grants −0.5 opinion per month to and from the target empire (up to −150 ) and removes the relation requirement for negative diplomatic actions
- First contact, which establishes communications
- Build a Spy Network, which increases infiltration in another empire over time and allows for operations to be conducted

Each Empire starts with 2 Envoys by default and can gain additional ones in the following ways:

| Available envoys 0 | |
|---|---|
| Source | Effect |
| Leader trait pawn Entourage III Councilor Trait | +3 |
| Leader trait pawn Entourage II Councilor Trait | +2 |
| Leader trait spymaster Shadow Broker Destiny Trait | +2 |
| Master Diplomat Destiny Trait | +2 |
| Fanatic Xenophile ethic | +2 |
| Diplomatic Corps civic | +2 |
| Public Relations Specialists civic | +2 |
| Familiar Face civic | +2 |
| Diplomatic Protocols | +2 |
| Shared Destiny ascension perk | +2 |
| Grand Embassy Complex building | +2 |
| Orbital Embassy Complex orbital ring building | +2 |
| Interstellar Assembly (Stage IV) | +2 |
| Leader trait pawn Entourage I Councilor Trait | +1 |
| Xenophile ethic | +1 |
| Broken Shackles origin | +1 |
| Pompous Purists civic | +1 |
| Secret Societies civic | +1 |
| Influential Cartel civic | +1 |
| Delegated Functions civic | +1 |
| Spyware Directives | +1 |
| Galactic Sovereign / Corporate Sovereign civic | +1 |
| Embassy Complex building | +1 |
| Sanctum of the Whisperers building | +1 |
| Politics tradition tree adopted | +1 |
| Enmity tradition tree finished | +1 |
| The Federation tradition | +1 |
| Universal Compatibility tradition | +1 |
| Double Agents tradition | +1 |
| Autonomous Agents technology | +1 |
| Embodied Dynamism technology | +1 |
| Interstellar Assembly (Stage II) | +1 |
| Federal Envoys president perk | +1 |
| Diplomatic Grants edict | +1 |
| Bureau of Espionage edict | +1 |
| Unknown Open Society empire modifier | +1 |
| Unknown Reconverted Leader empire modifier | +1 |
| Society insight technology (each) | +0.5 |
| Physics insight technology (each) | +0.25 |
| Engineering insight technology (each) | +0.25 |
| Inward Perfection civic | −1 |
| Leader trait unfriendly Blunt Luminary Trait | −1 |

## Diplomatic status

See also: Diplomacy interface

The contact and diplomacy screens show a summary of an empire's diplomatic treaties and relations with other empires, as well as certain other relevant information such as their diplomatic stance policy

The unilateral opinion of an empire also influences whether an AI empire supports or opposes proposed resolutions in the Galactic Community as well as their attitude towards an empire.

### Trust

| Trust cap source | |
|---|---|
| Base | **50** |
| Varies by agreement | **75** or **100** |
| Direct Diplomacy tradition | +50 |
| Universal Compatibility tradition | +50 with |
| Galactic Union member (level 5) Per official assigned to federation | +5 |

| Trust growth modifier source | |
|---|---|
| Direct Diplomacy tradition | +33% |
| Galactic Union member (level 3) Per official assigned to federation | +5% |
| Management Insights application | +10% |
| Master's Teachings: Diplomatic Trust edict | +100% |

Empires which engage in friendly diplomacy build **trust** over time. Each point of trust adds +1 opinion and +0.5 intel cap. The default trust cap is **50** . Certain diplomatic agreements increase this cap, with only the highest amount applying. Conversely, many diplomatic agreements require a certain amount of trust or relation level to be proposed.

Trust changes monthly based on the current diplomatic relationship between two empires. Most diplomatic agreements have a small amount of trust growth, while rivalry and war quickly decay any trust at −2 per month. If there are no active sources of trust growth, trust decays by −0.25 each month.

Modifiers for trust growth and trust cap can be found in the tables to the right.

### Threat

Empires that conquer or subjugate other empires generate **threat** . This represents other nearby empire's concerns and fears of being conquered next. Each empire has a threat rating at every other empire, and as it increases, the empire gains a stacking negative opinion modifier towards the aggressor empire, while becoming increasingly friendly with a stacking positive opinion modifier towards other empires that isn't also threatening. This makes empires with mutual threat more willing to form an alliance against an aggressive conqueror or crisis.

Threat is generated by:

- Conquest:
 - 2 Conquered a system
 - 4 Conquered an upgraded starbase
 - 8 Conquered a colony
 - ×0.75 if wargoal is Claim
 - ×0.67 if wargoal is Counterattack

- 0.5 Vassalize war victory or status quo with new empire created
- 0.25 Make Tributary or Make Subsidiary war victory or status quo with new empire created
- 0.1 Impose Ideology war victory or status quo with new empire created
- 0.5 Take Galatron war victory
- 0.5 Bring Into Fold war victory
- 0.5 Establish Hegemony war victory
- 0.5 Impounding Assets war victory
- 0.5 Bring Into Fold war victory
- 2 Prethoryn Scourge or Contingency conquered a colony
- 2 Unbidden, Aberrant, Vehement or Synth Queen destroyed a colony
- 1000 Upgraded an Aetherophasic Engine to stage 2
- 10 Destroy a star system by Star-Eater
- 3 Use World Cracker, Global Pacifier, Neutron Sweep, Divine Enforcer, Nanobot Diffuser, Deluge Machine, Toxifier or Devolving Beam on a colony belonging to another empire
- 1 Use World Cracker or Toxifier on a non-colony planet belonging to another empire

Once threat is generated, all empires gain their threat rating towards the threatening empire, with the following factors:

- Multiplied by Threat concern factor of AI personalities
- ×0 if same Federation with threatening empire
- ×0.5 if Non-Aggression Pact with threatening empire
- ×0.1 to ×2 from relative power to threatening empire
- ×0 to ×1 , x1 - 0.01 per 1 border distance to threatening empire
- ×0.75 to ×1.25 , x1 - 0.002 per 1 point of opinion towards threatening empire

Threat decays 0.25 per month, and there are no other ways to lower threat.

## Diplomatic actions and agreements

Diplomatic actions are divided into two types: simple actions, which happen as soon as an empire selects one, and agreements, which require the recipient to agree for it to take force. Many actions have a 10-year cooldown between uses. An empire has 6 months to respond to a diplomatic request before it is automatically declined.

Diplomatic agreements are various treaties that generally require both parties to accept before the agreement becomes active. Most agreements are bilateral and mutual, with a few agreements being asymmetric. Most agreements can be cancelled by either party without approval from the other. Most agreements cannot be proposed if the recipient has the Pompous Purists civic unless the proposer is their overlord. Empires with Inward Perfection can also not receive or propose most agreements.

Most diplomatic agreements require a certain level of either trust or relations between the two empires. Additionally, there must be an established embassy or the proposer must have the Diplomatic Networking tradition. Most diplomatic agreements add a minimum intel cap and provide greater details on related types of intelligence.

### General diplomacy

| Agreement | Effects | Requirements |
|---|---|---|
| Embassy | - Envoys improve relations 3 time faster<br>  - +20 Intel cap from diplomatic sources<br>  - +0.10 Trust growth<br>- Enables most other agreements without requiring the Diplomatic Networking tradition | No war or rivalry between proposer and recipient |
| Non-Aggression Pact | - Neither empire can declare war upon each other<br>  - **20** Minimum intel cap<br>  - +0.50 Trust growth and **75** trust cap<br>  - −0.25 Monthly influence upkeep | - **Both**<br>  - Neutral or better relations or 10 trust<br>  - Embassy or proposer is improving relations with recipient<br>  - Not at war with each other<br>  - Independent<br>  - Not in a federation |
| Commercial Pact | - Each empire gains 10% of the other's trade value without losing any for itself<br>  - **20** Minimum intel cap<br>  - +0.25 Trust growth<br>  - −0.25 Monthly influence upkeep | - **Both**<br>  - Positive or better relations or 20 trust<br>  - Either:<br>    - Embassy<br>    - Proposer has Diplomatic Networking tradition<br>    - Proposer has Universal Transactions ascension perk<br>  - Not at war with each other<br>  - Independent<br>  - Federation allows separate treaties or<br>    - in the same federation or not in a federation<br>  - Neither:<br>    - Gestalt Consciousness<br>    - Criminal Heritage<br>    - Inward Perfection |
| Research Agreement | - +25% Research speed for technologies already researched by the other empire<br>  - **30** Minimum intel cap<br>  - +0.10 Trust growth<br>  - −0.25 Monthly influence upkeep | - **Both**<br>  - Positive or better relations or 20 trust<br>  - Embassy or proposer has Diplomatic Networking tradition<br>  - Not at war with each other<br>  - Independent<br>  - Federation allows separate treaties or<br>    - in the same federation or not in a federation<br>  - Not Inward Perfection |
| Migration Treaty | - Pops from either empire can grow or be used in colony ships in the other empire<br>  - **30** Minimum intel cap<br>  - +0.25 Trust growth<br>  - −0.25 Monthly influence upkeep | - **Both**<br>  - Positive or better relations or 20 trust<br>  - Embassy or proposer has Diplomatic Networking tradition<br>  - Not at war with each other<br>  - Independent<br>  - Federation allows separate treaties or<br>    - in the same federation or not in a federation<br>  - Neither:<br>    - Gestalt Consciousness<br>    - Barbaric Despoilers<br>    - Inward Perfection<br>- **Proposer** is not Pompous Purists |
| Guarantee Independence | - Proposer joins recipient's defensive wars<br>- Recipient gains +10 opinion towards proposer<br>  - **20** Minimum intel cap<br>  - +0.25 Trust growth<br>  - −0.25 Monthly influence upkeep for proposer | - **Both**<br>  - Neutral or better relations or 10 trust<br>  - Embassy or proposer is improving relations with recipient<br>  - Not at war with each other<br>  - Independent<br>  - Not in a federation<br>  - Not Inward Perfection<br>  - No defensive pact |
| Defensive Pact | - Each empire joins defensive wars of the other<br>- Mutual +20 opinion<br>  - **40** Minimum intel cap<br>  - +0.75 Trust growth and **100** trust cap<br>  - −1.00 Monthly influence upkeep | - **Both**<br>  - Positive relations or 20 trust<br>  - Embassy or proposer has Diplomatic Networking tradition<br>  - At peace<br>  - Independent<br>  - Not in a federation<br>  - Not Inward Perfection |
| Rivalry | - Proposer gains:<br>  - +0.5 Monthly influence<br>  - Automatic closed borders against recipient except during a truce<br>  - Animosity casus belli against recipient<br>  - −20% Claim influence cost against recipient<br>- Mutual −100 opinion and −2 trust growth | - **Proposer** is not Inward Perfection<br>- Either:<br>  - Terrible relations<br>  - Proposer is harming relations<br>  - Proposer is at war with recipient<br>  - Either has supremacist diplomatic stance<br>  - Either has antagonistic diplomatic stance<br>  - Either is fallen empire unless proposer is a subject<br>  - Recipient has declared proposer a rival |

**Diplomatic actions**

| Action | Effects | Requirements |
|---|---|---|
| Recall Embassy | Recalls embassy | **Proposer** has an embassy with recipient |
| Break Non-Aggression Pact | - Ends non-aggression pact<br>- Creates 10-year truce between proposer and recipient<br>- Recipient gains decaying −25 opinion of proposer | **Proposer** has non-aggression pact with recipient |
| Break Commercial Pact | - Ends commercial pact<br>- Creates 10-year truce between proposer and recipient<br>- Recipient gains decaying −25 opinion of proposer | **Proposer** has commercial pact with recipient |
| Break Research Agreement | - Ends research agreement<br>- Recipient gains decaying −25 opinion of proposer | **Proposer** has research agreement with recipient |
| Break Migration Treaty | - Ends migration treaty<br>- Recipient gains decaying −15 opinion of proposer | **Proposer** has migration treaty with recipient |
| Revoke Guarantee | - Ends guarantee independence<br>- Creates 10-year truce from proposer toward recipient<br>- Recipient gains decaying −15 opinion of proposer | **Proposer** has guarantees recipient's independence |
| Break Defensive Pact | - Ends defensive pact<br>- Creates 10-year truce between proposer and recipient<br>- Recipient gains decaying −100 opinion of proposer | **Proposer** is at peace and has defensive pact with recipient |
| End Rivalry | Ends proposer's rivalry of recipient | **Proposer** has had recipient as a rival for at least 10 years |
| Improve Relations | - +0.25 Opinion monthly, up to +100 max<br>- Requires an assigned envoy<br>- If the envoy is recalled or reassigned, opinion decays by −1 monthly to **0** | - **Proposer**<br>  - Not at war or harming relations with recipient<br>  - Has an available envoy to assign |
| Harm Relations | - −0.5 Opinion monthly, up to −100 max<br>- Requires an assigned envoy<br>- If the envoy is recalled or reassigned, opinion decays by +1 monthly to **0** | - **Proposer**<br>  - Not at war or improving relations with recipient<br>  - Has an available envoy to assign |
| Build Spy Network | - Builds a Spy Network in recipient<br>- Requires an assigned envoy | - **Proposer**<br>  - Not already building a spy network in recipient<br>  - Has an available envoy to assign |
| Make Claims | Switches to the Claims interface. | **Proposer** is allowed to make claims |
| Declare War | - Enters the Wargoals menu to declare a war<br>- Mutual −50 opinion and −2 trust growth while at war | - **Proposer**<br>  - Is not at war with recipient<br>  - Does not have a truce, pact, or federation with recipient<br>  - Does not have any branch offices on recipient's planets |
| Open Borders | - Allows recipient's ships access to owned systems<br>- Borders are opened automatically:<br>  - After a peace treaty, during 10-year truce between all war participants<br>  - Between overlords and their subjects<br>  - By certain resolutions in the Galactic Community or Galactic Imperium | **Proposer** has not declared recipient a rival |
| Close Borders | - Prevents recipient's ships access to owned systems while at peace<br>- Borders automatically closed for rivals<br>- Recipient gains −20 opinion towards proposer | - **Proposer** does not have a truce with recipient<br>- Not available between overlords and subjects |
| Insult | - Recipient gains decaying −200 opinion towards proposer<br>- With the Satisfying Insults technology, instead:<br>  - Recipient gains −300 Opinion towards proposer<br>  - Proposer gains +50 Influence (5 years cooldown) | - Either:<br>  - Tense or worse relations<br>  - Proposer is harming relations<br>  - Proposer is at war with recipient<br>  - Either is fallen empire |
| Add to Imperial Council | Adds recipient to the Imperial Council at a cost of 100 influence | - **Proposer**<br>  - Has 100 influence<br>  - Is Galactic Emperor<br>- **Recipient** is a member of the Galactic Imperium<br>- By Appointment Imperial Council resolution is enacted<br>- There is an empty seat on the Imperial Council |
| Kick from Imperial Council | Removes recipient from the Imperial Council at a cost of 100 influence | - **Proposer**<br>  - Has 100 influence<br>  - Is Galactic Emperor<br>- **Recipient** is a member of the Imperial Council<br>- By Appointment Imperial Council resolution is enacted |
| Join the Galactic Imperium | Proposer joins the Galactic Imperium | - **Proposer** is not a member of the Galactic Imperium<br>- **Recipient** is the Galactic Emperor |

### Subject empire diplomacy

See also: Subject empire

Subject empires have certain obligations to their overlord, based on their agreement terms. Subject empires can be blocked from engaging in most diplomacy by the agreement term Limited Diplomacy . Even without that agreement term, most other diplomatic actions and agreements are blocked for subjects. Subjects have +25 opinion and +0.25 trust growth with their overlord. Additionally, subjects have an additional diplomatic factor, **loyalty** , which determines whether they will engage in trade or other diplomacy with their overlord.

Diplomatic subjugation, whether demanded or asked for, requires both parties to be independent and at peace. Additionally, the potential subject cannot be the Custodian or Galactic Emperor, nor have been declared a crisis . Awakened Empires can always propose subjugation.

| Agreement | Effects | Requirements |
|---|---|---|
| Propose Subjugation | Enters the terms menu to propose becoming overlord of recipient | - **Proposer**<br>  - Not guaranteeing recipient's independence<br>- **Recipient**<br>  - Not a member of the Galactic Imperium<br>    - Unless proposer also is a member<br>- **Both**<br>  - Excellent relations or 50 trust<br>  - Embassy or proposer has Diplomatic Networking tradition<br>  - Independent and at peace |
| Ask to be their Subject | Enters the terms menu to propose becoming subject of recipient | - **Proposer**<br>  - Not asking another empire already<br>  - Not Pompous Purists<br>- **Both**<br>  - Excellent relations or 50 trust<br>  - Embassy or proposer has Diplomatic Networking tradition<br>  - Independent and at peace<br>  - Members or not of Galactic Imperium<br>  - Federation allows separate treaties or<br>    - in the same federation or not in a federation |
| Ask to be Released | Grants independence to the subject and sets a 10-year Truce | **Proposer** is subject of recipient |
| Propose Secret Fealty | Proposer gains Allegiance War casus belli against recipient's overlord | - **Proposer**<br>  - Not a subject<br>  - Not overlord of recipient<br>- **Recipient**<br>  - Is a subject<br>  - Has not lost Allegiance War war in last 5 years<br>- **Both**<br>  - Excellent relations or 50 trust<br>  - Embassy or proposer has Diplomatic Networking tradition |

**Diplomatic actions**

| Action | Effects | Requirements |
|---|---|---|
| Release Subject | Grants independence to the subject and sets a 10-year Truce | **Proposer** is overlord of recipient |
| Integrate Subject | Integrates the subject into the overlord empire. | - **Proposer**<br>  - Overlord of recipient for at least 10 years<br>  - Has Integration Permitted agreement term with recipient<br>  - Not currently integrating a subject |
| Cancel Integration | Stops current integration | **Proposer** is integrating recipient |
| Support independence | - Proposer joins recipient if they declare an Independence War<br>- Adds proposer's power for relative power of subjects opinion modifier | - **Proposer**<br>  - Not Inward Perfection<br>  - Not overlord of recipient<br>- **Recipient** is a subject<br>- **Both**<br>  - Neutral or better relations or 10 trust<br>  - Embassy or proposer is improving relations with recipient |
| Cancel support independence | Ends support independence of recipient | **Proposer** is supporting independence of recipient |
| Pledge Secret Fealty | Recipient gains Allegiance War casus belli against proposer's overlord | - **Proposer**<br>  - Is a subject<br>  - Has not lost Allegiance War war in last 5 years<br>- **Recipient**<br>  - Not a subject<br>  - Not overlord of proposer<br>- **Both**<br>  - Excellent relations or 50 trust<br>  - Embassy or proposer has Diplomatic Networking tradition |
| End Secret Fealty | Ends secret fealty status with recipient | **Proposer** has pledged or received secret fealty with the recipient |

### Federation diplomacy

See also: Federation

Federations are multi-faceted and multi-lateral agreements between two or more empires to provide mutual defense and other benefits to the members of the federation. Agreements between federations members or between federation members and other empires depend in part on the current laws of the federation. Federation members cannot sign guarantee independence, support independence, non-aggression pacts, or defensive pacts with any empire. Members can sign research agreements, commercial pacts, and migration treaties with each other or other empires unless the federation's laws prevent them from doing so.

By default, joining a federation requires the unanimous approval of all current members of that federation, whether an empire petitions for membership or a current member invites another empire to join. With the Federations DLC, it is possible to change that requirement to be a majority vote or be decided by the federation president alone. Joining or leaving a federation requires the federation and the potential member to be at peace. Members of the Galactic Imperium cannot join or associate with federations.

Inward Perfection empires cannot join a federation diplomatically; they can be forced in with the Establish Hegemony casus belli or if their overlord joins a federation with the Yes Can Subjects Join law; they can be federation associates, however.

Federation members have +50 opinion, 100 trust cap, and +1 trust growth with each other; they must also pay −1 influence in diplomatic upkeep. Federation associates have +10 opinion, 100 trust cap, and +0.5 trust growth with members of the associated federation.

| Agreement | Effect | Federation vote | Requirements |
|---|---|---|---|
| Form Federation | Creates federation with recipient | None | - **Proposer** has The Federation tradition<br>- **Both**<br>  - Not in a Federation<br>  - Not a subject<br>  - Excellent relations or 30 trust<br>  - Embassy or proposer has Diplomatic Networking tradition |
| Invite to Federation | Invites recipient to join the Federation | By Invite Members law | - **Proposer** is a Federation member<br>- **Recipient**<br>  - Not in a Federation<br>  - Independent or subject of proposer<br>- **Both**<br>  - Excellent relations or 30 trust<br>  - Embassy or proposer has Diplomatic Networking tradition |
| Ask to join Federation | Requests to join an already existing Federation | By Invite Members law | - **Proposer**<br>  - Not in a Federation<br>  - Independent or subject of recipient<br>- **Recipient** is a Federation member<br>- **Both**<br>  - Excellent relations or 30 trust<br>  - Embassy or proposer has Diplomatic Networking tradition |
| Kick from Federation | - Starts a vote to kick the member from the Federation<br>- Recipient gains decaying −100 opinion of proposer<br>- Gains decaying −200 opinion of federation members if kicked | By Kick Members law | - **Both** members of same Federation<br>- **Proposer** is not subject of recipient<br>- At least three members in Federation |
| Ask to leave Federation | - Requests to leave the Federation<br>- Refusing grants the Secession casus belli and a decaying −45 opinion. | President only | - **Proposer** is Hegemony member<br>- **Recipient** is Hegemony president |
| Offer Association Status | The empire and the federation will not be able to declare war upon each other. | Unanimous | - **Proposer** is a Federation member<br>- **Recipient** is not in a Federation<br>- **Both**<br>  - Positive or better relations or 20 trust<br>  - Embassy or proposer has Diplomatic Networking tradition |
| Request Association Status | The empire and the federation will not be able to declare war upon each other. | Unanimous | - **Proposer** is not in a Federation<br>- **Recipient** is a Federation member<br>- **Both**<br>  - Positive or better relations or 20 trust<br>  - Embassy or proposer has Diplomatic Networking tradition |

**Diplomatic actions**

| Action | Effect | Federation vote | Requirements |
|---|---|---|---|
| Leave Federation | - Leaves the Federation<br>- Creates a truce between the federation and former member<br>- Federation members gain decaying −200 opinion with former member | None | - **Proposer**<br>  - Not a subject<br>  - Not Hegemony member |
| Revoke Association Status | - Creates a truce between the federation and former associate<br>- Recipient gains decaying −25 opinion with federation members if association status is revoked | Majority | - **Proposer** is a Federation member<br>- **Recipient** is a Federation associate |
| End Association Status | - Creates a truce between the federation and former associate<br>- Federation members gain decaying −25 opinion with former associate | None | **Proposer** is a Federation associate |

## Acceptance

The acceptance of diplomatic agreements by computer empires is determined by multiple factors.

| Agreement | Attitude | | | Relative power | | Scaling per | | | Other factors |
|---|---|---|---|---|---|---|---|---|---|
| Friendly | Receptive/Cordial/Protective | Neutral/Wary | Overwhelming | Superior | Shared Rival | 10 Opinion | Distance | | |
| Embassy | +100 | +40 | −25 | +20 | +10 | +40 | +5 | −0.5 | +60 per shared Defensive Pact |
| Non-Aggression Pact | +100 | +50 | **0** | +100 | +50 | +50 | +2 | −1 | −30 per existing Non-Aggression Pact |
| Commercial Pact | +100 | +50 | **0** | **0** | **0** | **0** | +4 | −1 | +1 per given Trade Value −30 per existing Commercial Pact |
| Research Agreement | +100 | +50 | **0** | **0** | **0** | **0** | +4 | −1 | +0.5 per tech either empire doesn't have −30 per existing Research Agreement |
| Migration Treaty | +10 | **0** | **0** | **0** | **0** | **0** | +5 | −1 | +10 Loyal attitude |
| Defensive Pact | +50 | +20 | −50 | +20 | +10 | +30 | +2 | −1 | +30 per shared Defensive Pact −50 per existing Defensive Pact |
| Federation | +30 | **0** | −50 | +20 | +10 | +10 | +1 | −1 | +100 Federation Associate +30 Crisis −30 different War Philosophy policy |
| Demand Subjugation | +20 | **0** | −20 | +100 | +50 | **0** | **0** | −0.5 | −100 below 50 Trust −0.25 per pop |

### Personality

The most specific factor that determines an empire's acceptance rate is its AI personality .

| AI personality | Agreement | | | | | Federation | | | | | | Trade Willingness |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |
| Decadent Hierarchy | +20 | −10 | **0** | **0** | −100 | −30 | −30 | −30 | −30 | −30 | −10 | 90% |
| Democratic Crusaders | **0** | +20 | **0** | **0** | **0** | +10 | **0** | +10 | **0** | **0** | −50 | 90% |
| Erudite Explorers | +5 | +5 | +50 | +10 | **0** | **0** | **0** | **0** | +10 | −10 | **0** | 90% |
| Evangelizing Zealots | **0** | **0** | −20 | −20 | **0** | −20 | −20 | −10 | −20 | +20 | −20 | 75% |
| Federation Builders | +25 | +25 | +15 | +15 | +10 | +20 | +10 | +10 | +10 | +10 | +10 | 95% |
| Harmonious Collective | +20 | **0** | +10 | +10 | −10 | **0** | **0** | **0** | **0** | **0** | **0** | 90% |
| Hegemonic Imperialists | −10 | +10 | −10 | −10 | −50 | −20 | −20 | −10 | −20 | −20 | **0** | 80% |
| Honorbound Warriors | −100 | +20 | **0** | −20 | **0** | −10 | −20 | **0** | −20 | −20 | −10 | 70% |
| Migratory Flock | +20 | **0** | +20 | +20 | +100 | +20 | +20 | +10 | +20 | −20 | +10 | 110% |
| Peaceful Traders | +20 | **0** | +10 | +20 | +20 | +10 | +20 | −10 | +10 | −10 | +10 | **100%** |
| Ruthless Capitalists | −10 | **0** | +10 | +20 | **0** | −10 | +10 | −10 | −10 | −10 | −10 | **100%** |
| Slaving Despots | −20 | **0** | **0** | **0** | −100 | −10 | −10 | −10 | −10 | −10 | **0** | 80% |
| Spiritual Seekers | +20 | +10 | +10 | +10 | +20 | +10 | +10 | +10 | −10 | +10 | +10 | 90% |
| Xenophobic Isolationists | +20 | −20 | −20 | −20 | −100 | −50 | −50 | −50 | −50 | −50 | −50 | 50% |
| Fanatical Befrienders | +50 | +50 | +50 | +50 | +50 | +50 | +30 | +30 | +30 | +30 | +30 | **100%** |
| Fanatical Purifiers | **0** | **0** | **0** | **0** | **0** | No | No | No | No | No | No | 50% |
| Hive Mind | −10 | −10 | **0** | No | No | −50 | −100 | −30 | −50 | −50 | −50 | 70% |
| Machine Intelligence | **0** | **0** | **0** | No | No | −30 | −100 | −20 | −20 | −100 | −30 | 80% |
| Rogue Servitors | **0** | **0** | **0** | No | No | **0** | **0** | **0** | **0** | −100 | +10 | 90% |
| Driven Assimilators | **0** | **0** | **0** | No | No | −50 | −50 | −50 | −50 | −100 | −50 | 50% |
| Determined Exterminators | **0** | **0** | **0** | No | No | No | No | No | No | No | No | **100%** |
| Crisis Aspirant | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **0** | 25% |
| Indolent Overlord | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **0** | **0** | 50% |
| Benevolent Corporation | +20 | −10 | +10 | +50 | +10 | **0** | **0** | **0** | **0** | **0** | **0** | 75% |

## Trade deals

Trade deals are instant or monthly transfers of resources or other assets between two empires. Deals that transfer monthly resources last between 10 and 30 years; once the AI fills their stockpile, long-term contracts become only viable option. It is possible to break long-term trade contracts if not enough resources are stockpiled, but this causes an opinion penalty. Diplomatic trades often can yield better deals than the market. The AI will never accept mixed long-term/instant trades. The value the AI places on a particular resource in a deal is largely based on how much of YOUR economy is devoted to producing that resource - shifting your economy to focus on a particular resource will cause all of the AI empires to value it less in deals. Although Gestalt Consciousness empires have no use for consumer goods or Zro, they are still willing to trade for them.

Trading requires a neutral or positive attitude between the two empires. Empires holding a negative attitude will accept only gifts (giving them resources without them giving anything in return). Fallen empires only trade if they are patronizing or enigmatic towards the proposing empire and will never trade strategic resources. Resources cannot be traded between overlords and subjects if the terms of agreement include contribution or subsidies in that resource.

Trade willingness shows how much an empire is open to trading with other empires and is dependent on their AI personality. The lower their trade willingness is, the more favorable a trade deal has to be for them to see it as fair. Empires with less than 75% trade willingness will never make offers.

In addition to resources, the following things can be traded diplomatically:

- Communications: Valued based on the number of new contacts. Does not include Enclaves. Fallen Empires always refuse.
- Active Sensor Link: Valued based on distance, neighboring empires being more interested. Allows the empire receiving the link to see everything the granting empire can see. Only available as a timed deal. Fallen Empires always refuse.
- Transfer System: Available only towards neighbors during peacetime, it is the most valued trade option and can be used to offer to cede one of your star systems, usually non-preferred planets that are too expensive to terraform or adapt pops to, or as a way to ease opinion penalty of claims or border tension. The AI will always refuse to trade away their own systems, and will not accept systems that contain colonized Holy Worlds or border the Militant Isolationists.
- Specimens: Valued by selling cost x1.3, or twice more if they don't have a specimen from that category.
- Transfer Leader: Only available to and from empires with the Tactical Algorithms civic or from a tier 2 specialized subject to the overlord. Valued based on the leader's abilities. Requires both empires to have the same authority if Gestalt Consciousness. Maximum one Leader per trade.

### Subject trade deals

Subject empires have additional trading options with their overlord:

- Borrow Fleet: Gives the subject temporary control a fleet. Valued based on how much of the total fleet power the fleets represent.
- Pledge Loyalty: Only available from a subject towards the overlord as a timed trade deal; if the subject has 150 opinion or better towards the overlord, it gives +2.5 loyalty monthly, otherwise +1.5 monthly.
- Share Empire Data: Adds +20 intel from the giver to the recipient; can be given by the overlord if they have 80 or less intel on the subject; can be given by the subject if they have 40 or less intel on the overlord.
- Loyalty: Only available from a subject towards its overlord, each point of loyalty will increase trade acceptance by 1 . Loyalty can be used even if the value would become negative, up to −100 .

Specialist subjects have additional, unique trade options which extend their bonuses to the overlord, usually at the cost of their own:

#### Timed trade actions

Timed trade action provide modifiers for the overlord at the expense of negative modifiers for the subject.

| Subject type | Trade action | Effect | | Overlord | Subject | Multiplied by tier |
|---|---|---|---|---|---|---|
| Bulwark | Bulwark Prefabs | Defense Platform | - Build cost<br>- Upkeep Upkeep | −25% / −50% / −75% | +25% / +50% / +75% | Yes |
| Prospectorium | Prospectorium Techniques | Monthly strategic resources | | +5% / +10% / +15% | −5% / −10% / −15% | Yes |
| Scholarium | Scholarium Processors | Research station output | | +20% / +30% / +40% | −10% / −15% / −20% | Yes |
| Scholarium Hypotheses | Research alternatives | | +1 | −1 | No | |

#### Technology sharing

Technology sharing trade actions are instant trade actions that give specialist technologies as research options to the overlord.

| Subject type | Trade action | Effect |
|---|---|---|
| Bulwark | Bulwark Technology | - Researched Bulwark technologies given as options to Overlord<br>- Subject gets Bulwark Technology Sharing modifier for Time 1 year:<br>  - −10% Engineering research if sharing:<br>  - −10% Physics research if sharing: |
| Prospectorium | Prospectorium Technology | - Researched Prospectorium technologies given as options to Overlord<br>- Subject gets Prospectorium Technology Sharing modifier for Time 1 year:<br>  - −10% Engineering research if sharing:<br>  - −10% Physics research if sharing:<br>  - −10% Society research if sharing:<br>- Subject pays 100 strategic resources by technology shared |

### Trade acceptance

The trade acceptance number shows how much the other empire favors a deal. A trade acceptance lower than 1 means that the other empire sees the deal as disadvantageous for them and will always refuse it. A trade acceptance of 1 means that AI empire sees the deal as fair and will always accept it. A trade acceptance higher than 1 means that the other empire sees the deal as advantageous for them and will give a temporary bonus to their opinion, up to a limit of +100 .

## Favors

Favors can only be obtained through events and have two purposes. First, an empire can call upon Favors to add another empire's Diplomatic Weight to theirs ( +10% per favor) when voting on Resolutions in the Galactic Community as long as the other empire is not already voting the same way. This does not decrease the other empire's diplomatic weight for the vote. Second, Favors increase the acceptance rate of certain diplomatic agreements or federation laws by +5 for each Favor. An empire can owe another empire up to 10 Favors.

Multiple empires can call upon Favors from the same target empire and one empire can simultaneously call upon Favors from multiple target empires.

## Attitude

Each empire will have a specific attitude towards other empires dictated by their AI personality, diplomatic interactions and the relative power of both empires.

| Attitude | Trade & Pacts | Prefer peace | Other Effects | Requirements | Description |
|---|---|---|---|---|---|
| Neutral | Yes | Yes | none | none below | This Empire does not consider us relevant to their interests. |
| Wary | Yes | Yes | none | inferior relative power and shared border | This Empire maintains a cautious attitude towards us. |
| Receptive | Yes | Yes | more inclined to accept diplomatic pacts | diplomatic AI personalities | 'This Empire is interested in closer relations with us. |
| Cordial | Yes | Yes | more inclined to accept diplomatic pacts | high opinion | This Empire is amenable to peaceful coexistence and trading with us. |
| Friendly | Yes | Yes | more inclined to accept diplomatic pacts and join a federation | high opinion and successful past diplomacy | 'This Empire views us as a friend and may be willing to form an alliance with us. |
| Protective | Yes | Yes | more inclined to accept diplomatic pacts and may propose subjugation | high opinion and superior relative power | This Empire believes that we are weak and need their protection. |
| Suspicious | No | Yes | none | low opinion | This Empire views us with suspicion and mistrust. |
| Rival | No | Yes | none | rival with low opinion | This Empire views us as their rival. |
| Hostile | No | No | none | very low opinion | This Empire views us as their enemy. They are likely to attack us if they think they can win. |
| Domineering | No | No | only uses the Subjugation Casus Belli | low opinion and Subjugator AI | This Empire believes that we would make a fine vassal. |
| Threatened | No | No | none | 50 or higher threat rating | This Empire views us as a threatening menace. |
| Overlord | Yes | Yes | none | overlord | This Empire is our overlord. |
| Loyal | Yes | Yes | none | subject with positive loyalty | This subject is loyal to us. |
| Disloyal | No | No | considers the relative power of other subjects as well | subject with negative loyalty | This subject resents its subservience to us. |
| Dismissive | No | Yes | none | Fallen Empire | This Fallen Empire considers us largely beneath their notice. |
| Patronizing | Yes | Yes | may bestow gifts | Fallen Empire with high opinion | This Fallen Empire views us as errant children in need of their guidance. They may deign to bestow gifts of technology, resources or ships on us. |
| Angry | No | No | will send a demand which will grant them Casus Belli if refused | Fallen Empire with low opinion | We have angered this Fallen Empire with our actions, and they may declare war to punish us. |
| Arrogant | No | Yes | no effect | distant Awakened Empire | This Awakened Empire views us with dismissive arrogance. |
| Imperious | No | Yes | will propose subjugation | neighbor Awakened Empire | This Awakened Empire views us as a future subject. They are likely to demand we surrender our independence. |
| Belligerent | No | No | none | Awakened Empire with low opinion | This Awakened Empire views us as a target of conquest. They are likely to attack us. |
| Custodial | Yes | Yes | accepts joining a Federation | Guardian Awakened Empires | This Awakened Empire believes that it needs to protect us from the crisis currently threatening the galaxy. They are likely to attempt to ally us. |
| Enigmatic | Yes | Yes | opinion is hidden and has no impact | Ancient Caretakers | This Fallen Empire is an ancient artificial intelligence that behaves in a strange and unpredictable manner. We do not know what to expect from it. |
| Berserk | No | No | attacks any empire nearby | Malfunctioning Custodians | This Awakened Empire is an ancient artificial intelligence that has gone berserk. It is likely to attack anything and anyone around it. |

## Genocidal Diplomacy

Due to their destructive nature, genocidal empires only have limited access to diplomacy, depending of what type of genocidal civic they possess:

- Empires with the Fanatic Purifiers civic can only engage in diplomacy with empires of the same founder species. Note that these other empires still have −1000 Opinion unless they are also Fanatic Purifiers, in which case they have +200 Opinion towards each other.
- Empires with the Determined Exterminator civic can only engage in diplomacy with empires with Machine or Mechanical founder species.
- Empires with the Devouring Swarm, Terravore and (unrecognized string “devouring wilderness” for Template:Icon ) Devouring Wilderness civics cannot engage in any diplomacy at all, not even with identical empires. Envoys are thus only useful to them for Espionage and First Contact.
- Empires with the Scorched World Heralds and Pyromanic Instinct civics can only engage in diplomacy with empires who have a Thermophile founder species.