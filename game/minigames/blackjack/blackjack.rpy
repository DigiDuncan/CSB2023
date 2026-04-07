init python:
    def get_hand_score(hand) -> int:
        score = 0
        # Scoring
        for card in hand:
            if "Ace" in card["rank"]:
                if score >= 21:
                    score += 1
                else:
                    score += card["points"]
            else:
                score += card["points"]
        return score

screen blackjack():
    modal True
    $ renpy.choice_for_skipping()

    default deck = [
        { "suit": "clubs", "rank": "Ace", "points": 11 }, 
        { "suit": "clubs", "rank": "2", "points": 2 }, { "suit": "clubs", "rank": "3",  "points": 3 }, { "suit": "clubs", "rank": "4", "points": 4 }, 
        { "suit": "clubs", "rank": "5", "points": 5 }, { "suit": "clubs", "rank": "6", "points": 6 }, { "suit": "clubs", "rank": "7", "points": 7 }, 
        { "suit": "clubs", "rank": "8", "points": 8 }, { "suit": "clubs", "rank": "9", "points": 9 },  { "suit": "clubs", "rank": "10",  "points": 10 }, 
        { "suit": "clubs", "rank": "Jack", "points": 10 }, 
        { "suit": "clubs", "rank": "Queen",  "points": 10 }, 
        { "suit": "clubs", "rank": "King",  "points": 10 },

        { "suit": "spades", "rank": "Ace", "points": 11 }, 
        { "suit": "spades", "rank": "2", "points": 2 }, { "suit": "spades", "rank": "3",  "points": 3 }, { "suit": "spades", "rank": "4", "points": 4 }, 
        { "suit": "spades", "rank": "5", "points": 5 }, { "suit": "spades", "rank": "6", "points": 6 }, { "suit": "spades", "rank": "7", "points": 7 }, 
        { "suit": "spades", "rank": "8", "points": 8 }, { "suit": "spades", "rank": "9", "points": 9 },  { "suit": "spades", "rank": "10",  "points": 10 }, 
        { "suit": "spades", "rank": "Jack", "points": 10 }, 
        { "suit": "spades", "rank": "Queen",  "points": 10 }, 
        { "suit": "spades", "rank": "King",  "points": 10 },

        { "suit": "hearts", "rank": "Ace", "points": 11 }, 
        { "suit": "hearts", "rank": "2", "points": 2 }, { "suit": "hearts", "rank": "3",  "points": 3 }, { "suit": "hearts", "rank": "4", "points": 4 }, 
        { "suit": "hearts", "rank": "5", "points": 5 }, { "suit": "hearts", "rank": "6", "points": 6 }, { "suit": "hearts", "rank": "7", "points": 7 }, 
        { "suit": "hearts", "rank": "8", "points": 8 }, { "suit": "hearts", "rank": "9", "points": 9 },  { "suit": "hearts", "rank": "10",  "points": 10 }, 
        { "suit": "hearts", "rank": "Jack", "points": 10 }, 
        { "suit": "hearts", "rank": "Queen",  "points": 10 }, 
        { "suit": "hearts", "rank": "King",  "points": 10 },

        { "suit": "diamonds", "rank": "Ace", "points": 11 }, 
        { "suit": "diamonds", "rank": "2", "points": 2 }, { "suit": "diamonds", "rank": "3",  "points": 3 }, { "suit": "diamonds", "rank": "4", "points": 4 }, 
        { "suit": "diamonds", "rank": "5", "points": 5 }, { "suit": "diamonds", "rank": "6", "points": 6 }, { "suit": "diamonds", "rank": "7", "points": 7 }, 
        { "suit": "diamonds", "rank": "8", "points": 8 }, { "suit": "diamonds", "rank": "9", "points": 9 },  { "suit": "diamonds", "rank": "10",  "points": 10 }, 
        { "suit": "diamonds", "rank": "Jack", "points": 10 }, 
        { "suit": "diamonds", "rank": "Queen",  "points": 10 }, 
        { "suit": "diamonds", "rank": "King",  "points": 10 }
    ]

    default dealer_hand = []
    default player_hand = []
    default dealer_score = 0
    default player_score = 0
    default card_spritesheet = "minigames/blackjack/cards.png" # You'll want to make sure the cards in this sheet are in the same order as the deck data above.
    default card_size = (73, 98) # Size of one card
    default hovered_card = ""
    default game_state = "setup"

    if game_state == "setup":

        # Construct card images from the sprite sheet
        python:
            for ndx, card in enumerate(deck):

                col_number = 0
                row_number = 0

                # Pick column by rank
                if card["rank"] == "Ace":
                    col_number = 0
                elif card["rank"] == "Jack":
                    col_number = 10
                elif card["rank"] == "Queen":
                    col_number = 11
                elif card["rank"] == "King":
                    col_number = 12
                else:
                    col_number = int(card["rank"])

                # Pick row by suit
                if card["suit"] == "clubs":
                    row_number = 0
                elif card["suit"] == "spades":
                    row_number = 1
                elif card["suit"] == "hearts":
                    row_number = 2
                elif card["suit"] == "diamonds":
                    row_number = 3

                this_card = Crop( 
                    (
                        col_number * card_size[0], 
                        row_number * card_size[1], 
                        card_size[0], 
                        card_size[1]
                    ), 
                        card_spritesheet
                    )

                deck[ndx]["image"] = this_card

            renpy.random.shuffle(deck)
            game_state = "ready"
            
        frame:
            xalign 0.5 yalign 0.5
            vbox:
                xalign 0.5 yalign 0.5
                text _("Shuffling cards..."):
                    xalign 0.5 yalign 0.5 text_align 0.5
                if game_state == "ready":
                    textbutton _("Ready."):
                        xalign 0.5 yalign 0.5 text_align 0.5
                        action SetScreenVariable("game_state", "draw")
            
    elif game_state == "draw":

        # $ hovered_card = GetTooltip() or ""
        # text hovered_card
        
        # frame:
        #     xsize 1200
        #     xalign 0.5 yalign 0.5

        #     vbox:
        #         xalign 0.5 yalign 0.5

        #         text _("Hi, this doesn't work yet. Have some cards."):
        #             xalign 0.5 text_align 0.5

        #         hbox:
        #             xalign 0.5 xsize 1000

        #             textbutton _("Shuffle Again"):
        #                 xalign 0.5 text_align 0.5
        #                 action [
        #                     Function(renpy.random.shuffle, deck),
        #                     Function(renpy.restart_interaction)
        #                 ]

        #             textbutton _("Done."):
        #                 xalign 0.5 text_align 0.5
        #                 action [
        #                     Return(),
        #                     With("dissolve")
        #                 ]
                    
        #         vpgrid:
        #             cols 13
        #             xalign 0.5 yalign 0.5
        #             spacing 5

        #             for ndx, x in enumerate(deck):
        #                 $ this_card = deck[ndx]["rank"]+" of "+deck[ndx]["suit"]

        #                 imagebutton:
        #                     idle deck[ndx]["image"]
        #                     tooltip this_card
        #                     action NullAction()

        # Draw the field
        frame:
            xalign 0.5 yalign 0.5
            xsize 1800 ysize 900

            # Deck / Hit button
            frame:
                background None
                xalign 0.7 yalign 0.5
                button:
                    if len(deck) > 0:
                        action [
                            Function(player_hand.append, deck[-1]),
                            Function(deck.remove, deck[-1]),
                            Function(renpy.restart_interaction)
                        ]
                    vbox:
                        frame:
                            xsize card_size[0] ysize card_size[1]
                            if len(deck) > 0:
                                for ndx, card in enumerate(deck):
                                    add deck[ndx]["image"]:
                                        xalign 0.5 yalign 0.5
                                        yoffset -0.25*ndx
                        text _("Hit!"):
                            xalign 0.5 text_align 0.5

            # Player's side
            vbox:
                xsize 1.0 ysize card_size[1]
                xalign 0.5 yalign 1.0

                hbox:
                    # Player hand
                    for ndx, card in enumerate(player_hand):
                        add player_hand[ndx]["image"]

                # Display score
                $ player_score = get_hand_score(player_hand)
                text _("Score: ") + str(player_score):
                    xalign 0.5 text_align 0.5
