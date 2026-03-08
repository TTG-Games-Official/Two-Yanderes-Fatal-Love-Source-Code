screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"

    if main_menu:

        if persistent.yandere_menu_enabled == False:
            add "backgrounds/Uncle Mugen/Front School.webp"
        elif persistent.yandere_menu_enabled == True:
            add "backgrounds/Uncle Mugen/Front School Scary.webp"
        else:
            pass
        
        add "mainmenu/Black.webp" at transparent(0.7)

    else:

        add "mainmenu/Black.webp" at transparent(0.9)

        on "show" action SetVariable("pause_menu_open", True)
        on "hide" action SetVariable("pause_menu_open", False)


    add "mainmenu/1.webp" at menugrid1()
    add "mainmenu/2.webp" at menugrid2()

    text "{color=#ff54e2}{size=+5}v[config.version]" xalign 0.98 yalign 0.02

    if main_menu:
        add "mainmenu/menugamelogo.webp"
    else:
        if persistent.language == "Türkçe":
            add "mainmenu/menugamepause_tr.webp"
        else:
            add "mainmenu/menugamepause_en.webp"

    add "mainmenu/navigationbg.webp"
    add "mainmenu/navigationbg2.webp"

    frame:
        style "game_menu_outer_frame"

        hbox:

            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    use navigation

    if main_menu:
        textbutton _("RETURN"):
            style_prefix "mainmenu"
            yalign 0.946
            xpos 307

            action [Function(play_click_sound), Return()]

    else:
        textbutton _("CONTINUE"):
            style_prefix "mainmenu"
            yalign 0.946
            xpos 307

            action [Function(play_click_sound), Return()]

    label title

    if main_menu:

        key "game_menu" action ShowMenu("main_menu")

        if persistent.yandere_menu_enabled == True:
            add "images/Vignette.webp" at transparent(0.3)