label beach.boardwalk_dawn:
    "Pretend an event happened at the boardwalk at dawn."
    "Returning to the map."
    call screen beach_overworld_map(
        current_time = "day",
        current_location = (1109, 531, "Boardwalk"),
        left_hand = "arc", 
        right_hand = "cs", 
        jump_points = [ 
            (500, 690, "Beach\n{size=-12}(Unimplemented){/size}", "beach.beach_day"),
            (1400, 690, "Boardwalk\n{size=-12}(Unimplemented){/size}", "beach.boardwalk_day"),
            (1200, 300, "Downtown\n{size=-12}(Unimplemented){/size}", "beach.downtown_day"),
            (600, 450, "Park\n{size=-12}(Unimplemented){/size}", "beach.park_day")
        ]
    ) 