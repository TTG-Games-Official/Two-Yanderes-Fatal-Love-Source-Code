init offset = -3

# This section defines custom key bindings for keyboard and gamepad inputs.
init python:
    config.keymap = dict(

        screenshot = ['alt_K_s', 'alt_shift_K_s', 'noshift_K_s'],
        toggle_afm = [],
        toggle_fullscreen = ['alt_K_RETURN', 'alt_K_KP_ENTER', 'K_F11', 'noshift_K_f'],
        game_menu = [],
        hide_windows = ['mouseup_2', 'noshift_K_h'],
        launch_editor = [], 
        dump_styles = [],
        reload_game = ['alt_K_r', 'shift_K_r'],
        inspector = [],
        full_inspector = [],
        developer = ['alt_K_d', 'shift_K_d'],
        quit = [],
        iconify = [],   
        help = [],
        choose_renderer = [],
        progress_screen = [],
        accessibility = [],

        # Accessibility.
        self_voicing = [],
        clipboard_voicing = [],
        debug_voicing = [],

        # Say.
        rollforward = ['any_K_PAGEDOWN', 'any_KP_PAGEDOWN', 'mousedown_5'],
        dismiss = ['K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT', 'mouseup_1'],
        dismiss_unfocused = [],

        # Pause.
        dismiss_hard_pause = [],

        # Focus.
        focus_left = ['any_K_LEFT', 'any_KP_LEFT'],
        focus_right = ['any_K_RIGHT', 'any_KP_RIGHT'],
        focus_up = ['any_K_UP', 'any_KP_UP'],
        focus_down = ['any_K_DOWN', 'any_KP_DOWN'],

        # Button.
        button_ignore = ['mousedown_1'],
        button_select = ['K_RETURN', 'K_KP_ENTER', 'K_SELECT', 'mouseup_1'],
        button_alternate = ['mouseup_3'],
        button_alternate_ignore = ['mousedown_3'],

        # Input.
        input_backspace = ['any_K_BACKSPACE'],
        input_enter = ['K_RETURN', 'K_KP_ENTER'],
        input_next_line = ['shift_K_RETURN', 'shift_K_KP_ENTER'],
        input_left = ['any_K_LEFT', 'any_KP_LEFT'],
        input_right = ['any_K_RIGHT', 'any_KP_RIGHT'],
        input_up = ['any_K_UP', 'any_KP_UP'],
        input_down = ['any_K_DOWN', 'any_KP_DOWN'],
        input_delete = ['any_K_DELETE', 'any_KP_DELETE'],
        input_home = ['K_HOME', 'KP_HOME', 'meta_K_LEFT'],
        input_end = ['K_END', 'KP_END', 'meta_K_RIGHT'],
        input_copy = ['ctrl_noshift_K_INSERT', 'ctrl_noshift_K_c', 'meta_noshift_K_c'],
        input_paste = ['shift_K_INSERT', 'ctrl_noshift_K_v', 'meta_noshift_K_v'],
        input_jump_word_left = ['osctrl_K_LEFT', 'osctrl_KP_LEFT'],
        input_jump_word_right = ['osctrl_K_RIGHT', 'osctrl_KP_RIGHT'],
        input_delete_word = ['osctrl_K_BACKSPACE'],
        input_delete_full = ['meta_K_BACKSPACE'],

        # Viewport.
        viewport_leftarrow = ['any_K_LEFT', 'any_KP_LEFT'],
        viewport_rightarrow = ['any_K_RIGHT', 'any_KP_RIGHT'],
        viewport_uparrow = ['any_K_UP', 'any_KP_UP'],
        viewport_downarrow = ['any_K_DOWN', 'any_KP_DOWN'],
        viewport_wheelup = ['mousedown_4'],
        viewport_wheeldown = ['mousedown_5'],
        viewport_drag_start = ['mousedown_1'],
        viewport_drag_end = ['mouseup_1'],
        viewport_pageup = ['any_K_PAGEUP', 'any_KP_PAGEUP'],
        viewport_pagedown = ['any_K_PAGEDOWN', 'any_KP_PAGEDOWN'],

        # These keys control skipping.
        skip = ['K_LCTRL', 'K_RCTRL'],
        stop_skipping = [],
        toggle_skip = ['K_TAB'],
        fast_skip = [],

        # Bar.
        bar_activate = ['mousedown_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT'],
        bar_deactivate = ['mouseup_1', 'K_RETURN', 'K_KP_ENTER', 'K_SELECT'],
        bar_left = ['any_K_LEFT', 'any_KP_LEFT'],
        bar_right = ['any_K_RIGHT', 'any_KP_RIGHT'],
        bar_up = ['any_K_UP', 'any_KP_UP'],
        bar_down = ['any_K_DOWN', 'any_KP_DOWN'],

        # Delete a save.
        save_delete = ['K_DELETE', 'KP_DELETE'],

        # Draggable.
        drag_activate = ['mousedown_1'],
        drag_deactivate = ['mouseup_1'],

        # Debug console.
        console = ['shift_K_o', 'alt_shift_K_o'],
        console_older = ['any_K_UP', 'any_KP_UP'],
        console_newer = ['any_K_DOWN', 'any_KP_DOWN'],

        # Director
        director = [],

        # Ignored (kept for backwards compatibility).
        toggle_music = [],
        viewport_up = [],
        viewport_down = [],

        # Profile commands.
        performance = ['K_F3'],
        image_load_log = [],
        profile_once = [],
        memory_profile = [],

    )

    # Gamepad Controls
    config.pad_bindings = {
        
        "pad_leftshoulder_press" : [],
        "pad_lefttrigger_pos" : [],
        "pad_back_press" : [],

        "repeat_pad_leftshoulder_press" : [],
        "repeat_pad_lefttrigger_pos" : [],
        "repeat_pad_back_press" : [],

        "pad_guide_press" : [],
        "pad_start_press" : [],

        "pad_y_press" : ["hide_windows"],
        "pad_x_press" : ["button_alternate"],

        "pad_rightshoulder_press" : [],
        "repeat_pad_rightshoulder_press" : [],

        "pad_righttrigger_pos" : ["dismiss", "button_select", "bar_activate", "bar_deactivate"],
        "pad_a_press" : ["dismiss", "button_select", "bar_activate", "bar_deactivate"],
        "pad_b_press" : [],

        "pad_dpleft_press" : ["focus_left", "bar_left", "viewport_leftarrow"],
        "pad_leftx_neg" : ["focus_left", "bar_left", "viewport_leftarrow"],
        "pad_rightx_neg" : ["focus_left", "bar_left", "viewport_leftarrow"],

        "pad_dpright_press" : ["focus_right", "bar_right", "viewport_rightarrow"],
        "pad_leftx_pos" : ["focus_right", "bar_right", "viewport_rightarrow"],
        "pad_rightx_pos" : ["focus_right", "bar_right", "viewport_rightarrow"],

        "pad_dpup_press" : ["focus_up", "bar_up", "viewport_uparrow"],
        "pad_lefty_neg" : ["focus_up", "bar_up", "viewport_uparrow"],
        "pad_righty_neg" : ["focus_up", "bar_up", "viewport_uparrow"],

        "pad_dpdown_press" : ["focus_down", "bar_down", "viewport_downarrow"],
        "pad_lefty_pos" : ["focus_down", "bar_down", "viewport_downarrow"],
        "pad_righty_pos" : ["focus_down", "bar_down", "viewport_downarrow"],

        "repeat_pad_dpleft_press" : ["focus_left", "bar_left", "viewport_leftarrow"],
        "repeat_pad_leftx_neg" : ["focus_left", "bar_left", "viewport_leftarrow"],
        "repeat_pad_rightx_neg" : ["focus_left", "bar_left", "viewport_leftarrow"],

        "repeat_pad_dpright_press" : ["focus_right", "bar_right", "viewport_rightarrow"],
        "repeat_pad_leftx_pos" : ["focus_right", "bar_right", "viewport_rightarrow"],
        "repeat_pad_rightx_pos" : ["focus_right", "bar_right", "viewport_rightarrow"],

        "repeat_pad_dpup_press" : ["focus_up", "bar_up", "viewport_uparrow"],
        "repeat_pad_lefty_neg" : ["focus_up", "bar_up", "viewport_uparrow"],
        "repeat_pad_righty_neg" : ["focus_up", "bar_up", "viewport_uparrow"],

        "repeat_pad_dpdown_press" : ["focus_down", "bar_down", "viewport_downarrow"],
        "repeat_pad_lefty_pos" : ["focus_down", "bar_down", "viewport_downarrow"],
        "repeat_pad_righty_pos" : ["focus_down", "bar_down", "viewport_downarrow"],
    }


init python:
    gui.init(1920, 1080)

    config.character_id_prefixes.append('namebox')
    config.overlay_screens.append("quick_menu")

    # Defining the music and sfx voice channels.
    renpy.music.register_channel("click", "sfx", False)
    renpy.music.register_channel("sound2", "sfx", False)
    renpy.music.register_channel("sound3", "sfx", False)

    renpy.music.register_channel("skipmusic", "music", True)

    renpy.music.register_channel("lsanity", "music", True)
    renpy.music.register_channel("msanity", "music", True)
    renpy.music.register_channel("hsanity", "music", True)


# These functions handle various game-related features.
init python:

    global sanity
    current_name = ""

    def start_game_with_fade():
        config.allow_skipping = False
        renpy.show_screen("block_input", 3)
        renpy.show_screen("start_game")
        renpy.transition(ff__)
        renpy.music.stop(fadeout=1.5)

    def ost_screen_with_fade():
        config.allow_skipping = False
        renpy.show_screen("block_input", 3)
        renpy.show_screen("start_game_ost")
        renpy.transition(ff__)
        renpy.music.stop(fadeout=1.5)

    def play_click_sound():
        if sanity >= 70:
            renpy.sound.play("audio/sfx/TTG Games/Button Click Sound.opus", channel="click")
        else:
            renpy.sound.play("audio/sfx/TTG Games/Button Click Sound Echo.opus", channel="click")

    def select_button(button_name):
        global selected_button
        selected_button = button_name

    def cancel_name_input():
        persistent.playernameentered = False
        persistent.playername = ""

    def delete_all_saves():
        for saves in renpy.list_saved_games(fast=True):
            renpy.unlink_save(saves)

    def stop_music(fadeout=0):
        renpy.music.stop(channel="hsanity", fadeout=fadeout)
        renpy.music.stop(channel="msanity", fadeout=fadeout)
        renpy.music.stop(channel="lsanity", fadeout=fadeout)


init python:
    # These python functions checks if the game is running for the first time by creating and checking the "firstrun" file.
    import os

    def create_firstrun():
        file_path = os.path.join(config.gamedir, "firstrun")
        with open(file_path, 'w') as f:
            pass

    def check_firstrun():
        file_path = os.path.join(config.gamedir, "firstrun")
        if os.path.exists(file_path):
            return True
        else:
            return False


# This function generates a random text by randomly selecting symbols. It is used to create a distorted text effect in specific scenes.
init python:
    import random

    random_symbol = "ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZabcçdefgğhıijklmnoöprsştuüvyz0123456789!#$%&'*+,$€-.:;<=>?@^`~"

    def random_text(length):
        return "".join(random.choice(random_symbol) for _ in range(length))


# This function defines the intro screen messages.
init python:
    entry_messages = [
        _("What happens if two yanderes fell for each other?"),
        _("I want to keep you close... so close that no one else can touch you."),
        _("You are mine, and mine alone!"),
        _("We will be together forever!"),
        _("Would you ever commit a crime just for your partner?"),
        _("Hey! Don't look at that girl!"),
        _("Don't you dare to cheat on me. Or else..."),
        _("Don't ever try to mess with yanderes."),
        _("If you really love me, kill this girl."),
        _("Shall we burn all of the world and live, just two of us?")
    ]


# This function disables or enables the dismiss keys.
init python:
    def lock_dismiss():
        config.keymap['dismiss'] = []
        renpy.display.behavior.clear_keymap_cache()

    def unlock_dismiss():
        config.keymap['dismiss'] = ['K_RETURN', 'K_SPACE', 'K_KP_ENTER', 'K_SELECT', 'mouseup_1']
        renpy.display.behavior.clear_keymap_cache()


# This function checks if the player is skipping the dialogue when active.
init python:

    global pause_menu_open
    monitor_skip = False

    def monitoring_skip():
        if monitor_skip and config.skipping and config.allow_skipping and not pause_menu_open:
            # Do Something

    config.interact_callbacks.append(monitoring_skip)


# Sanity Releated Functions
init python:
    def sanity_mode(mode, delay=0.5): # This function mutes or unmutes the music channels according to the main character's sanity.

        global sanity_mod

        if mode == "low":
            sanity_mod = "low"
            renpy.music.set_volume(1.0, delay=delay, channel='lsanity') # Low Sanity
            renpy.music.set_volume(0.0, delay=delay * 4, channel='msanity') # Medium Sanity
            renpy.music.set_volume(0.0, delay=delay * 4, channel='hsanity') # High Sanity

        elif mode == "medium":
            sanity_mod = "medium"
            renpy.music.set_volume(1.0, delay=delay, channel='msanity') # Medium Sanity
            renpy.music.set_volume(0.0, delay=delay * 4, channel='lsanity') # Low Sanity
            renpy.music.set_volume(0.0, delay=delay * 4, channel='hsanity') # High Sanity
            
        else:
            sanity_mod = "high"
            renpy.music.set_volume(1.0, delay=delay, channel='hsanity') # High Sanity
            renpy.music.set_volume(0.0, delay=delay * 4, channel='lsanity') # Low Sanity
            renpy.music.set_volume(0.0, delay=delay * 4, channel='msanity') # Medium Sanity

    def change_sanity(prefix, amount):

        # This function changes the sanity percentage according to given arguments and automatically sets the opacity of the vignette of the screen according to the sanity percentage.

        global sanity
        global sanity_mod
        global textbox
        global atmosphere

        if prefix == "+":

            if persistent.low_fps_optimization == False:

                for _ in range(amount):

                    if sanity < 100:

                        sanity += 1

                        if sanity >= 50 and not textbox == "normal":
                            textbox = "normal"
                        elif sanity < 50 and not textbox == "yandere":
                            textbox = "yandere"
                        else:
                            pass

                        if sanity >= 70 and not sanity_mod == "high":
                            sanity_mode("high")
                        elif sanity >= 36 and sanity <= 69 and not sanity_mod == "medium":
                            sanity_mode("medium")
                        elif sanity <= 35 and not sanity_mod == "low":
                            sanity_mode("low")
                        else:
                            pass

                        renpy.show("yandereblack", layer="yblack", at_list=[transparent(1.0 - pow(sanity / 100, 1))])

                        renpy.pause(0.0, hard=True) # 0 seconds is one framerate waiting. It prevents the variable from reaching the target value instantly.

            else:
                
                for _ in range(int(amount / 5)):

                    if sanity < 96:

                        sanity += 5

                        if sanity >= 50 and not textbox == "normal":
                            textbox = "normal"
                        elif sanity < 50 and not textbox == "yandere":
                            textbox = "yandere"
                        else:
                            pass

                        if sanity >= 70 and not sanity_mod == "high":
                            sanity_mode("high")
                        elif sanity >= 36 and sanity <= 69 and not sanity_mod == "medium":
                            sanity_mode("medium")
                        elif sanity <= 35 and not sanity_mod == "low":
                            sanity_mode("low")
                        else:
                            pass

                        renpy.show("yandereblack", layer="yblack", at_list=[transparent(1.0 - pow(sanity / 100, 1))])

                        renpy.pause(0.0, hard=True)

        elif prefix == "-":

            if persistent.low_fps_optimization == False:

                for _ in range(amount):

                    if sanity > 0:

                        sanity -= 1

                        if sanity >= 50 and not textbox == "normal":
                            textbox = "normal"
                        elif sanity < 50 and not textbox == "yandere":
                            textbox = "yandere"
                        else:
                            pass

                        if sanity >= 70 and not sanity_mod == "high":
                            sanity_mode("high")
                        elif sanity >= 36 and sanity <= 69 and not sanity_mod == "medium":
                            sanity_mode("medium")
                        elif sanity <= 35 and not sanity_mod == "low":
                            sanity_mode("low")
                        else:
                            pass

                        renpy.show("yandereblack", layer="yblack", at_list=[transparent(1.0 - pow(sanity / 100, 1))])

                        renpy.pause(0.0, hard=True)

            else:
                
                for _ in range(int(amount / 5)):

                    if sanity > 4:

                        sanity -= 5

                        if sanity >= 50 and not textbox == "normal":
                            textbox = "normal"
                        elif sanity < 50 and not textbox == "yandere":
                            textbox = "yandere"
                        else:
                            pass

                        if sanity >= 70 and not sanity_mod == "high":
                            sanity_mode("high")
                        elif sanity >= 36 and sanity <= 69 and not sanity_mod == "medium":
                            sanity_mode("medium")
                        elif sanity <= 35 and not sanity_mod == "low":
                            sanity_mode("low")
                        else:
                            pass

                        renpy.show("yandereblack", layer="yblack", at_list=[transparent(1.0 - pow(sanity / 100, 1))])

                        renpy.pause(0.0, hard=True)


    def set_sanity(value): # This function directly sets the sanity percentage to the given value (you can't use negative values).

        global sanity
        global textbox
        sanity = value

        if sanity >= 50 and not textbox == "normal":
            textbox = "normal"
        elif sanity < 50 and not textbox == "yandere":
            textbox = "yandere"
        else:
            pass

        if sanity >= 70 and not sanity_mod == "high":
            sanity_mode("high")
        elif sanity >= 36 and sanity <= 69 and not sanity_mod == "medium":
            sanity_mode("medium")
        elif sanity <= 35 and not sanity_mod == "low":
            sanity_mode("low")
        else:
            pass

        renpy.show("yandereblack", layer="yblack", at_list=[transparent(1.0 - pow(sanity / 100, 1))])


# Atmosphere Releated Functions
init python:     
    def change_atmosphere(prefix, amount):

        # This function changes the atmosphere percentage according to given arguments.

        global atmosphere

        if prefix == "+":

            if persistent.low_fps_optimization == False:

                for _ in range(amount):
                    if atmosphere < 100:
                        atmosphere += 1
                        renpy.pause(0.0, hard=True) # 0 seconds is one framerate waiting. It prevents the variable from reaching the target value instantly.

            else:

                for _ in range(int(amount / 5)):
                    if atmosphere < 96:
                        atmosphere += 5
                        renpy.pause(0.0, hard=True)


        elif prefix == "-":

            if persistent.low_fps_optimization == False:

                for _ in range(amount):
                    if atmosphere > 0:
                        atmosphere -= 1
                        renpy.pause(0.0, hard=True)

            else:

                for _ in range(int(amount / 5)):
                    if atmosphere > 4:
                        atmosphere -= 5
                        renpy.pause(0.0, hard=True)

    def set_atmosphere(amount): # This function instantly sets the atmosphere percentage to the given value (you can't set it to negative numbers or more than 100).

        global atmosphere

        atmosphere = amount

    def atm_matrix(): # This function changes the color saturation and brightness of the sprites according to atmosphere percentage (to prevent them appearing too dark or black and white).

        global atmosphere
        global ignore_atm

        if atmosphere > 67 or ignore_atm == True:
            return SaturationMatrix(1.2)
        elif atmosphere > 50:
            return SaturationMatrix(1.2) * ContrastMatrix(1.15) * BrightnessMatrix(0.05)
        elif atmosphere > 35:
            return SaturationMatrix(1.3) * ContrastMatrix(1.2) * BrightnessMatrix(0.07)
        elif atmosphere > 10:
            return SaturationMatrix(1.4) * ContrastMatrix(1.4) * BrightnessMatrix(0.1)
        elif atmosphere <= 10:
            return SaturationMatrix(1.5) * ContrastMatrix(1.7) * BrightnessMatrix(0.15)
        else:
            pass
        
    def update_sun(trans, st, at): # This function changes the opacity of the sun depending on the atmosphere percentage in atmosphere screen.
        global atmosphere
        
        current_atm = max(0, min(100, atmosphere))
        
        trans.alpha = current_atm / 100.0
        
        return 0

    def update_cloud(trans, st, at): # This function changes the opacity of the cloud depending on the atmosphere percentage in atmosphere screen.
        global atmosphere
        current_atm = max(0, min(100, atmosphere))
        
        trans.alpha = (100 - current_atm) / 100.0
        
        val = 100 - current_atm
        trans.matrixcolor = ContrastMatrix(1.0 + (val * 0.008) ** 0.7)
        
        return 0

    def enable_atm(mode): # This function sets if the atmosphere is enabled or disabled. If you disable it, the game world will not be affected by the atmosphere percentage.

        global ignore_atm

        if mode == True:
            ignore_atm = False
            renpy.call("atm_normal") 
            
        elif mode == False:
            ignore_atm = True
            renpy.call("atm_disabled")


# Police Suspicion Releated Functions
init python:
    def change_suspicion(prefix, amount): # This function changes the suspicion percentage of the police.

        global suspicion

        if prefix == "+":

            if persistent.low_fps_optimization == False:

                for _ in range(amount):
                    if suspicion < 100:
                        suspicion += 1
                        renpy.pause(0.0, hard=True) # 0 seconds is one framerate waiting. It prevents the variable from reaching the target value instantly.

            else:

                for _ in range(int(amount / 5)):
                    if suspicion < 96:
                        suspicion += 5
                        renpy.pause(0.0, hard=True)


        elif prefix == "-":

            if persistent.low_fps_optimization == False:

                for _ in range(amount):
                    if suspicion > 0:
                        suspicion -= 1
                        renpy.pause(0.0, hard=True)

            else:

                for _ in range(int(amount / 5)):
                    if suspicion > 4:
                        suspicion -= 5
                        renpy.pause(0.0, hard=True)
                    
        else:
            pass


# This function is the cardiograph behind the sanity percentage. It changes its speed and color depending on the sanity varible.
init python:

    import math

    global sanity

    class Cardiograph(renpy.Displayable):
        def __init__(self, **kwargs):
            super(Cardiograph, self).__init__(**kwargs)
            
            self.width = 200
            self.height = 70
            self.base_y = 35
            
            self.points = [self.base_y] * self.width
            self.head_x = 0
            self.last_st = 0
            
            self.pulse_timer = 0.0
            self.accumulator = 0.0 
            
        def render(self, width, height, st, at):
            
            # Cardiograph line color depending on the sanity percentage. 
            if sanity >= 70:
                line_color = "#ff8efd"
            elif sanity > 35:
                line_color = "#ff7878"
            else:
                line_color = "#ff0000"

            # Cardiograph beat speed depending on the sanity percentage. 
            beat_duration = 1.0 - ( (100 - sanity) * 0.007)
            if beat_duration < 0.3: beat_duration = 0.3

            if self.last_st == 0:
                self.last_st = st
            
            dt = st - self.last_st
            self.last_st = st
            
            self.accumulator += dt
            
            seconds_per_pixel = 1.0 / 60.0 
            
            while self.accumulator >= seconds_per_pixel:
                
                self.accumulator -= seconds_per_pixel
                self.pulse_timer += seconds_per_pixel
                
                if self.pulse_timer >= beat_duration:
                    self.pulse_timer %= beat_duration
                
                t = self.pulse_timer
                y_pos = self.base_y
                
                # Cardiograph beat shape and time. (Y + 30 in 0.03 seconds, Y - 60 in 0.06 seconds, Y + 30 in 0.03 seconds) 
                if 0.0 <= t < 0.03:
                    progress = t / 0.03
                    y_pos = 35 + (30 * progress)

                elif 0.03 <= t < 0.05:
                    y_pos = 65 

                elif 0.05 <= t < 0.11:
                    progress = (t - 0.05) / 0.06
                    y_pos = 65 - (60 * progress)

                elif 0.11 <= t < 0.13:
                    y_pos = 5
                
                elif 0.13 <= t < 0.16:
                    progress = (t - 0.13) / 0.03
                    y_pos = 5 + (30 * progress)

                else:
                    y_pos = self.base_y
                
                if y_pos < 4: y_pos = 4
                if y_pos > 66: y_pos = 66
                
                self.head_x = (self.head_x + 1) % self.width
                self.points[self.head_x] = y_pos

            render = renpy.Render(self.width, self.height)
            canvas = render.canvas()
            
            gap_size = 40 # The gap between the line's head and the end of the tail. 
            
            for i in range(self.width - 1):
                dist = (i - self.head_x) % self.width
                
                if 0 < dist < gap_size:
                    continue

                thickness = 1 # The thickness of the line. 

                dist_behind = (self.head_x - i) % self.width
                if dist_behind < 5:
                    thickness = 3 # The thickness of the line's head. 

                p1 = (i, self.points[i])
                p2 = (i+1, self.points[i+1])
                
                dist2 = ((i+1) - self.head_x) % self.width
                if not (0 < dist2 < gap_size):
                    canvas.line(line_color, p1, p2, width=thickness)

            renpy.redraw(self, 0)
            
            return render