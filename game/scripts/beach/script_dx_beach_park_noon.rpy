label beach.park_noon:
    "Pretend an event happened at the park at noon."
    "Returning to the map."
    call screen beach_overworld_map(
        current_time = "dusk",
        current_location = (1109, 531, "Downtown"),
        left_hand = "arc", 
        right_hand = "cs", 
        jump_points = [ 
            (500, 690, "Beach\n{size=-12}(Unimplemented){/size}", "beach.beach_dusk"),
            (1400, 690, "Boardwalk\n{size=-12}(Unimplemented){/size}", "beach.boardwalk_dusk"),
            (1200, 300, "Downtown\n{size=-12}(Unimplemented){/size}", "beach.downtown_dusk"),
            (600, 450, "Park\n{size=-12}(Unimplemented){/size}", "beach.park_dusk")
        ]
    ) 