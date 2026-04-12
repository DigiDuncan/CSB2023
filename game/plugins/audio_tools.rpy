init python:
    # Given a raw filename, map it to its internal jukebox ID
    def find_id_by_filename(track):
        for id, data in MUSIC_MAP.items():
            if data.get("file") == track:
                return id

    # Given a jukebox ID, find a track in the audio store
    def find_store_by_id(track):
        return getattr(store.audio, track, None)

    # Handles the "Now Playing" in the pause menu
    def get_now_playing():
        current = re.sub(r'(<.*>)', "", str(renpy.music.get_playing("music")), flags=re.IGNORECASE)

        song = None
        if current:
            for t in MUSIC_MAP:
                if current == MUSIC_MAP[t]["file"]:
                    song_id = t
                    current_song = MUSIC_MAP[t]["title"]
                    current_artist = MUSIC_MAP[t]["artist"]
                    song = (current_song, current_artist)

        return song