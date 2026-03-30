define config.layers = ['master', 'transient', 'a', 'askip', 'vignette', 'yblack', 'uiimages', 'screens', 'color', 'overlay']
default forbidden_names = ["akira", "clara", "counselor", "teacher", "souta", "takuya", "kenta", "daichi", "katori", "haruki", "boy", "girl"]

default settings_enabled = True
default history_enabled = True
default hide_enabled = True
default auto_enabled = True
default atm_active = True

default ignore_atm = False
default hide_sanity_force = False
default quick_menu = False
default pause_menu_open = False
default show_sanity_important = False
default show_police_suspect = False
default yandere_menu_check = False
default yandere_menu_afterload = False
default scarytext = False
default rejected_crime = False
default akira_cat = False
default yelled_akira = False

default selected_button = None
default random_number = None
default chapter = None
default caught = None
default suspended = None
default counselor_answer = None
default destroy_completely = None
default police_suspect = None
default cat_akira_approved = None

default preferences.text_cps = 75
default preferences.afm_time = 8
default sanity = 100
default atmosphere = 100
default atmosphere_saved = 100
default suspicion = 0
default saved_suspicion = 0

default sanity_cardiograph = Cardiograph()

default extras_category = "achievements"
default sanity_mod = "high"
define config.window = "hide"
default textbox = "normal"


default persistent.game_finished_achievement_notification = True
default persistent.bad_ending_achievement_notification = True
default persistent.police_caught_achievement_notification = True
default persistent.police_not_caught_achievement_notification = True
default persistent.police_0suspicion_achievement_notification = True
default persistent.police_100suspicion_achievement_notification = True
default persistent.music_player_popup = True
default persistent.intro = True

default persistent.entry_seen = False
default persistent.go_main_menu = False
default persistent.playernameentered = False
default persistent.ymenu_enabled_saved = False
default persistent.yandere_menu_enabled = False
default persistent.music_player_enabled = False
default persistent.akira_fail_seen = False
default persistent.game_started_once = False
default persistent.game_finished_once = False
default persistent.reached_bad_ending_once = False
default persistent.police_caught_once = False
default persistent.police_not_caught_once = False
default persistent.police_0suspicion_once = False
default persistent.police_100suspicion_once = False
default persistent.counselor_not_suspended_once = False
default persistent.counselor_suspended_once = False
default persistent.skip_hint_shown = False
default persistent.low_fps_optimization = False
default persistent.new_game_clicked = False

default persistent.selected_chapter = None
default persistent.save_destroy_completely = None
default persistent.save_police_suspect = None
default persistent.save_cat_akira_approved = None
default persistent.save_caught = None
default persistent.save_counselor_answer = None
default persistent.save_suspended = None

default persistent.playername = ""
default persistent.show_sanity = "dynamic"
default persistent.language = "English"

default persistent.him_her = "him"
default persistent.his_her = "his"
default persistent.gender = "boy"
default persistent.he_she = "he"
default persistent.He_She = "He"
default persistent.çocuk_kız = "çocuk"

default persistent.music_volume = 0.5
default persistent.sfx_volume = 0.5
default persistent.voice_volume = 0.5
default persistent.entry_count = 0
default persistent.display = 1
default persistent.return_main_menu_counter = 0
default persistent.achievements_unlocked = 0
default persistent.change_speed = 0.15

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

define ffff = Dissolve(0.2)
define fff_ = Dissolve(0.5)
define ff__ = Dissolve(1.0)
define f___ = Dissolve(3.0)

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
define config.version = "3.1.5"

define config.image_cache_size_mb = 512
define config.gl2 = True

define build.name = "TYFL"
define config.save_directory = "Two Yanderes & Fatal Love"
define config.window_icon = "gui/overlay/window_icon.webp"

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }