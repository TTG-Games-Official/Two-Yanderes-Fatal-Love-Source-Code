label splashscreen:

    if persistent.playername == "":
        $ persistent.playernameentered = False

    $ persistent.new_game_clicked = False
    $ persistent.selected_chapter = None

    if config.developer:
        $ config.keymap['rollback'] = ['any_K_PAGEUP', 'any_KP_PAGEUP', 'K_AC_BACK', 'mousedown_4']
    else:
        $ config.keymap['rollback'] = []

    $ quick_menu = False
    $ config.allow_skipping = False
    $ monitor_skip = False
    $ style.say_dialogue = style.normaltext
    
    $ preferences.volumes['music'] = persistent.music_volume ** 2
    $ preferences.volumes['sfx'] = persistent.sfx_volume ** 2
    $ preferences.volumes['voice'] = persistent.voice_volume ** 2

    if not persistent.entry_seen:
        scene previous_save with ff__
        $ renpy.pause(1.0, hard=True)
        window show

        $ lock_dismiss()
        "{cps=30}This visual novel is not suitable for children or those who are easily disturbed.{nw}"
        $ unlock_dismiss()
        "This visual novel is not suitable for children or those who are easily disturbed.{fast}"

        $ lock_dismiss()
        "{cps=30}It contains psychological horror elements, disturbing themes, bad language, and suggestive dialogue.{nw}"
        $ unlock_dismiss()
        "It contains psychological horror elements, disturbing themes, bad language, and suggestive dialogue.{fast}"

        $ lock_dismiss()
        "{cps=30}Blood and violence are present, but are usually conveyed through narration rather than shown directly.{nw}"
        $ unlock_dismiss()
        "Blood and violence are present, but are usually conveyed through narration rather than shown directly.{fast}"

        $ lock_dismiss()
        "{cps=30}By continuing, you confirm that you are at least 13 years old and consent to experiencing unsettling narrative content.{nw}"
        $ unlock_dismiss()

        menu:

            "By continuing, you confirm that you are at least 13 years old and consent to experiencing unsettling narrative content.{fast}"

            "I Agree":

                window hide
                show black with ff__
                $ renpy.pause(2.0, hard=True)
                pass
    
    if check_firstrun():
        jump entry

    elif not persistent.entry_seen:
        $ create_firstrun()
        $ delete_all_saves()
        jump entry

    else:

        scene previous_save

        $ lock_dismiss()
        "{cps=30}A previous save file has been found. Would you like to reset your progress and start over?{nw}"
        $ unlock_dismiss()

        menu:
            "A previous save file has been found. Would you like to reset your progress and start over?{fast}"

            "Yes, reset my progress.":

                $ lock_dismiss()
                "{cps=30}Resetting Progress...{w=0.5}{nw}"
                $ unlock_dismiss()

                $ display_setting = persistent.display
                $ preferences.skip_unseen = False
                $ preferences.skip_after_choices = False
                $ preferences.text_cps = 75
                $ preferences.afm_time = 8
                $ preferences.afm_enable = False
                $ selected_button = None
                $ afm_pause = False
                
                $ persistent.display = display_setting

                $ persistent.entry_seen = False
                $ persistent.go_main_menu = False
                $ persistent.playernameentered = False
                $ persistent.ymenu_enabled_saved = False
                $ persistent.yandere_menu_enabled = False
                $ persistent.music_player_enabled = False
                $ persistent.akira_fail_seen = False
                $ persistent.game_started_once = False
                $ persistent.game_finished_once = False
                $ persistent.reached_bad_ending_once = False
                $ persistent.police_caught_once = False
                $ persistent.police_not_caught_once = False
                $ persistent.police_0suspicion_once = False
                $ persistent.police_100suspicion_once = False
                $ persistent.counselor_not_suspended_once = False
                $ persistent.counselor_suspended_once = False
                $ persistent.skip_hint_shown = False
                $ persistent.low_fps_optimization = False

                $ persistent.game_finished_achievement_notification = True
                $ persistent.bad_ending_achievement_notification = True
                $ persistent.return_main_menu_achievement_notification = True
                $ persistent.police_caught_achievement_notification = True
                $ persistent.police_not_caught_achievement_notification = True
                $ persistent.police_0suspicion_achievement_notification = True
                $ persistent.police_100suspicion_achievement_notification = True
                $ persistent.music_player_popup = True
                $ persistent.prologue = True

                $ persistent.selected_chapter = None

                $ persistent.playername = ""
                $ persistent.show_sanity = "dynamic"

                $ persistent.music_volume = 0.5
                $ persistent.sfx_volume = 0.5
                $ persistent.voice_volume = 0.5
                $ persistent.entry_count = 0
                $ persistent.achievements_unlocked = 0
                $ persistent.change_speed = 0.15

                $ persistent.chapter1enabled = True
                $ persistent.chapter2enabled = False
                $ persistent.chapter3enabled = False
                $ persistent.chapter4enabled = False
                $ persistent.chapter5enabled = False
                $ persistent.chapter6enabled = False
                $ persistent.chapter7enabled = False
                $ persistent.chapter8enabled = False
                $ persistent.chapter9enabled = False
                $ persistent.chapter10enabled = False
                $ persistent.chapter11enabled = False
                $ persistent.chapter12enabled = False

                $ persistent.save_destroy_completely = None
                $ persistent.save_police_suspect = None
                $ persistent.save_cat_akira_approved = None
                $ persistent.save_caught = None
                $ persistent.save_counselor_answer = None
                $ persistent.save_suspended = None

                $ delete_all_saves()
                $ create_firstrun()
                scene black

                jump splashscreen

            "No, continue where I left off.":

                $ renpy.pause(0.5, hard=True)
                $ create_firstrun()

                jump entry

label entry:

    $ lock_dismiss()

    if config.developer:
        $ config.keymap['rollback'] = ['any_K_PAGEUP', 'any_KP_PAGEUP', 'K_AC_BACK', 'mousedown_4']
    else:
        $ config.keymap['rollback'] = []
        
    if persistent.yandere_menu_enabled == True:
        $ config.main_menu_music = scaryhorror  
        show vignette onlayer yblack at transparent(0.3)

    else:
        $ config.main_menu_music = myfirstlove


    if config.developer and persistent.entry_seen or persistent.entry_count > 9:
        $ config.allow_skipping = True
        show screen skip
        
    play music config.main_menu_music
    scene night
    show logos with fff_

    $ renpy.pause(2, hard=True)

    hide logos with fff_
    
    if persistent.entry_count < 10:
        show text entry_messages[persistent.entry_count] with fff_
    else:
        $ random_number = renpy.random.randint(0, 9)
        show text entry_messages[random_number] with fff_

    $ renpy.pause(3.5, hard=True)

    hide text with fff_

    if persistent.entry_seen:
        $ config.allow_skipping = True
        show screen skip

    scene black

    if not persistent.yandere_menu_enabled:
        show front_school with fff_

    elif persistent.yandere_menu_enabled:
        show front_school_scary with fff_

    $ renpy.pause(0.5, hard=True)

    show menulogo with fff_

    $ renpy.pause(0.5, hard=True)

    if persistent.yandere_menu_enabled == False:
        show a nk n oe cm happy at show_akira_menu()
    else:
        show a k y se om happy at show_akira_menu()
        
    show white
    hide white with ff__

    $ renpy.pause(0.5, hard=True)
    $ persistent.entry_seen = True
    hide screen skip

    $ persistent.entry_count += 1

    $ config.allow_skipping = True
    $ unlock_dismiss()

    if persistent.music_player_enabled and persistent.music_player_popup:
        $ persistent.music_player_popup = False

    return