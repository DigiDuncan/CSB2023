### GRAMMAR
- Make sure all writing is in present tense.
> CS walks into the room.
- The word "like" (and other filler words like 'um') should be surrounded by commas.
> You haven't said anything, like, at all.

- Instances of the Christian God should have a capital G.
- cs188 (with the number) should be lowercase.
- CS (without the number) should be uppercase.
- Sentences should not be connected with commas.
- Do not use all caps for emphasis, use italics. (or shake text!)
- Em-dashes (when used to cut off a sentence) should be represented with --.
- Small text (like whispering) should use the prefix `{size=-15}`

### FILES
- Backgrounds must be 1920x1080
- All audio should be 44.1kHz 16bit .ogg 
- SFX must have the `sfx_` prefix and be placed in the `/sfx` folder.
- Videos have to be awfully encoded (enforced by Ren'Py), use Handbrake and make a `.webm` with Vorbis audio.
    - PLEASE use 1:1 pixel ratio. that's why fail_end was broken.

### CODE
- When labelling characters in script_start, it goes in the order:
    - `<character> <form> <emotion> <outfit> <time/color shader> <flipped>`
    - An example would be: `mean human happy hat dark flipped`
- All music and sound effects should be defined in `script_start`, under the correct header.
    - Do not use `<loop 0>`, it doesn't do anything.
    - Do not use `volume 1`, it also doesn't do anything.
- All labels should start with the route they're a part of.
    - Example: `train_start` or `fired_new_plan`
- At the beginning of a new label, re-setup the character positions and music.
    - If a music track should continue from the last label, use `if_changed` at the end of the `play` statement.
    - Test your label by jumping to it with the debug menu and making sure it looks right.
- If you play a music track, make sure:
    - It's in the Jukebox
    - You show the music popup with `music <title> - <artist>`
    - You call `music end` when the music is over
- DO NOT USE `with fade`
    - Use `with dissolve`
    - Just trust us

### CHECKS BEFORE RELEASE
- Is all music in the jukebox?
- Does all music have a popup?
- Is all music audio balanced?
- Does every important character have a bio?
- Does every very important character have a beep?
- Are choices marked with their type in the menus for Streamer Mode?
- Do all characters transition onto screen smoothly?
- Are all fade transitions using `dissolve`?
- Do all important choices result in an achievement?
- Are all backgrounds, character sprites, music, and sound effects declared as variables?
- Have all minigames been tested thoroughly?
- Have the RPG fights been balance tested?
- Are all endings added in the endings registry?
- Are all minigames added in the minigames registry?
- Did Tate do a grammar pass?
- Did Baker do an asset pass?

### WORKFLOW
- Flowchart
- Script writing
- Basic asset creation
- Basic transitions
- Music
- Sound effects
- Grammar pass
- Asset pass
- Transition/cinematography pass
 - Video creation would happen here
- Add music to jukebox
- Add bios
- Add achievements
- Add minigames (optional)