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

    def draw_card(deck, hand):
        if deck:
            hand.append(deck[-1])
            deck.remove(deck[-1])

    def dealer_logic(deck, hand, score):
        if score < 16:
            draw_card(deck, hand)
        elif score >= 17 and score <= 21:
            pass # stand

screen blackjack():
    modal True
    $ renpy.choice_for_skipping()
    $ _skipping = False

    # Prevent the skipping bug (I hope)
    key "skip" action NullAction()
    key "toggle_skip" action NullAction()
    key "dismiss" action NullAction()

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
    default card_back = "minigames/blackjack/card_back.png"
    default card_size = (73, 98) # Size of one card
    # default hovered_card = ""
    default game_state = "setup"
    default game_result = ""
    default player_won = None

    # text game_state
    # text "\n"+game_result

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
                    col_number = int(card["rank"])-1

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
                    timer 1:
                        action [
                            # Put two cards in each player's hand
                            Function(draw_card, deck, player_hand),
                            Function(draw_card, deck, player_hand),
                            Function(draw_card, deck, dealer_hand),
                            Function(draw_card, deck, dealer_hand),
                            SetScreenVariable("game_state", "draw")
                        ]

    elif game_state == "draw":

        if player_score > 21:
            $ game_state = "lose"

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
                            Function(draw_card, deck, player_hand),
                            Function(renpy.restart_interaction)
                        ]
                    vbox:
                        frame:
                            xsize card_size[0] ysize card_size[1]
                            xalign 0.5 yalign 0
                            if len(deck) > 0:
                                for ndx, card in enumerate(deck):
                                    add card_back:
                                        xalign 0.5 yalign 0.5
                                        yoffset -0.25*ndx
                        text _("Hit!"):
                            idle_color gui.idle_color
                            hover_color gui.hover_color
                            xalign 0.5 text_align 0.5

                        textbutton _("Stand!"):
                            xalign 0.5 text_align 0.5
                            action [
                                SetScreenVariable("game_state", "stand"),
                                Function(renpy.restart_interaction)
                            ]

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

            # Dealer's side
            vbox:
                xsize 1.0 ysize card_size[1]
                xalign 0.5 yalign 0

                hbox:
                    # Dealer's hand
                    for ndx, card in enumerate(dealer_hand):
                        if ndx == 1:
                            add card_back
                        else:
                            add dealer_hand[ndx]["image"]

                # Display score
                $ dealer_score = get_hand_score(dealer_hand)
                text _("Score: ") + str(dealer_hand[0]["points"]) + "...?":
                    xalign 0.5 text_align 0.5

    elif game_state == "stand":
        # Draw the field
        frame:
            xalign 0.5 yalign 0.5
            xsize 1800 ysize 900

            # Deck / Hit button
            frame:
                background None
                xalign 0.7 yalign 0.5
                
                vbox:
                    frame:
                        xsize card_size[0] ysize card_size[1]
                        xalign 0.5 yalign 0
                        if len(deck) > 0:
                            for ndx, card in enumerate(deck):
                                add card_back:
                                    xalign 0.5 yalign 0.5
                                    yoffset -0.25*ndx
                    text _("Hit!"):
                        xalign 0.5 text_align 0.5
                        color gui.insensitive_color

                    text _("Stand!"):
                        xalign 0.5 text_align 0.5    
                        color gui.insensitive_color            

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

            # Dealer's side
            vbox:
                xsize 1.0 ysize card_size[1]
                xalign 0.5 yalign 0

                hbox:
                    # Dealer's hand
                    for ndx, card in enumerate(dealer_hand):
                        add dealer_hand[ndx]["image"]

                # Display score
                $ dealer_score = get_hand_score(dealer_hand)
                text _("Score: ") + str(dealer_score):
                    xalign 0.5 text_align 0.5
            

    elif game_state == "end":

        # Draw the field
        frame:
            xalign 0.5 yalign 0.5
            xsize 1800 ysize 900

            # Deck / Hit button
            frame:
                background None
                xalign 0.7 yalign 0.5
                
                vbox:
                    frame:
                        xsize card_size[0] ysize card_size[1]
                        xalign 0.5 yalign 0
                        if len(deck) > 0:
                            for ndx, card in enumerate(deck):
                                add card_back:
                                    xalign 0.5 yalign 0.5
                                    yoffset -0.25*ndx
                    text _("Hit!"):
                        xalign 0.5 text_align 0.5
                        color gui.insensitive_color

                    text _("Stand!"):
                        xalign 0.5 text_align 0.5    
                        color gui.insensitive_color            

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

            # Dealer's side
            vbox:
                xsize 1.0 ysize card_size[1]
                xalign 0.5 yalign 0

                hbox:
                    # Dealer's hand
                    for ndx, card in enumerate(dealer_hand):
                        add dealer_hand[ndx]["image"]

                # Display score
                $ dealer_score = get_hand_score(dealer_hand)
                text _("Score: ") + str(dealer_score):
                    xalign 0.5 text_align 0.5

        frame:
            xalign 0.5 yalign 0.5
            vbox:
                text game_result+" Play again?":
                    xalign 0.5 yalign 0.5 text_align 0.5
                hbox:
                    xalign 0.5
                    textbutton _("Yes"):
                        xalign 0.3 text_align 0.5
                        action [
                            SelectedIf(False),
                            ShowTransient("blackjack")
                        ]
                    textbutton _("No"):
                        xalign 0.7 text_align 0.5
                        action Return()
                    
    # elif game_state == "testing":
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

    # Game logic
    python:
        if game_state == "draw":
            if player_score > 21:
                game_result = "Bustin' makes me feel bad!"
                game_state = "end"
                player_won = False
                renpy.restart_interaction()

            elif player_score == 21 and len(player_hand) == 2:
                game_result = "Blackjack!"
                game_state = "end"
                player_won = True
                renpy.restart_interaction()


        elif game_state == "stand":
            if dealer_score < 17:
                dealer_logic(deck, dealer_hand, dealer_score)
                dealer_score = get_hand_score(dealer_hand)
                renpy.restart_interaction()

            elif dealer_score == 21 and len(dealer_hand) == 2:
                game_result = "Dealer had a blackjack!"
                game_state = "end"
                player_won = False
                renpy.restart_interaction()

            elif dealer_score > player_score and dealer_score <= 21:
                game_result = "Dealer wins!"
                game_state = "end"
                player_won = False
                renpy.restart_interaction()

            elif dealer_score > 21:
                game_result = "Bust goes the dealer!"
                game_state = "end"
                player_won = True
                renpy.restart_interaction()

            elif player_score == 21 and len(player_hand) == 2:
                game_result = "Blackjack!"
                game_state = "end"
                player_won = True
                renpy.restart_interaction()

            elif player_score > dealer_score and player_score <= 21:
                game_result = "You win!"
                game_state = "end"
                player_won = True
                renpy.restart_interaction()

            elif player_score > 21:
                game_result = "Bustin' makes me feel bad!"
                game_state = "end"
                player_won = False
                renpy.restart_interaction()

            elif dealer_score == player_score:
                game_result = "It's a draw!"
                game_state = "end"
                player_won = False
                renpy.restart_interaction()            