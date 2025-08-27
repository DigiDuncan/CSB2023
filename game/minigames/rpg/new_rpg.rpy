init python:
    import math

    class NewRPGGameDisplayable(renpy.Displayable):
        def __init__(self):
            renpy.Displayable.__init__(self)
            self.start_time = None
            self.win = None

        def render(self, width, height, st, at):
            if self.start_time is None:
                self.start_time = st
            r = renpy.Render(1920, 1080)
            s = r.canvas()
            fight_menu = NewFightMenuDisplayable(Fighters.get("ARCEUS"))
            fighterbox_1 = NewStatBlockDisplayable(Fighters.get("ARCEUS"))
            fighterbox_1.define_box_height()
            r.place(fight_menu, 0, 1080-fight_menu.height)
            r.place(fighterbox_1, 0, (1080-fight_menu.height)-fighterbox_1.render_height - 2)
            return r

        def event(self, ev, x, y, st):
            import pygame
            if ev.type == pygame.KEYDOWN and ev.key == pygame.K_END:
                self.win = True
            if self.win is not None:
                return self.win

        def visit(self):
            return [] # Assets needed to load
    
    class NewStatBlockDisplayable(renpy.Displayable):
        def __init__(self, fighter: Fighter):
            # This is where I define everything that needs to be in the stat block
            self.fighter = fighter
            self.fighter_name = Text(self.fighter.display_name, color = "#FFFFFF", size = 52, xanchor = 1.0, textalign = 1.0)
            self.health_text = Text(str(self.fighter.health_points)+"/"+str(self.fighter.max_health)+" HP", size = 32, xanchor= 1.0, textalign = 1.0)
            self.health_bar = Image("gui/rpg/hp_bar.png")
            self.is_turn = True
            self.defense_stat_icon = Image("gui/rpg/defense.png", yanchor = 0.5)
            self.defense_text = Text(str(self.fighter.armor_points), textalign = 0.0, size = 32, yanchor = 0.5)
            self.attack_stat_icon = Image("gui/rpg/attack.png", yanchor = 0.5)
            self.attack_text = Text(str(self.fighter.attack_points), textalign = 0.0, size = 32, yanchor = 0.5)
            self.stat_back_big = Image("gui/rpg/tall_box.png")
            self.stat_back_small = Image("gui/rpg/small_box.png")
            self.attack_button = AttackButtonDisplayable()
            self.defend_button = ImageButton("gui/rpg/defend_button.png")
            self.render_height = 105
            if self.fighter.sprite:
                self.fighter_image = self.fighter.sprite
            else:
                self.fighter_image = Image("gui/rpg/portraits/unknown.png")
            self.sprite_back = Image("gui/rpg/fighter_icon_frame.png", yanchor=0.5)
            super().__init__(self)

        def render(self, width, height, st, at):
            self.define_box_height()
            r = renpy.Render(475, self.render_height)
            if self.is_turn:
                r.place(self.stat_back_big)
                r.place(self.attack_button, x = 10, y = 105) 
                r.place(self.defend_button, x = 250, y = 105)
            else:
                r.place(self.stat_back_small)
            r.place(self.fighter_name, x = 470,y = 0)
            health_bar_size = int(lerp(0, 228, self.fighter.health_points / self.fighter.max_health))
            health_crop = Crop((0, 0, health_bar_size, 50), self.health_bar)
            health_bar_renderer = renpy.render(health_crop, 1920, 1080, st, at)
            r.blit(health_bar_renderer, (470-health_bar_size, 55))
            r.place(self.health_text, x = 470, y = 55)
            r.place(self.sprite_back, x = 10, y = 105/2)
            r.place(self.fighter_image, x = 10, y = 10)
            r.place(self.attack_stat_icon, x = 108, y = (105/16)*5)
            r.place(self.attack_text, x = 138, y = (105/16)*5)
            r.place(self.defense_stat_icon, x = 108, y = (105/16)*11)
            r.place(self.defense_text, x = 138, y = (105/16)*11)
            return r

        def define_box_height(self):
            self.render_height = 105
            if self.is_turn:
                self.render_height = 201
            


    class NewFightMenuDisplayable(renpy.Displayable):
        def __init__(self, fighter: Fighter):
            self.fighter = fighter
            self.attack_count = len(self.fighter.attacks)
            self.height = 262
            self.width = 1916
            super().__init__(self)
        
        def render(self, width, height, st, at):
            r = renpy.Render(self.width, self.height)
            r.place(Image("gui/rpg/main_box.png"))
            return r

    class AttackButtonDisplayable(renpy.Displayable):
        def __init__(self):
            super().__init__(self)
        
        def render(self, width, height, st, at):
            r = renpy.Render(215,87)
            r.place(Image("gui/rpg/attack_button.png"))
            return r

screen newrpggame():
    default newrpggame = NewRPGGameDisplayable()
    # Add a background or any static images here.
    add newrpggame

label play_newrpggame:
    window hide
    $ quick_menu = False
    call screen newrpggame
    $ quick_menu = True
    window show

    if _return == True:
        pass
        # Thing for win condition
    else:
        pass
        # Thing for lose condition

label newrpggame_done:
    # Thing to do after the game if we reach here.
    pass
