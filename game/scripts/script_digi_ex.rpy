### HERE WE GO. ###
init python:
    import math
    import json

    line_list = renpy.open_file("secret/dd/code.txt", "utf-8").read().replace("[", "[[").split("\n")
    chart_enemy = renpy.open_file("secret/dd/missingno_enemy.json", "utf-8").read()
    chart_player = renpy.open_file("secret/dd/missingno_player.json", "utf-8").read()

    _current_st = 0

    LOOP_POINT = 44.702
    LOOP_LENGTH = 125.825
    SONG_END = LOOP_POINT + LOOP_LENGTH

    class Note:
        def __init__(self, time, lane, type, length):
            self.time = time
            self.lane = lane
            self.type = type
            self.length = length

    def show_code(st, at, addtl = 100):
        lines = int(st * 5) % 171
        lines2 = lines + addtl
        t = "\n".join((line_list + line_list)[lines:lines2])
        c = str(t)
        d = Text(c, size = 20, font = "FiraCode-Retina.ttf", color = "#ffffff77")
        return d, 0.2

    def show_code_big(st, at):
        return show_code(st, at, 50)

    def show_code_small(st, at):
        return show_code(st, at, 100)

    def _dict_to_note(d: dict):
        return Note(d["time"], d["lane"], d["type"], d["length"])

    enemy_json_data = json.loads(chart_enemy)
    player_json_data = json.loads(chart_player)
    enemy_chart_data = [_dict_to_note(n) for n in enemy_json_data]
    player_chart_data = [_dict_to_note(n) for n in player_json_data]
    enemy_chart_index = Index(enemy_chart_data, "time")
    player_chart_index = Index(player_chart_data, "time")

    def charm_arrow(st, at, index, note_type = "charm"):
        global _current_st
        _current_st = st
        if st > SONG_END:
            st = ((st - LOOP_POINT) % LOOP_LENGTH) + LOOP_POINT
        latest_note = index.lteq(st)
        if latest_note:
            a = ease_linear(1, 0, latest_note.time + latest_note.length, latest_note.time + latest_note.length + 0.25, st)
            return Transform(Image(f"secret/dd/{note_type}_{latest_note.lane}.png"), alpha = a), 0.01
        else:
            return Null(width = 128), 0.01

    def charm_arrow_bf(st, at):
        return charm_arrow(st, at, player_chart_index, "heal")

    def charm_arrow_mno(st, at):
        return charm_arrow(st, at, enemy_chart_index, "blue")

    def move_dir(st, index, dist) -> tuple[float, float]:
        if st > SONG_END:
            st = ((st - LOOP_POINT) % LOOP_LENGTH) + LOOP_POINT
        latest_note = index.lteq(st)
        if latest_note:
            rt = st - latest_note.time
            a = easeout_circ(0, dist, 0, 0.1, rt) if rt < 0.1 else ease_quad(dist, 0, 0.1 + latest_note.length, 0.5 + latest_note.length, rt)
            if latest_note.lane == 0:
                # right
                r = (0, a)
            elif latest_note.lane == 1:
                # left
                r = (0, -a)
            elif latest_note.lane == 2:
                # up
                r = (-a, 0)
            elif latest_note.lane == 3:
                # down
                r = (a, 0)
            else:
                r = (0, 0)
        else:
            r = (0, 0)
        return r

    def digi_ex_displayable(st, at):
        # img = "secret/dd/digi_back.png" if 5 < st % 20 < 15 else "images/characters/digi.png"
        img = "images/characters/digi.png"
        return Transform(img,
            xanchor = 0.5, yanchor = 0.5,
            xpos = 0.5 + move_dir(st, enemy_chart_index, 0.05)[1],
            ypos = 0.4 + move_dir(st, enemy_chart_index, 0.05)[0] + ease_quad(0, 0.025, 0, 1, abs(st % 2 - 1))
        ), 0.025

    def flash_f(st, at):
        if st > SONG_END:
            st = ((st - LOOP_POINT) % LOOP_LENGTH) + LOOP_POINT
        st += 0.5
        a1 = ease_linear(127, 0, 66, 66.25, st)
        a2 = ease_linear(127, 0, 66.25, 66.5, st)
        if 66.5 > st and st < 66:
            return Null(1920, 1080), 0.01
        else:
            a = a1 if st < 66.25 else a2
            return Solid((255, 255, 255, a)), 0.01
        

    renpy.add_layer("back", above = "master")
    renpy.add_layer("fore1", above = "back")
    renpy.add_layer("digi", above = "fore1")
    renpy.add_layer("fore2", above = "digi")
    renpy.add_layer("fore3", above = "fore2")

init python:
    # https://www.shadertoy.com/view/tlVGDt
    renpy.register_shader(
        "shader.octagrams",
        variables="""
            uniform float u_time;
            uniform vec2 u_model_size;
            uniform vec2 res0;
            uniform sampler2D tex0;
            uniform sampler2D tex1;
            varying vec2 v_tex_coord;
        """,
        fragment_functions="""
            mat2 rot(float a) {
                float c = cos(a), s = sin(a);
                return mat2(c,s,-s,c);
            }

            float sdBox( vec3 p, vec3 b )
            {
                vec3 q = abs(p) - b;
                return length(max(q,0.0)) + min(max(q.x,max(q.y,q.z)),0.0);
            }

            float box(vec3 pos, float scale) {
                pos *= scale;
                float base = sdBox(pos, vec3(.4,.4,.1)) /1.5;
                pos.xy *= 5.;
                pos.y -= 3.5;
                pos.xy *= rot(.75);
                float result = -base;
                return result;
            }

            float box_set(vec3 pos, float iTime, float gTime) {
                vec3 pos_origin = pos;
                pos = pos_origin;
                pos .y += sin(gTime * 0.4) * 2.5;
                pos.xy *=   rot(.8);
                float box1 = box(pos,2. - abs(sin(gTime * 0.4)) * 1.5);
                pos = pos_origin;
                pos .y -=sin(gTime * 0.4) * 2.5;
                pos.xy *=   rot(.8);
                float box2 = box(pos,2. - abs(sin(gTime * 0.4)) * 1.5);
                pos = pos_origin;
                pos .x +=sin(gTime * 0.4) * 2.5;
                pos.xy *=   rot(.8);
                float box3 = box(pos,2. - abs(sin(gTime * 0.4)) * 1.5);	
                pos = pos_origin;
                pos .x -=sin(gTime * 0.4) * 2.5;
                pos.xy *=   rot(.8);
                float box4 = box(pos,2. - abs(sin(gTime * 0.4)) * 1.5);	
                pos = pos_origin;
                pos.xy *=   rot(.8);
                float box5 = box(pos,.5) * 6.;	
                pos = pos_origin;
                float box6 = box(pos,.5) * 6.;	
                float result = max(max(max(max(max(box1,box2),box3),box4),box5),box6);
                return result;
            }

            float map(vec3 pos, float iTime, float gTime) {
                vec3 pos_origin = pos;
                float box_set1 = box_set(pos, iTime, gTime);

                return box_set1;
            }
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
            vec2 p = (gl_FragCoord.xy * 2. - u_model_size.xy) / min(u_model_size.x, u_model_size.y);
            vec3 ro = vec3(0., -0.2 ,u_time * 4.);
            vec3 ray = normalize(vec3(p, 1.5));
            ray.xy = ray.xy * rot(sin(u_time * .03) * 5.);
            ray.yz = ray.yz * rot(sin(u_time * .05) * .2);
            float t = 0.1;
            vec3 col = vec3(0.);
            float ac = 0.0;
            float gTime = u_time;

            for (int i = 0; i < 99; i++){
                vec3 pos = ro + ray * t;
                pos = mod(pos-2., 4.) -2.;
                gTime = u_time -float(i) * 0.01;
                
                float d = map(pos, u_time, gTime);

                d = max(abs(d), 0.01);
                ac += exp(-d*23.);

                t += d* 0.55;
            }

            col = vec3(ac * 0.02);

            col +=vec3(0.,0.2 * abs(sin(u_time)),0.5 + sin(u_time) * 0.2);


            gl_FragColor = vec4(col ,1.0 - t * (0.02 + 0.02 * sin (u_time)));
        """
    )

    # https://www.shadertoy.com/view/MltBzf
    renpy.register_shader(
        'shader.glitch',
        variables="""
            uniform float u_time;
            uniform vec2 u_model_size;
            uniform sampler2D tex0;
            varying vec2 v_tex_coord;
        """,
        fragment_functions="""
            float rand(vec2 p, float seed)
            {
                float t = floor(seed * 20.) / 10.;
                return fract(sin(dot(p, vec2(t * 12.9898, t * 78.233))) * 43758.5453);
            }

            float noise(vec2 uv, float blockiness, float seed)
            {   
                vec2 lv = fract(uv);
                vec2 id = floor(uv);
                
                float n1 = rand(id, seed);
                float n2 = rand(id+vec2(1,0), seed);
                float n3 = rand(id+vec2(0,1), seed);
                float n4 = rand(id+vec2(1,1), seed);
                
                vec2 u = smoothstep(0.0, 1.0 + blockiness, lv);

                return mix(mix(n1, n2, u.x), mix(n3, n4, u.x), u.y);
            }

            float fbm(vec2 uv, int count, float blockiness, float complexity, float seed)
            {
                float val = 0.0;
                float amp = 0.5;
                
                while(count != 0)
                {
                    val += amp * noise(uv, blockiness, seed);
                    amp *= 0.5;
                    uv *= complexity;    
                    count--;
                }
                
                return val;
            }
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
            const float glitchAmplitude = 0.2; // increase this
            const float glitchNarrowness = 4.0;
            const float glitchBlockiness = 2.0;
            const float glitchMinimizer = 5.0; // decrease this

            // Normalized pixel coordinates (from 0 to 1)
            vec2 uv = v_tex_coord;
            vec2 a = vec2(uv.x * (u_model_size.x / u_model_size.y), uv.y);
            vec2 uv2 = vec2(a.x / u_model_size.x, exp(a.y));
            vec2 id = floor(uv * 8.0);
            //id.x /= floor(texture2D(tex0, vec2(id / 8.0)).r * 8.0);

            // Generate shift amplitude
            float shift = glitchAmplitude * pow(fbm(uv2, int(rand(id, u_time) * 6.), glitchBlockiness, glitchNarrowness, u_time), glitchMinimizer);
            
            // Create a scanline effect
            float scanline = abs(cos(uv.y * 400.));
            scanline = smoothstep(0.0, 2.0, scanline);
            shift = smoothstep(0.00001, 0.2, shift);
            
            // Apply glitch and RGB shift
            float colR = texture2D(tex0, vec2(uv.x + shift, uv.y)).r * (1. - shift);
            float colG = texture2D(tex0, vec2(uv.x - shift, uv.y)).g * (1. - shift) + rand(id, u_time) * shift;
            float colB = texture2D(tex0, vec2(uv.x - shift, uv.y)).b * (1. - shift);
            // Mix with the scanline effect
            vec3 f = vec3(colR, colG, colB) - (0.1 * scanline);
            
            // Output to screen
            gl_FragColor = vec4(f, texture2D(tex0, uv).a);
        """
    )

    renpy.register_shader(
        'shader.digilight',
        variables="""
        uniform float u_time;
        uniform vec2 u_model_size;
        uniform vec3 u_ambient;
        uniform vec3 u_left;
        uniform vec3 u_right;
        uniform float u_flip;
        uniform mat4 u_transform;
        uniform sampler2D tex0;
        uniform vec2 res0;
        varying vec2 v_tex_coord;
        """,
        fragment_functions="""
            float rand(vec2 p, float seed)
            {
                float t = floor(seed * 20.) / 10.;
                return fract(sin(dot(p, vec2(t * 12.9898, t * 78.233))) * 43758.5453);
            }

            float noise(vec2 uv, float blockiness, float seed)
            {   
                vec2 lv = fract(uv);
                vec2 id = floor(uv);
                
                float n1 = rand(id, seed);
                float n2 = rand(id+vec2(1,0), seed);
                float n3 = rand(id+vec2(0,1), seed);
                float n4 = rand(id+vec2(1,1), seed);
                
                vec2 u = smoothstep(0.0, 1.0 + blockiness, lv);

                return mix(mix(n1, n2, u.x), mix(n3, n4, u.x), u.y);
            }

            float fbm(vec2 uv, int count, float blockiness, float complexity, float seed)
            {
                float val = 0.0;
                float amp = 0.5;
                
                while(count != 0)
                {
                    val += amp * noise(uv, blockiness, seed);
                    amp *= 0.5;
                    uv *= complexity;    
                    count--;
                }
                
                return val;
            }
        """,
        vertex_300="""
            v_tex_coord = a_tex_coord;
        """,
        fragment_300="""
        const float glitchAmplitude = 0.2; // increase this
        const float glitchNarrowness = 4.0;
        const float glitchBlockiness = 2.0;
        const float glitchMinimizer = 5.0; // decrease this

        // Normalized pixel coordinates (from 0 to 1)
        vec2 uv = v_tex_coord;
        vec2 a = vec2(uv.x * (u_model_size.x / u_model_size.y), uv.y);
        vec2 uv2 = vec2(a.x / u_model_size.x, exp(a.y));
        vec2 id = floor(uv * 8.0);
        //id.x /= floor(texture2D(tex0, vec2(id / 8.0)).r * 8.0);

        // Generate shift amplitude
        float shift = glitchAmplitude * pow(fbm(uv2, int(rand(id, u_time) * 6.), glitchBlockiness, glitchNarrowness, u_time), glitchMinimizer);
        
        // Create a scanline effect
        float scanline = abs(cos(uv.y * 400.));
        scanline = smoothstep(0.0, 2.0, scanline);
        shift = smoothstep(0.00001, 0.2, shift);
        
        // Apply glitch and RGB shift
        float colR = texture2D(tex0, vec2(uv.x + shift, uv.y)).r * (1. - shift);
        float colG = texture2D(tex0, vec2(uv.x - shift, uv.y)).g * (1. - shift) + rand(id, u_time) * shift;
        float colB = texture2D(tex0, vec2(uv.x - shift, uv.y)).b * (1. - shift);
        // Mix with the scanline effect
        vec3 f = vec3(colR, colG, colB) - (0.1 * scanline);
        
        // Output to screen
        vec4 col = vec4(f, texture2D(tex0, uv).a);

        float sqrt_2 = 0.70710678118;
        // vec4 col = texture2D(tex0, v_tex_coord);
        vec3 facing = (u_transform * vec4(0.0, 0.0, -1.0, 0.0) * u_flip).xyz;
        float right = clamp(dot(facing, vec3(-sqrt_2, 0.0, sqrt_2)), 0.0, 1.0);
        float left = clamp(dot(facing, vec3(sqrt_2, 0.0, sqrt_2)), 0.0, 1.0);
        vec3 light = u_left * left + u_right * right + u_ambient;
        gl_FragColor = vec4(col.rgb * light, col.a);
        """
    )

init 0:
    image fractal = "bg/green.png"
    image num = spritesheet_animation("secret/dd/num.png", 10, 1, looping = True)
    image arrow_bf = DynamicDisplayable(charm_arrow_bf)
    image arrow_mno = DynamicDisplayable(charm_arrow_mno)
    image digi back = "secret/dd/digi_back.png"
    image digi ex = DynamicDisplayable(digi_ex_displayable)
    image flash = DynamicDisplayable(flash_f)
init 1:
    image num_blossom = SnowBlossom("num", 20, start = 0.1, fast = True, xspeed = (0, 0))
    image num_blossom_small:
        SnowBlossom("num", 100, start = 0.1, fast = True, xspeed = (0, 0), yspeed = (50, 100), border = 1000)
        zoom 0.5

init 2 python:
    for i in range(24):
        renpy.image(f"note_{i}", DynamicDisplayable(charm_arrow_bf))

transform t_bg_blur:
    blur 20

transform alpha(x):
    alpha x

transform zoom(x):
    zoom x

transform t_player_arrow:
    xalign 0.5
    yanchor 0.5
    ypos 0.85

transform t_digi_ex_idle:
    zoom 0.66
    shader "shader.digilight"
    u_ambient (0.4, 0.4, 0.4)
    u_left (0.0, 0.3, 0.6)
    u_right (0.0, 0.0, 0.6)
    u_flip 0.5

transform t_octograms:
    shader "shader.octagrams"
    pause 0
    repeat

transform t_glitch:
    shader "shader.glitch"
    pause 0
    repeat

transform note(index):
    xanchor 0.5
    yanchor 0.5
    zoom (0.75 / 2) + (0.05 * abs(index - 8))
    zpos -0.5
    ypos 0.5
    xpos (1 / 14) * (index - 1)
    parallel:
        linear 0.5 xpos (1 / 14) * index
    parallel:
        linear 0.5 zoom (0.75 / 2) + (0.05 * abs(index - 7))
    repeat

image code = DynamicDisplayable(show_code_big)
image code2 = DynamicDisplayable(show_code_small)

define audio.missingno_start = "secret/dd/missingno_start.ogg"
define audio.missingno_loop = "secret/dd/missingno_loop.ogg"
define audio.missingno_end = "secret/dd/missingno_end.ogg"

define digi_ex = Character("Digi EX", 
    callback = renpy.partial(char_callback, name = "digi", beep = "digi"),
    window_background = "secret/dd/TextBox_Sci-Fi_02_transparent.png",
    who_left_padding = 210, who_top_padding = 25,
    what_left_padding = 320,
    who_xoffset = 210, what_xoffset = 320,
    who_yoffset = 20, what_yoffset = 20,
    namebox_background = None,
    what_font = "STATIC.OTF", what_size = 40,
    who_font = "STATIC.OTF", who_size = 40, who_color = "#FFF",
    what_outlines = [(absolute(2), "#1eb8c0", absolute(0), absolute(0))],
    who_outlines = [(absolute(2), "#1eb8c0", absolute(0), absolute(0))])

label dx_digi_corruption:
    scene black
    stop music
    camera fore:
        perspective True
        ease 1 xrotate 1.3 yrotate -1.2 zrotate 0.9
        ease 1 xrotate 1 yrotate 0 zrotate 0.1
        ease 1 xrotate -1.3 yrotate -1.5 zrotate 0.1
        ease 1 xrotate -0.5 yrotate -1 zrotate 0.5
        ease 1 xrotate 0 yrotate 1 zrotate -0.9
        ease 1 xrotate 0.5 yrotate 0.5 zrotate 0.4
        ease 1 xrotate 0 yrotate 0 zrotate 0
        repeat
    camera digi:
        perspective True
    camera fore2:
        perspective True
        ease 1 xrotate 1.3 yrotate -1.2 zrotate 0.9
        ease 1 xrotate 1 yrotate 0 zrotate 0.1
        ease 1 xrotate -1.3 yrotate -1.5 zrotate 0.1
        ease 1 xrotate -0.5 yrotate -1 zrotate 0.5
        ease 1 xrotate 0 yrotate 1 zrotate -0.9
        ease 1 xrotate 0.5 yrotate 0.5 zrotate 0.4
        ease 1 xrotate 0 yrotate 0 zrotate 0
        repeat
    show fractal onlayer back at t_octograms
    show black onlayer back at alpha(0.5)
    show code2 onlayer fore1:
        align (1.0, 0.0)
        zpos -1
        zoom 0.5
        alpha 0.25
        zzoom True
        yrotate 180
    show code onlayer fore1:
        align (0.0, 0.0)
        zpos -1
    show num_blossom_small at t_glitch onlayer fore1:
        zpos -1
        zzoom True
    show num_blossom_small at t_glitch onlayer fore1 as duplicate:
        zpos -1
        zzoom True
        xpos 0.5
    show arrow_mno at truecenter, alpha(0.8), zoom(2) onlayer fore1
    # show arrow_bf at t_player_arrow, zoom(0.8) onlayer digi

    python:
        for i in range(24):
            renpy.show(f"note_{i}", [note(i)], layer = "fore1")

    show digi ex at t_digi_ex_idle onlayer digi
    show num_blossom at t_glitch onlayer fore2:
        zpos 1

    show flash onlayer fore3

    play music missingno_start if_changed
    $ persistent.heard.add("missingno")
    queue music missingno_loop

    $ config.window_show_transition = None
    $ config.window_hide_transition = None

    show black with Fade(0.0, 0.0, 5.0)

    digi_ex "Enjoy the show."
    window hide

    pause

    $ config.window_show_transition = Dissolve(.2)
    $ config.window_hide_transition = Dissolve(.2)

    return
