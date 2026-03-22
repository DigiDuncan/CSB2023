label beach.park_dusk:
    "Pretend an event happened at the park at dusk."
    "Returning to the map."
    call screen beach_overworld_map(
        current_time = "night",
        current_location = (1109, 531, "Downtown"),
        left_hand = "arc", 
        right_hand = "cs", 
        jump_points = [ 
            (500, 690, "Beach\n{size=-12}(Unimplemented){/size}", "beach.beach_night"),
            (1400, 690, "Boardwalk\n{size=-12}(Unimplemented){/size}", "beach.boardwalk_night"),
            (1200, 300, "Downtown\n{size=-12}(Unimplemented){/size}", "beach.downtown_night"),
            (600, 450, "Park\n{size=-12}(Unimplemented){/size}", "beach.park_night")
        ]
    ) 