label easter_egg_trigger:

    $ config.allow_skipping = False
    stop music

    if not persistent.yandere_menu_enabled:
        scene front_school
        $ persistent.ymenu_enabled_saved = False

    else:
        scene front_school_scary
        $ persistent.ymenu_enabled_saved = True

    show black at transparent(0.7)
    show image "mainmenu/2.webp"

    $ get_achievement("this_is_her_game")

    $ renpy.pause(1, hard=True)
    $ play_ygirl_laugh_sound()
    $ persistent.yandere_menu_enabled = "easteregg"
    $ persistent.reset_easteregg_after_reload = False
    $ renpy.pause(4.5, hard=True)
    $ renpy.utter_restart()


label after_load:

    if persistent.lock_atmosphere_level:
        $ set_atmosphere(persistent.locked_atmosphere_percentage)

    if persistent.lock_sanity_level:
        $ set_sanity(persistent.locked_sanity_percentage)

    if persistent.enable_atmosphere_outside_school:
        $ enable_atm(True)

    $ restart_dynamic_music_after_load()
    
    $ persistent.ymenu_enabled_saved = yandere_menu_afterload
    $ persistent.yandere_menu_enabled = persistent.ymenu_enabled_saved 

    if not persistent.skip_hint_shown:
        show screen skip_hint
        $ persistent.skip_hint_shown = True

    $ akira_mc = Character(_("Akira & [persistent.playername]"), who_color="#fff700", ctc="ctc", ctc_position="fixed")
    $ mc = Character(_(persistent.playername), who_color="#29bf00", ctc="ctc", ctc_position="fixed")
    $ player = persistent.playername

    $ unlock_dismiss()