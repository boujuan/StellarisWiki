---
title: "Modding"
categories: ["Timeless", "Articles_with_potentially_outdated_sections", "Modding"]
---

# Modding

**Modding** , or creating mods , is the act of modifying the behavior of the base game (often referred to as vanilla ), either for personal use, or to release publicly to other players, for instance via the Steam Workshop .

As with all Paradox games, Stellaris is moddable to a great extent. Motivations of modders may vary widely; better translation to native language, more events or decisions, better map, major overhaul, shameless cheating, etc.

This guide is intended to lower the entry barriers to the world of Stellaris modding. However, there is still a learning curve to it, and it cannot replace the need to read some working vanilla code, and do lots of trial and error experimentation!

## Guidelines

- **Follow theRules for User Made Mods and Edits of PDS gamesand theEULA.** Mods that use DLC-exclusive features must lock the features behind the DLC purchase. To determine what DLC-exclusive means, if the feature can be fully used with DLC turned off, then you do not have to require the DLC in your mod. For example, espionage is a base game feature and you can add new operations without requiring any DLC, but if you are modding espionage operations from the Nemesis DLC, you must keep the Nemesis check.
- **Create a mod for your modifications** : use a personal mod even for small changes, and never directly modify the game files in the Steam Stellaris folder, as they may be overwritten without warning.
- **Use a good text editor** (recommended: VSCodium or Visual Studio Code ) to edit files and search into multiple files. A good text editor can also format the displayed text so that braces can be collapsed if complete, and complete/incomplete pairs are highlighted.
- **Use the error.log file to get execution errors** : The log folder can be found right next to the mod folder. Good Editors usually have the ability to track changes to files from outside the program and prompt for a reload, thus showing you errors with one glance at the file. Note that some modifications need a game to be loaded or even the option to be used on screen/in the back-end before their code will run.
- **Use CWTools for advanced validation and auto-complete** : CWTools is a syntax validator for Stellaris modding, developed as an extension for Visual Studio Code and also available for Sublime. Read the forum post by the developer for more info.
- **Minimize overwrites of vanilla files** , unless that is your main goal or somehow necessary (on_action triggers). Adding separate files and use loading from folders whenever possible, to improve mod compatibility and maintenance. Your files can have any name, all files in the folder will be loaded by the game. So choose a prefix no one else will ever use like the name of your mod. Even DLC follows that pattern.
- **Use a proper merge tool** (like WinMerge , or the Visual Studio Code Extension L13 Diff ), to merge between folders , and update modified vanilla files to a new vanilla patch.
- **Backup your work** to avoid losing everything. Consider using a source control system like Git and a collaborative forge like GitHub to manage team collaboration.
 - The Modding Git Guide is a community made guide for using Git, GitHub/GitLab, and related tools such as KDiff3. It can be a useful stop for questions beyond this wiki, and contains step by step guides for much of what is talked about here. Though the examples are HOI4 based, the principles apply equally well to any Paradox game mod.

- **Use UTF-8 encoding** for text and .mod files.
- **Use UTF-8 with BOM** for localization and name list files.
- **Indent properly** and, again, use a good text editor, to easily spot unclosed curly braces. Vanilla uses 1 tab for indentation rather than spaces.
- **Use comments** starting with a # character, to remember your reasons for writing tricky stuff.

## A note for programmers

If a new modder has a programming background with languages like C, Java, and Python, they may find the structure of Stellaris script confusing. This is likely for two reasons:

- The Clausewitz Engine’s scripting language doesn't separate basic syntax and keywords from game-specific structures and higher-level structures. For example, Triggers contains both the switch flow control structure and a conditional iteration any_playable_country , which are difficult to distinguish in form. Effects has both create_rebels and the while flow control.
- The scripting language uses the = operator for Boolean operations, assignments, scope changes, and for activating Triggers and Effects.

The following is a common example of valid structure:

```
capital_scope = {							# change to the scope of the country's capital planet
	every_deposit = {						# iterate through every deposit on the planet
		limit = {							# check each deposit for these conditions
			category = deposit_cat_blockers	# Boolean comparison using check the deposit's category
		}
		remove_deposit = yes				# activate an Effect to cause a change
	}
}

```

For this reason, it is recommended that they follow the modding tutorial linked below and read the vanilla game files to better understand how the scripts function.

## Modding tutorial

There is a modding tutorial available which covers steps necessary to create a basic mod.

## Mod management

The first steps of modding is getting to know where the mods are located, how they're structured and what to do when uploading your first mod!

### Mod folder location

| OS | Path |
|---|---|
| Linux | ~/.local/share/Paradox Interactive/Stellaris/mod |
| Windows | …\Documents\Paradox Interactive\Stellaris\mod |
| Mac OS | ~/Documents/Paradox Interactive/Stellaris/mod |

Mods from the Steam Workshop will be placed in …\SteamLibrary\SteamApps\workshop\content\281990 , named by their Workshop ID. Mods from Paradox Mods will be placed in the mod folder location, named PDX_*MOD_ID* .

### File and folder structure

Getting the structure set up correctly when creating a mod is essential for it to run properly.

This is the required structure inside the main mod folder:

- modname.mod – Includes the information used by the Stellaris (PDX) launcher
- modname – Folder where all the modified files are placed, in the same file and folder structure as the game folder
 - Mod contents
 - descriptor.mod – Required for the new launcher added in patch 2.4. Ignored in the old launcher.
 - image.ext – PNG and JPEG files are supported. With the new 2.4 launcher, must be a PNG named thumbnail.png

modname.mod and descriptor.mod both contain the mod information that the launcher uses when displaying the mod and uploading it. The 2.4 launcher prefers descriptor.mod and will modify modname.mod to match the information in descriptor.mod , however if the file is not found, it'll use the information in modname.mod . The pre-2.4 launcher ignores it. The path="XXX" is not needed in descriptor.mod. Note that folder and file names are case-sensitive on Mac OS X and Linux.

**modname.mod structure** This also applies to descriptor.mod .

| Name | Required | Description | Example |
|---|---|---|---|
| name | **Yes** | Name of your mod. | name="My Stellaris Mod" |
| path | modname.mod: **Yes** descriptor.mod: **No** (Ignored) | Defines which folder is the mod’s folder. It can be an absolute directory or relative to the …\Documents\Paradox Interactive\Stellaris directory. The Paradox Launcher will automatically correct a relative path to the corresponding absolute path. **Note:** Stellaris uses (Unix) slash / instead of (Microsoft) backslash \ (or \\ ). | path="mod/MyStellarisMod" |
| dependencies | No | Specifies if the mod should be loaded after the listed mod (s), if they exist. Very useful for sub-mods or compatibility patches to make sure they overrule certain mods. | dependencies={ "My Other Stellaris Mod" "Not My Stellaris Mod" } |
| picture | No | Specifies the mod thumbnail used on Steam Workshop . With the new 2.4 launcher, this must be an exact fixed name thumbnail.png . | picture="thumbnail.png" |
| tags | No | List of tags for Steam Workshop . Using tags besides the predefined ones may prevent uploading on Paradox Mods. **Warning:** Maximal 10 are allowed (at least since launcher version 2022.10) . Don't forget quotes for tags that contain spaces. | tags={ "Tag1" "Tag2" } |
| version | No | Specifies what the launcher will show as the version of the mod. (Not the version of the game it’s meant for). Any string is accepted. | version="v4.5" |
| supported_version | Recommended | Specifies what game version the mod supports. The last number can be replaced with the asterisk (*) symbol to tell the launcher that the mod supports any value, like `v3.12.*`. | supported_version="v3.13.1" |
| remote_file_id | No | Property added by the launcher that includes the Steam Workshop ID. Ignore it. | remote_file_id="1234567890" |

The data structure is similar to the proprietary Valve Data Format.

**Example modname.mod fileSomeMod.mod**

```
name="SomeMod"
path="mod/SomeMod"
dependencies={
	"othermod"
	"another mod"
}
tags={
	"Graphics"
	"Economy"
	"Overhaul"
}
picture="thumbnail.png"
remote_file_id="1234567890"
supported_version="v3.12.*"

```

### Adding a thumbnail

The Steam Workshop allows for a preview thumbnail picture that'll be displayed when searching for mods and as a preview picture if you haven't uploaded any, otherwise it'll be placed to the right of the preview pictures. It’s recommended to make the thumbnail 512px × 512px at minimum, which is used by the workshop frontpage. Additionally, the thumbnail file should be under **1 MB** in size, otherwise, it will not be uploaded. Both JPEG and PNG are supported, and after 2.4, the image file must be named **thumbnail.png** .

1. Make sure the Stellaris launcher is closed, so that it doesn't revert your changes
2. Open up modname.mod and descriptor.mod files
3. Make sure picture="thumbnail.png" exists, if not, add it
4. Add your image file in your mod folder
5. Start up the launcher and update your mod
6. Thumbnail should now show up at the Steam Workshop mod page

You can always update the thumbnail at any time by updating the mod (unless you are only a co-author).

### Creating a mod

You can use the game launcher to set up a mod structure for you by following these simple steps according to your launcher of choice:

| # | Launcher v1 (<=2.3.3) | Launcher v2 (>=2.4.0) | Launcher v⁇⁇ |
|---|---|---|---|
| 1 | Launch the game | | |
| 2 | Navigate to the mods tab | | |
| 3 | Click **Mod Tools** | | Click **Upload Mod** |
| 4 | Click **Create Mod** | | Click **Create Mod** |
| 5 | Insert the relevant information and click **Create Mod** at the bottom | | |
| 6 | Navigate to the mod folder and locate your mod folder | | |
| 7 | Start modding! | | |

### Uploading and updating a mod

Uploading and updating a mod follows the same procedure, depending on your launcher of choice:

| # | Launcher v1 (<=2.3.3) | Launcher v2 (>=2.4.0) |
|---|---|---|
| 1 | Launch the game | |
| 2 | Navigate to the mods tab | |
| 3 | Click **Mod Tools** | |
| 4 | Click **Upload Mod** | Click **Upload a Mod** |
| 5 | Select your mod from the list | |
| 6 | Click **Fetch Info** and wait for a response | Select mod site |
| 7 | | Insert description ***** |
| 8 | Click **Upload** | Click **Upload Mod** |
| 9 | The launcher will now upload your changes and inform you when it’s done or if an error occurred. | |
| 10 | Navigate to the mod service of choice and locate your mod; **Steam Workshop** , visit the Workshop page, and locate the "Files you've posted" button by hovering over "Your Files" on the right **Paradox Mods** , visit the Mods page, login, and click "My uploaded mods" in the dropdown menu that appears when hovering over your name | |

Note that if you subscribe to an uploaded version of your mod while you still have the .mod file of your original mod in the mods folder, the uploaded mod will likely not work.

## Game data

- Console commands , useful for debugging mods.
- Defines , which allows you to influence some hardcoded vanilla behaviors
- Scopes , Conditions , and Commands used for scripting
- Modifiers , used to influence calculations made by the game
- Events , used to define popups with decisions
- Map , used for pre-generated galaxy maps

## Game structure

Below is a list of game files and folders, listed alongside the modding guide for each.

#### Stellaris/common/

Main article: #Common folder

| File | Summary | Guides |
|---|---|---|
| achievements.txt | Definitions for achievements. Modding this file doesn't make sense, since achievements are disabled for any "common" changing/expanding mods anyway. | |
| alerts.txt | | Messages |

#### Stellaris/events/

| Folder/File | Summary | Guides |
|---|---|---|
| example_events.txt | Contains the event code for a set of events. | Events |

#### Stellaris/flags/

| Folder/File | Summary | Guides |
|---|---|---|
| *.dds | A flag image file. | Flags |
| colors.txt | Sets up the allowed colors for flags and the randomizable combos. | Flags |

#### Stellaris/fonts/

| File | Summary | Guides |
|---|---|---|
| fonts.asset | Sets up the fonts used by the game. | Fonts |

#### Stellaris/gfx/

| Folder/File | Summary | Guides |
|---|---|---|
| advisorwindow | Sets up the 3D view for the advisor | Graphics |
| arrows | Contains the images used by various arrows ingame. | Graphics |
| cursors | Contains the cursor files/images used ingame. | Graphics |
| event_pictures | Contains the pictures used in **events** . | Events |
| fonts | Contains the font files used ingame. | Fonts |
| FX | Contains the FX shaders used ingame. | Graphical Effect |
| interface/ | Contains the images used for interfaces ingame. | Graphics |
| interface/anomaly | Contains the images used for the anomaly mechanic | Graphics |
| interface/buttons | Contains the images used for buttons | Graphics |
| interface/diplomacy | Contains the images used for the diplomacy interface. | Graphics |
| interface/elections | Contains the images used for the election interface. | Graphics |
| interface/event_window | Contains the images used for the event window. | Graphics |
| interface/flags | Contains the image masks used for flags. | Graphics |
| interface/fleet_view | Contains the images used for fleets. | Graphics |
| interface/frontend | Contains the images used for the frontend interface. | Graphics |
| interface/government_mod_window | Contains the images used for the government modification interface. | Graphics |
| interface/icons | Contains the icons used for everything in the game. | Graphics |
| interface/main | Contains the images used for generic actions. | Graphics |
| interface/old | Contains the images used from EU4 | Graphics |
| interface/outliner | Contains the images used for the outliner interface. | Graphics |
| interface/planetview | Contains the images used for the planet view interface. | Graphics |
| interface/progressbars | Contains the images used for progress bars ingame. | Graphics |
| interface/ship_designer | Contains the images used for the ship designer interface. | Graphics |
| interface/situation_log | Contains the images used for the situation log interface. | Graphics |
| interface/sliders | Contains the images used for sliders ingame. | Graphics |
| interface/system | Contains the images used for the system view interface. | Graphics |
| interface/tech_view | Contains the images used for the technology view interface. | Graphics |
| interface/tiles | Contains the images used for the tile view interface. | Graphics |
| interface/topbar | Contains the images used for the topbar interface. | Graphics |
| interface/waroverview | Contains the images used for the war view interface. | Graphics |
| keyicons | Contains the images used for button presses ingame. | Graphics |
| lights | Contains the logic used for the light effects ingame. | Graphical Effect |
| loadingscreens | Contains the images used for loadscreens. | Graphics |
| models | Contains the model .mesh files and images. | Models |
| models/portraits | Contains the portrait .mesh files and images. | Portraits |
| particles | Contains the logic and images used for particles. | Graphics |
| pingmap | Contains the logic used for pings. | Graphics |
| portraits | Contains the logic used for portrait images. | Portraits |
| projectiles | Contains the logic used for projectiles. | Graphics |
| shipview | Contains the logic used for ship view. | Graphics |
| worldgfx | Contains the logic and images used for world graphic effects. | Graphics |

#### Stellaris/interface/

| Folder | Summary | Guides |
|---|---|---|
| *.gfx | Controls the assignment of image to interface variable. | Interfaces |
| *.gui | Controls the visual logic of an interface. | Interfaces |

#### Stellaris/localisation/

| File | Summary | Guides |
|---|---|---|
| *l_braz_por.yml | Contains Brazilian Portuguese localisation | Localisation |
| *l_simp_chinese.yml | Contains Chinese localisation | Localisation |
| *l_english.yml | Contains English localisation | Localisation |
| *l_french.yml | Contains French localisation | Localisation |
| *l_german.yml | Contains German localisation | Localisation |
| *l_korean.yml | Contains Korean localisation | Localisation |
| *l_polish.yml | Contains Polish localisation | Localisation |
| *l_russian.yml | Contains Russian localisation | Localisation |
| *l_spanish.yml | Contains Spanish localisation | Localisation |
| *l_braz_por.yml | Contains Brazilian/Portuguese localisation | Localisation |

#### Stellaris/map/

| Folder/File | Summary | Guides |
|---|---|---|
| galaxy | Contains the galaxy options. You cannot add new ones currently. | Galaxy |
| setup_scenarios | Controls the logic for different sizes of galaxies. | Galaxy |

#### Stellaris/music/

| Folder/File | Summary | Guides |
|---|---|---|
| *.ogg | A music file. | Music |
| songs.asset | Controls the assignment of music to a code name, and sets the volume of playback. | Music |
| songs.txt | | Music |

#### Stellaris/prescripted_countries/

| Folder/File | Summary | Guides |
|---|---|---|
| *.txt | Contains a pre-scripted setup for a country. Listed on the side ingame. | Galaxies |
| setup_scenarios | Controls the logic for different sizes of galaxies. | Galaxies |

#### Stellaris/sound/

| Folder/File | Summary | Guides |
|---|---|---|
| *.asset | Sets up sounds. | Sound |
| *.wav | A sound file. | Sound |

## Overwriting specific elements

See also: #Mod load order

Occasionally, it is possible to overwrite a specific game element without needing to replace the entire vanilla file. In some cases adding an element with a similar identifier (id or key) into another file will duplicate that element for the game. But in other cases, the version that comes first (First In, Only Served; **FIOS** )/last (Last In, Only Served; **LIOS** ) will be used instead. The order in which files are processed is based on ASCIIbetical order of the filenames. If the names are the same, they'll be processed based on the displayed order in the launcher (or loading template). Before patch 2.5 the load order was the reverse-ASCIIbetical order of the mod display name, with vanilla always being first (if it’s at the top of the mod list, it'll be loaded last ). Note that if there are multiple mods with the same display name, only the one whose mod file comes first, will be used.

Note that this feature is not documented and thus might be subject to arbitrary changes between versions.

### Common folder

| Folder | Overwrite | | | Contents |
|---|---|---|---|---|
| Type | Error Log | Notes | | |
| achievements | ❓ | ❓ | | Achievements |
| council_agendas renamed v3.7 | LIOS | Object key already exists | Agendas are given to leader-candidates in Oligarchic government-forms | Agendas definitions and weights. |
| agreement_presets since v3.4 | ❓ | ❓ | Functions are limited/restricted by: diplomatic_actions and game_rules | Subject empire type definitions. |
| agreement_resources since v3.4 | ❓ | ❓ | | Definitions for subject types. |
| agreement_term_values since v3.4 | FIOS | Object with key already exists | | Definitions for subject types. |
| agreement_terms since v3.4 | ❓ | ❓ | | Definitions for subject types |
| ai_budget | ❓ | ❓ | | What fractions of its resources the AI wants to spend on things. |
| ai_espionage | ❓ | ❓ | | None (all content in subfolders) |
| ├───operations | ❓ | ❓ | | |
| └───spynetworks | ❓ | ❓ | | |
| ambient_objects | ❓ | ❓ | References used by code to spawn ambient objects. | Graphics objects . |
| anomalies | LIOS | Object key already exists | Events that occur for research ships | Anomaly description keys, images, spawn chances and conditions, and event pointers. |
| archaeological_site_types | ❓ | ❓ | Definitions for Archaeological Sites to be discovered and delved by Science Ships. | Ancestral Relics definitions. |
| armies | LIOS | Object key already exists | | Army type definitions. |
| artifact_actions | LIOS | Object key already exists | | Minor Artifact artifact action definitions. |
| ascension_perks | LIOS | [None] since v3.0 | Pre v3.0: [Error log] Object key already exists | Ascension Perk definitions. |
| asteroid_belts | ❓ | ❓ | | Graphics for asteroid belts. |
| attitudes | LIOS | Object key already exists | | AI Attitude definitions. |
| bombardment_stances | LIOS | Object key already exists | | Bombardment Stances definitions. |
| buildings | LIOS since v3.3 | Object key already exists | Pre v3.3: Breaks auto-generated modifiers | Buildings definitions. |
| button_effects | LIOS | Object key already exists | | |
| bypass | LIOS | Object key already exists | | Definitions for Bypasses (gateway, worm hole and l-gate) type definitions. |
| country_focus since v4.0 | ❓ | ❓ | | |
| casus_belli | LIOS | Object key already exists | | Casus Belli war conditions. |
| colony_automation | ❓ | ❓ | | How player colonies controlled by automated sector management determine which districts and buildings to build. Each designation has its own script. Not used by AI empires. |
| colony_automation_categories | LIOS | Object key already exists | | Lists the categories of planetary automation that you can select in the planet interface |
| colony_automation_exceptions | ❓ | ❓ | | Conditional overrides to automated sector management. |
| colony_types | LIOS | Object key already exists | | Colony Designation definitions. |
| colors | ❓ | ❓ | | RGB country and species color sets. |
| component_sets | FIOS | Object key already exists | | Ship component icon and frame assignment. |
| component_slot_templates | ❓ | ❓ | | Graphics assignments for weapon slot types. |
| component_tags | ❓ | ❓ | | List of referenceable tags assignable to ship components . |
| component_templates | FIOS | Object key already exists | | Ship component definitions. |
| country_container | ❓ | ❓ | | |
| country_customization | ❓ | ❓ | | Which capital building types and robot portraits empires use. |
| country_limits | LIOS | ❓ | | None (all content in subfolders) |
| ├───ownership_limits | LIOS | Object key already exists | | ship_of_size_limits for each country type |
| └───ship_of_size_limits | LIOS | Object key already exists | | Number of ships that can be built based on size_multiplier and naval_cap_div |
| country_types | LIOS | [None] since v3.0 | Pre v3.0: [Error log] Object key already exists | Rules for empires, enclaves, and other country types. |
| crisis_levels | LIOS | ❓ | | Become the Crisis ascension perk crisis level definitions. |
| crisis_objectives | LIOS | ❓ | | Menace rewards for completing Become the Crisis objectives. |
| decisions | LIOS | Object key already exists | | Decision definitions and AI weights. |
| defines | LIOS | [none] | The block the define is in must be included as well. E.g.: NGameplay = { POLICY_YEARS = 10 } | Global variables and settings. |
| deposit_categories | ❓ | ❓ | | List of orbital deposit and planetary feature categories. |
| deposits | LIOS | Object key already exists | | Orbital deposit , planetary feature , and blocker definitions and drop weights. |
| diplo_phrases | ❓ | ❓ | | Diplomatic phrase keys and conditions for diplomatic actions. |
| diplomatic_economy | LIOS | Object key already exists | | Diplomatic agreement costs. |
| diplomatic_actions | LIOS | Object key already exists | | Diplomatic action conditions. |
| districts | LIOS since v3.3 | Object key already exists | Pre v3.3: Breaks auto-generated modifiers | District definitions. |
| dynamic_text | ❓ | ❓ | | |
| economic_categories | LIOS | Object key already exists | | Definitions and modifier generation for<br>economic categories<br>used by<br>resource blocks<br>and AI budgets.<br>- Includes job categories and subcategories which determine which modifiers apply to which jobs |
| economic_plans | ❓ | ❓ | | AI empire resource income goals. |
| edicts | LIOS | Object key already exists | | Edict definitions and AI weights. |
| espionage_assets | LIOS | ❓ | Entire override : PASS | Espionage asset definitions. |
| espionage_operation_categories | ❓ | ❓ | | List of espionage operation and intel categories. |
| espionage_operation_types | LIOS | … already exists, using the one at file: … | Entire override : PASS | Espionage operation definitions. |
| ethics | LIOS | Object key already exists | Might break "selected ethic" graphic if too many Ethics; **WARNING:** Due to new multiple ethics files, the auto-generated file will randomly break off as some empires have no ethics when randomly generated. So entire overwrite is suggested. | Empire ethic definitions and ethic attraction modifiers. |
| event_chains | FIOS | [none] | | Event chain image assignment and referenceable counters. |
| fallen_empires | ❓ | ❓ | | Fallen empire definitions. |
| federation_law_categories | ❓ | ❓ | | Federation law category assignment. |
| federation_laws | ❓ | ❓ | | Federation law definitions and AI weights. |
| federation_perks | ❓ | ❓ | | Federation perk definitions. |
| federation_types | ❓ | ❓ | | Federation type definitions. |
| first_contact | ❓ | ❓ | | First contact progression definitions. |
| galactic_community_actions | ❓ | ❓ | | Costs to perform special galactic community actions. |
| galactic_focuses | ❓ | ❓ | | Galactic focus definitions. |
| game_concept_categories since v4.0 | ❓ | ❓ | | |
| game_rules | LIOS | [none] | | Tooltip generating conditions. |
| gamesetup_settings since v4.0 | ❓ | ❓ | | Settings shown in the game setup UI. |
| global_ship_designs | FIOS | A ship design already exists | | Premade ship designs. |
| governments | LIOS | Object key already exists | | Government type conditions, ruler titles, and election candidate weights. |
| ├───authorities | FIOS | Object key already exists | Specific override is impossible. Entries override ONLY. | Authority definitions. |
| └───civics | LIOS | Object key already exists | | Civic and origin definitions. |
| graphical_culture | ❓ | ❓ | | Graphics info for ship skins. |
| greeting_overlay_sounds | ❓ | ❓ | | |
| inline_scripts since v3.5 | DUPL | ❓ | Only works when the file is fully replaced in my experience | Inline scripts . |
| intel_categories | ❓ | ❓ | | Which information is revealed by specific intel category levels . |
| intel_levels | ❓ | ❓ | | Assigns intel category levels to intel level. |
| job_tags since v4.0 | ❓ | ❓ | | Job Tags are used to group jobs together |
| lawsuits | ❓ | ❓ | | Unused |
| leader_classes | LIOS | Object key already exists | | Leader type definitions. |
| leader_tiers since v4.1 | ❓ | ❓ | | Leader tiers definitions. |
| mandates | LIOS | Object key already exists | | Mandate definitions. |
| map_modes | LIOS | Object key already exists | | Map mode definitions. |
| megastructures | LIOS | Object key already exists | | Megastructure definitions. |
| menace_perks since v3.0 | ❓ | ❓ | | Bonus perk definitions for Become the Crisis. |
| message_types | ❓ | ❓ | | Alert message icon definitions. |
| missions since v3.13 | ❓ | ❓ | | Cosmic Storms missions definitions. |
| mutations since v3.14 | ❓ | ❓ | | Space fauna mutations definitions. |
| name_lists | DUPL | ❓ | | Sets of random names for ships, fleets, armies, planets, and leaders. |
| notification_modifiers | ❓ | ❓ | | |
| observation_station_missions | DUPL/LIOS | ❓ | Entire override ONLY. | Observation post mission definitions and AI weights. |
| on_actions | NO/MERGE | [none] | Cannot modify existing entries; new entries will be merged with the existing entry with the same NAME={}. Load order is top first. | Assigns events to be triggered when certain game actions happen. |
| opinion_modifiers | DUPL/LIOS | [none] | add_opinion_modifier is LIOS | Opinion modifiers and conditions. |
| patrons since v4.1 | ❓ | ❓ | | Definitions of shroud entities that act as Patrons . |
| personalities | LIOS | Object key already exists | | AI Personality definitions and weights. |
| planet_classes | DUPL/LIOS | [none] | DUPL – breaks habitability modifiers if individually overwritten. | Celestial body graphics and definitions. |
| planet_modifiers | LIOS | Object key already exists | | Planet modifiers, Random planet modifier spawn chances. |
| policies | LIOS | Object key already exists | Existing Object key can be override with NAME = {} | Policy definitions and AI weights. |
| pop_categories | LIOS | Object key already exists | | Pop category type definitions. |
| pop_faction_types | LIOS | Object key already exists | | Faction demands, join conditions, attraction modifiers, and actions. |
| pop_jobs | LIOS since v3.3 | Object key already exists | Pre v3.3: [Type] NO – Breaks auto-generated modifiers if overwriting a specific job and not the whole file. | Job definitions and auto-assignment weights. |
| precursor_civilizations | ❓ | ❓ | | List of Precursor civilizations and conditions. |
| random_names | ❓ | ❓ | | Components for randomly generated Empire, Federation, Faction, First Contact, and War names. |
| └───base | ❓ | ❓ | | Lists of celestial object names and randomly generated species name affixes. |
| prescripted flags since v4.0 | ❓ | ❓ | | Flags for pre-scripted empires |
| relics | LIOS | Object with key already exists | | Relic definitions and AI triumph weights. |
| resolution_categories | ❓ | ❓ | | Defines which category individual resolutions are in and the category icon. |
| resolution_groups | LIOS | Object with key already exists | | Assigns frames and text colors to resolution categories. |
| resolutions | LIOS | Object with key already exists | | Resolution definitions and AI weights. |
| script_values | LIOS | ❓ | | Dynamically calculated referenceable values. |
| scripted_effects | LIOS | Object key already exists | | Scripted effects . |
| scripted_loc | FIOS | [none] | Existing Object key can be override with name = key | Dynamic localization . |
| scripted_modifiers since v3.4 | LIOS | Object key already exists | | Scripted modifiers . |
| scripted_triggers | LIOS | Object key already exists | | Boolean trigger conditions . |
| scripted_variables | FIOS | Variable name taken | | Global variables . |
| section_templates | NO DUPL/FIOS | Duplicate section template found. Multiple sections are named … | **Warning** : existing can't be overwritten, used ships/starbases will get deleted. | Ship section definitions. |
| sector_focuses | LIOS | Object key already exists | | Sector automation construction weights. |
| sector_types | ❓ | ❓ | | Sector definitions. |
| ship_behaviors | FIOS | Behavior name already exists | | Ship AI. |
| ship_categories since v3.14 | ❓ | ❓ | | Space fauna entity type (ships) definitions. |
| ship_sets since v4.0 | ❓ | ❓ | | Ship Sets contains lists of gfx cultures. |
| ship_sizes | LIOS | Object key already exists | | Ship chassis definitions, including Starbases and spaceborne aliens . |
| situations | LIOS | Object key already exists | | Situation definitions. |
| solar_system_initializers | FIOS | Initializer already exists | | Predefined solar systems , some including country, colony, and/or fleet generation. |
| special_projects | FIOS | Object key already exists | | Special project definitions. |
| specialist_subject_perks | LIOS since v3.4 | ❓ | | |
| specialist_subject_types | LIOS since v3.4 | ❓ | | |
| species_archetypes | LIOS since v3.3 | Object key already exists | Pre v3.3: Breaks auto-generated modifiers. | Assigns Trait Points and Trait sets to Species archetypes. |
| species_classes | LIOS | Object key already exists | | Assigns portraits, species archetype, and graphical culture to species classes . |
| species_names | ❓ | ❓ | | Lists for randomly generating species names. |
| species_rights | LIOS | Object key already exists | Effect tooltips are independent of the effects. | Species rights definitions and AI weights. |
| specimens since v3.14 | LIOS | ❓ | | Grand Archive – Specimens definitions. |
| star_classes | LIOS | ❓ | | Spawn odds and planet generation rules and environmental hazards based on the central star or star set. |
| starbase_buildings | LIOS | Object key already exists | | Starbase building definitions and AI weight modifiers. |
| starbase_levels | LIOS | Object key already exists | | Starbase chassis definitions. |
| starbase_modules | LIOS | Object key already exists | | Starbase module definitions. |
| starbase_types | LIOS | Object key already exists | | Starbase designation conditions, AI ratios, and AI buildings & module weights. |
| start_screen_messages | FIOS | [none] | The first valid part for each location will be used and the rest discarded without issue. | Localization keys and conditions used to assemble the game start message. |
| static_modifiers | LIOS | [none] | | Modifier definitions. |
| storm_types since v3.13 | ❓ | ❓ | | Cosmic Storms definitions. |
| strategic_resources | DUPL | [none] | Must replace the whole file with the same filename or it won't work. | All resource definitions. |
| subjects | LIOS | [None] – REMOVED in v3.4, s. agreement_presets | Functions are limited/restricted by: diplomatic_actions and game_rules | Subject empire type definitions. |
| system_tooltips | ❓ | ❓ | | Tooltips displayed when hovering over a system. |
| system_types | LIOS | Object key already exists | | System designation type conditions and weights. |
| target_types since v4.0 | ❓ | ❓ | | |
| technology | LIOS* | Duplicate technology: [ tech ] | LIOS overrides mostly still work despite the DUPL-type error entry. However, if the overwriting tech lacks a "potential" block, it will inherit the "potential" block from the overwritten tech. | Technology definitions, drop weights, and AI weights. |
| ├───category | ❓ | ❓ | | List of research categories and icon assignments. |
| └───tier | LIOS | ❓ | | List of technology tiers. Defines number of previous tier tech requirements. |
| terraform | DUPL | [none] | | Terraforming costs and conditions for every valid planet type pair. |
| timeline_events since v4.0 | ❓ | ❓ | | Timeline Events Database |
| trade_conversions | LIOS | Object key already exists – REMOVED in v4.0 | | Trade Policy definitions. |
| tradition_categories | LIOS | Object key already exists | | Tradition tree definitions and AI weights. |
| traditions | LIOS | Object key already exists | Effect tooltips are independent of the effects. | Individual tradition definitions, including adoption and finisher effects. |
| trait_tags since v4.0 | ❓ | ❓ | | Trait Tags are used to group traits together |
| traits | DUPL/NO | [none] | Entire override ONLY. | Species trait and Leader trait definitions. |
| war_goals | LIOS | Object key already exists | | War goal definitions, conditions, and AI weights. |
| zone_slots since v4.0 | ❓ | ❓ | | Planet District Zone Slots |
| zones since v4.0 | ❓ | ❓ | | Planet District Zones |

FIOS – First in, only served.

LIOS – Last in, only served

DUPL – Duplicates

NO – Cannot individually overwrite

Please note that not everything could be tested extensively.

### Localisation folder

Localisation is likely LIOS

A guide for overwriting localisation can be found here .

### Events folder

Events are usually treated as FIOS (note: The error log will make it look like it is LIOS, but this is not true, it is definitely FIOS)

### Interface folder

Interface is likely LIOS

### Fonts folder

Fonts are LIOS.

## Tools & utilities

### Tools

- Notepad++ – Powerful editor to change files.
- WinMerge – Contrasts the difference between two text files. Useful for updating mods.
- VSCodium – Powerful, hackable, free open source editor. Use with CWTools extension, powerful syntax checker for Paradox games.
- VS Code – Powerful, hackable, free editor from Microsoft (based on open source code). Use with CWTools extension, powerful syntax checker for Paradox games.
- Intellij IDEA – Pwerful and smart IDE. Use with Paradox Language Support, the plugin for Paradox games modding, which is smart, convenient and with more potential. (Intellij IDEA Community version and other JetBrains IDEs are also available).
- Maya exporter – Clausewitz Maya Exporter to create your own 3D models.
- Spaceship Generator – A Blender script to procedurally generate 3D spaceships
- paint.net – Freeware software for digital photo editing
- Irony Mod Manager – Mod Manager with conflict solver for Paradox Games
- Stellaris Galaxy Generator – by BlackPhoenix134 ( preview )
- Static Galaxy Generator – A static galaxy generator and editor for your mods. ( How to use )
- Sublime Text – Powerful, moddable, hackable text editor. Install packages as your needs evolve.
- Random Empire Generator – by u/MarinusWA0 .
- List of Stellaris triggers, modifiers and effects – for most game versions since launch, includes compare between Stellaris patches GitHub feature.
- IO PDX Mesh – Blender (2.93+) & Maya (2018+) plugin for "editing of mesh and animation files used in the various Clausewitz Engine games created by Paradox Development Studios"
- SageThumbs – Showcase thumbnails of .dds files on Windows Explorer.

### Help links

- Steam Workshop – The place for where you can share your creations with other players.
- The Stellaris Modding Den – the central modding discord for Stellaris.
- Stellaris Modding Subreddit
- Paradox Graphics – A Comprehensive Guide – In-depth documentation for preparing 3d models for Clausewitz engine games like Stellaris.

## Advanced tips

- For the bigger mods using a source control management tool (Git, …), it is handy to create a symbolic link between Stellaris mod folder and the working directory of the local repository, especially if the mod also has sub-mods. Note that you'll still need to copy the .mod file (s) manually, but they rarely change. Run the following command from the parent directory of main git folder, replacing:
 - <mod_path_name> by the value of path attribute from .mod file
 - <git_mod_folder> by the name of the sub-folder that contain mod data (folders common, decisions, events, etc…)

```
mklink /J "%USERPROFILE%\Documents\Paradox Interactive\Stellaris\mod\<mod_path_name>" ".\<git_mod_folder>"

```

### Testing Mods

Certain, more obscure Console commands (that don't show up if you type 'help' in the console) are extremely useful in the process of testing a mod and more specific alterations.

- observe – switches you to Observer Mode. You will no longer play as any specific character – this will allow the game to run for a long period of time, uninterrupted. It also makes every invisible trait and secret religion visible.
- run <filename.txt> – runs script in a txt file located in the in the Documents install directory. It will be executed from the player’s scope. Useful for testing tricky scripts – you can just have the script open in a different window, run it, tweak the script, save it, and run it again – it will be recompiled every time.
- reloadevents – reloads and recompiles every single event (may take a while depending on your hardware). Useful if you want to tweak an entire event or chain of events without rebooting the game every time. not yet implemented
- reloadloc reload text – reloads the entire localisation table. Useful if you spot a typo while testing your mod, or if you are trying to fit as much text in an event frame as possible.

### Troubleshooting mod installation

Multiplayer requires same mod list and load order for all players.

Try reload mods button in launcher. All installed mods > Reload installed mods.

Check if non-ASCII characters exist in the address of the mod folder.

Verify integrity of Stellaris installation files (for Steam right click on Stellaris > Properties > Local files > Verify). Warning: Verification tool does not check for any additional files put into the installation folder, and those might still alter the checksum. Check patch notes and compare your unmodded game (vanilla) with reference checksum.

Make sure your antivirus is not blocking the launcher. It might do so silently without a warning.

Check if your OneDrive ran out space or is disconnected if you are using it (you might not know that you are).

If you have a mod both as a local and as a workshop subscription game will refuse to load it. Remove or move one, including root Stellaris/mod/*.mod file.

: If the local mod no longer appears in the launcher, a manual solution is to fix the overridden values ( dirPath and status ) in the launcher-v2.sqlite .

Delete Paradox Launcher database files as they might be corrupted (backup first):

1. Do the steps on point 5 at #Purging all mods .
2. In the Paradox Launcher use Mods > Reload installed mods.

If you are using Irony Mod Manager do not fire Conflict Solver unless you intend to use it. Conflict Solver creates list of conflicts and generates overwrites for each one based on your load order. So if you change mod composition of a collection or load order you have to rerun conflict solver each time (alternatively delete patch folder in /Stellaris/mod/) You can purge Irony settings stored in .roaming/Mario/ if you ever need to.

### Purging all mods

This will reset your mod settings completely (nuclear option!):

1. Quit Stellaris and Stellaris (Paradox) Launcher
2. Unsubscribe from all mods. Stellaris Workshop -> Your files (under your avatar) -> Subscribed items – > Unsubscribe From All .
3. Quit Steam
4. Go to SteamLibrary\steamapps\workshop\content\281990 and delete everything.
5. Go to the Stellaris settings folder (one above the mod folder) and delete the following files (some of these might not be present in the actual version) :
 - dlc_load.json
 - game_data.json (only pre 2.8 launcher)
 - mods_registry.json (only pre 2.8 launcher)
 - launcher-v2.sqlite (since v2.8 beta launcher)
 - in settings.txt everything inside last_mods={ }

6. Restart Steam.
7. Open Paradox launcher.
8. Close Paradox launcher.
9. Resubscribe to your mods.
10. WAIT UNTIL ALL DOWNLOADS ARE DONE. DO NOT START PARADOX LAUNCHER UNTIL DOWNLOADS ARE COMPLETE.
11. Start Paradox Launcher.
12. Close Paradox launcher.

### Mod load order

Ordering mods incorrectly can lead to problems in game. The following section will give general tips on load order and a general load order guide. Ordering mods correctly will reduce problems, but is not guaranteed to fix direct mod incompatibilities.

**General Tips**

1. Mods at the top of the list are loaded first, mods lower down will generally overwrite if they're allowed.
2. Stellaris loads mods depending on file naming. Load orders are mostly important in the case of submods, and ui mods, as submods tend to use the same file name as the base mod itself.

1. Mods can be ordered in two ways.
 - Irony Mod Manager (IMM): In IMM mods can be ordered in the right hand Collection Mods panel. Mods can be moved by clicking and holding the left mouse button while dragging the mod up or down the list. A mod can also be moved by editing their order number, or moved to first/last position or moved up or down by one position using the arrow icons to the left and right of the mod number. Once ordering is done click apply.
 - Paradox Launcher: Similar to IMM you can drag a mod up or down, or renumber the mod to change its order.

2. Mods beginning with **~** go at the very top of the list.
3. Mods beginning with **!** go towards the bottom.
4. Mods that resolve conflicts (patch mods) between 2 or more mods go anywhere below the mods they patch. A section after all your normal mods is probably better for organization and visualization.
5. Mods that are submods go below the main mod. For example, Planetary Diversity would be higher in the load order, and the sub modules (such as Planetary Diversity – Exotic Worlds) go below Planetary Diversity main mod.

**General Order**

- Mods inside the brackets are just examples of some mods that fit these descriptions, the actual modlist is nonesense.
- The category of mods is highly unlikely to matter outside of this list. A shipset doesn't need to go below or above a technology mod or vice versa.

1. Unofficial patches (Ariphaos Unofficial Patch)
2. Gameplay mods (Planetary diversity, Extra ship components: next, Gigastructural engineering. Etc.)
3. Submods and patches (Planetary Bugversity, Acquisition of technology, Playable Katzenartig Imperium. Etc.)
4. UI mods (UI Overhaul Dynamic)
5. UI patches (UI Overhaul Dynamic – Extended Topbar, UI Overhaul Dynamic + Ethics and Civics Classic)
6. Universal patches (Meger of rules, universal resource patch)

**Mod list example**

- Category will be in brackets
- This list shows what a normal load order could look like, rearranging any of the gameplay mods will not change the outcome.

1. Ariphaos Unofficial Patch (Unofficial patch)
2. Amazing space battles (Gameplay mod)
3. Planetary Diversity (Gameplay mod)
4. Ethics & Civics: Bug Branch (Gameplay mod)
5. Gigastructural Engineering (Gameplay mod)
6. Ancient Cache of Technologies (Gameplay mod)
7. Acquisition of Technology (Submod)
8. ACOT + Bug Branch FE Fix (patch)
9. Planetary Bugversity (Submod)
10. Ui overhaul dynamic (UI mod)
11. UI Overhaul Dynamic + Planetary Diversity (UI submod)
12. UI Overhaul Dynamic + Bug Branch (UI submod)
13. Meger of rules (Universal patch)
14. Universal resource patch (Universal patch)