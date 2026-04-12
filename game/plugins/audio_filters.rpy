#### Audio Filter Templates ####
# Thank you for downloading my filter pack! (https://berinrin.itch.io/audiofilter-templates-for-renpy)
# Just drop this file into your Ren'Py project, and you can start using the audio filters
#
# Example using the walkie_talkie_af filter:
#                                 v sound channel to apply the filter to (e.g. music, sound, voice)
# $ renpy.music.set_audio_filter("sound", walkie_talkie_af)
# play sound <your sound here>
#
# To remove the filter again, set it to "None" like this:
#
# $ renpy.music.set_audio_filter("sound", None)
#
# Check out the official documentation for audio filters if you want to change these (https://www.renpy.org/doc/html/audio_filters.html)
# You don't need to credit me, but if you do it regardless, I'd be happy!
# - Berin
# 

# Please don't change the following line
define af = renpy.audio.filter

##
## Equalizer Effects ##
##

# walkie-talkie filter
define walkie_talkie_af = [af.Highpass(frequency=100), af.Highshelf(frequency=300, gain=2.0), af.Lowpass(frequency=2000), af.Peaking(frequency=900, q=1.00, gain=8.0)]

# telephone filter
define telephone_af = [af.Highpass(frequency=220), af.Highpass(frequency=400), af.Lowpass(frequency=3500), af.Lowpass(frequency=5000)]

# radio filter
define radio_af = [af.Highpass(frequency=35), af.Highpass(frequency=50), af.Lowpass(frequency=5000), af.Lowpass(frequency=6000)]

# Bass (low frequency) boost and bass cut
define basscut_af = [af.Highpass(frequency=300)]
define bassboost_af = [af.Highshelf(frequency=300, gain=3.0), af.Highshelf(frequency=200, gain=3.0), af.Highshelf(frequency=100, gain=3.0)]

# Treble (high frequency) boost and treble cut
define treblecut_af = [af.Lowpass(frequency=6000), af.Lowpass(frequency=8000)]
define trebleboost_af = [af.Lowshelf(frequency=4000, gain=3.0), af.Lowshelf(frequency=5000, gain=6.00)]

##
## Reverb Effects ##
##

define reverb_vocal_af = [af.Reverb(resonance=0.5, dampening=2970, dry=0.9)]
# Heavy reverb, use this one sparingly
define reverb_heavyvocal_af = [af.Reverb(resonance=0.7, dampening=2970, wet=0.6, dry=0.50, delay_times=[0.02, 0.022, 0.24, 0.26], delay_subchannel=0.001)]

# Reverb for different sizes of rooms
define reverb_bathroom_af = [af.Reverb(resonance=0.15, dampening=50, dry=0.9)]
define reverb_small_room_af = [af.Reverb(resonance=0.3, dampening=1500, dry=0.85)]
define reverb_medium_room_af = [af.Reverb(resonance=0.5, dampening=1500, dry=0.85)]
define reverb_large_room_af = [af.Reverb(resonance=0.6, dampening=1500, dry=0.60)]
define reverb_church_hall_af = [af.Reverb(resonance=0.7, dampening=1500, dry=0.25)]
define reverb_cathedral_af = [af.Reverb(resonance=0.9, dampening=1500, dry=0.00)]

# Licence

# Copyright 2025 Berin

# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), 
# to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, 
# and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, 
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER 
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS 
# IN THE SOFTWARE.

