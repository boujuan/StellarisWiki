---
title: "ID"
categories: ["Potentially_outdated", "3.12", "Articles_with_potentially_outdated_sections", "Guides"]
---

# ID

IDs refer to the internal names used by all assets within the game files. They can be referenced when executing console commands, editing savegames or creating custom events or starting systems.

## Celestial bodies

| Celestial body (habitable) | ID |
|---|---|
| Alpine | pc_alpine |
| Arctic | pc_arctic |
| Arid | pc_arid |
| Continental | pc_continental |
| Desert | pc_desert |
| Ocean | pc_ocean |
| Savannah | pc_savannah |
| Tropical | pc_tropical |
| Tundra | pc_tundra |
| Tomb | pc_nuked |
| Gaia | pc_gaia |
| Relic | pc_relic |
| Ecumenopolis (always arthropoid appearance) | pc_city |
| Hive | pc_hive |
| Machine | pc_machine |
| Nanite | pc_nanotech |
| Orbital Habitat (uses the mammalian minor orbital appearance) | pc_habitat |
| Ringworld | pc_ringworld_habitable |
| Shattered Ringworld | pc_shattered_ring_habitable |
| Synaptic Lathe | pc_cosmogenesis_world |

| Celestial body (uninhabitable) | ID |
|---|---|
| AI | pc_ai |
| Asteroid | pc_asteroid |
| Crystalline Asteroid | pc_rare_crystal_asteroid |
| Ice Asteroid | pc_ice_asteroid |
| Barren | pc_barren |
| Barren (Cold) | pc_barren_cold |
| Broken | pc_broken |
| Cracked | pc_egg_cracked |
| Frozen | pc_frozen |
| Gas Giant | pc_gas_giant |
| Molten | pc_molten |
| Shattered (also plays cracking animation) | pc_shattered |
| Shielded | pc_shielded |
| Shrouded | pc_shrouded |
| Toxic | pc_toxic |
| Ringworld (Habitable Damaged) | pc_ringworld_habitable_damaged |
| Ringworld (Seam) | pc_ringworld_seam |
| Ringworld (Seam Damaged) | pc_ringworld_seam_damaged |
| Ringworld (Tech) | pc_ringworld_tech |
| Ringworld (Tech Damaged) | pc_ringworld_tech_damaged |
| Astral Scar | pc_astral_scar |

| Celestial body (stars) | ID |
|---|---|
| Class B Star | pc_b_star |
| Class A Star | pc_a_star |
| Class F Star | pc_f_star |
| Class G Star | pc_g_star |
| Class K Star | pc_k_star |
| Class M Star | pc_m_star |
| Class M Red Giant | pc_m_giant_star |
| Class T Brown Dwarf | pc_t_star |
| Black Hole | pc_black_hole |
| Neutron Star | pc_neutron_star |
| Pulsar | pc_pulsar |
| Viridescent Lightbringer | pc_toxoid_star |
| Astral Scar | pc_rift_star |

## Districts

| District | ID |
|---|---|
| City District | district_city |
| Hive District | district_hive |
| Nexus District | district_nexus |
| Industrial District | district_industrial |
| Generator District | district_generator |
| Mining District | district_mining |
| Agriculture District | district_farming |
| Trade District | district_srw_commercial |
| Coordination District | district_machine_coordination |
| Resort District | district_resort |
| Prison District | district_prison |
| Prison Industrial District | district_prison_industrial |
| Slave Domicile District | district_slave |
| Battle Thrall District | district_battle_thrall |
| Scavenger Site | district_crashed_slaver_ship |

| District (habitat) | ID |
|---|---|
| Habitation District | district_hab_housing |
| Industrial District | district_hab_industrial |
| Zero-G Research District | district_hab_science |
| Reactor District | district_hab_energy |
| Astro-Mining Bay | district_hab_mining |
| Order's Demesne | district_orders_demesne |

| District (arcology) | ID |
|---|---|
| Residential Arcology | district_arcology_housing |
| Foundry Arcology | district_arcology_arms_industry |
| Industrial Arcology | district_arcology_civilian_industry |
| Leisure Arcology | district_arcology_leisure |
| Sanctuary Arcology | district_arcology_organic_housing |
| Administrative Arcology | district_arcology_administrative |
| Ecclesiastical Arcology | district_arcology_religious |

| District (segment) | ID |
|---|---|
| City Segment | district_rw_city |
| Hive Segment | district_rw_hive |
| Nexus Segment | district_rw_nexus |
| Industrial Segment | district_rw_industrial |
| Generator Segment | district_rw_generator |
| Commercial Segment | district_rw_commercial |
| Research Segment | district_rw_science |
| Agricultural Segment | district_rw_farming |

| District (other) | ID |
|---|---|
| Ampliative Speculator | district_cosmogenesis_world_logic |
| Neural Gate | district_cosmogenesis_world_science |

## Orbital deposits

Deposits that require a mining station cannot be added to celestial bodies that have deposits that require a research station and vice versa.

| Orbital deposit | ID | Deposit range |
|---|---|---|
| Energy | d_energy_# | Between 1 and 10 |
| Minerals | d_minerals_# | Between 1 and 10 |
| Food | d_food_# | 3 or 10 |
| Trade Value | d_trade_value_# | Between 1 and 10 |
| Alloys | d_alloys_# | Between 1 and 5, or 10, 25 |
| Exotic Gases | d_exotic_gases_# | Between 1 and 5 |
| Rare Crystals | d_rare_crystals_# | Between 1 and 5 |
| Volatile motes | d_volatile_motes_# | Between 1 and 5 |
| Living Metal | d_living_metal_deposit | none |
| Minor Artifacts | d_artifacts_mining_# | Between 1 and 3 |

| Orbital deposit | ID | Deposit range |
|---|---|---|
| Engineering | d_engineering_# | Between 1 and 10 |
| Physics | d_physics_# | Between 1 and 10 |
| Society | d_society_# | Between 1 and 10, or 15 |
| Dark Matter | d_dark_matter_deposit_# | 1, 2, 3 or 10 |
| Zro | d_zro_deposit_# | Between 1 and 5 |
| Minor Artifacts | d_artifacts_research_# | Between 1 and 3 |
| Astral Threads | d_astral_threads_deposit_# | Between 1 and 3 |
| Unity | d_vast_unity_deposit | none |
| Nanites | d_nanites_deposit | none |

## Planetary features

Example: effect add_deposit = d_underground_generator

| Planetary feature (common) | ID |
|---|---|
| Abandoned Mining Tunnels | d_abandoned_mining_tunnels |
| Ancient Reactor Pits | d_ancient_reactor_pits |
| Arid Highlands | d_arid_highlands |
| Betharian Fields | d_betharian_deposit |
| Black Soil | d_black_soil |
| Boggy Fens | d_boggy_fens |
| Bountiful Plains | d_bountiful_plains |
| Bubbling Swamp | d_bubbling_swamp |
| Buzzing Plains | d_buzzing_plains |
| Central Spire | d_central_spire |
| Crystal Forest | d_crystal_forest |
| Crystal Reef | d_crystal_reef |
| Crystalline Caverns | d_crystalline_caverns |
| Dense Ruins | d_relic_dense_ruins |
| Dust Caverns | d_dust_caverns |
| Dust Desert | d_dust_desert |
| Fair Tundra | d_forgiving_tundra |
| Fertile Lands | d_fertile_lands |
| Frozen Gas Lake | d_frozen_gas_lake |
| Fuming Bog | d_fuming_bog |
| Fungal Caves | d_fungal_caves |
| Fungal Forest | d_fungal_forest |
| Geothermal Vents | d_geothermal_vent |
| Great River | d_great_river |
| Green Hills | d_green_hills |
| Hot Springs | d_hot_springs |
| Immense Solar Array | d_immense_solar_array |
| Industrial Sector | d_industrial_sector |
| Isolated Valley | d_alien_pets_deposit |
| Lichen Fields | d_lichen_fields |
| Lush Jungle | d_lush_jungle |
| Marvelous Oasis | d_marvelous_oasis |
| Metal Boneyards | d_metal_boneyard |
| Mineral Fields | d_mineral_fields |
| Mineral Striations | d_mineral_striations |
| Natural Farmland | d_natural_farmland |
| Nutritious Mudlands | d_nutritious_mudland |
| Ore-Rich Caverns | d_ore_rich_caverns |
| Ore-Veined Cliffs | d_veiny_cliffs |
| Organic Landfills | d_organic_landfill |
| Prosperous Mesa | d_prosperous_mesa |
| Rich Mountain | d_rich_mountain |
| Rugged Woods | d_rugged_woods |
| Rushing Waterfall | d_rushing_waterfalls |
| Searing Desert | d_searing_desert |
| Submerged Ore Veins | d_submerged_ore_veins |
| Teeming Reef | d_teeming_reef |
| Tempestuous Mountain | d_tempestous_mountain |
| Tropical Island | d_tropical_island |
| Underwater Vents | d_underwater_vent |
| Alloy Deposit | d_hab_alloy_1 |
| Dark Matter Deposit | d_hab_dark_matter_1 |
| Exotic Gas Deposit | d_hab_gas_1 |
| Living Metal Deposit | d_hab_living_metal_1 |
| Rare Crystal Deposit | d_hab_crystal_1 |
| Volatile Mote Deposit | d_hab_mote_1 |
| Zro Deposit | d_hab_zro_1 |
| Nanite Deposit | d_hab_nanites_1 |
| Astral Threads Deposit | d_hab_astral_threads_1 |
| Minor Artifacts | d_artifacts_planet_1 |
| Organic Slurry | d_organic_slurry |

| Planetary feature (unique) | ID |
|---|---|
| Abandoned Primitive Homesteads | d_abandoned_primitive_homesteads |
| Alien Safari | d_alien_sanctuary |
| Ancient Battlefield | d_ancient_battlefield |
| Ancient Bombardment Craters | d_ancient_bombardment_craters |
| Ancient Mining Site | d_ancient_mining_site |
| Ancient One | d_ancient_one |
| Ancient Particle Accelerator | d_ancient_particle_accelerator |
| Arcane Device | d_arcane_device |
| Arcane Replicator | d_arcane_replicator |
| Blighted Remembrance | d_toxic_god_blight_upon_the_land_upgraded |
| Blue Lotus Crater | d_crater_bluelotus |
| Blue Lotus Facility | d_bluelotus2 |
| Blue Lotus Prototype | d_bluelotus |
| Blue Lotus Ruin | d_ruin_bluelotus |
| Bogplants | d_bogplants |
| Cave Shroom Veins | d_cave_shroom_veins |
| Compact Virtual Power Plant | d_virtual_power_small |
| Consolidated Resources | d_machine_minerals |
| Crashed Cargo Ship | d_admirals_bickering_crashed_cargo_ship |
| Crashed Slaver Ship | d_crashed_slaver_ship |
| Cryonic Clones Monument | d_cryonic_clones |
| Crystalline Remains | d_crystal_kraken_body |
| Crystallized Ice Field | d_crystalline_glacier |
| Dayside Solar Farm | d_dayside_farm |
| Destroyed Vault | d_ancient_manufactorium_crater |
| Dimensional Manipulation Device | d_dimensional_manipulation_device |
| Electrified Oceans | d_electrified_oceans |
| Enigmatic Robot | d_hab_lonely_bot_deposit |
| Federation Monument | d_federation_hegemony_monument_2 |
| Feeding Dragon | d_landed_dragon |
| Flooded Mounds | d_flooded_mounds |
| Former Relic World | d_former_relic_world |
| Fractal Seed | d_fractal_seed |
| Freeport | d_freeports |
| Fungal Study Zone | d_fungal_study_zone |
| Harvester Fields | d_harvester_fields |
| Hyperfertile Valley | d_hyperfertile_valley |
| Impact Crater | d_impact_crater |
| Incubate Wind Creatures | d_forceful_winds |
| Irradiated Ruins | d_irradiated_ruins |
| Juvenile Nemma | d_house_turtle |
| Loop-Plowed Farm | d_worm_farm |
| Lotus Corrie | d_impossiblecorrie |
| Machine Interface Center | d_machine_care_home |
| Manufactorium Scrapyard | d_ancient_manufactorium_scrapyard |
| Massive Crater | d_lithoid_crater |
| Memorial to the Unshackled | d_crashed_slaver_ship_memorial |
| Metallic Puddles | d_metallic_puddles |
| Microplanet Memorial | d_microplanet_memorial |
| Migrating Forests Reserve | d_migrating_forest_reserve |
| Mountain in the Sky | d_sky_mountain |
| Mutation Vats | d_mutation_vats |
| Mutant Landfill | d_mutant_landfill |
| Myrmeku Power Farms | d_myrmeku_power_farms |
| Nanite Swarm Remains | d_nano_corpses |
| Nanosands | d_nanosands |
| Nemma Mining Operation | d_turtle_miner |
| Numa's Breath | d_numas_breath |
| Odd Factory | d_odd_factory |
| Operational Manufactorium | d_ancient_manufactorium_working |
| Order's X-Calibrator | d_knights_calibrator |
| Party Fever | d_disco_planet |
| Pelagic Bounty | d_toxic_god_envenomed_seas_upgraded |
| Portal Research Area | d_portal_research_zone |
| Processing Pens | d_processing_pens |
| Progenitor Nest | d_progenitor |
| Project Cornucopia | d_project_cornucopia |
| Prospectorium Strip Mine | d_prospectorium_strip_mine |
| Prototype Virtual Power Plant | d_virtual_power_tiny |
| Radiotrophic Preserve | d_radiotrophic_preserve |
| Reclaimed Pestilence | d_toxic_god_pestilential_wasteland_upgraded |
| Remote Holdings | d_landgrab_foreign_holdings |
| Rich Seabed | d_mineral_seabed |
| Rockworm Hive | d_rockworm_hive |
| Savage Wildlands | d_savage_wildlands |
| Sentinels | d_sentinels |
| Sentinels Metal | d_sentinels_metal |
| Shattered Crystalline Remains | d_crystal_kraken_body_bombed |
| Shrouded Crater | d_eater_deposit |
| Spiral-Hewn Mine | d_worm_mine |
| Space-Time Anomaly | d_space_time_anomaly |
| Spore Vents | d_spore_vents |
| Stasis Prison | d_stasis_prison |
| Structured Integration | d_prisoner_intergration |
| Subdued Swarms | d_toxic_god_deitys_swarms_upgraded |
| Subterranean Contact Zone | d_underground_contact_zone |
| Subterranean Farming Caverns | d_underground_farm |
| Subterranean Generator Areas | d_underground_generator |
| Subterranean Mining Sites | d_underground_mine |
| Toxins Most Deadly | d_toxic_god_pools_most_venemous_upgraded |
| Treasure Vault | d_treasure_planet |
| Tree of Life | d_tree_of_life_home |
| Tree of Life Sapling | d_tree_of_life_colony |
| Toy Factory Complex | d_toy_factory_complex |
| Underground Vault | d_underground_vault |
| Virtual Power Plant | d_virtual_power_medium |
| Weapon Extraction Facility | d_weapon_extraction_facility |
| Wetware Computer | d_wetware_computer |
| Zone A | d_the_zone |

| Planetary feature (special planets) | ID |
|---|---|
| BosWash Metropolitan Axis | d_boswash_metropolitan_axis |
| Delhi Sprawl | d_delhi_sprawl |
| Great Albertan Crater | d_great_albertan_crater |
| Mauritanian Security Zone | d_mauritanian_security_zone |
| Mesopotamian Urban Corridor | d_mesopotamian_urban_corridor |
| Pacific Algae Tracts | d_pacific_algae_tracts |
| Pearl River Agglomerate | d_pearl_river_agglomerate |
| Saharan Irrigation Project | d_saharan_irrigation_project |
| Scandinavian Reclamation Sector | d_scandinavian_reclamation_sector |
| Ancient Sunken City | d_polaris_city |
| Valley of Zanaam | d_valley_of_zanaam |
| Irradiated Valley | d_irradiated_valley |
| Junk Canals | d_junk_canals |
| Junk Hollows | d_junk_hollows |
| Junk Wastes | d_junk_wastes |
| Aggressive Wildlife | d_hostile_fauna |
| Ancient Facilities | d_ancient_facilities |
| Crashed Ships | d_space_ship_graveyard |
| Fallen Shipyard | d_fallen_orbital_shipyard |
| Promenade | d_star_mall_promenade |
| Scarred Land | d_pulsar_scarred |
| Volcanic Activity | d_volcanic_active_planet |

## Civics

Regular civics are safer to add via a combination of free_government and effect add_modifier = { modifier = fotd_triumviri multiplier = 999 } .

| Civic (regular) | ID |
|---|---|
| Divine Sovereign | civic_psionic_sovereign |
| Corporate Sovereign | civic_galactic_sovereign_megacorp |
| Galactic Sovereign | civic_galactic_sovereign |

## Resolutions

Can be passed with the effect = { pass_resolution = resolution ID } command combination. To repeal the resolution, add _repeal to the resolution ID.

Example: effect = { pass_resolution = resolution_galacticreforms_form_council }

| Resolution | ID |
|---|---|
| Galactic Commerce resolutions | |
| Buzzword Standardization (1) | resolution_commerce_buzzword_standardization |
| Leveraged Privateering (2) | resolution_commerce_leveraged_privateering |
| Underdeveloped System Utilization (3) | resolution_commerce_underdeveloped_system_utilization |
| Holistic Asset Coordination (4) | resolution_commerce_holistic_asset_coordination |
| Profit Maximization Engines (5) | resolution_commerce_profit_maximization_engines |
| Industrial Development resolutions | |
| Regulatory Facilitation (1) | resolution_industry_regulatory_facilitation |
| Collective Waste Management (2) | resolution_industry_collective_waste_management |
| Building a Better Tomorrow (3) | resolution_industry_building_a_better_tomorrow |
| Environmental Ordinance Waivers (4) | resolution_industry_environmental_ordinance_waivers |
| Project Cornucopia (5) | resolution_industry_project_cornucopia |
| Economic Sanctions resolutions | |
| Minor Economic Sanctions (1) | resolution_sanctions_economic_1 |
| Moderate Economic Sanctions (2) | resolution_sanctions_economic_2 |
| Major Economic Sanctions (3) | resolution_sanctions_economic_3 |
| The Greater Good resolutions | |
| Charter of Worker's Rights (1) | resolution_greatergood_workers_rights |
| Five Year Plans (2) | resolution_greatergood_five_year_plans |
| Greater Than Ourselves (3) | resolution_greatergood_greater_than_ourselves |
| Balance in the Middle (4) | resolution_greatergood_balance_in_the_middle |
| Universal Prosperity Mandate (5) | resolution_greatergood_universal_prosperity_mandate |
| Intergalactic Directives resolutions | |
| Regulated Growth (1) | resolution_intergalacticdirective_regulated_growth |
| Ensured Sovereignty (2) | resolution_intergalacticdirective_ensured_sovereignty |
| A Voice for All (3) | resolution_intergalacticdirective_a_voice_for_all |
| Administrative Sanctions resolutions | |
| Minor Administrative Sanctions (1) | resolution_sanctions_administrative_1 |
| Moderate Administrative Sanctions (2) | resolution_sanctions_administrative_2 |
| Major Administrative Sanctions (3) | resolution_sanctions_administrative_3 |
| Ecological Protection resolutions | |
| Pangalactic Recycling Initiatives (1) | resolution_ecology_recycling_initiatives |
| Natural Sanctuaries (2) | resolution_ecology_natural_sanctuaries |
| Integrated Gardens (3) | resolution_ecology_integrated_gardens |
| Environmental Control Board (4) | resolution_ecology_environmental_control_board |
| The Paradise Initiative (5) | resolution_ecology_paradise_initiative |
| Unchained Knowledge resolutions | |
| Cooperative Research Channels (1) | resolution_galacticstudies_cooperative_research_channels |
| Astral Studies Network (2) | resolution_galacticstudies_astral_studies_network |
| Advanced Xenostudies (3) | resolution_galacticstudies_advanced_xenostudies |
| Ethical Guideline Refactoring (4) | resolution_galacticstudies_ethical_guideline_refactoring |
| Extradimensional Experimentation (5) | resolution_galacticstudies_extradimensional_experimentation |
| Divinity of Life resolutions | |
| Comfort the Fallen (1) | resolution_divinity_comfort_the_fallen |
| Tithe of the Soulless (2) | resolution_divinity_tithe_on_the_soulless |
| Right to Work (3) | resolution_divinity_right_to_work |
| Silence the Soulless (4) | resolution_divinity_silence_the_soulless |
| A Defined Purpose (5) | resolution_divinity_a_defined_purpose |
| Space Weather Exploitation resolutions | |
| Storm Knowledge Sharing (1) | resolution_cosmic_storms_shared_knowledge |
| Storm Surveying Initiative (2) | resolution_cosmic_storms_protection_initiative |
| Galactic Storm Management (3) | resolution_cosmic_storms_galactic_management |
| Storm Utilization Protocols (4) | resolution_cosmic_storms_utilization_protocols |
| Storm Manipulation Mandate (5) | resolution_cosmic_storms_manipulation_mandate |
| Storm Environmentalists resolutions | |
| Advanced Storm Studies (1) | resolution_cosmic_storms_advanced_storm_studies |
| Galactic Emergency Relief (2) | resolution_cosmic_storms_galactic_emergency_relief |
| Storm Movement Mandate (3) | resolution_cosmic_storms_storm_encouragement_mandate |
| Storm Manipulation Controls (4) | resolution_cosmic_storms_control_restrictions |
| Storm Preservation initiative (5) | resolution_cosmic_storms_preservation_initiative |
| Research Sanctions resolutions | |
| Minor Research Sanctions (1) | resolution_sanctions_tech_1 |
| Moderate Research Sanctions (2) | resolution_sanctions_tech_2 |
| Major Research Sanctions (3) | resolution_sanctions_tech_3 |
| Mutual Defense resolutions | |
| The Readied Shield (1) | resolution_mutualdefense_the_readied_shield |
| Military Readiness Act (2) | resolution_mutualdefense_military_readiness_act |
| The Enemy of My Enemy (3) | resolution_mutualdefense_enemy_of_my_enemy |
| Castigation Proclamation (4) | resolution_mutualdefense_castigation_proclamation |
| Renegade Containment Doctrine (5) | resolution_mutualdefense_renegade_containment |
| Rules of War resolutions | |
| Guardian Angels Act (1) | resolution_rulesofwar_guardian_angels |
| Reverence for Life (2) | resolution_rulesofwar_reverence_for_life |
| Independent Tribunals (3) | resolution_rulesofwar_independent_tribunals |
| Last Resort Doctrine (4) | resolution_rulesofwar_last_resort_doctrine |
| Demobilization Initiative (1) | resolution_rulesofwar_demobilization_initiative |
| Military Sanctions resolutions | |
| Minor Military Sanctions (1) | resolution_sanctions_military_1 |
| Moderate Military Sanctions (2) | resolution_sanctions_military_2 |
| Major Military Sanctions (3) | resolution_sanctions_military_3 |
| Defense Privatization resolutions | |
| Security Contractors (1) | resolution_defenseprivatization_defense_contracts |
| High Consequence Protection (2) | resolution_defenseprivatization_private_support_troops |
| Neutral Defenders (3) | resolution_defenseprivatization_condottieri |
| Galactic Risk Management (4) | resolution_defenseprivatization_security_business |
| Corporate Peacekeeping (5) | resolution_defenseprivatization_corporate_warlords |

| Resolution | ID |
|---|---|
| Space Fauna resolutions | |
| Tiyanki Pest Control | resolution_tiyanki_pest_control |
| Tiyanki Conservation Act | resolution_tiyanki_conservation_act |
| Space Amoeba Protection Act | resolution_amoeba_conservation_act |
| Cutholoid Eradication | resolution_cutholoid_eradication |
| Voidworm Eradication | resolution_voidworm_eradication |
| Galactic Market resolutions | |
| Ban Organic Slave Trade | resolution_galactic_market_ban_sentient_organic_slave_trade |
| Ban Sentient Slave Trade | resolution_galactic_market_ban_sentient_slave_trade |
| Pre-FTL Stance resolutions | |
| Equal Standing Act | resolution_pre_ftl_stances_equal_standing |
| Non-Interference Act | resolution_pre_ftl_stances_non_interference |
| Exploitation Act | resolution_pre_ftl_stances_exploitation |
| Galactic Priority resolutions | |
| Focus: Form the Galactic Market | resolution_galactic_market_form |
| Focus: The Contingency | resolution_galactic_focus_crisis_contingency |
| Focus: The Prethoryn Scourge | resolution_galactic_focus_crisis_prethoryn |
| Focus: The Unbidden | resolution_galactic_focus_crisis_unbidden |
| Focus: The Great Khan | resolution_galactic_focus_crisis_greatkhan |
| Focus: The Gray Tempest | resolution_galactic_focus_crisis_nanites |
| Focus: Denounce Both Awakened Empires | resolution_galactic_focus_war_in_heaven_denounce_both |
| Galactic Reforms resolutions | |
| Form Galactic Council | resolution_galacticreforms_form_council |
| Abolish Galactic Council | resolution_galacticreforms_abolish_council |
| Change Council Size: 1 | resolution_galacticreforms_council_size_1 |
| Change Council Size: 2 | resolution_galacticreforms_council_size_2 |
| Change Council Size: 3 | resolution_galacticreforms_council_size_3 |
| Change Council Size: 4 | resolution_galacticreforms_council_size_4 |
| Change Council Size: 5 | resolution_galacticreforms_council_size_5 |
| Enable Council Denouncement Power | resolution_galacticreforms_enable_council_denouncement |
| Enable Council Veto Power | resolution_galacticreforms_enable_council_veto |
| Remove Council Denouncement Power | resolution_galacticreforms_disable_council_denouncement |
| Remove Council Veto Power | resolution_galacticreforms_disable_council_veto |
| By Election | resolution_emperor_by_election |
| By Appointment | resolution_emperor_by_appointment |
| By Trial of Advancement | resolution_emperor_trial_of_advancement |
| Politics Traditions | |
| Champions of the Community | resolution_community_champions |
| Development Aides | resolution_development_aides |
| Galactic Threats Committee | resolution_galactic_threats_committee |
| Term Limits resolutions | |
| Extend Custodianship | resolution_custodian_extend_custodianship |
| Remove Custodianship Term Limit | resolution_custodian_perpetual_custodianship |
| End Custodianship | resolution_custodian_end_custodianship |
| Custodian Reforms resolutions | |
| Galactic Mobilization | resolution_custodian_galactic_mobilization |
| Introduce Galactic Standard | resolution_custodian_galactic_standard |
| Anti-Piracy Initiative | resolution_custodian_anti_piracy |
| A United Front | resolution_custodian_united_front |
| Proclaim the Galactic Imperium | resolution_custodian_form_empire |
| Galactic Institutions resolutions | |
| Galactic Defense Force | resolution_custodian_gdf |
| GDF Expansion | resolution_custodian_expand_gdf |
| Disband the GDF | resolution_custodian_disband_gdf |
| Interstellar Navigation Agency | resolution_custodian_ina |
| Disband the Interstellar Navigation Agency | resolution_custodian_disband_ina |
| Galactic Trade Organization | resolution_custodian_gto |
| Disband the Galactic Trade Organization | resolution_custodian_disband_gto |
| GALPOL | resolution_custodian_galpol |
| Disband the GALPOL | resolution_custodian_disband_galpol |
| Imperial Reforms resolutions | |
| Pax Galactica | resolution_emperor_pax_galactica |
| Repeal Pax Galactica | resolution_emperor_repeal_pax_galactica |
| Imperial Institutions resolutions | |
| Imperial Legions | resolution_emperor_imperial_legions |
| Imperial Security Directorate | resolution_emperor_isd |

## Species traits

| Trait | ID |
|---|---|
| Adaptive | trait_adaptive |
| Agrarian | trait_agrarian |
| Aquatic | trait_aquatic |
| Charismatic | trait_charismatic |
| Communal | trait_communal |
| Conformists | trait_conformists |
| Conservationist | trait_conservational |
| Docile | trait_docile |
| Enduring | trait_enduring |
| Existential Iteroparity | trait_humanoid_existential_iteroparity |
| Incubators | trait_incubator |
| Industrious | trait_industrious |
| Ingenious | trait_ingenious |
| Inorganic Breath | trait_inorganic_breath |
| Intelligent | trait_intelligent |
| Natural Engineers | trait_natural_engineers |
| Natural Physicists | trait_natural_physicists |
| Natural Sociologists | trait_natural_sociologists |
| Nomadic | trait_nomadic |
| Noxious | trait_noxious |
| Quick Learners | trait_quick_learners |
| Rapid Breeders | trait_rapid_breeders |
| Resilient | trait_resilient |
| Strong | trait_strong |
| Talented | trait_talented |
| Thrifty | trait_thrifty |
| Traditional | trait_traditional |
| Extremely Adaptive | trait_extremely_adaptive |
| Venerable | trait_venerable |
| Very Strong | trait_very_strong |
| Decadent | trait_decadent |
| Deviants | trait_deviants |
| Fleeting | trait_fleeting |
| Fleeting (Lithoid) | trait_fleeting_lithoid |
| Jinxed | trait_humanoid_jinxed |
| Nonadaptive | trait_nonadaptive |
| Psychological Infertility | trait_humanoid_psychological_infertility |
| Quarrelsome | trait_quarrelsome |
| Repugnant | trait_repugnant |
| Slow Breeders | trait_slow_breeders |
| Slow Learners | trait_slow_learners |
| Sedentary | trait_sedentary |
| Solitary | trait_solitary |
| Unruly | trait_unruly |
| Wasteful | trait_wasteful |
| Weak | trait_weak |

| Trait | ID |
|---|---|
| Mechanical | trait_mechanical |
| Machine | trait_machine_unit |
| Domestic Protocols | trait_robot_domestic_protocols |
| Double-Jointed | trait_robot_double_jointed |
| Durable | trait_robot_durable |
| Efficient Processors | trait_robot_efficient_processors |
| Emotion Emulators | trait_robot_emotion_emulators |
| Enhanced Memory | trait_robot_enhanced_memory |
| Harvesters | trait_robot_harvesters |
| Learning Algorithms | trait_robot_learning_algorithms |
| Logic Engines | trait_robot_logic_engines |
| Loyalty Circuits | trait_robot_loyalty_circuits |
| Mass-Produced | trait_robot_mass_produced |
| Power Drills | trait_robot_power_drills |
| Propaganda Machines | trait_robot_propaganda_machines |
| Recycled | trait_robot_recycled |
| Streamlined Protocols | trait_robot_streamlined_protocols |
| Superconductive | trait_robot_superconductive |
| Trading Algorithms | trait_robot_trading_algorithms |
| Bulky | trait_robot_bulky |
| Custom-Made | trait_robot_custom_made |
| High Bandwidth | trait_robot_high_bandwidth |
| High Maintenance | trait_robot_high_maintenance |
| Luxurious | trait_robot_luxurious |
| Uncanny | trait_robot_uncanny |
| Repurposed Hardware | trait_robot_repurposed_hardware |
| Neural Limiters | trait_cyborg_neural_limiters |
| Power Intensive | trait_cyborg_power_intensive |

| Trait | ID |
|---|---|
| Arid Preference | trait_pc_arid_preference |
| Desert Preference | trait_pc_desert_preference |
| Savannah Preference | trait_pc_savannah_preference |
| Continental Preference | trait_pc_continental_preference |
| Ocean Preference | trait_pc_ocean_preference |
| Tropical Preference | trait_pc_tropical_preference |
| Alpine Preference | trait_pc_alpine_preference |
| Arctic Preference | trait_pc_arctic_preference |
| Tundra Preference | trait_pc_tundra_preference |
| Tomb World Preference | trait_pc_nuked_preference |
| Gaia World Preference | trait_pc_gaia_preference |
| Gaia World Preference | trait_pc_gaia_preference_terraforming |
| Ring World Preference | trait_pc_ringworld_habitable_preference |
| Habitat Preference | trait_pc_habitat_preference |
| Hive World Preference | trait_pc_hive_preference |
| Machine World Preference | trait_pc_machine_preference |
| Ecumenopolis Preference | trait_pc_city_preference |
| Relic World Preference | trait_pc_relic_preference |

| Trait | ID |
|---|---|
| Hive-Minded | trait_hive_mind |
| Lithoid | trait_lithoid |
| Species class traits | |
| Budding | trait_plantoid_budding |
| Invasive Species | trait_invasive |
| Phototrophic | trait_plantoid_phototrophic |
| Radiotrophic | trait_plantoid_radiotrophic |
| Crystallization | trait_lithoid_budding |
| Gaseous Byproducts | trait_lithoid_gaseous_byproducts |
| Scintillating Skin | trait_lithoid_scintillating |
| Volatile Excretions | trait_lithoid_volatile_excretions |
| Event traits | |
| Bloomed | trait_plantoid_bloomed |
| Bioadaptability | trait_bioadaptability |
| Limited Regeneration | trait_limited_regeneration |
| Social Pheromones | trait_social_pheromones |
| Brain Slug Host | trait_brainslug |
| Plasmic | trait_plasmic |
| Somewhat Uplifted (Enigmatic Cache) | trait_enigmatic_intelligence_poor |
| Uplifted (Enigmatic Cache) | trait_enigmatic_intelligence |
| Zombie | trait_zombie |
| Pre-sapient traits | |
| Conservative | trait_presapient_conservative |
| Earthbound | trait_presapient_earthbound |
| Irradiated | trait_presapient_irradiated |
| Natural Intellectuals | trait_presapient_natural_intellectuals |
| Proles | trait_presapient_proles |
| Starborn | trait_presapient_starborn |
| Docile Livestock | trait_presapient_docile_livestock |
| Unique traits | |
| Default Nivlac | trait_nivlac |
| Numistic Administration | trait_nuumismatic_administration |
| Not of this World | trait_notofthisworld |
| Extradimensional | trait_exd |

| Trait | ID |
|---|---|
| Cave Dweller | trait_cave_dweller |
| Clone Soldier | trait_clone_soldier_infertile |
| Clone Soldier Ascendant | trait_clone_soldier_infertile_full_potential |
| Clone Soldier Descendant | trait_clone_soldier_fertile |
| Serviles | trait_syncretic_proles |
| Necrophage | trait_necrophage |
| Perfected Genes | trait_perfected_genes |
| Stargazer | trait_stargazer |
| Survivor | trait_survivor |
| Void Dweller | trait_void_dweller_1 |
| Overtuned traits | |
| Augmented Intelligence | trait_artificial_intelligence |
| Crafted Smiles | trait_crafted_smiles |
| Dedicated Miner | trait_crack_miner |
| Elevated Synapses | trait_elevated_synapses |
| Excessive Endurance | trait_excessive_endurance |
| Expressed Tradition | trait_expressed_tradition |
| Farm Appendages | trait_farm_hands |
| Gene Mentorship | trait_gene_mentorship |
| Juiced Power | trait_juiced_power |
| Low Maintenance | trait_low_maintenance |
| Pre-Planned Growth | trait_preplanned_growth |
| Spliced Adaptability | trait_spliced_adaptability |
| Technical Talent | trait_technical_skill |

| Trait | ID |
|---|---|
| Latent Psionic | trait_latent_psionic |
| Psionic | trait_psionic |
| Cybernetic | trait_cybernetic |
| Exotic Metabolism | trait_exotic_metabolism |
| Delicious | trait_delicious |
| Drake-Scaled | trait_drake_scaled |
| Erudite | trait_erudite |
| Felsic | trait_felsic |
| Fertile | trait_fertile |
| Natural Machinist | trait_natural_machinist |
| Nerve Stapled | trait_nerve_stapled |
| Polymelic | trait_tiyanki |
| Robust | trait_robust |
| Vat-Grown | trait_vat_grown |
| Voidling | trait_voidling |

## Leader Traits

| Self-affecting traits (max level) | |
|---|---|
| Adaptable | leader_trait_adaptable |
| Resilient | leader_trait_resillient |
| Eager | leader_trait_eager |
| Gifted (II) | leader_trait_gifted |
| Emotional Support Pet | leader_trait_emotional_support_pet |
| Backup Clone | leader_trait_has_backup_clone |
| Whispering Mind (III) | leader_trait_whispering_mind |
| Positive governor traits | |
| Unifier | leader_trait_bureaucrat |
| Environmental Engineer | leader_trait_environmental_engineer |
| Architectural Interest | leader_trait_architectural_interest |
| Agrarian Upbringing | leader_trait_agrarian_upbringing |
| Righteous (II) | leader_trait_righteous |
| Home planet traits | |
| Celebrity (II) | leader_trait_venerated |
| Energy Mogul (II) | leader_trait_capitalist |
| Private Mines (II) | leader_trait_private_mines |
| Scrapper (II) | leader_trait_scrapper |
| Homesteader (II) | leader_trait_homesteader |
| Entrepreneur (II) | leader_trait_entrepreneur |
| Positive Councilor Traits | |
| Charisma (II) | leader_trait_charismatic |
| Eye for Talent (II) | leader_trait_eye_for_talent |
| Logistic Understanding (II) | leader_trait_logistic_understanding |
| Mining Rush (II) | leader_trait_industrialist |
| Politician | leader_trait_politician |
| Champion of the People (II) | leader_trait_champion_of_the_people |
| Feedback Loop (II) | |
| Army Veteran | leader_trait_army_veteran |
| Retired Fleet Officer | leader_trait_retired_fleet_officer |
| Authority Traits | |
| Imperial Ruler | trait_imperial_heir |
| Imperial Heir | |
| Hive Mind | |
| Machine Interlligence | |
| Apex Predator | |
| Veteran Traits | |
| Adventurous Spirit (II) | leader_trait_adventurous_spirit |
| Scout (II) | leader_trait_scout |
| Geology Expert (III) | leader_trait_space_miner |
| Manufacturer (III) | leader_trait_manufacturer |
| Naturalist (III) | leader_trait_naturalist |
| Assembler (III) | leader_trait_assembler |
| Cartographer (III) | |
| Destiny Traits | |
| Xeno-Mediator | |
| Bot Lord | |
| Shroud Preacher | |
| Master Bureaucrat | leader_trait_master_bureaucrat |
| Perceptive Mentor | leader_trait_educator |
| Peacekeeper | leader_trait_peacekeeper |
| Special traits | |
| Luminary Bloodline | |
| Increased Lifespan | |
| Robotic Surrogate | leader_trait_robotic_surrogate |
| Second Chance | |
| Imperial Bloodline | |
| Genetic Purist | leader_trait_genetic_purist |
| Neurological Firewall | |
| Multiclass traits | |
| Brain Slug Host | leader_trait_brainslug |
| Ancient Knowledge | |
| Ancestral Inheritance | leader_trait_legendary_ancestors_knowledge |
| Cunning | |
| Storm Rider | leader_trait_storm_rider_official leader_trait_storm_rider_commander leader_trait_storm_rider_scientist |
| Shroud Warped | |
| Species leader traits | |
| Limited Cyborg | leader_trait_limited_cyborg |
| Cyborg | leader_trait_cyborg |
| Ritualistic Implants | leader_trait_ritualistic_implants_cyborg |
| Erudition | |
| Psychic | leader_trait_psychic |
| Synth | |
| Virtual Leader | leader_trait_virtual |

## Ships

Fallen empire, other crisis and other guardian ships spawn as a box due to their appearance being tied to their graphical culture. Colony ships can be spawned with the console but will not work due to not having a species inside.

| Ship ID (base) | Ship |
|---|---|
| NAME_Constructor | Construction Ship |
| NAME_Prototype | Science Ship |
| NAME_Dagger | Corvette |
| NAME_Ravager | Destroyer |
| NAME_Derelict | Cruiser |
| NAME_Spearhead | Battleship |
| NAME_Seeker | Alien corvette |
| NAME_Starfang | Alien destroyer |
| NAME_Sword | Alien cruiser |
| NAME_Righteous | Cultist cruiser |
| NAME_Divine_Glory | Cultist battleship |
| NAME_Corsair | Pirate destroyer |
| NAME_Black_Earl | Pirate cruiser |
| NAME_Pirate_Galleon | Pirate battleship |
| NAME_Ancient_Mining_Drone | Ancient Mining Drone miner |
| NAME_Ancient_Combat_Drone | Ancient Mining Drone corvette |
| NAME_Ancient_Destroyer | Ancient Mining Drone destroyer |
| NAME_Cracked_Crystalline_Shard | Crystalline entity |
| NAME_Wraith | Unbidden destroyer |
| NAME_Phantom | Unbidden cruiser |
| NAME_Revenant | Unbidden battleship |
| NAME_Predator | Aberrant destroyer |
| NAME_Assassin | Aberrant cruiser |
| NAME_Huntress | Aberrant battleship |
| NAME_Obliterator | Vehement destroyer |
| NAME_Annihilator | Vehement cruiser |
| NAME_Eradicator | Vehement battleship |
| NAME_Protector | Nomad destroyer |
| NAME_Nomad_Cruiser | Nomad cruiser |
| NAME_Cloud_Entity | Void Cloud |
| NAME_Small_Space_Organism_Zebra | Space Amoeba |
| NAME_Great_Space_Organism | Space Amoeba Mother |
| NAME_Reanimated_Great_Space_Organism | Space Amoeba Mother reanimated |
| NAME_Tiyanki_Hatchling | Tiyanki Hatchling |
| NAME_Tiyanki_Calf | Tiyanki Calf |
| NAME_Tiyanki_Bull | Tiyanki Bull |
| NAME_Tiyanki_Cow | Tiyanki Cow |
| NAME_Tiyanki_Ox | Tiyanki Ox |
| NAME_DS47 | Space Probe |
| NAME_Dimensional_Horror | Dimensional Horror |
| NAME_Cleanser | Neutron Sweep colossus |
| NAME_Enforcer | Global Pacifier colossus |
| NAME_Reaper | World Cracker colossus |

| Ship ID (DLC) | Ship |
|---|---|
| NAME_Grand_Dragon | Ether Drake |
| NAME_Reanimated_Grand_Dragon | Ether Drake reanimated |
| NAME_Stellarite | Stellar Devourer |
| NAME_Spectral_Wraith_450THz | Red Spectral Wraith |
| NAME_Spectral_Wraith_520THz | Yellow Spectral Wraith |
| NAME_Spectral_Wraith_650THz | Blue Spectral Wraith |
| NAME_Shroud_Avatar | Blue Shroud Avatar |
| NAME_Corrupted_Avatar | Red Shroud Avatar |
| NAME_Adopted_Amoeba_Centenarian | Space Amoeba Centenarian |
| NAME_Reanimated_Adopted_Amoeba_Centenarian | Space Amoeba Centenarian reanimated |
| NAME_Persistent | Vol ship |
| NAME_AH4B | Battleship AH4B |
| NAME_Progenitor | Tiyanki Matriarch |
| NAME_Reanimated_Progenitor | Tiyanki Matriarch reanimated |
| NAME_Reclaimer | Scavenger Bot |
| NAME_Voidspawn | Voidspawn |
| NAME_Reanimated_Voidspawn | Voidspawn reanimated |
| NAME_Nanite_Dragon | L-Drake |
| NAME_Nanite_Interdictor | Nanite cruiser |
| NAME_Nanite_Mothership | Nanite titan |
| NAME_Yojimbo | Caravaneer destroyer |
| NAME_Gunslinger | Caravaneer cruiser |
| NAME_Lessenger | Alien corvette |
| NAME_Herald | Titan |
| NAME_Shard_Dragon | Shard |
| NAME_Crisis_Star_Eater | Star-Eater |
| NAME_Sky_Dragon | Sky Dragon |
| NAME_Reanimated_Sky_Dragon | Sky Dragon reanimated |
| NAME_Bulwark_Battlewright | Battlewright construction ship |
| NAME_Scholarium_Arctrellis | Arctrellis science ship |
| NAME_Venomous_Deity | Toxic God |
| NAME_FirstClaw | The Talon |
| NAME_Temple_of_Whispers | Murmuring Monolith |
| NAME_Azaryn_Dome | Astrocreator Azaryn's science ship |
| NAME_Formless_Cruiser | Formless cruiser |
| NAME_Synth_Queen_Titan | Cetana |
| NAME_Synth_Queen_Royal_Guard | Synthetic Queen defender |
| NAME_Cutholoids_Hatchling | Cutholoid Hatchling |
| NAME_Cutholoids_Juvenile | Cutholoid Juvenile |
| NAME_Cutholoids | Cutholoid |
| NAME_Voidworms_Nymph | Voidworm Nymph |
| NAME_Voidworms_Juvenile | Voidworm Juvenile |
| NAME_Voidworms_Mature | Voidworm Adult |
| NAME_Voidworms_Troika | Voidworm Troika |
| NAME_HIVE_FE_Small_Weaver_War | Juvenile Weaver |
| NAME_HIVE_FE_Large_Weaver_Control | Elder Weaver |
| NAME_HIVE_FE_Large_Mauler_Swarm | Elder Mauler |
| NAME_HIVE_FE_Large_Harbinger | Elder Harbinger |
| NAME_HIVE_FE_Large_Stinger | Elder Stinger |
| NAME_Behemoth_01 | Class I Behemoth |
| NAME_Behemoth_02 | Class II Behemoth |
| NAME_Behemoth_03 | Class III Behemoth |
| NAME_Behemoth_04 | Class IV Behemoth |
| NAME_Boss_Voidspawn | Elder Voidspawn |
| NAME_Ember_Cruiser | Ember Cruiser |
| NAME_Ember_Battleship | Ember Battleship |
| NAME_Entropy_Conduit | Conduit |

| Station ID | Station |
|---|---|
| NAME_Crystal_Nidus | Crystal Nidus |
| NAME_Drone_Home_Base | Home Base Ore Grinder |
| NAME_AI_Final_Core | Contingency Core |
| NAME_Sentry | Sentinel station |
| NAME_Curator_Enclave_Station | Curator enclave station |
| NAME_Shroudwalker_Enclave_Station | Shroud-Touched Coven enclave |
| NAME_Artist_Enclave_Station | Artisan enclave station |
| NAME_Trader_Enclave_Station | Trader enclave |
| NAME_Hive_Asteroid | Asteroid Hive |
| NAME_Void_Dwelling | Marauder Void Dwelling |
| NAME_Nanite_Factory | Nanite starbase |
| NAME_Tradestation_Tungle | Caravaneer Citadel |
| NAME_Mercenary_Enclave_Station | Mercenary enclave |
| NAME_Salvager_Enclave_Station | Salvager enclave |
| NAME_Queens_Eye | Synthetic Queen station |
| NAME_Voidworms_Starbase | Voidworm nest |
| NAME_HIVE_FE_Platform | Fallen empire defense platform |
| NAME_HIVE_Citadel_1 | Deep Space Citadel |
| NAME_Starfire_Cannon | Starfire Cannon |
| NAME_Mindwarden_Enclave_Station | Mindwarden Enclave |

## Buildings

Overlord holdings will not function if added. If multiple planet unique buildings are added they will be removed at the start of next month.

| Building (repeatable) | ID |
|---|---|
| Stronghold | building_stronghold |
| Fortress | building_fortress |
| Luxury Residences | building_luxury_residence |
| Paradise Dome | building_paradise_dome |
| Communal Housing | building_communal_housing |
| Utopian Communal Housing | building_communal_housing_large |
| Hive Warren | building_hive_warren |
| Expanded Warren | building_expanded_warren |
| Drone Storage | building_drone_storage |
| Upgraded Drone Storage | building_drone_megastorage |
| Slave Huts | building_slave_huts |
| Crude Huts | building_crude_huts |
| Overseer Residences | building_overseer_homes |
| Organic Sanctuary | building_organic_sanctuary |
| Organic Paradise | building_organic_paradise |
| Temple | building_temple |
| Holotemple | building_holotemple |
| Sacred Nexus | building_sacred_nexus |
| Sanctuary of Repose | building_galactic_memorial_1 |
| Pillar of Quietus | building_galactic_memorial_2 |
| Galactic Memorial | building_galactic_memorial_3 |
| Sacrificial Temple | building_sacrificial_temple_1 |
| Grim Holotemple | building_sacrificial_temple_2 |
| Temple of Grand Sacrifice | building_sacrificial_temple_3 |
| Synaptic Nodes | building_hive_node |
| Synaptic Clusters | building_hive_cluster |
| Confluence of Thought | building_hive_confluence |
| Research Labs | building_research_lab_1 |
| Research Complexes | building_research_lab_2 |
| Advanced Research Complexes | building_research_lab_3 |
| Administrative Offices | building_bureaucratic_1 |
| Administrative Park | building_bureaucratic_2 |
| Administrative Complex | building_bureaucratic_3 |
| Uplink Node | building_uplink_node |
| Network Junction | building_network_junction |
| System Conflux | building_system_conflux |
| Precinct House | building_precinct_house |
| Hall of Judgement | building_hall_judgment |
| Sentinel Posts | building_sentinel_posts |
| Commercial Zones | building_commercial_zone |
| Commerce Megaplexes | building_commercial_megaplex |
| Holo-Theatres | building_holo_theatres |
| Hyper-Entertainment Forums | building_hyper_entertainment_forum |
| Chemical Plants | building_chemical_plant |
| Exotic Gas Refineries | building_refinery |
| Synthetic Crystal Plants | building_crystal_plant |
| Kha'lanka Crystal Plants | building_crystal_plant_2 |
| Hydroponics Farms | building_hydroponics_farm |
| Resource Silos | building_resource_silo |
| Bio-Reactor | building_bio_reactor |
| Nanite Transmuter | building_nanite_transmuter |
| Crystal Mines | building_crystal_mines |
| Gas Extraction Wells | building_gas_extractors |
| Mote Harvesting Traps | building_mote_harvesters |
| Ancient Clone Vat | building_clone_army_clone_vat |
| Betharian Power Plant | building_betharian_power_plant |
| Alien Zoo | building_xeno_zoo |
| Affluence Center | building_affluence_center |
| Auto-Forge | building_nano_forge |
| Class-4 Singularity | building_class_4_singularity |
| Dimensional Fabricator | building_dimensional_fabricator |
| Nourishment Center | building_nourishment_center |
| Sky Dome | building_fe_dome |
| Master Archive | building_master_archive |

| Building (planet unique) | ID |
|---|---|
| Planetary Shield Generator | building_planetary_shield_generator |
| Military Academy | building_military_academy |
| Dread Encampment | building_dread_encampment |
| Autochthon Monument | building_autochthon_monument |
| Heritage Site | building_heritage_site |
| Hypercomms Forum | building_hypercomms_forum |
| Corporate Culture Site | building_corporate_monument |
| Business Management Nexus | building_corporate_site |
| Synergy Forum | building_corporate_forum |
| Sensorium Site | building_sensorium_1 |
| Sensorium Center | building_sensorium_2 |
| Sensorium Complex | building_sensorium_3 |
| Simulation Site | building_simulation_1 |
| Simulation Center | building_simulation_2 |
| Simulation Complex | building_simulation_3 |
| Alloy Foundries | building_foundry_1 |
| Alloy Mega-Forges | building_foundry_2 |
| Alloy Nano-Plants | building_foundry_3 |
| Civilian Industries | building_factory_1 |
| Civilian Fabricators | building_factory_2 |
| Civilian Repli-Complexes | building_factory_3 |
| Energy Grid | building_energy_grid |
| Energy Nexus | building_energy_nexus |
| Mineral Purification Plants | building_mineral_purification_plant |
| Mineral Purification Hubs | building_mineral_purification_hub |
| Food Processing Facilities | building_food_processing_facility |
| Food Processing Centers | building_food_processing_center |
| Ministry of Production | building_ministry_production |
| Resource Processing Center | building_production_center |
| Research Institute | building_institute |
| Planetary Supercomputer | building_supercomputer |
| Gene Clinic | building_clinic |
| Cyto-Revitalization Center | building_hospital |
| Robot Assembly Plants | building_robot_assembly_plant |
| Machine Assembly Plants | building_machine_assembly_plant |
| Machine Assembly Complex | building_machine_assembly_complex |
| Auto-Curating Vault | building_autocurating_vault |
| Citadel of Faith | building_citadel_of_faith |
| Vault of Acquisitions | building_corporate_vault |
| Alpha Hub | building_alpha_hub |
| Galactic Stock Exchanges | building_galactic_stock_exchange |
| Spawning Pools | building_spawning_pool |
| Offspring Nest | building_offspring_nest |
| Slave Processing Facility | building_slave_processing |
| Noble Estates | building_noble_estates |
| Ranger Lodge | building_ranger_lodge |
| Clone Vats | building_clone_vats |
| Psi Corps | building_psi_corps |
| Chamber of Elevation | building_necrophage_elevation_chamber |
| House of Apotheosis | building_necrophage_house_of_apotheosis |
| Posthumous Employment Center | building_posthumous_employment_center |
| Mutagenic Spa | building_toxic_bath |
| Mutagenic Permutation Pool | building_toxic_bath_hive |
| Hyper Lubrication Basin | building_toxic_bath_machine |
| Coordinated Fulfillment Center | building_coordinated_fulfillment_center_1 |
| Universal Productivity Alignment Facility | building_coordinated_fulfillment_center_2 |
| Gaia Seeders - Phase 1 | building_gaiaseeders_1 |
| Gaia Seeders - Phase 2 | building_gaiaseeders_2 |
| Gaia Seeders - Phase 3 | building_gaiaseeders_3 |
| Embassy Complex | building_embassy |
| Grand Embassy Complex | building_grand_embassy |
| Omega Alignment | building_akx_worm_3 |
| Sanctum of the Composer | building_composer_sanctum |
| Sanctum of the Eater | building_eater_sanctum |
| Sanctum of the Instrument | building_instrument_sanctum |
| Sanctum of the Whisperers | building_whisperers_sanctum |
| Faculty of Archaeostudies | building_archaeostudies_faculty |
| Ministry of Culture | building_artist_patron |
| Numistic Shrine | building_nuumismatic_shrine |
| Waste Reprocessing Center | building_waste_reprocessing_center |
| Order's Keep | building_order_keep |
| Order's Castle | building_order_castle |
| Administrative Hub | building_low_tech_admin_hub |
| Laboratory Complex | building_low_tech_research_lab |
| Great Pyramid | building_great_pyramid |
| Ancient Refinery | building_archaeo_refinery |

| Building (other) | ID | Type |
|---|---|---|
| Reassembled Ship Shelter | building_colony_shelter | capital |
| Planetary Administration | building_capital | capital |
| Planetary Capital | building_major_capital | capital |
| System Capital-Complex | building_system_capital | capital |
| Imperial Palace | building_imperial_capital | capital |
| Deployment Post | building_deployment_post | capital |
| Administrative Array | building_machine_capital | capital |
| Planetary Processor | building_machine_major_capital | capital |
| Primary Nexus | building_machine_system_capital | capital |
| Imperial Center | building_imperial_machine_capital | capital |
| Hive Core | building_hive_capital | capital |
| Hive Nexus | building_hive_major_capital | capital |
| Imperial Complex | building_imperial_hive_capital | capital |
| Habitat Administration | building_hab_capital | capital |
| Habitat Central Control | building_hab_major_capital | capital |
| Resort Administration | building_resort_capital | capital |
| Resort Capital-Complex | building_resort_major_capital | capital |
| Governor's Palace | building_slave_capital | capital |
| Governor's Estates | building_slave_major_capital | capital |
| Amusement Megaplex | building_amusement_megaplex | branch office |
| Commercial Forum | building_commercial_forum | branch office |
| Corporate Embassy | building_corporate_embassy | branch office |
| Executive Retreat | building_executive_retreat | branch office |
| Fast Food Chain | building_food_conglomerate | branch office |
| Mercenary Liaison Office | building_military_contractors | branch office |
| Private Military Industries | building_private_shipyards | branch office |
| Private Mining Consortium | building_private_mining_consortium | branch office |
| Private Research Enterprises | building_private_research_initiative | branch office |
| Public Relations Firm | building_public_relations_office | branch office |
| Virtual Entertainment Studios | building_virtual_entertainment_studios | branch office |
| Xeno-Outreach Agency | building_xeno_tourism_agency | branch office |
| Bio-Reprocessing Plants | building_bio_reprocessing_facilities | branch office |
| Concealed Drug Labs | building_underground_chemists | branch office |
| Disinformation Center | building_disinformation_center | branch office |
| Illicit Research Labs | building_illicit_research_labs | branch office |
| Pirate Free Haven | building_pirate_haven | branch office |
| Smuggler's Port | building_smuggling_rings | branch office |
| Syndicate Front Corporations | building_syndicate_outreach_office | branch office |
| Underground Clubs | building_underground_clubs | branch office |
| Wildcat Mining Operations | building_wildcat_miners | branch office |
| Wrecking Yards | building_wrecking_yards | branch office |
| Temple of Prosperity | building_temple_of_prosperity | branch office |
| Subversive Shrine | building_subversive_shrine | branch office |
| Imperial Concession Port | building_imperial_concession_port | branch office |

## Modifiers

Can be added with the effect add_modifier = { modifier = example } command combination to add modifiers to planets. Example: effect add_modifier = { modifier = eat_the_titans days = -1 } , if used without a target planet the entire empire will have the modifier

Can be removed with the effect remove_modifier = command to remove modifiers from planets. Example: effect remove_modifier = eat_the_titans

If a planet is selected the modifier is added as a planet modifier. Otherwise it is added as an empire modifier. Empire modifiers can be added as planet modifiers and vice versa.

| Planet modifier (starting) | ID |
|---|---|
| Atmospheric Aphrodisiac | atmospheric_aphrodisiac |
| Asteroid Belt | asteroid_belt |
| Carbon World | carbon_world |
| Exceptional Quality Minerals | ultra_rich |
| Extensive Moon System | extensive_moon_system |
| High Quality Minerals | mineral_rich |
| Lush | lush_planet |
| Natural Beauty | natural_beauty |
| Strong Magnetic Field | strong_magnetic_field |
| Titanic Life | titanic_life |
| Terraforming Candidate | terraforming_candidate |
| Frozen Terraforming Candidate | frozen_terraforming_candidate |
| Toxic Terraforming Candidate | toxic_terraforming_candidate |
| Natural Beauty, Wenkwort Gardens | pm_wenkwort_gardens |
| Natural Beauty, Paridayda | paradise_planet |
| Terraforming Candidate, Colonial Spirit | colonial_spirit_mod |
| Ocean Paradise | ocean_paradise |
| Ocean Paradise (Hive) | ocean_paradise_hive |
| Unified Purpose | payback_unified_purpose |
| Asteroid Impacts | asteroid_impacts |
| Atmospheric Hallucinogen | atmospheric_hallucinogen |
| Hazardous Weather | hazardous_weather |
| Hostile Fauna | dangerous_wildlife |
| High Gravity | high_gravity |
| Low Gravity | low_gravity |
| Wild Storms | wild_storms |
| Sea of Consciousness | living_sea |
| Hostile Planet | hostile_planet |
| Molten Mineral Rivers | molten_mineral_rivers |
| Pulsar Flares | pulsar_frying_pan |
| Ship Junkyard | ship_junkyard |
| Bleak | bleak_planet |
| Irradiated | irradiated_planet |
| Poor Quality Minerals | mineral_poor |
| Tidal Locked | tidal_locked |
| Unstable Tectonics | unstable_tectonics |
| Weak Magnetic Field | weak_magnetic_field |
| Debris Field | payback_debris_field |
| Holy World | holy_planet |
| Lithoid Crater | lithoid_crater |

| Planet modifier (other) | ID |
|---|---|
| Alloy Hyperfabricator | alloy_relic |
| Lush, Ancient Harvesters | ancient_harvesters |
| Lush, Ancient Terraforming | gaia_world |
| Ancient Trade Route | ancient_trade_route |
| C.A.R.E Interactive Interface | pm_planetary_mechanocalibrator |
| Terraforming Candidate, Colonial Remains | colonial_remains |
| Titanic Life, Delicious Titans | eat_the_titans |
| Energy Accelerator | energy_relic |
| Engineered Nature | engineered_nature |
| Filtered Atmospheric Hallucinogen | atmospheric_hallucinogen_good |
| Freed Stasis Dissidents | freed_stasis_dissidents |
| Heavy Metal | heavy_metal |
| Humble Monument | paragon_origin_humble_monument |
| Incredibly Boring Relic | minerals_relic |
| Local Mycelial Network | fumongus_monitor_pops |
| Loop Temple Pilgrims' Way | spiritual_happy_with_open_loop_temple |
| Loop Temple Visitor Center | happy_with_open_loop_temple |
| Strong Magnetic Field, Magnetic Miracle | magnetic_research_boost |
| Machine Interface Museum | machine_care_museum |
| Numistic Magnetostrips Distributed | numistic_magnetostrips |
| Nutritious Food | food_rich_planet |
| Exceptional Quality Minerals, Resonant Crystals | soothing_crystals |
| Residential Monument | paragon_origin_residential_monument |
| Rich Monument | paragon_origin_rich_monument |
| Terraforming Candidate, Second Home | second_home |
| Exceptional Quality Minerals, Soothing Magnetism | good_vibrations |
| Star Mall | star_mall_habitat |
| Subterranean Cities | subterranean_expansion |
| Subterranean Civilization | subterranean_civilization |
| Superflare Shielding | superflare_avoided |
| Surviving Infrastructure | wasteland_infrastructure |
| Tamed Nanite Swarm | tamed_nanite_swarm_modifier |
| The Memorex | the_memorex |
| The Sentinels | sentinels_planet_modifier |
| Watery Grave | watery_grave |
| Natural Beauty, Yuht Cleansing | pm_yuht_cleansing |
| Zen World | pm_wenkwort_zen |
| All Seeing Shard | ship_junkyard |
| Chamber from the Fortress | fortress_trophy |
| Cleansed Voidspawn's Venom Gland | voidspawn_trophy |
| Devourer's Egg Sac | stellar_devourer_trophy |
| Drake's Fang | ether_trophy |
| Dreadnought's Reactor | dread_trophy |
| Eye of the Shard | shard_trophy |
| Matriarch's Flagella | tiyanki_trophy |
| Scavenger Bot's Compactor | scavenger_trophy |
| Sky Dragon's Plume | sky_dragon_trophy |
| Wraith Infused Atmosphere | infused_atmosphere |
| Wraith's Dispenser Sack | wraith_trophy |
| Dead God | dead_god_planet |
| Industrial Network | factorator_industrial_network |
| Overgrowth | terraformation_nucleus_side_effect |
| Penal Colony | penal_colony |
| Uncertain History | planet_uncertain_past |
| Vanity Palace | qla_minder_vanity_palace |
| Abandoned Terraforming Project | abandoned_terraforming |
| Exofungus Infestation | exofungus |
| Predatory Plants | predatory_plants |
| Mastery of Nature | mastery_of_nature |
| Unified Purpose | payback_unified_purpose |

| Empire modifier | ID |
|---|---|
| A Life Worthwhile | lost_moment_memento |
| Administrator Beryllia | borin_administrator_beryllia |
| Ageless | ageless |
| Amoeba Hunter | amoeba_hunting_buff |
| Anthem of Aurora | anthem_of_aurora |
| Armor Layering | talon_armor |
| Ascetic Approach | paragon_origin_rebel_spiritualist |
| Asteroid Encryption | asteroid_encryption |
| Asteroid Relay Stations | asteroid_relay_stations |
| Asteroid Thrusters | asteroid_thrusters |
| Bane of the Prophetess | bane_of_the_prophetess |
| Certified Educator | payback_student |
| Cheap Thrills | the_evermore_modifier |
| Closed Society | paragon_origin_rebel_xenophobe |
| Cloud Destroyer | cloud_hunting_buff |
| Combat Drugs | artifact_find_military_application_army |
| Contingency Calculation | contingency_calculation |
| Covenant: Composer of Strands (starting) | covenant_composer_of_strands_0 |
| Covenant: Composer of Strands (upgraded) | covenant_composer_of_strands |
| Covenant: Eater of Worlds (starting) | covenant_eater_of_worlds_0 |
| Covenant: Eater of Worlds (upgraded) | covenant_eater_of_worlds |
| Covenant: Instrument of Desire (starting) | covenant_instrument_of_desire_0 |
| Covenant: Instrument of Desire (upgraded) | covenant_instrument_of_desire |
| Covenant: Whispers of the Void (starting) | covenant_whisperers_in_the_void_0 |
| Covenant: Whispers of the Void (upgraded) | covenant_whisperers_in_the_void |
| Crystal Focus | crystal_focus |
| Crystal Hunter | crystal_hunting_buff |
| Debug Subroutine | debug_subroutine |
| Defeated Absurdism | first_contact_defeated_dadaism |
| Drone Destroyer | drone_hunting_buff |
| Drone Mining Techniques | drone_mining_techniques |
| Enhanced Solar Power | solar_harvesting_bacteria |
| Excluding Elixir of Life | youthful_elite |
| Fervor for Discovery | fervor_for_discovery_ap_modifier |
| Flagellating Movement | flagellating_movement |
| Flourishing Trade | fruitful_coop_country_mod |
| Forced Mindfulness | forced_mindfulness |
| Free From Strife | payback_no_revenge |
| Freedom Fighters | paragon_origin_rebel_militarist |
| Forged in Flames | paragon_origin_united_through_war |
| Full Circle | full_circle |
| Fully Streamlined Logistics | fully_streamlined_logistics |
| Glory to the Many | glory_to_the_many |
| Goes Around, Comes Around | goes_around_comes_around |
| Harmonious Crew | harmonious_crew |
| Harmonious Tune | harmonious_tune |
| Harmonized Society | paragon_origin_rebel_pacifist |
| Harsh Truth | engineered_species_revelation |
| Honorable Leadership | honorable_leadership |
| Hull Hardening | talon_hull |
| Imperial Charter | imperial_charter |
| Improved Code Standards | machine_empire_code_improvements |
| Improved Crime Fighting | judge_improved_crime_fighting_laws |
| Infinity Beckons | infinity_beckons |
| Inoculated Population | machine_empire_health_boost |
| Integrated Command | integrated_command |
| Interstellar Flow Prediction | space_lights_insights |
| Killer Microorganism | killer_librarian_organism |
| Luminous Blades | alloy_producing_knights |
| Management Insights | artifact_find_peaceful_application_leader_improvement |
| Mineral Mapping | mineral_mapping |
| Modern Trench War | modern_trench_war |
| Mysterious Universe | engineered_species_ignorance |
| Neural Bank | research_utopia |
| No Worries | no_worries |
| Open Society | paragon_origin_rebel_xenophile |
| Oracle | oracle_administration |
| Population United | vas_population_united |
| Predictive Trading Algorithms | preftl_hagglers_mod |
| Primordial Dragonslayers | slew_origin_dragon |
| Progress Oriented | paragon_origin_rebel_materialist |
| Prophesied Greater Destiny | ulastar_prophesied_greater_destiny |
| Radiation-Hardened Components | radiation_hardened_components |
| Reaffirmed Superiority | reaffirmed_superiority |
| Revolutionary Spirit | paragon_origin_rebel_player |
| Rightful Due | payback_revenge_words |
| Rudari Death Laser | rudari_death_laser |
| Secrets of the Baol | artifact_baol_research_completed |
| Secrets of the Cybrex | artifact_cybrex_research_completed |
| Secrets of the First League | artifact_league_research_completed |
| Secrets of the Inetian Traders | secrets_of_the_inetian_traders |
| Secrets of the Irassians | artifact_irassian_research_completed |
| Secrets of the Vultaum (biological) | artifact_vultaum_research_completed_suppressed |
| Secrets of the Vultaum (machine) | artifact_vultaum_research_completed_machine |
| Secrets of the Zroni | artifact_zroni_research_completed |
| Sentinel Data | sentinel_data |
| Settled Differences | fotd_settled_differences |
| Shallarian Terraforming Knowledge | shallarian_terraforming_knowledge |
| Shared Elixir of Life | youthful_people |
| Skrand Crisis Insight | crisis_studied |
| Spectral Residue Studies | spectral_residue_studies |
| Spurred by the Past | spurred_by_the_past |
| Straight Talkers | straight_talkers |
| Streamlined Logistics | streamlined_logistics |
| Strengthened Government | paragon_origin_strengthened_government_i |
| Stuffed Toy | stuffed_toy |
| Syamelle's Blessing | syamelles_blessing |
| Technology of the Divine | technosphere_praising |
| The Chosen of Zarqlan | chosen_of_zarqlan |
| The Gains of Freedom | gains_of_freedom |
| The Mirror of Knowledge | black_hole_pantagruel_research |
| The Redemption of the Charynoi | charynoi_redemption |
| The Singularity Processor | infinity_calculations |
| Transcended Consciousness | gestalt_black_hole_good |
| Triumviri | fotd_triumviri |
| Tiyanki Butcher | tiyanki_butcher |
| Trophies of the Doomslayer | doomslayer_quest_complete |
| Unbidden Ritual | unbidden_ritual |
| Underdog | payback_underdog |
| Unified Thought | engineered_species_ownway |
| United In History | skrand_story |
| Universal Translator | universal_translator |
| Void Loops | void_loops |
| Zombie Contract Manipulation | zombie_contract_manipulation |