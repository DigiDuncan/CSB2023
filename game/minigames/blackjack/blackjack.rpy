init python:
    def get_hand_score(hand) -> int:
        score = 0
        aces_held = 0

        # Scoring everything but the ace
        for card in hand:
            if "Ace" not in card["rank"]:
                score += card["points"]

            elif "Ace" in card["rank"]:
                aces_held += 1

        # Aces only
        for a in range(aces_held):
            if score + 11 <= 21:
                score += 11
            else:
                score+= 1
            
        return score

    def draw_card(deck, hand):
        if deck:
            hand.append(deck[-1])
            deck.remove(deck[-1])

    def dealer_logic(deck, hand, score):
        if score < 17:
            draw_card(deck, hand)
        elif score >= 17 and score <= 21:
            pass # stand

    def dealer_sprites(dealer_sprite, game_state, player_won):
        dealer_img = "minigames/blackjack/luigi_deal.png"

        # Handle dealer sprites
        if game_state in ["setup", "stand"]:
            dealer_img = "minigames/blackjack/luigi_deal.png"
        elif game_state == "draw":
            dealer_img = "minigames/blackjack/luigi_wait.png"
        elif game_state == "end" and player_won == True:
            dealer_img = "minigames/blackjack/luigi_wait.png"
        elif game_state == "end" and  player_won == False:
            dealer_img = "minigames/blackjack/luigi_win.png"

        return dealer_img

screen blackjack():
    modal True
        
    timer 1:
        action [
            Play("music", "luigis_casino.ogg", if_changed=True, loop=True),
            Function(persistent.heard.add, "luigis_casino")
        ]

    default master_deck = [
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

    default deck = master_deck
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
    default dealer_sprite = "minigames/blackjack/luigi_deal.png"

    # text game_state
    # text "\n"+game_result
    # text str(dealer_score)

    add "minigames/blackjack/bg.png"
    add dealer_sprites(dealer_sprite, game_state, player_won):
        xalign 0.5
    add "minigames/blackjack/fg.png"

    if game_state == "setup":
        $ dealer_sprite = dealer_sprites(dealer_sprite, game_state, player_won)
        # Construct card images from the sprite sheet
        python:
            # Also reset the deck in case we're playing again
            deck = master_deck

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
                textbutton _("Shuffling cards..."):
                    xalign 0.5 yalign 0.5 text_align 0.5
                    text_color gui.text_color
                    # Now THIS should prevent the skipping bug.
                    action [
                        SensitiveIf(False),
                        NullAction() 
                    ]
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

    else:        
        # Draw the field
        frame:
            background None
            xalign 0.5 yalign 1.0 yoffset -24
            xsize 1500 ysize 400

            # Deck / Hit + Stand buttons
            frame:
                background None
                xalign 0.8 yalign 0.5
                button:
                    if len(deck) > 0:
                        
                        action [
                            SensitiveIf(game_state == "draw"),
                            Function(draw_card, deck, player_hand),
                            Function(renpy.restart_interaction)
                        ]
                    vbox:
                        frame:
                            background None

                            xsize card_size[0] ysize card_size[1]
                            xalign 0.5 yalign 0
                            if len(deck) > 0:
                                for ndx, card in enumerate(deck):
                                    add card_back:
                                        rotate -45
                                        xalign 0.5 yalign 0.5
                                        yoffset -0.25*ndx

                        text _("Hit!"):
                            xalign 0.5 text_align 0.5
                            idle_color gui.text_color
                            hover_color gui.hover_color
                            insensitive_color gui.insensitive_color
                            outlines [ (absolute(4.5), "#000", absolute(0), absolute(0)) ]
                            
                        textbutton _("Stand!"):
                            xalign 0.5 text_align 0.5
                            text_idle_color gui.text_color
                            text_hover_color gui.hover_color
                            text_idle_outlines [ (absolute(4.5), "#000", absolute(0), absolute(0)) ]
                            text_hover_outlines [ (absolute(4.5), "#000", absolute(0), absolute(0)) ]
                            text_insensitive_outlines [ (absolute(4.5), "#000", absolute(0), absolute(0)) ]
                            action [
                                SensitiveIf(game_state == "draw"),
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
                        add player_hand[ndx]["image"]:
                            zoom 1.5

                # Display score
                $ player_score = get_hand_score(player_hand)
                text _("Score: ") + str(player_score):
                    xalign 0.5 text_align 0.5
                    color gui.idle_color
                    outlines [ (absolute(4.5), "#000", absolute(0), absolute(0)) ]
                    size 28

            # Dealer's side
            vbox:
                xsize 1.0 ysize card_size[1]
                xalign 0.5 yalign 0
                box_reverse True

                hbox:
                    # Dealer's hand
                    for ndx, card in enumerate(dealer_hand):

                        if game_state == "draw":
                            if ndx == 1:
                                add card_back
                            else:
                                add dealer_hand[ndx]["image"]
                        else:
                            add dealer_hand[ndx]["image"]

                # Display score
                $ dealer_score = get_hand_score(dealer_hand)
                if game_state == "draw":
                    $ dealer_score_text = "?"
                else:
                    $ dealer_score_text = str(dealer_score)

                text _("Score: ") + dealer_score_text:
                    xalign 0.5 text_align 0.5
                    color gui.idle_color
                    outlines [ (absolute(4.5), "#000", absolute(0), absolute(0)) ]
                    size 28

        # Draw this on top of everything else at the end
        if game_state == "end":
            frame:
                xsize 950 ysize 200
                xalign 0.5 yalign 0.5
                
                text game_result+" Play again?":
                    xalign 0.5 yalign 0.2 text_align 0.5
                
                textbutton _("Yes"):
                    xalign 0.3 yalign 0.8 text_align 0.5
                    action [
                        SelectedIf(False),
                        ShowTransient("blackjack")
                    ]
                textbutton _("No"):
                    xalign 0.7 yalign 0.8 text_align 0.5
                    action [
                        Stop("music", fadeout=0.5),
                        Return(player_won)
                    ]

    # Game logic
    python:
        if game_state == "draw":
            # Player busts, BUT prevent the two aces on first turn == 22 thing
            if player_score > 21:
                current_score = get_hand_score(player_hand) 

                if current_score > 21:
                    game_result = "Bustin' makes me feel bad!"
                    game_state = "end"
                    player_won = False
                    renpy.restart_interaction()
                
            # Try to fix blackjack (10 + ace)
            elif player_score == 21 and len(player_hand) == 2:
                game_result = "You got a Blackjack!"
                game_state = "end"
                player_won = True
                renpy.restart_interaction()

        elif game_state == "stand":
            # Dealer draws
            if dealer_score < 17:
                dealer_logic(deck, dealer_hand, dealer_score)
                dealer_score = get_hand_score(dealer_hand)
                renpy.restart_interaction()

            # Dealer gets a blackjack (10 + ace)
            elif dealer_score == 21 and len(dealer_hand) == 2:
                game_result = "Dealer got a blackjack!"
                game_state = "end"
                player_won = False
                renpy.restart_interaction()

            # Dealer is closer to 21
            elif dealer_score > player_score and dealer_score <= 21:
                game_result = "Dealer wins!"
                game_state = "end"
                player_won = False
                renpy.restart_interaction()

            # Dealer busts but also prevent the aces high thing
            elif dealer_score > 21:
                current_score = get_hand_score(dealer_hand) 

                if current_score > 21:
                    game_result = "Bust goes the dealer!"
                    game_state = "end"
                    player_won = True
                    renpy.restart_interaction()

            # Player is closer to 21
            elif player_score > dealer_score and player_score <= 21:
                game_result = "You win!"
                game_state = "end"
                player_won = True
                renpy.restart_interaction()

            # Player busts
            elif player_score > 21:
                game_result = "Bustin' makes me feel bad!"
                game_state = "end"
                player_won = False
                renpy.restart_interaction()

            # It's a draw
            elif dealer_score == player_score:
                game_result = "It's a draw!"
                game_state = "end"
                player_won = False
                renpy.restart_interaction()            