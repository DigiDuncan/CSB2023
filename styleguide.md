# CS Bounciness III & CS Bounciness HD I.5 + II.5 Style Guide

## File Structure

* Script files (minus the main file, `script.rpy`), go in `/scripts`.
* Image files go in `/images`.
  * Background images go in `/images/background`.
  * Character images go in `/images/characters`.
* ~~Audiophiles~~ Audio files go in `/audio`.
* Videos files go in `/movies`.
* GUI files go in `/gui`.
* All other files go in the root (`/game`) directory (as of 2023/06/05, this may change.)
* `monika.chr` should be ~~deleted~~ i̘͐͊n̩͇̊ t̷͐̄h̸̖᷊e̢ͤ᷀ ǵ̲͝ä̲̖m̧᷊͍e̱͋͘'̦ͮͥs᷊̮ͩ f͈̠͡ḯ̜̍l̩᷅̚e̡̝̔s̬ͯ̎ a͑́̽t̜᷊͝ a̰͋͒l̫͂͊l̢͔̒ t͂́͢i̺̟̻m̘̯͞e͏̏̃s̸̡͋.̡̪͊

## Python Rules

* Indentation levels should be marked by four spaces (soft tabs).
* There should not be a newline to begin an indented block.  
  **Example:** 
  ```python
    label special:
        CS "Take this!"
    ```
* Comments should follow the format `# <comment>`.
  * TODO comments should follow the format `# TODO: <comment>`.
* There should be a space surrounding both sides of operators.  
  **Example:**
  ```python
  stupidity = True
  ```

## Ren'Py Rules

* Blocks of dialog and blocks of statements should be separated by a newline.  
  **Example:**
  ```python
    CS "Take this!"
    "{i}CS chops Wesley and a fight ensues.{/i}"
    Wesley "You'll pay for that!"
    CS "Like hell I will!"

    hide cs with easeoutleft
    hide wesley with easeoutright
    hide helipad with fade
  ```
* Narrator dialog should be denoted as a bare string.  
  **Example:**
  ```python
  "{i}The three dig their way out of the cell and make a break into the dark of the evening.{/i}"
  ```
* One-off characters without definitions should be called by creating a `Character` object on the dialog line.  
  **Example:**
  ```python
  Character("HoH SiS operator") "{i}hangs up{/i}"
  ```
* Modifier statements should be on the same line as the statement they modify.  
  **Example:**
  ```python
    show ed at right with easeinright
  ```
* Label names **must be unique across all files.**
* Definitions (of characters, images, audio, and video) should be done in `definitions.rpy`.

## Naming Conventions

* Character objects should be named in PascalCase.
* Images, audio, and videos should be named in snake_case. (All lowercase with underscores.)
  * This includes their filenames.

## Images

* Backgrounds should be opaque PNGs of resolution 1920x1080.
* Characters should be transparent PNGs of variable width, and look good next to CS.

## Sound

* Use mp3 for the music format.
* Use ogg for sound effects.