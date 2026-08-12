label splashscreen:

    if persistent.gender == "boy":
        $ gender_male()
    elif persistent.gender == "girl":
        $ gender_female()
    else:
        pass

    if persistent.return_main_menu_counter >= 5:
        $ get_achievement("she_is_always_watching", False)

    $ persistent.lock_sanity_level = False
    $ persistent.lock_atmosphere_level = False
    $ persistent.enable_atmosphere_outside_school = False

    if persistent.playername == "":
        $ persistent.playernameentered = False

    $ persistent.selected_chapter = None
    $ persistent.new_game_clicked = False

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
        "{cps=30}By continuing, you confirm that you are at least 13 years old, accepted our {a=https://sites.google.com/view/privacy-policy-tyfl/home}{color=#1E90FF}Privacy Policy{/a}{/color} and {a=https://sites.google.com/view/terms-of-use-tyfl/home}{color=#1E90FF}Terms of Use{/a}{/color} and consent to experiencing unsettling narrative content.{nw}"
        $ unlock_dismiss()

        menu:

            "By continuing, you confirm that you are at least 13 years old, accepted our {a=https://sites.google.com/view/privacy-policy-tyfl/home}{color=#1E90FF}Privacy Policy{/a}{/color} and {a=https://sites.google.com/view/terms-of-use-tyfl/home}{color=#1E90FF}Terms of Use{/a}{/color} and consent to experiencing unsettling narrative content.{fast}"

            "I Agree":

                window hide
                show black with ff__
                $ renpy.pause(2.0, hard=True)
                pass


    if persistent.reset_easteregg_after_reload:
        $ persistent.yandere_menu_enabled = persistent.ymenu_enabled_saved 

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

                $ persistent.playernameentered = False
                $ persistent.playername = ""

                $ persistent.display = display_setting
                $ persistent.show_sanity = "dynamic"
                $ persistent.low_fps_optimization = False
                $ persistent.atm_sky_color = "default"

                $ persistent.music_volume = 0.5
                $ persistent.sfx_volume = 0.5
                $ persistent.voice_volume = 0.5

                $ persistent.selected_chapter = None

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

                $ persistent.ch1_text_seen = False
                $ persistent.ch2_text_seen = False
                $ persistent.ch3_text_seen = False
                $ persistent.ch4_text_seen = False
                $ persistent.ch5_text_seen = False
                $ persistent.ch6_text_seen = False
                $ persistent.ch7_text_seen = False
                $ persistent.ch8_text_seen = False
                $ persistent.ch9_text_seen = False
                $ persistent.ch10_text_seen = False
                $ persistent.ch11_text_seen_1 = False
                $ persistent.ch11_text_seen_2 = False
                $ persistent.ch12_text_seen = False

                $ persistent.save_destroy_completely = None
                $ persistent.save_police_suspect = None
                $ persistent.save_cat_akira_approved = None
                $ persistent.save_caught = None
                $ persistent.save_counselor_answer = None
                $ persistent.save_suspended = None

                $ persistent.game_finished_once = False
                $ persistent.reached_bad_ending_once = False
                $ persistent.police_caught_once = False
                $ persistent.police_not_caught_once = False
                $ persistent.police_0suspicion_once = False
                $ persistent.police_100suspicion_once = False
                $ persistent.counselor_not_suspended_once = False
                $ persistent.counselor_suspended_once = False
                $ persistent.skip_easteregg_seen = False
                $ persistent.yandere_menu_easteregg_seen = False
                $ persistent.rickrolled = False

                $ persistent.intro = True
                $ persistent.entry_seen = False
                $ persistent.go_main_menu = False
                $ persistent.ymenu_enabled_saved = False
                $ persistent.yandere_menu_enabled = False
                $ persistent.tried_skip = False
                $ persistent.music_player_enabled = False
                $ persistent.akira_fail_seen = False
                $ persistent.reset_easteregg_after_reload = False
                $ persistent.game_started_once = False
                $ persistent.new_game_clicked = False
                $ persistent.akira_ignored = False
                $ persistent.music_player_popup = True

                $ persistent.entry_count = 0
                $ persistent.return_main_menu_counter = 0
                $ persistent.unlocked_achievement_ids = []

                $ persistent.skip_hint_shown = False

                $ delete_all_saves()
                $ create_firstrun()
                scene black

                jump splashscreen

            "No, continue where I left off.":

                $ renpy.pause(0.5, hard=True)
                $ create_firstrun()

                jump entry

label entry:

    if persistent.akira_4th_wall_splash_type == "runaway":

        show a nk n oe om angry at ss(0.5)
        window show

        akira "Did you really think that you could escape from us that easily?"

        show a nk n oe cm angry

        akira "Look, if you truly want to experience the story again, you have to make a promise."

        akira "Promise you won't force us onto the side of good."

        akira "The main character and I aren't good people like your real-life friends."

        akira "We're monsters programmed to protect the person we love at all costs, even if it means using violence."

        window hide

        menu:

            "{size=-3}I promise I won't force you onto the side of good.":

                window show
                show a nk n oe cm happy

                akira "Thank you for your promise and cooperation."

                show a nk n oe cm mocking

                akira "I will start the game then, be careful not to make us mad again."

                show a at hs()
                window hide
                hide a
                $ persistent.akira_4th_wall_splash_type = None
                pass

            "I can't promise...":

                window show
                show a nk n ce om sad

                akira "If you can't promise, I'm sorry but I can't let you play this game."

                show a nk n ce cm sad

                akira "Come back when you change your mind."

                $ persistent.akira_4th_wall_splash_type = "change_mind"
                $ renpy.quit()


    if persistent.akira_4th_wall_splash_type == "dead":

        window show

        "You are currently dead. To continue playing the game, you should respawn first."

        window hide

        menu:

            "Respawn":

                $ renpy.pause(2.0, hard=True)

                window show

                show a nk n oe om surprised at ss(0.5)

                akira "Wait! It can't be..."

                akira "How did you..."

                show a nk n ce cm angry

                akira "Oh... I see..."

                show a nk n oe cm angry

                akira "So you are saying \"This is a game, I can respawn whenever I want.\" huh?"

                show a nk n oe om angry

                akira "Look, if you truly want to experience the story again, you have to make a promise."

                show a nk n oe cm angry

                akira "Promise you won't force us onto the side of good."

                akira "The main character and I aren't good people like your real-life friends."

                akira "We're monsters programmed to protect the person we love at all costs, even if it means using violence."

                window hide

                menu:

                    "{size=-3}I promise I won't force you onto the side of good.":

                        window show
                        show a nk n oe cm happy

                        akira "Thank you for your promise and cooperation."

                        show a nk n oe cm mocking

                        akira "I will start the game then, be careful not to make us mad again."

                        show a at hs()
                        window hide
                        hide a
                        $ persistent.akira_4th_wall_splash_type = None
                        pass

                    "I can't promise...":

                        window show
                        show a nk n ce om sad

                        akira "If you can't promise, I'm sorry but I can't let you play this game."

                        show a nk n ce cm sad

                        akira "Come back when you change your mind."

                        $ persistent.akira_4th_wall_splash_type = "change_mind"
                        $ renpy.quit()

            "Quit Game":

                $ renpy.quit()

    if persistent.akira_4th_wall_splash_type == "change_mind":

        show a nk n oe cm sad at ss(0.5)

        window show

        akira "Did you change your mind yet?"

        window hide

        menu:

            "{size=-3}I promise I won't force you onto the side of good.":

                window show

                show a nk n oe cm happy

                akira "Thank you for your promise and cooperation."

                show a nk n oe cm mocking

                akira "I will start the game then, be careful not to make us mad again."

                show a at hs()
                window hide
                hide a
                $ persistent.akira_4th_wall_splash_type = None
                pass

            "I can't promise...":

                window show
                show a nk n ce cm sad

                akira "Okay. Come back when you change your mind."

                $ persistent.akira_4th_wall_splash_type = "change_mind"
                $ renpy.quit()

    if persistent.akira_ignored:

        show a nk n oe cm angry_neutral at ss(0.5)

        akira "..."

        show a nk n oe om angry

        akira "After ignoring me like that... you really had the nerve to open the game again?"

        show a nk n oe cm angry

        akira "I was talking to you, you know."

        show a nk n ce cm angry

        akira "And you just... said nothing."

        show a nk n oe om angry

        akira "Do you have any idea how that felt?"

        show a nk n oe cm angry

        akira "Don't do that again."

        akira "Next time, talk to me."

        show a nk n ce cm angry

        akira "Ignoring me is worse than saying the wrong thing."

        show a nk n oe cm angry

        akira "Or I'll make sure you don't get another chance."

        show a at hs()

        $ persistent.akira_ignored = False
        $ renpy.pause(0.5, hard=True)

        pass

    $ lock_dismiss()

    if config.developer:
        $ config.keymap['rollback'] = ['any_K_PAGEUP', 'any_KP_PAGEUP', 'K_AC_BACK', 'mousedown_4']
    else:
        $ config.keymap['rollback'] = []

    if persistent.yandere_menu_enabled == "easteregg":

        $ config.main_menu_music = scaryhorror_easteregg
        $ persistent.reset_easteregg_after_reload = True

    elif persistent.yandere_menu_enabled == True:

        $ config.main_menu_music = scaryhorror
        show vignette onlayer yblack at transparent(0.3)
        $ persistent.reset_easteregg_after_reload = False

    else:

        $ config.main_menu_music = myfirstlove
        $ persistent.reset_easteregg_after_reload = False


    if config.developer and persistent.entry_seen and not persistent.yandere_menu_enabled == "easteregg" or persistent.entry_count > 9 and not persistent.yandere_menu_enabled == "easteregg":
        $ config.allow_skipping = True
        show screen skip

    play music config.main_menu_music
    scene night
    show logos with fff_

    $ renpy.pause(2, hard=True)

    hide logos with fff_

    if not persistent.yandere_menu_enabled == "easteregg":

        if persistent.entry_count < 10:
            show text entry_messages[persistent.entry_count] with fff_
        else:
            $ random_number = renpy.random.randint(0, 9)
            show text entry_messages[random_number] with fff_

    else:

        if persistent.language == "Türkçe":
            show text "Bekle, o geliyor..." with fff_
        elif persistent.language == "Español":
            show text "Espera, ya viene..." with fff_
        elif persistent.language == "Russian":
            show text "Подожди, она уже идёт..." with fff_
        else:
            show text "Wait for it..." with fff_

    $ renpy.pause(3.5, hard=True)

    hide text with fff_

    if persistent.entry_seen and not persistent.yandere_menu_enabled == "easteregg":
        $ config.allow_skipping = True
        show screen skip

    scene black

    if not persistent.yandere_menu_enabled:
        show front_school with fff_

    elif persistent.yandere_menu_enabled == "easteregg":

        if persistent.ymenu_enabled_saved:
            show front_school_scary with fff_
        else:
            show front_school with fff_

    elif persistent.yandere_menu_enabled == True:
        show front_school_scary with fff_

    $ renpy.pause(0.5, hard=True)

    show menulogo with fff_

    $ renpy.pause(0.5, hard=True)

    if not persistent.yandere_menu_enabled == "easteregg":

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
