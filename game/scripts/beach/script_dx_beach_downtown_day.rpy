label beach.downtown_day:
    "Pretend an event happened downtown during the day."
    "Returning to the map."
    call screen beach_overworld_map(
        current_time = "noon",
        current_location = (1109, 531, "Downtown"),
        left_hand = "arc", 
        right_hand = "cs", 
        jump_points = [ 
            (500, 690, "Beach\n{size=-12}(Unimplemented){/size}", "beach.beach_noon"),
            (1400, 690, "Boardwalk\n{size=-12}(Unimplemented){/size}", "beach.boardwalk_noon"),
            (1200, 300, "Downtown\n{size=-12}(Unimplemented){/size}", "beach.downtown_noon"),
            (600, 450, "Park\n{size=-12}(Unimplemented){/size}", "beach.park_noon")
        ]
    ) 