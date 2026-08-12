screen navigation():

    vbox:
    
        style_prefix "mainmenu"
        yalign 0.72

        if not persistent.new_game_clicked:

            if persistent.language == "Türkçe":

                if main_menu:

                    if persistent.yandere_menu_enabled == "easteregg":

                        if persistent.music_player_enabled:

                            spacing -20
                            xalign 0.09

                        else:

                            spacing -12
                            xalign 0.09

                    else:

                        if persistent.music_player_enabled:

                            spacing -20
                            xalign 0.078

                        else:

                            spacing -12
                            xalign 0.078
                
                else:

                    spacing -20
                    xalign 0.09

            elif persistent.language == "Español":

                if main_menu:

                    if persistent.yandere_menu_enabled == "easteregg":

                        if persistent.music_player_enabled:

                            spacing -20
                            xalign 0.054

                        else:

                            spacing -12
                            xalign 0.055

                    else:

                        if persistent.music_player_enabled:

                            spacing -20
                            xalign 0.084

                        else:

                            spacing -12
                            xalign 0.108

                else:

                    spacing -20
                    xalign 0.1

            elif persistent.language == "Russian":

                if main_menu:

                    if persistent.yandere_menu_enabled == "easteregg":

                        if persistent.music_player_enabled:

                            spacing -20
                            xalign 0.06

                        else:

                            spacing -12
                            xalign 0.06

                    else:

                        if persistent.music_player_enabled:

                            spacing -20
                            xalign 0.098

                        else:

                            spacing -12
                            xalign 0.097

                else:

                    spacing -20
                    xalign 0.097

            else:

                if main_menu:

                    if persistent.yandere_menu_enabled == "easteregg":

                        if persistent.music_player_enabled:

                            spacing -20
                            xalign 0.092

                        else:

                            spacing -12
                            xalign 0.091

                    else:

                        if persistent.music_player_enabled:

                            spacing -20
                            xalign 0.092

                        else:

                            spacing -12
                            xalign 0.108

                else:

                    spacing -20
                    xalign 0.108

                
            if main_menu:

                if not persistent.yandere_menu_enabled == "easteregg":
                    textbutton _("CHAPTERS") action [Function(play_click_sound), Return(), If(persistent.playernameentered, true=[Show("select_chapter"), SetField(persistent, "new_game_clicked", True)], false=Show(screen="name_input", message="Please Enter Your Name", ok_action=[Show("select_chapter"), SetField(persistent, "new_game_clicked", True)]))]
                else:
                    textbutton _("LOVES") action [Function(play_click_sound), Return(), If(persistent.playernameentered, true=[Show("select_chapter"), SetField(persistent, "new_game_clicked", True)], false=Show(screen="name_input", message="Please Enter Your Name", ok_action=[Show("select_chapter"), SetField(persistent, "new_game_clicked", True)]))]
            
            else:

                textbutton _("STATS") action [Function(play_click_sound), Function(select_button, "Stats"), ShowMenu("stats")]
                textbutton _("HISTORY") action [Function(play_click_sound), Function(select_button, "History"), ShowMenu("history")]
                textbutton _("SAVE GAME") action [Function(play_click_sound), Function(select_button, "Save Game"), ShowMenu("save")]


            if not persistent.yandere_menu_enabled == "easteregg":

                textbutton _("LOAD SAVE") action [Function(play_click_sound), If(persistent.playernameentered, true=ShowMenu("load"), false=Show(screen="name_input", message=_("To access the Load Save screen,\nplease enter your name."), ok_action=[Hide("name_input"), ShowMenu("load")]))]
                textbutton _("SETTINGS") action [Function(play_click_sound), Function(select_button, "Settings"), ShowMenu("preferences")]
            
            else:

                textbutton _("LOAD LOVE") action [Function(play_click_sound), Function(select_button, "Load Game"), ShowMenu("load")]
                textbutton _("SET LOVE") action [Function(play_click_sound), Function(select_button, "Settings"), ShowMenu("preferences")]


            if main_menu:

                if not persistent.yandere_menu_enabled == "easteregg":
                    textbutton _("EXTRAS") action [Function(play_click_sound), Function(select_button, "Extras"), ShowMenu("extras")]
                    textbutton _("CREDITS") action [Function(play_click_sound), Function(select_button, "Credits"), ShowMenu("credits")]
                else:
                    textbutton _("EXTRA LOVE") action [Function(play_click_sound), Function(select_button, "Extras"), ShowMenu("extras")]
                    textbutton _("CREDIT LOVE") action [Function(play_click_sound), Function(select_button, "Credits"), ShowMenu("credits")]
            
            else:

                textbutton _("MAIN MENU") action [Function(play_click_sound), Show("main_menu_confirm", message=_("Are you sure you want to return to the main menu?\nYou will lose your unsaved progress."))]


            if persistent.music_player_enabled and main_menu:
                
                if not persistent.yandere_menu_enabled == "easteregg":
                    textbutton _("MUSIC PLAYER") action [Function(play_click_sound), Function(ost_screen_with_fade)]
                else:
                    textbutton _("LOVE MUSIC") action [Function(play_click_sound), Function(ost_screen_with_fade)]
            
            
            if not persistent.yandere_menu_enabled == "easteregg":

                textbutton _("CONTROLS") action [Function(play_click_sound), Function(select_button, "Controls"), ShowMenu("help")]
                textbutton _("EXIT GAME") action [Function(play_click_sound), Quit(confirm=True)]
            
            else:

                textbutton _("CONTROL LOVE") action [Function(play_click_sound), Function(select_button, "Controls"), ShowMenu("help")]
                textbutton _("EXIT LOVE") action [Function(play_click_sound), Show("no_exit")]