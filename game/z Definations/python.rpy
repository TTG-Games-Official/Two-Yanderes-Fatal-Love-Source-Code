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

# This function sets up a saturation shader.
init python:

    renpy.register_shader(

        "tyfl.red_protected_saturation",

        variables="""
            uniform float u_rps_saturation;
            uniform float u_rps_strength;
            uniform float u_rps_red_start;
            uniform float u_rps_red_full;
        """,

        fragment_410="""

            float px_alpha = gl_FragColor.a;

            if (px_alpha > 0.00001) {

                vec3 rgb = gl_FragColor.rgb / px_alpha;

                float gray = dot(rgb, vec3(0.2126, 0.7152, 0.0722));

                float total_rgb = rgb.r + rgb.g + rgb.b;

                float red_share = rgb.r / max(total_rgb, 0.00001);

                float red_mask = smoothstep(u_rps_red_start, u_rps_red_full, red_share);

                float base_sat = clamp(u_rps_saturation, 0.0, 1.1);

                float strength = clamp(u_rps_strength,0.0, 1.0);

                float desat_amount = max(1.1 - base_sat, 0.0);

                float local_sat = base_sat + desat_amount * red_mask * strength;

                vec3 result = mix(vec3(gray), rgb, local_sat);

                result = clamp(result, vec3(0.0), vec3(1.0));

                gl_FragColor = vec4(result * px_alpha, px_alpha);
            }
        """
    )

# These functions updates the screen depending on the sanity and atmosphere percentage while preserving red colors.
init python:

    def update_atm_camera(trans, st, at):

        global sanity
        global atmosphere
        global ignore_atm
        global red_protection_strength

        current_sanity = max(0.0, min(100.0, float(sanity)))
        current_atmosphere = max(0.0, min(100.0, float(atmosphere)))

        sanity_factor = (current_sanity / 100.0) ** 2.5

        if ignore_atm:

            current_saturation = 0.1 + 1.0 * sanity_factor
            current_matrix = IdentityMatrix()

        else:

            current_saturation = ((0.3 - ((100 - current_sanity) * 0.002)) + (current_atmosphere * 0.01) * sanity_factor)
            current_contrast = (1.0 - ((100.0 - current_atmosphere) * 0.004) ** 0.7)
            current_brightness = -(100.0 - current_atmosphere) * 0.003

            current_matrix = ContrastMatrix(current_contrast) * BrightnessMatrix(current_brightness)

        trans.u_rps_saturation = current_saturation
        trans.u_rps_strength = red_protection_strength
        trans.u_rps_red_start = 0.40
        trans.u_rps_red_full = 0.75
        trans.matrixcolor = current_matrix

        return None

    atm_camera_transform = Transform(function=update_atm_camera)

    atm_camera_transform.mesh = False
    atm_camera_transform.shader = "tyfl.red_protected_saturation"

    atm_camera_transform.u_rps_saturation = 1.0
    atm_camera_transform.u_rps_strength = 0.0
    atm_camera_transform.u_rps_red_start = 0.40
    atm_camera_transform.u_rps_red_full = 0.75
    atm_camera_transform.matrixcolor = IdentityMatrix()

    def clamp01(value):
        return max(0.0, min(1.0, float(value)))

    def get_atm_camera_values(atm_value=None):

        if atm_value is None:
            atm_value = atmosphere

        current_atm = max(0.0, min(100.0, float(atm_value)))

        normalized_atm = current_atm / 100.0

        current_contrast = (1.0 - ((100.0 - current_atm) * 0.004) ** 0.7)

        current_brightness = (-(100.0 - current_atm) * 0.003)

        return (
            normalized_atm,
            current_contrast,
            current_brightness
        )

    def get_atm_sky_alpha():

        target_gray, contrast, brightness = get_atm_camera_values()

        white_after_camera = 0.5 + contrast * (0.5 + brightness)

        black_after_camera = 0.5 + contrast * (brightness - 1.0)

        black_after_camera = clamp01(black_after_camera)

        value_range = (white_after_camera - black_after_camera)

        if abs(value_range) < 0.000001:
            return 0.0

        alpha = (white_after_camera - target_gray) / value_range

        return clamp01(alpha)

# Core GUI and audio channel setup.
init python:

    gui.init(1920, 1080)

    config.character_id_prefixes.append('namebox')
    config.overlay_screens.append("quick_menu")

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
        
        if persistent.yandere_menu_enabled == "easteregg":
            persistent.yandere_menu_enabled = persistent.ymenu_enabled_saved 
        
        renpy.show_screen("block_input", 3)
        renpy.show_screen("start_game_ost")
        renpy.transition(ff__)
        renpy.music.stop(fadeout=1.5)

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
        global current_dynamic_music
        current_dynamic_music = None

        renpy.music.stop(channel="hsanity", fadeout=fadeout)
        renpy.music.stop(channel="msanity", fadeout=fadeout)
        renpy.music.stop(channel="lsanity", fadeout=fadeout)

    def get_allowed_textbox_type(textbox_type):

        if textbox_type == "invisible":
            return "invisible"

        elif textbox_type == "yandere":
            return "yandere"

        elif textbox_type == "normal":

            if persistent.lock_sanity_level:

                if sanity >= 50:
                    return "normal"
                else:
                    return "yandere"
            
            else:
                return "normal"
    
    def trigger_easter_egg():
        renpy.jump("easter_egg_trigger")

# These functions are dynamic sound effects depending on the sanity.
init python:

    def _play_sanity_sound(normal_sound, echo_sound, channel="sound", volume=1.0, queue=False):
        
        selected_sound = normal_sound if sanity >= 70 else echo_sound

        if queue:
            renpy.sound.queue(selected_sound, channel=channel, relative_volume=volume)
        else:
            renpy.sound.play(selected_sound, channel=channel, relative_volume=volume)

    def play_click_sound(channel="click", volume=1.0):
        _play_sanity_sound(click, click_echo, channel=channel, volume=volume)

    def play_stab_sound(channel="sound", volume=1.0, queue=False):
        _play_sanity_sound(stab, stab_echo, channel=channel, volume=volume, queue=queue)

    def play_clothrustle_sound(channel="sound", volume=1.0, queue=False):
        _play_sanity_sound(clothrustle, clothrustle_echo, channel=channel, volume=volume, queue=queue)

    def play_girl_scream_sound(channel="sound", volume=1.0, queue=False):
        _play_sanity_sound(girl_scream, girl_scream_echo, channel=channel, volume=volume, queue=queue)

    def play_girl_scream2_sound(channel="sound", volume=1.0, queue=False):
        _play_sanity_sound(girl_scream2, girl_scream2_echo, channel=channel, volume=volume, queue=queue)

    def play_boy_scream_sound(channel="sound", volume=1.0, queue=False):
        _play_sanity_sound(boy_scream, boy_scream_echo, channel=channel, volume=volume, queue=queue)

    def play_boy_scream2_sound(channel="sound", volume=1.0, queue=False):
        _play_sanity_sound(boy_scream2, boy_scream2_echo, channel=channel, volume=volume, queue=queue)

    def play_boy_scream3_sound(channel="sound", volume=1.0, queue=False):
        _play_sanity_sound(boy_scream3, boy_scream3_echo, channel=channel, volume=volume, queue=queue)

    def play_boy_scream4_sound(channel="sound", volume=1.0, queue=False):
        _play_sanity_sound(boy_scream4, boy_scream4_echo, channel=channel, volume=volume, queue=queue)

    def play_yboy_laugh_sound(channel="sound", volume=1.0, queue=False):
        _play_sanity_sound(yboy_laugh, yboy_laugh_echo, channel=channel, volume=volume, queue=queue)

    def play_ygirl_laugh_sound(channel="sound", volume=1.0, queue=False):
        _play_sanity_sound(ygirl_laugh, ygirl_laugh_echo, channel=channel, volume=volume, queue=queue)

    def play_ygirl2_laugh_sound(channel="sound", volume=1.0, queue=False):
        _play_sanity_sound(ygirl2_laugh, ygirl2_laugh_echo, channel=channel, volume=volume, queue=queue)

    def play_run_sound(channel="sound", volume=1.0, queue=False):
        _play_sanity_sound(run, run_echo, channel=channel, volume=volume, queue=queue)

# These are localized asset helpers.
init python:

    localized_asset_suffixes = {
        "Türkçe": "tr",
        "Español": "es",
        "Russian": "ru",
        "English": "en",
    }

    localized_asset_folders = {
        "Türkçe": "Turkce",
        "Español": "Espanol",
        "Russian": "Russian",
        "English": "English",
    }

    localized_asset_codes = {
        "Türkçe": "TR",
        "Español": "ES",
        "Russian": "RU",
        "English": "EN",
    }

    def localized_asset_suffix():
        return localized_asset_suffixes.get(persistent.language, "en")

    def localized_asset_folder():
        return localized_asset_folders.get(persistent.language, "English")

    def localized_asset_code():
        return localized_asset_codes.get(persistent.language, "EN")

    def localized_image(base_name, fallback_suffix="en"):
        
        image_name = "{}_{}".format(base_name, localized_asset_suffix())

        if renpy.has_image(image_name):
            return image_name

        return "{}_{}".format(base_name, fallback_suffix)

    def show_localized_image(base_name, *transforms, **kwargs):

        renpy.show(
            localized_image(base_name),
            at_list=list(transforms),
            layer=kwargs.get("layer", None),
            zorder=kwargs.get("zorder", None),
        )

    def hide_localized_image(base_name, layer=None):

        for suffix in localized_asset_suffixes.values():
            renpy.hide("{}_{}".format(base_name, suffix), layer=layer)

    def localized_asset_path(path_template):

        path = path_template.format(
            folder=localized_asset_folder(),
            suffix=localized_asset_suffix(),
            code=localized_asset_code(),
        )

        if renpy.loadable(path):
            return path

        return path_template.format(folder="English", suffix="en", code="EN")

    ACHIEVEMENT_LEGACY_FLAGS = {
        "forever_yours": "game_finished_once",
        "wrong_love_story": "reached_bad_ending_once",
        "just_a_student": "police_not_caught_once",
        "perfect_innocence": "police_0suspicion_once",
        "cuffed_and_loved": "police_caught_once",
        "abnormal_panic": "police_100suspicion_once",
        "too_careless": "counselor_suspended_once",
        "behind_the_mask": "counselor_not_suspended_once",
        "rickrolled": "rickrolled",
        "are_you_trying_to_skip": "skip_easteregg_seen",
        "this_is_her_game": "yandere_menu_easteregg_seen",
    }

    def _achievement_data_by_id():

        return {
            achievement["id"]: achievement
            for achievement in extras_achievement_data
        }

    def _required_achievement_ids():

        return set(
            achievement["id"]
            for achievement in extras_achievement_data
            if not achievement.get("debug_only", False)
            and achievement["id"] != "loyal_player"
        )

    def _migrate_legacy_achievement_ids():

        valid_ids = set(_achievement_data_by_id())
        unlocked_ids = []

        for achievement_id in (persistent.unlocked_achievement_ids or []):

            if achievement_id in valid_ids and achievement_id not in unlocked_ids:
                unlocked_ids.append(achievement_id)

        for achievement_id, legacy_flag in ACHIEVEMENT_LEGACY_FLAGS.items():

            if getattr(persistent, legacy_flag, False) and achievement_id not in unlocked_ids:
                unlocked_ids.append(achievement_id)

        if _required_achievement_ids().issubset(set(unlocked_ids)) and "loyal_player" not in unlocked_ids:
            unlocked_ids.append("loyal_player")

        if unlocked_ids != (persistent.unlocked_achievement_ids or []):
            persistent.unlocked_achievement_ids = unlocked_ids

        return unlocked_ids

    def achievement_is_unlocked(achievement_id):

        achievement = _achievement_data_by_id().get(achievement_id)

        if achievement is None:
            return False
    
        if achievement.get("debug_only", False):
            return True

        return achievement_id in _migrate_legacy_achievement_ids()

    def _show_achievement_notification(achievement_id, transform):

        image_name = localized_image("ac_{}".format(achievement_id))

        if renpy.has_image(image_name):

            renpy.show(
                image_name,
                at_list=[transform],
                layer="uiimages",
                zorder=10,
            )

    def get_achievement(achievement_id, show_notification=True):

        achievement = _achievement_data_by_id().get(achievement_id)

        if achievement is None:
            raise Exception("Unknown achievement id: {}".format(achievement_id))
        
        if achievement.get("debug_only", False):
            return False

        unlocked_ids = _migrate_legacy_achievement_ids()

        if achievement_id in unlocked_ids:
            return False

        unlocked_ids = unlocked_ids + [achievement_id]
        persistent.unlocked_achievement_ids = unlocked_ids

        legacy_flag = ACHIEVEMENT_LEGACY_FLAGS.get(achievement_id)
        
        if legacy_flag:
            setattr(persistent, legacy_flag, True)

        if show_notification:
            _show_achievement_notification(achievement_id, show_slide_achievement)

        if (
            achievement_id != "loyal_player"
            and "loyal_player" not in unlocked_ids
            and _required_achievement_ids().issubset(set(unlocked_ids))
        ):
            persistent.unlocked_achievement_ids = unlocked_ids + ["loyal_player"]

            if show_notification:
                _show_achievement_notification("loyal_player", show_slide_achievement2)
        
        renpy.save_persistent()
        return True


# These are player gender pronouns.
init python:

    def gender_male():

        persistent.him_her = "him"
        persistent.his_her = "his"
        persistent.gender = "boy"
        persistent.he_she = "he"
        persistent.He_She = "He"

        persistent.çocuk_kız = "çocuk"
        persistent.çocuğu_kızı = "çocuğu"

        persistent.el_ella = "él"
        persistent.El_Ella = "Él"
        persistent.lo_la = "lo"
        persistent.un_una = "un"
        persistent.chico_chica = "chico"
        persistent.o_a = "o"
        persistent.nosotros_nosotras = "nosotros"
        persistent.Nosotros_Nosotras = "Nosotros"
        persistent.vosotros_vosotras = "vosotros"
        persistent.Vosotros_Vosotras = "Vosotros"
        persistent.ellos_ellas = "ellos"
        persistent.Ellos_Ellas = "Ellos"
        persistent.los_las = "los"
        persistent.Los_Las = "Los"
        persistent.el_jugador_la_jugadora = "el jugador"
        persistent.al_jugador_a_la_jugadora = "al jugador"

        persistent.он_она = "он"
        persistent.Он_Она = "Он"
        persistent.его_её = "его"
        persistent.ему_ей = "ему"
        persistent.ним_ней = "ним"
        persistent.него_неё = "него"
        persistent.мальчик_девочка = "мальчик"
        persistent.мальчиком_девочкой = "мальчиком"
        persistent.хороший_хорошая = "хороший"
        persistent.хорошим_хорошей = "хорошим"
        persistent.окончание_а = ""
        persistent.счастлив_счастлива = "счастлив"

    def gender_female():

        persistent.him_her = "her"
        persistent.his_her = "her"
        persistent.gender = "girl"
        persistent.he_she = "she"
        persistent.He_She = "She"

        persistent.çocuk_kız = "kız"
        persistent.çocuğu_kızı = "kızı"

        persistent.el_ella = "ella"
        persistent.El_Ella = "Ella"
        persistent.lo_la = "la"
        persistent.un_una = "una"
        persistent.chico_chica = "chica"
        persistent.o_a = "a"
        persistent.nosotros_nosotras = "nosotras"
        persistent.Nosotros_Nosotras = "Nosotras"
        persistent.vosotros_vosotras = "vosotras"
        persistent.Vosotros_Vosotras = "Vosotras"
        persistent.ellos_ellas = "ellas"
        persistent.Ellos_Ellas = "Ellas"
        persistent.los_las = "las"
        persistent.Los_Las = "Las"
        persistent.el_jugador_la_jugadora = "la jugadora"
        persistent.al_jugador_a_la_jugadora = "a la jugadora"

        persistent.он_она = "она"
        persistent.Он_Она = "Она"
        persistent.его_её = "её"
        persistent.ему_ей = "ей"
        persistent.ним_ней = "ней"
        persistent.него_неё = "неё"
        persistent.мальчик_девочка = "девочка"
        persistent.мальчиком_девочкой = "девочкой"
        persistent.хороший_хорошая = "хорошая"
        persistent.хорошим_хорошей = "хорошей"
        persistent.окончание_а = "а"
        persistent.счастлив_счастлива = "счастлива"

init python: # This python function checks if the game is running for the first time by creating and checking the "firstrun" file.
    
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


# This function generates a random text by randomly selecting symbols.
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


# These functions disable or enable the dismiss keys.
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
    monitor_skip_call_active = False

    def can_trigger_monitoring_skip():

        if not monitor_skip or monitor_skip_call_active or not config.skipping:
            return False
        elif not config.allow_skipping or persistent.tried_skip or pause_menu_open:
            return False
        elif not renpy.store._skipping:
            return False
        elif renpy.game.preferences.skip_unseen or config.skipping == "fast":
            return True

        context = renpy.game.context()
        translate_identifier = context.translate_identifier

        return context.seen_current(True) or (translate_identifier and renpy.seen_translation(translate_identifier))

    def monitoring_skip():
        
        global monitor_skip_call_active

        if can_trigger_monitoring_skip():
            monitor_skip_call_active = True
            renpy.call("dontskip")

    config.interact_callbacks.append(monitoring_skip)


# Sanity Releated Functions
init python:

    def sanity_mode(mode, delay=0.5): # This function mutes or unmutes the music channels according to the main character's sanity.

        global sanity_mod

        if persistent.lock_sanity_level:

            if persistent.locked_sanity_percentage >= 70:
                mode = "high"
            elif persistent.locked_sanity_percentage >= 36:
                mode = "medium"
            else:
                mode = "low"

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

        if persistent.lock_sanity_level:
            return

        if prefix == "+":

            if persistent.low_fps_optimization == False:

                for _ in range(amount):

                    if sanity < 100:

                        sanity += 1

                        if sanity >= 50 and not textbox == "normal":
                            textbox = get_allowed_textbox_type("normal")
                        elif sanity < 50 and not textbox == "yandere":
                            textbox = get_allowed_textbox_type("yandere")
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

                        renpy.show("yandereblack", layer="yblack", at_list=[transparent(1.0 - (sanity / 100))])

                        renpy.pause(0.0, hard=True) # 0 seconds is one framerate waiting. It prevents the variable from reaching the target value instantly.

            else:

                for _ in range(int(amount / 5)):

                    if sanity < 96:

                        sanity += 5

                        if sanity >= 50 and not textbox == "normal":
                            textbox = get_allowed_textbox_type("normal")
                        elif sanity < 50 and not textbox == "yandere":
                            textbox = get_allowed_textbox_type("yandere")
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

                        renpy.show("yandereblack", layer="yblack", at_list=[transparent(1.0 - (sanity / 100))])

                        renpy.pause(0.0, hard=True)

        elif prefix == "-":

            if persistent.low_fps_optimization == False:

                for _ in range(amount):

                    if sanity > 0:

                        sanity -= 1

                        if sanity >= 50 and not textbox == "normal":
                            textbox = get_allowed_textbox_type("normal")
                        elif sanity < 50 and not textbox == "yandere":
                            textbox = get_allowed_textbox_type("yandere")
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

                        renpy.show("yandereblack", layer="yblack", at_list=[transparent(1.0 - (sanity / 100))])

                        renpy.pause(0.0, hard=True)

            else:

                for _ in range(int(amount / 5)):

                    if sanity > 4:

                        sanity -= 5

                        if sanity >= 50 and not textbox == "normal":
                            textbox = get_allowed_textbox_type("normal")
                        elif sanity < 50 and not textbox == "yandere":
                            textbox = get_allowed_textbox_type("yandere")
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

                        renpy.show("yandereblack", layer="yblack", at_list=[transparent(1.0 - (sanity / 100))])

                        renpy.pause(0.0, hard=True)


    def set_sanity(value): # This function directly sets the sanity percentage to the given value (you can't use negative values).

        global sanity
        global textbox
        sanity = value

        if sanity >= 50 and not textbox == "normal":
            textbox = get_allowed_textbox_type("normal")
        elif sanity < 50 and not textbox == "yandere":
            textbox = get_allowed_textbox_type("yandere")
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

        renpy.show("yandereblack", layer="yblack", at_list=[transparent(1.0 - (sanity / 100))])


# Atmosphere Releated Functions
init python:

    def change_atmosphere(prefix, amount, force=False):

        # This function changes the atmosphere percentage according to given arguments.

        global atmosphere
        global atmosphere_visual_updating

        atmosphere_visual_updating = True
        refresh_atmosphere_visuals()

        if persistent.lock_atmosphere_level and not force:
            atmosphere_visual_updating = False
            refresh_atmosphere_visuals()
            return

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

        atmosphere_visual_updating = False
        refresh_atmosphere_visuals()

    def set_atmosphere(amount): # This function instantly sets the atmosphere percentage to the given value (you can't set it to negative numbers or more than 100).

        global atmosphere

        atmosphere = amount
        refresh_atmosphere_visuals()

    def refresh_atmosphere_visuals():

        if renpy.showing("atm_sun"):
            renpy.show("atm_sun", at_list=[atm_sun_behavior()])

        if renpy.showing("atm_cloud"):
            renpy.show("atm_cloud", at_list=[atm_cloud_behavior()])

    def atm_matrix(): # This function changes the color saturation and brightness of the sprites according to atmosphere percentage (to prevent them appearing too dark or black and white).

        global atmosphere
        global ignore_atm

        if atmosphere > 67 or ignore_atm == True:
            return SaturationMatrix(1.0) * ContrastMatrix(1.0) * BrightnessMatrix(0.0)
        elif atmosphere > 50:
            return SaturationMatrix(1.0) * ContrastMatrix(1.15) * BrightnessMatrix(0.05)
        elif atmosphere > 35:
            return SaturationMatrix(1.0) * ContrastMatrix(1.2) * BrightnessMatrix(0.07)
        elif atmosphere > 10:
            return SaturationMatrix(1.0) * ContrastMatrix(1.4) * BrightnessMatrix(0.1)
        elif atmosphere <= 10:
            return SaturationMatrix(1.0) * ContrastMatrix(1.7) * BrightnessMatrix(0.15)
        else:
            pass

    def enable_atm(mode): # This function sets if the atmosphere is enabled or disabled. If you disable it, the game world will not be affected by the atmosphere percentage.

        global ignore_atm

        if persistent.enable_atmosphere_outside_school:
            ignore_atm = False
            renpy.call("atm_normal")
            return
    
        if mode == True:
            ignore_atm = False
            renpy.call("atm_normal")

        elif mode == False:
            ignore_atm = True
            renpy.call("atm_disabled")


    # These functions change the opacity of the sun and cloud image depending on the atmosphere percentage at the start of the chapters.
    def update_sun(trans, st, at):

        global atmosphere
        global atmosphere_visual_updating

        current_atm = max(0, min(100, atmosphere))

        trans.alpha = current_atm / 100.0

        if atmosphere_visual_updating:
            return 0

        return None

    def update_cloud(trans, st, at):

        global atmosphere
        global atmosphere_visual_updating

        current_atm = max(0, min(100, atmosphere))

        trans.alpha = (100 - current_atm) / 100.0

        value = 100 - current_atm
        trans.matrixcolor = ContrastMatrix(1.0 + (value * 0.008) ** 0.7)

        if atmosphere_visual_updating:
            return 0

        return None


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
            self.cached_sanity = None
            self.cached_line_color = "#ff8efd"
            self.cached_beat_duration = 1.0

        def render(self, width, height, st, at):

            if self.cached_sanity != sanity:
                self.cached_sanity = sanity

                # Cardiograph line color depending on the sanity percentage.
                if sanity >= 70:
                    self.cached_line_color = "#ff8efd"
                elif sanity > 35:
                    self.cached_line_color = "#ff7878"
                else:
                    self.cached_line_color = "#ff0000"

                # Cardiograph beat speed depending on the sanity percentage.
                self.cached_beat_duration = 1.0 - ((100 - sanity) * 0.007)

                if self.cached_beat_duration < 0.3:
                    self.cached_beat_duration = 0.3

            line_color = self.cached_line_color
            beat_duration = self.cached_beat_duration

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

                if y_pos < 4:
                    y_pos = 4

                if y_pos > 66:
                    y_pos = 66

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

init python:

    def sync_audio_volume(channel, persistent_field):
        
        try:
            value = float(getattr(persistent, persistent_field, 0.5))
        except (TypeError, ValueError):
            value = 0.5

        value = max(0.0, min(1.0, value))
        setattr(persistent, persistent_field, value)
        preferences.volumes[channel] = value ** 2

    def audio_volume_bar_value(channel, persistent_field):
        return FieldValue(persistent, persistent_field, range=1.0, action=Function(sync_audio_volume, channel, persistent_field))
