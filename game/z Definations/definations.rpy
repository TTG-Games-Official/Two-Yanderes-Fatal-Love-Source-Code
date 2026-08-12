# Engine Layers
define config.layers = ['master','atm_sky', 'atm_world', 'transient', 'a', 'askip', 'vignette', 'yblack', 'uiimages', 'screens', 'color', 'overlay']

# Player and Forbidden Names
default forbidden_names = ["akira", "police 3", "police 4", "male police", "clara", "counselor", "teacher", "mother", "souta", "takuya", "kenta", "daichi", "katori", "haruki", "boy", "girl", "girl 1", "girl 2", "girl 3", "girl 4", "boy 1", "boy 2", "boy 3", "boy 4"]
default persistent.playernameentered = False
default persistent.playername = ""

# Language and Gender
default persistent.language = "English"

default persistent.him_her = "him"
default persistent.his_her = "his"
default persistent.gender = "boy"
default persistent.he_she = "he"
default persistent.He_She = "He"

default persistent.çocuk_kız = "çocuk"
default persistent.çocuğu_kızı = "çocuğu"

default persistent.el_ella = "él"
default persistent.El_Ella = "Él"
default persistent.lo_la = "lo"
default persistent.un_una = "un"
default persistent.chico_chica = "chico"
default persistent.o_a = "o"
default persistent.nosotros_nosotras = "nosotros"
default persistent.Nosotros_Nosotras = "Nosotros"
default persistent.vosotros_vosotras = "vosotros"
default persistent.Vosotros_Vosotras = "Vosotros"
default persistent.ellos_ellas = "ellos"
default persistent.Ellos_Ellas = "Ellos"
default persistent.los_las = "los"
default persistent.Los_Las = "Los"
default persistent.el_jugador_la_jugadora = "el jugador"
default persistent.al_jugador_a_la_jugadora = "al jugador"

default persistent.он_она = "он"
default persistent.Он_Она = "Он"
default persistent.его_её = "его"
default persistent.ему_ей = "ему"
default persistent.ним_ней = "ним"
default persistent.него_неё = "него"
default persistent.мальчик_девочка = "мальчик"
default persistent.мальчиком_девочкой = "мальчиком"
default persistent.хороший_хорошая = "хороший"
default persistent.хорошим_хорошей = "хорошим"
default persistent.окончание_а = ""
default persistent.счастлив_счастлива = "счастлив"

# Quick Menu
default quick_menu = False

default settings_enabled = True
default history_enabled = True
default hide_enabled = True
default auto_enabled = True

# Settings
default selected_button = None
default pause_menu_open = False

default extras_category = "achievements"

default persistent.display = 1
default persistent.show_sanity = "dynamic"
default persistent.low_fps_optimization = False
default persistent.atm_sky_color = "default"

default preferences.text_cps = 75
default preferences.afm_time = 8

default persistent.music_volume = 0.5
default persistent.sfx_volume = 0.5
default persistent.voice_volume = 0.5

# Gameplay Systems
default ignore_atm = False
default atmosphere_visual_updating = False

default hide_sanity_force = False
default show_sanity_important = False

default show_police_suspect = False

default sanity = 100
default atmosphere = 100
default suspicion = 0
default saved_suspicion = 0

default red_protection_strength = 1.0
default sanity_cardiograph = Cardiograph()
default sanity_mod = "high"
default textbox = "normal"

# Story Choice States
default kill_now = False
default scarytext = False
default rejected_crime = False
default akira_cat = False
default yelled_akira = False
default amusement_p = False

default tool = ""

default eşya = ""
default eşyayı = ""

default herramienta = ""
default herramienta_indef = ""

default инструмент = ""
default инструмент_вин = ""
default инструмент_тв = ""

# Story General
default random_number = None
default chapter = None

# Cheats
default persistent.lock_sanity_level = False
default persistent.lock_atmosphere_level = False
default persistent.enable_atmosphere_outside_school = False
default persistent.locked_sanity_percentage = 100
default persistent.locked_atmosphere_percentage = 100

# Chapter Unlocks
default persistent.selected_chapter = None

default persistent.chapter1enabled = True
default persistent.chapter2enabled = False
default persistent.chapter3enabled = False
default persistent.chapter4enabled = False
default persistent.chapter5enabled = False
default persistent.chapter6enabled = False
default persistent.chapter7enabled = False
default persistent.chapter8enabled = False
default persistent.chapter9enabled = False
default persistent.chapter10enabled = False
default persistent.chapter11enabled = False
default persistent.chapter12enabled = False

# Chapter Start Text Seen
default persistent.ch1_text_seen = False
default persistent.ch2_text_seen = False
default persistent.ch3_text_seen = False
default persistent.ch4_text_seen = False
default persistent.ch5_text_seen = False
default persistent.ch6_text_seen = False
default persistent.ch7_text_seen = False
default persistent.ch8_text_seen = False
default persistent.ch9_text_seen = False
default persistent.ch10_text_seen = False
default persistent.ch11_text_seen_1 = False
default persistent.ch11_text_seen_2 = False
default persistent.ch12_text_seen = False

# Persistent Story Stats
default persistent.save_destroy_completely = None
default persistent.save_police_suspect = None
default persistent.save_cat_akira_approved = None
default persistent.save_caught = None
default persistent.save_counselor_answer = None
default persistent.save_suspended = None

# Story Stats
default destroy_completely = None
default police_suspect = None
default cat_akira_approved = None
default caught = None
default counselor_answer = None
default suspended = None

default persistent.akira_4th_wall_splash_type = None

# Achievements
default persistent.game_finished_once = False
default persistent.reached_bad_ending_once = False
default persistent.police_caught_once = False
default persistent.police_not_caught_once = False
default persistent.police_0suspicion_once = False
default persistent.police_100suspicion_once = False
default persistent.counselor_not_suspended_once = False
default persistent.counselor_suspended_once = False
default persistent.skip_easteregg_seen = False
default persistent.yandere_menu_easteregg_seen = False
default persistent.rickrolled = False

# Persistent Progress Flags
default persistent.intro = True
default persistent.entry_seen = False
default persistent.go_main_menu = False
default persistent.ymenu_enabled_saved = False
default persistent.yandere_menu_enabled = False
default persistent.tried_skip = False
default persistent.music_player_enabled = False
default persistent.akira_fail_seen = False
default persistent.reset_easteregg_after_reload = False
default persistent.game_started_once = False
default persistent.new_game_clicked = False
default persistent.akira_ignored = False
default persistent.music_player_popup = True

# Persistent Counters
default persistent.entry_count = 0
default persistent.return_main_menu_counter = 0
default persistent.unlocked_achievement_ids = []

# Misc Runtime Defaults
default yandere_menu_afterload = False
default persistent.skip_hint_shown = False

# Transitions
define ffff = Dissolve(0.2)
define fff_ = Dissolve(0.5)
define ff__ = Dissolve(1.0)
define f___ = Dissolve(3.0)

# Game Config
define config.window = "hide"

define config.enter_transition = ffff
define config.exit_transition = ffff
define config.intra_transition = ffff
define config.after_load_transition = None
define config.end_game_transition = None

define config.window_show_transition = ffff
define config.window_hide_transition = ffff

define config.has_sound = True
define config.has_music = True
define config.has_voice = False

define config.name = _("Two Yanderes & Fatal Love")
define gui.show_name = False
define config.version = "3.4.1"

define config.image_cache_size_mb = 512
define config.gl2 = True

define build.name = "TYFL"
define config.save_directory = "Two Yanderes & Fatal Love"
define config.window_icon = "gui/overlay/window_icon.webp"
define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }
