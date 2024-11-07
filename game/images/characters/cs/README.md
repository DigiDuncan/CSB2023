Hello, asset peruser!

As of 11/7/2024, these assets have been "remastered", in a semi-peculiar way.
The changes are documented and their drawbacks are explained here, in case rollbacks are desired or changes are needed.

The `.psd` file is provided in the root folder. Individual layers could be exported if the team decided to go down the route of utilizing Tate's LayeredImage solution for outfits. (See the bottom of this page for an important note about this PSD file.)

## CHANGES
- All previous CS assets have been moved to `/_old`, except for:
  - `CSnake_Angry` -> `snake/angry`
  - `CSnake_worried_gown` -> `snake/worried_gown`
  - `fake_god`
  - `guitar`
  - `horse`
- All assets otherwise were remade, and moved to subfolders:
  - [no prefix] -> `base/`
  - `ce/` -> `coat/`
  - `full` -> `full/`
  - `insane` -> `insane/`
  - `metal` -> `gown/`
  - `pencil` -> `pencil/`
  - `prison` -> `prison/`
  - `robe` -> `robe/`
  - `CSnake_` -> `snake/`
- Expressions that were not yet used in the game were created using the nine currently available faces.
- Some assets were renamed in a way not detailed above:
  - `disappointedmetal` -> `gown/eyepatch`
  - `disappointedmetal2` -> `gown/neutral`
  - `disappointedmetal3` -> `gown/disappointed`
  - `disappointedmetal4` -> `gown/scared`
  
## NOTES/DRAWBACKS
Due to the way these assets were unified, some compromises and caveats exist:
- All half-body sprites have had three pixels trimmed from the bottom, meaning CS' sprites are now **877** as opposed to **880** pixels tall. As a side note, I don't know if CS' sprite being 880px tall was intentionally a cs188 joke, but if it was, sadly this refactor compromises that, since several of the outfits (namely ones based on the guard design) don't line up correctly with the neck otherwise.
- All assets were designed to match the original art resolution of 2018px height, which when cropped to the half-body shot used for most of the game, puts the image height at 1166px. The game, however, assumes these sprites to be 877px tall. To accomplish this, some art was upscaled to 1166px, then downscaled back to 877px on export. This may mean that some facial expressions experienced minor loss of quality.
- The eyepatch component was redrawn from scratch.
- The face shadow component used in the robe outfit was redrawn from scratch.
- Several outfits were masked from their original sprite art to be overlay layers. As of such, there may be minor inconsistencies in outline width, brush style, etc. The intention is to minimize the pixels changed per sprite change, as to be less noticable to the eye, but that comes at the cost at some sprites not holding up as consistent under scrutiny.
- Some outfits are missing from the `.psd` file, due to erroneous destructive edit. If you edit the PSD to include these outfits, *please* re-export the corropsonding sprites in order to maintain consistency with the template.
  - Pencil
  - Robe/Robe Shadow