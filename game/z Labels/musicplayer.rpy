init python:

    ost_text_screens = ["osttext%d" % i for i in range(1, 28)]

    def hide_ost_text_screens():
        
        for screen_name in ost_text_screens:
            renpy.hide_screen(screen_name)


label play_ost_track(screen_name, music_name, background_name, black_alpha, character_name, show_vignette=False):

    $ renpy.pause(0.5, hard=True)

    if black_alpha is None:
        $ renpy.show("black")
    else:
        $ renpy.show("black", at_list=[transparent(black_alpha)])

    $ renpy.show(background_name, at_list=[ostbg_move])

    if show_vignette:
        show vignette

    $ renpy.show("menulogo", at_list=[zoom(1.4)])
    $ renpy.show(character_name, at_list=[akira_ost])
    $ renpy.pause(0.5, hard=True)
    $ renpy.show_screen(screen_name)
    $ renpy.music.play(music_name, channel="music")

    return


label ost:

    $ quick_menu = False
    stop music
    hide vignette onlayer yblack
    scene white

    menu:
        
        "Arrest Panic":
            call play_ost_track("osttext1", arrest_panic, "ostbg_normal", 0.5, "a nk n oe om surprised")

        "Unfixable Pain":
            call play_ost_track("osttext2", unfixable_pain, "ostbg_normal", 0.5, "a nk n oe cm verysad")

        "Corpse Panic":
            call play_ost_track("osttext3", corpse_panic, "ostbg_normal", 0.1, "a nk n oe om surprised", True)

        "Evening Glow":

            $ renpy.pause(0.1, hard=True)

            menu:

                "High Atmosphere - High Sanity":
                    call play_ost_track("osttext4", evening_glow_h_h, "ostbg_normal", 0.1, "a nk n oe cm happy")

                "High Atmosphere - Medium Sanity":
                    call play_ost_track("osttext5", evening_glow_h_m, "ostbg_yandere", 0.1, "a nk y se om happy", True)

                "High Atmosphere - Low Sanity":
                    call play_ost_track("osttext6", evening_glow_h_l, "ostbg_yandere", None, "a b bk y se om happy", True)

                "Medium Atmosphere - High Sanity":
                    call play_ost_track("osttext22", evening_glow_m_h, "ostbg_normal", 0.3, "a nk n oe cm neutral")

                "Medium Atmosphere - Medium Sanity":
                    call play_ost_track("osttext23", evening_glow_m_m, "ostbg_yandere", 0.3, "a nk n se cm neutral", True)

                "Medium Atmosphere - Low Sanity":
                    call play_ost_track("osttext24", evening_glow_m_l, "ostbg_yandere", None, "a b bk y se cm angry_neutral", True)

                "Low Atmosphere - High Sanity":
                    call play_ost_track("osttext25", evening_glow_l_h, "ostbg_normal", 0.5, "a nk n oe cm sad")

                "Low Atmosphere - Medium Sanity":
                    call play_ost_track("osttext26", evening_glow_l_m, "ostbg_yandere", 0.5, "a nk y se cm angry", True)

                "Low Atmosphere - Low Sanity":
                    call play_ost_track("osttext27", evening_glow_l_l, "ostbg_yandere", None, "a b bk y se om angry", True)
                
                "<<< | Go Back To Music List":
                    $ renpy.pause(0.1, hard=True)
                    jump ost

        "Schoolday":

            $ renpy.pause(0.1, hard=True)

            menu:

                "High Atmosphere - High Sanity":
                    call play_ost_track("osttext7", schoolday_h_h, "ostbg_normal", 0.1, "a nk n oe cm happy")

                "High Atmosphere - Medium Sanity":
                    call play_ost_track("osttext8", schoolday_h_m, "ostbg_yandere", 0.1, "a nk y se om happy", True)

                "High Atmosphere - Low Sanity":
                    call play_ost_track("osttext9", schoolday_h_l, "ostbg_yandere", None, "a b bk y se om happy", True)

                "Medium Atmosphere - High Sanity":
                    call play_ost_track("osttext10", schoolday_m_h, "ostbg_normal", 0.3, "a nk n oe cm neutral")

                "Medium Atmosphere - Medium Sanity":
                    call play_ost_track("osttext11", schoolday_m_m, "ostbg_yandere", 0.3, "a nk n se cm neutral", True)

                "Medium Atmosphere - Low Sanity":
                    call play_ost_track("osttext12", schoolday_m_l, "ostbg_yandere", None, "a b bk y se cm angry_neutral", True)

                "Low Atmosphere - High Sanity":
                    call play_ost_track("osttext13", schoolday_l_h, "ostbg_normal", 0.5, "a nk n oe cm sad")

                "Low Atmosphere - Medium Sanity":
                    call play_ost_track("osttext14", schoolday_l_m, "ostbg_yandere", 0.5, "a nk y se cm angry", True)

                "Low Atmosphere - Low Sanity":
                    call play_ost_track("osttext15", schoolday_l_l, "ostbg_yandere", None, "a b bk y se om angry", True)

                "<<< | Go Back To Music List":
                    $ renpy.pause(0.1, hard=True)
                    jump ost

        "Echoes of Love":

            $ renpy.pause(0.1, hard=True)

            menu:

                "High Atmosphere - High Sanity":
                    call play_ost_track("osttext16", echoesoflove_h_h, "ostbg_normal", 0.1, "a nk n oe cm happy")

                "High Atmosphere - Medium Sanity":
                    call play_ost_track("osttext17", echoesoflove_h_m, "ostbg_yandere", 0.1, "a nk y se om happy", True)

                "High Atmosphere - Low Sanity":
                    call play_ost_track("osttext18", echoesoflove_h_l, "ostbg_yandere", None, "a b bk y se om happy", True)

                "Low Atmosphere - High Sanity":
                    call play_ost_track("osttext19", echoesoflove_l_h, "ostbg_normal", 0.5, "a nk n oe cm sad")

                "Low Atmosphere - Medium Sanity":
                    call play_ost_track("osttext20", echoesoflove_l_m, "ostbg_yandere", 0.5, "a nk y se cm angry", True)

                "Low Atmosphere - Low Sanity":
                    call play_ost_track("osttext21", echoesoflove_l_l, "ostbg_yandere", None, "a b bk y se om angry", True)

                "<<< | Go Back To Music List":
                    $ renpy.pause(0.1, hard=True)
                    jump ost

        "(?) Some Tracks Are Missing?":

            window show

            "Some of the music used in the game is licensed from third-party providers."

            "Because of licensing limitations, those tracks are not considered part of the original soundtrack."

            "For this reason, only the tracks produced by the developer are available in this music player."

            window hide

            jump ost

        "<<< | Go To Main Menu":
            $ renpy.pause(0.3, hard=True)
            jump go_to_main_menu


label waiting:

    pause

    menu:

        "Choose Another Music":

            $ hide_ost_text_screens()

            $ renpy.pause(0.3, hard=True)

            jump ost

        "Go To Main Menu":
            $ renpy.pause(0.3, hard=True)
            jump go_to_main_menu

        "Nevermind":
            jump waiting