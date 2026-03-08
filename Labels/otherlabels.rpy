label atm_normal:

    camera:

        matrixcolor SaturationMatrix(0.3 + ((atmosphere * 0.008) ** 0.9) * ((sanity / 100.0) ** 1.7)) * ContrastMatrix(1.0 - ((100 - atmosphere) * 0.004) ** 0.7) * BrightnessMatrix(0.0 - (100 - atmosphere) * 0.003)

    return

label atm_disabled:

    camera:

        matrixcolor SaturationMatrix(0.3 + 0.8 * ((sanity / 100.0) ** 1.7))

    return

label go_to_main_menu:
    hide a
    stop music
    $ config.allow_skipping = True
    $ persistent.go_main_menu = True
    $ persistent.return_main_menu_counter += 1
    $ persistent.selected_chapter = None

    if persistent.yandere_menu_enabled:
        $ config.main_menu_music = scaryhorror
    else:
        $ config.main_menu_music = myfirstlove
        
    $ renpy.full_restart()

label before_main_menu:

    if persistent.yandere_menu_enabled == True:
        show vignette onlayer yblack at transparent(0.3)

    if persistent.go_main_menu:

        if not persistent.yandere_menu_enabled:
            scene black
            show front_school
            show a nk n oe cm happy at show_akira_menu()
        else:
            scene black
            show front_school_scary
            show a k y se om happy at show_akira_menu()

        show menulogo
        show white onlayer color

        hide white onlayer color with ff__

        if persistent.return_main_menu_counter == 5:
            $ renpy.pause(4.5, hard=True)
        else:
            $ renpy.pause(0.5, hard=True)

        $ persistent.go_main_menu = False

        if persistent.music_player_enabled and persistent.music_player_popup:
            
            show screen music_player
            $ persistent.music_player_popup = False

        return
