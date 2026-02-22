---
title: "User interface"
categories: ["4.2", "Stellaris", "Guides"]
---

# User interface

Stellaris' Interface , also called graphical user interface ( GUI or simply UI ), has a number of specific screens and visual elements. This article will focus on the pragmatic purpose and utility of the interface (as opposed to the stylistic elements).

The first portion focuses on the game setup interface prior to any actual gaming while later portions deal with the in-game interface itself.

## Launcher

The Stellaris game launcher is used to handle all pre-game options before launching the game. It is divided into two main sections as described below.

**Tabbed section:**

- News tab - Shows any recent developments regarding Stellaris. Clicking on the displayed banner will open the source in the browser.
- DLC tab – Lists all available DLCs and add-ons with quick enable/disable options.
- Mods tab – Lists all available mods with quick enable/disable options. Also available are the mod tools for mod creation and uploading.

**Bottom section:**

- Clear User Directory - Clears some user created content. Recommended if experiencing crashes.
- Language - Pick one of the following game languages: English, French, German, Polish, Portuguese, Russian, Spanish or Chinese.
- Sound - Enable/disable sound in the launcher.
- Display - Setup initial display parameters for: display mode, resolution and refresh rate.
- Paradox account – Used to create/log-in to the PDX account if one wishes to use features such as leader-boards, etc.
- Play - launches the game itself.

## Main menu

**Menu options**

- Usual variety of game related options; of note:
- Multiplayer - Based on the Steam network code and requires client to be online
- Cooperative (beta) - Special multiplayer mode which allows up to five players to simultaneously play as one empire. Like traditional multiplayer, it requires the client to be online.
- Settings - More options to tweak graphics, audio and controls options (details below).
 - Graphics - Options for display mode, resolution, refresh rate, multisample level, graphics quality, bloom quality, lens flare toggle and UI scaling.
 - Sound - Options for voice-over (if available), master volume slider and separate volume sliders for: effect, music ambient and advsior.
 - Gameplay - Options for autosave frequency, cloud save (uses Steam), tutorial toggle and event popup/auto-pause.

**Game version**

- Patch code-name and version
- Checksum - Calculated again after loading game assets
- Hovering shows the SVN revisions of the game, engine and external libraries

**Social media**

- Various game-related links: Website , Forums , Facebook , Twitter , YouTube , Discord

## Single player

Main article: Beginner's guide#Choosing an empire

- Single-player setup
- Species setup

When starting a new game players have the choice to pick one of the game's pre-defined species, player-created species (indicated by a phoenix icon which, if enabled, may also appear in other campaigns) or a randomly generated species.

Players who opt to customize their own species (either by Create new option or Edit of an exiting setup) are greeted by the species setup screen. This screen allows players to change anything from cosmetics - appearance and names of species, homeworld, ships and flag - to more defining features - species traits, government, ethics and civics. Players can review their species of choice before proceeding forward.

The final step before the game starts involves the galaxy setup options (same options as shown to the right in the MP screen setup below). Options vary from galaxy size and shape to number of AI players and difficulty.

## Multiplayer

- Multiplayer host
- Multiplayer servers

**Hosting a new game**

Hosting a new game requires only a server name. A host can choose to set a password to restrict the server to specific people and use tags/description to give joining players a general idea of what they should expect.

Once the server is created, a game lobby will open, where the host can configure the galaxy settings, following same process as in singleplayer. Other players can join the lobby and configure their empires.

The ServerID (shown when hovering above the server icon below the galaxy settings section) can also be given to other players, allowing them to use Direct Join to join this specific MP session.

Once all players are ready, the host can start the game.

**Hosting a save game**

If the game is a continuation of a previous session, the host needs to choose the Host Saved Game option and - after repeating the first step (setting server name, password, etc.) - pick the save game to host (singleplayer saves may be used as well).

This will not create a game lobby and will instead load the save directly. Once the game is loaded, the host can select an empire to play (or join as observer). A similar process is then repeated for other players joining the game.

To copy the ServerID of a hosted save game into the clipboard, the host can click on the pause icon while holding Ctrl .

**Joining a game**

Players looking to join a MP game can scan for servers (shows closest servers) to look for games about to start or ones already in-progress. If players can't find a specific session they can use the Direct Join function to input the ServerID given to them by the host player.

If the game has already started (or is a hosted save game), the player will have to hot-join instead of joining a game lobby. Once hot-joining players finish receiving the save (containing the data required for them to join the session), they cannot create or select their own empires, and instead have to pick one of the existing empires within the game.

## Load game

Stellaris employs a somewhat more advanced save system compared to other (older) PDS games.

- Saves are sorted per campaign (left half) with individual saves within the campaign (right half).
- Gauntlet icon - Indicates an ironman game; meaning, one (auto-) save per campaign. Note: This currently requires Steam cloud synchronization (local save not supported at present).
- Floppy disk icon - Indicates a version-incompatible save game. This usually occurs after major patch updates. To continue the saved game without issues it is recommended to roll back to the save-game's version (via Steam -> Betas tab).
- Cloud icon - Indicates whether this is a local-save (red), a cloud-save (green) or in the middle of cloud-save synchronization (blue).
- Garbage bin icon - Used to delete saves. Can be done for per campaign or per individual save. To enable deletion, click the bin icon, proceed to delete saves, and click the bin icon again to disable deletion.
- Individual saves also display the player's number of fleets and number of controlled planets.
- Autosave frequency is player dependent (through Settings --> Gameplay/Autosave frequency).

**Save Game Location**

| OS | Location |
|---|---|
| Windows auto saves (including ironman saves) | \Steam\userdata\%STEAMUSERID%\281990\remote\save games\$EMPIRENAME+ID\ |
| Windows custom saves | %USERPROFILE%\Documents\Paradox Interactive\Stellaris\save games\$EMPIRENAME+ID\ |
| Mac | $HOME/Documents/Paradox Interactive/Stellaris/save games/$EMPIRENAME+ID |
| Linux | $HOME/.local/share/Paradox Interactive/Stellaris/save games/$EMPIRENAME+ID ( $XDG_DATA_HOME is ignored!) |
| Linux (newer versions) | $STEAMFOLDER/userdata/$STEAMID/281990/remote/save games/$EMPIRENAME+ID |