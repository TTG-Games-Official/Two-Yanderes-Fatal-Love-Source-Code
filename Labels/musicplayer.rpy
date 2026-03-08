label ost:

    $ quick_menu = False
    stop music
    hide vignette onlayer yblack
    scene white
    menu:
        "Arrest Panic":

            $ renpy.pause(0.5, hard=True)
            show black at transparent(0.5)
            show ostbg_normal at ostbg_move
            show menulogo at zoom(1.4)
            show a nk n oe om surprised at akira_ost
            $ renpy.pause(0.5, hard=True)
            show screen osttext1
            play music arrest_panic

        "Unfixable Pain":
            $ renpy.pause(0.5, hard=True)
            show black at transparent(0.5)
            show ostbg_normal at ostbg_move
            show menulogo at zoom(1.4)
            show a nk n oe cm verysad at akira_ost
            $ renpy.pause(0.5, hard=True)
            show screen osttext2
            play music unfixable_pain

        "Corpse Panic":
            $ renpy.pause(0.5, hard=True)
            show black at transparent(0.1)
            show ostbg_normal at ostbg_move
            show vignette
            show menulogo at zoom(1.4)
            show a nk n oe om surprised at akira_ost
            $ renpy.pause(0.5, hard=True)
            show screen osttext3
            play music corpse_panic

        "Evening Glow":

            $ renpy.pause(0.1, hard=True)

            menu:
                "High Atmosphere - High Sanity":
                    $ renpy.pause(0.5, hard=True)
                    show black at transparent(0.1)
                    show ostbg_normal at ostbg_move
                    show menulogo at zoom(1.4)
                    show a nk n oe cm happy at akira_ost
                    $ renpy.pause(0.5, hard=True)
                    show screen osttext4
                    play music evening_glow_h_h

                "High Atmosphere - Medium Sanity":
                    $ renpy.pause(0.5, hard=True)
                    show black at transparent(0.1)
                    show ostbg_yandere at ostbg_move
                    show vignette
                    show menulogo at zoom(1.4)
                    show a nk y se om happy at akira_ost
                    $ renpy.pause(0.5, hard=True)
                    show screen osttext5
                    play music evening_glow_h_m

                "High Atmosphere - Low Sanity":
                    $ renpy.pause(0.5, hard=True)
                    show black
                    show ostbg_yandere at ostbg_move
                    show vignette
                    show menulogo at zoom(1.4)
                    show a b bk y se om happy at akira_ost
                    $ renpy.pause(0.5, hard=True)
                    show screen osttext6
                    play music evening_glow_h_l

                "<<< | Go Back To Music List":
                    $ renpy.pause(0.1, hard=True)
                    jump ost

        "Schoolday":

            $ renpy.pause(0.1, hard=True)

            menu:
                "High Atmosphere - High Sanity":
                    $ renpy.pause(0.5, hard=True)
                    show black at transparent(0.1)
                    show ostbg_normal at ostbg_move
                    show menulogo at zoom(1.4)
                    show a nk n oe cm happy at akira_ost
                    $ renpy.pause(0.5, hard=True)
                    show screen osttext7
                    play music schoolday_h_h

                "High Atmosphere - Medium Sanity":
                    $ renpy.pause(0.5, hard=True)
                    show black at transparent(0.1)
                    show ostbg_yandere at ostbg_move
                    show vignette
                    show menulogo at zoom(1.4)
                    show a nk y se om happy at akira_ost
                    $ renpy.pause(0.5, hard=True)
                    show screen osttext8
                    play music schoolday_h_m

                "High Atmosphere - Low Sanity":
                    $ renpy.pause(0.5, hard=True)
                    show black
                    show ostbg_yandere at ostbg_move
                    show vignette
                    show menulogo at zoom(1.4)
                    show a b bk y se om happy at akira_ost
                    $ renpy.pause(0.5, hard=True)
                    show screen osttext9
                    play music schoolday_h_l

                "Medium Atmosphere - High Sanity":
                    $ renpy.pause(0.5, hard=True)
                    show black at transparent(0.3)
                    show ostbg_normal at ostbg_move
                    show menulogo at zoom(1.4)
                    show a nk n oe cm neutral at akira_ost
                    $ renpy.pause(0.5, hard=True)
                    show screen osttext10
                    play music schoolday_m_h

                "Medium Atmosphere - Medium Sanity":
                    $ renpy.pause(0.5, hard=True)
                    show black at transparent(0.3)
                    show ostbg_yandere at ostbg_move
                    show vignette
                    show menulogo at zoom(1.4)
                    show a nk n se cm neutral at akira_ost
                    $ renpy.pause(0.5, hard=True)
                    show screen osttext11
                    play music schoolday_m_m

                "Medium Atmosphere - Low Sanity":
                    $ renpy.pause(0.5, hard=True)
                    show black
                    show ostbg_yandere at ostbg_move
                    show vignette
                    show menulogo at zoom(1.4)
                    show a b bk y se cm angry_neutral at akira_ost
                    $ renpy.pause(0.5, hard=True)
                    show screen osttext12
                    play music schoolday_m_l

                "Low Atmosphere - High Sanity":
                    $ renpy.pause(0.5, hard=True)
                    show black at transparent(0.5)
                    show ostbg_normal at ostbg_move
                    show menulogo at zoom(1.4)
                    show a nk n oe cm sad at akira_ost
                    $ renpy.pause(0.5, hard=True)
                    show screen osttext13
                    play music schoolday_l_h

                "Low Atmosphere - Medium Sanity":
                    $ renpy.pause(0.5, hard=True)
                    show black at transparent(0.5)
                    show ostbg_yandere at ostbg_move
                    show vignette
                    show menulogo at zoom(1.4)
                    show a nk y se cm angry at akira_ost
                    $ renpy.pause(0.5, hard=True)
                    show screen osttext14
                    play music schoolday_l_m

                "Low Atmosphere - Low Sanity":
                    $ renpy.pause(0.5, hard=True)
                    show black
                    show ostbg_yandere at ostbg_move
                    show vignette
                    show menulogo at zoom(1.4)
                    show a b bk y se om angry at akira_ost
                    $ renpy.pause(0.5, hard=True)
                    show screen osttext15
                    play music schoolday_l_l

                "<<< | Go Back To Music List":
                    $ renpy.pause(0.1, hard=True)
                    jump ost

        "Echoes of Love":

            $ renpy.pause(0.1, hard=True)

            menu:
                "High Atmosphere - High Sanity":
                    $ renpy.pause(0.5, hard=True)
                    show black at transparent(0.1)
                    show ostbg_normal at ostbg_move
                    show menulogo at zoom(1.4)
                    show a nk n oe cm happy at akira_ost
                    $ renpy.pause(0.5, hard=True)
                    show screen osttext16
                    play music echoesoflove_h_h

                "High Atmosphere - Medium Sanity":
                    $ renpy.pause(0.5, hard=True)
                    show black at transparent(0.1)
                    show ostbg_yandere at ostbg_move
                    show vignette
                    show menulogo at zoom(1.4)
                    show a nk y se om happy at akira_ost
                    $ renpy.pause(0.5, hard=True)
                    show screen osttext17
                    play music echoesoflove_h_m

                "High Atmosphere - Low Sanity":
                    $ renpy.pause(0.5, hard=True)
                    show black
                    show ostbg_yandere at ostbg_move
                    show vignette
                    show menulogo at zoom(1.4)
                    show a b bk y se om happy at akira_ost
                    $ renpy.pause(0.5, hard=True)
                    show screen osttext18
                    play music echoesoflove_h_l

                "Low Atmosphere - High Sanity":
                    $ renpy.pause(0.5, hard=True)
                    show black at transparent(0.5)
                    show ostbg_normal at ostbg_move
                    show menulogo at zoom(1.4)
                    show a nk n oe cm sad at akira_ost
                    $ renpy.pause(0.5, hard=True)
                    show screen osttext19
                    play music echoesoflove_l_h

                "Low Atmosphere - Medium Sanity":
                    $ renpy.pause(0.5, hard=True)
                    show black at transparent(0.5)
                    show ostbg_yandere at ostbg_move
                    show vignette
                    show menulogo at zoom(1.4)
                    show a nk y se cm angry at akira_ost
                    $ renpy.pause(0.5, hard=True)
                    show screen osttext20
                    play music echoesoflove_l_m

                "Low Atmosphere - Low Sanity":
                    $ renpy.pause(0.5, hard=True)
                    show black
                    show ostbg_yandere at ostbg_move
                    show vignette
                    show menulogo at zoom(1.4)
                    show a b bk y se om angry at akira_ost
                    $ renpy.pause(0.5, hard=True)
                    show screen osttext21
                    play music echoesoflove_l_l

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
            hide screen osttext1
            hide screen osttext2
            hide screen osttext3
            hide screen osttext4
            hide screen osttext5
            hide screen osttext6
            hide screen osttext7
            hide screen osttext8
            hide screen osttext9
            hide screen osttext10
            hide screen osttext11
            hide screen osttext12
            hide screen osttext13
            hide screen osttext14
            hide screen osttext15
            hide screen osttext16
            hide screen osttext17
            hide screen osttext18
            hide screen osttext19
            hide screen osttext20
            hide screen osttext21

            $ renpy.pause(0.3, hard=True)
            jump ost

        "Go To Main Menu":
            $ renpy.pause(0.3, hard=True)
            jump go_to_main_menu

        "Nevermind":
            jump waiting