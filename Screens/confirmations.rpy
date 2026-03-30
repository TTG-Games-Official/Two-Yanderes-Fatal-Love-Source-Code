screen confirm(message, yes_action, no_action):

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("YES") action [Function(play_click_sound), yes_action]
                textbutton _("NO") action [Function(play_click_sound), no_action]

    key "K_ESCAPE" action no_action
    key "K_KP_ENTER" action [Function(play_click_sound), yes_action]
    key "K_RETURN" action [Function(play_click_sound), yes_action]


screen delete_saves():

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _("Are you sure you want to delete all save files?\nThis action cannot be undone."):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("YES") action [Function(play_click_sound), Function(delete_all_saves), Hide("delete_saves")]
                textbutton _("NO") action [Function(play_click_sound), Hide("delete_saves")]
                
    key "K_KP_ENTER" action [Function(play_click_sound), Function(delete_all_saves), Hide("delete_saves")]
    key "K_RETURN" action [Function(play_click_sound), Function(delete_all_saves), Hide("delete_saves")]
    key "K_ESCAPE" action Hide("delete_saves")


screen music_player():

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _("You have unlocked the Music Player!\nNow you can listen to game's original soundtrack in your game."):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("OK") action [Function(play_click_sound), Hide("music_player")]
                
    key "K_KP_ENTER" action [Function(play_click_sound), Hide("music_player")]
    key "K_RETURN" action [Function(play_click_sound), Hide("music_player")]
    key "K_ESCAPE" action Hide("music_player")


screen skip_hint():

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _("Tip: You can use the skip button on the top right\nto skip the text you already read."):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("OK") action [Function(play_click_sound), Hide("skip_hint")]
                
    key "K_KP_ENTER" action [Function(play_click_sound), Hide("skip_hint")]
    key "K_RETURN" action [Function(play_click_sound), Hide("skip_hint")]
    key "K_ESCAPE" action Hide("skip_hint")


screen main_menu_confirm(message):
    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("YES") action [Function(play_click_sound), Hide("main_menu_confirm"), Jump("go_to_main_menu")]
                textbutton _("NO") action [Function(play_click_sound), Hide("main_menu_confirm")]

    key "K_KP_ENTER" action [Function(play_click_sound), Hide("main_menu_confirm"), Jump("go_to_main_menu")]
    key "K_RETURN" action [Function(play_click_sound), Hide("main_menu_confirm"), Jump("go_to_main_menu")]
    key "K_ESCAPE" action Hide("main_menu_confirm")


screen name_input(message, ok_action):
    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            
            xalign 0.5
            yalign 0.5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            input default "" value VariableInputValue("persistent.playername") length 12 allow "ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZabcçdefgğhıijklmnoöpqrsştuüvwxyz" xalign 0.5

            hbox:
                style "confirm_prompt"
                xalign 0.5
                spacing 150

                if persistent.playername == "":
                    textbutton _("OK")
                    key "K_KP_ENTER" action NullAction()
                    key "K_RETURN" action NullAction()
                else:
                    textbutton _("OK") action [Function(play_click_sound), Show("change_gender"), Hide("name_input"), ok_action, SetVariable("persistent.playernameentered", True)]
                    key "K_KP_ENTER" action [Function(play_click_sound), Show("change_gender"), Hide("name_input"), ok_action, SetVariable("persistent.playernameentered", True)]
                    key "K_RETURN" action [Function(play_click_sound), Show("change_gender"), Hide("name_input"), ok_action, SetVariable("persistent.playernameentered", True)]

                textbutton _("CANCEL") action [Function(play_click_sound), Hide("name_input"), Function(cancel_name_input)]
                key "K_ESCAPE" action [Hide("name_input"), Function(cancel_name_input)]

            if persistent.playername.lower() in forbidden_names:
                text _("{color=#ff6a00}{size=-10}This name is already used by an in-game character.\nChoosing it may cause confusion during the story.")


screen change_name():
    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            
            xalign 0.5
            yalign 0.5
            spacing 45

            label _("Please Enter Your Name"):
                style "confirm_prompt"
                xalign 0.5

            input value VariableInputValue("persistent.playername") length 12 allow "ABCÇDEFGĞHIİJKLMNOÖPQRSŞTUÜVWXYZabcçdefgğhıijklmnoöpqrsştuüvwxyz" xalign 0.5

            vbox:
                style "confirm_prompt"
                xalign 0.5

                if persistent.playername == "":
                    textbutton _("OK")
                    key "K_KP_ENTER" action NullAction()
                    key "K_RETURN" action NullAction()
                else:
                    textbutton _("OK") action [Function(play_click_sound), Hide("change_name"), Show("change_gender"), SetVariable("persistent.playernameentered", True)]
                    key "K_KP_ENTER" action [Function(play_click_sound), Hide("change_name"), Show("change_gender"), SetVariable("persistent.playernameentered", True)]
                    key "K_RETURN" action [Function(play_click_sound), Hide("change_name"), Show("change_gender"), SetVariable("persistent.playernameentered", True)]

            if persistent.playername.lower() in forbidden_names:
                text _("{color=#ff6a00}{color=#ff6a00}This name is already used by an in-game character.\nChoosing it may cause confusion during the story.")


screen change_gender():
    modal True
    zorder 200
    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            
            xalign 0.5
            yalign 0.5
            spacing 45

            label _("Please choose your gender.\nThis will only change the pronouns in the story."):
                    style "confirm_prompt"
                    xalign 0.5

            hbox:
                style "confirm_prompt"
                xalign 0.5
                spacing 200

                textbutton _("MALE") action [Function(play_click_sound), Hide("change_gender"), Function(gender_male)]
                textbutton _("FEMALE") action [Function(play_click_sound), Hide("change_gender"), Function(gender_female)]


screen change_name_error():

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _("You can't change your name during the story.\nTo change your name, please go to main menu first."):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("OK") action [Function(play_click_sound), Hide("change_name_error")]
                
    key "K_KP_ENTER" action [Function(play_click_sound), Hide("change_name_error")]
    key "K_RETURN" action [Function(play_click_sound), Hide("change_name_error")]
    key "K_ESCAPE" action Hide("change_name_error")


screen ch12_warning():

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _("Starting this chapter will prevent you from going back to main menu for a while.\nAre you sure you want to proceed?"):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 200

                textbutton _("YES") action [Hide("select_chapter"), Hide("ch12_warning"), Function(play_click_sound), Function(start_game_with_fade), SetField(persistent, "new_game_clicked", False), SetField(persistent, "selected_chapter", 12)] xalign 0.97 yalign 0.97
                textbutton _("NO") action [Function(play_click_sound), Hide("ch12_warning")]
                
    key "K_RETURN" action [Function(play_click_sound), Hide("ch12_warning")]
    key "K_ESCAPE" action Hide("ch12_warning")

screen source_code_spoiler_warning():

    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _("The source code contains massive spoilers regarding the game's story and systems.\nDo you still want to proceed to the GitHub repository?"):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 200

                textbutton _("YES") action [Function(play_click_sound), Hide("source_code_spoiler_warning"), OpenURL("https://github.com/TTG-Games-Official/Two-Yanderes-Fatal-Love-Source-Code")]
                textbutton _("NO") action [Function(play_click_sound), Hide("source_code_spoiler_warning")]
                
    key "K_RETURN" action Hide("source_code_spoiler_warning")
    key "K_ESCAPE" action Hide("source_code_spoiler_warning")