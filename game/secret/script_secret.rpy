label secret:
    scene black with fade
    play music "<loop 0>secret/space_classroom.mp3"
    show digi at center with Dissolve(3)
    $ persistent.seen.add("digi")
    digi "Oh, you're back."
    digi "You keep ending up in scenes that don't exist."
    digi "It takes a while to write these, you know?"
    digi "I'm a busy guy. I have a whole game to make."
    digi "Like, listen. I like you. You're a digger of rabbit holes.{w} A finder of secrets."
    digi "Just, don't blame {i}me{/i} when things break."
    hide digi with dissolve
    window hide
    pause 3.0
