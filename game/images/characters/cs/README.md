Hello, asset peruser!

As of 11/8/2024, these assets have been "remastered", in a semi-peculiar way.
The changes are documented and their drawbacks are explained here, in case rollbacks are desired or changes are needed.

The `.psd` file is provided in the root folder. Individual layers could be exported if the team decided to go down the route of utilizing Tate's LayeredImage solution for outfits.

## CHANGES
- CS's base texture was based on the full-resolution `full/neutral` art, with some edits for cleanliness.
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
- New sprite packs were made:
  - `/christmas`
  - `/christmas_full`
  - `/coat`
  - `/coat_hat`
  
## NOTES/DRAWBACKS
Due to the way these assets were unified, some compromises and caveats exist:
- All half-body sprites have had three pixels trimmed from the bottom, meaning CS' sprites are now **877** as opposed to **880** pixels tall. As a side note, I don't know if CS' sprite being 880px tall was intentionally a cs188 joke, but if it was, sadly this refactor compromises that, since several of the outfits (namely ones based on the guard design) don't line up correctly with the neck otherwise.
- All assets were designed to match the original art resolution of 2018px height, which when cropped to the half-body shot used for most of the game, puts the image height at 1166px. The game, however, assumes these sprites to be 877px tall. To accomplish this, some art was upscaled to 1166px, then downscaled back to 877px on export. This may mean that some facial expressions experienced minor loss of quality.
  - The full-height sprite, in order to stay consistent with the half-body shot, ends up at 1518px.
- The eyepatch component was redrawn from scratch.
- The face shadow component used in the robe outfit was redrawn from scratch.
- Several outfits were masked from their original sprite art to be overlay layers. As of such, there may be minor inconsistencies in outline width, brush style, etc. The intention is to minimize the pixels changed per sprite change, as to be less noticable to the eye, but that comes at the cost at some sprites not holding up as consistent under scrutiny.
- The robe outfit is not include in the PSD due to it's unusual final size.
- The crop box is slighty wrong when the PSD is resized to 1518px. To solve it, extend the bottom of the rectangle by 2px.