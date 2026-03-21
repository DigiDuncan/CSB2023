# These functions are used only for the character selection screens. Do not modify without talking to Tate.

init python:
    # Fill a given slot
    def rpg_fill_slot(slots_list, current_slot, char_stored_data):
        slots_list[current_slot] = char_stored_data

    # Automatically select the next unselected slot (AI-assisted)
    def rpg_slot_autoselect(slots_list, current_slot):

        # Do NOT try party_size*2 again, it is why the screen took two clicks to update
        total_slots = len(slots_list)

        # Load-bearing crash prevention (well, hopefully)
        if total_slots <= 1:
            return 0

        # Search for any empty slots
        for i in range(1, total_slots):
            checked_slot = (current_slot + i) % total_slots
            if slots_list[checked_slot][0] == "(Pending)":
                return checked_slot

        # Failsafe - just give me the next slot
        return (current_slot + 1) % total_slots
