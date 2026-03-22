label beach.beach_day:
    "Pretend an event happened at the beach during the day."
    "Returning to the map."
    call screen beach_overworld_map( 
        current_time = "noon",
        current_location = (800, 200, "Some beach"),
        jump_points = [
            (550, 800, "Beach\n{size=-12}(Unimplemented){/size}", "beach.beach_noon"),
            (1400, 690, "Boardwalk\n{size=-12}(Unimplemented){/size}", "beach.boardwalk_noon"),
            (1200, 300, "Downtown\n{size=-12}(Unimplemented){/size}", "beach.downtown_noon"),
            (600, 450, "Park\n{size=-12}(Unimplemented){/size}", "beach.park_noon")
        ]
    )