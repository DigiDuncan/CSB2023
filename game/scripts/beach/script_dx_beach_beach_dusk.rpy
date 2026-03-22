label beach.beach_dusk:
    "Pretend an event happened at the beach at dusk."
    "Returning to the map."
    call screen beach_overworld_map( 
        current_time = "night",
        current_location = (800, 200, "Some beach"),
        jump_points = [
            (550, 900, "Beach\n{size=-12}(Unimplemented){/size}", "beach.beach_night"),
            (1400, 690, "Boardwalk\n{size=-12}(Unimplemented){/size}", "beach.boardwalk_night"),
            (1200, 300, "Downtown\n{size=-12}(Unimplemented){/size}", "beach.downtown_night"),
            (600, 450, "Park\n{size=-12}(Unimplemented){/size}", "beach.park_night")
        ]
    )