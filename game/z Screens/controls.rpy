screen help():

    tag menu

    if main_menu and not persistent.yandere_menu_enabled == "easteregg" and persistent.game_started_once:
        key "e" action Function(trigger_easter_egg)
        key "E" action Function(trigger_easter_egg)

    use game_menu(_("                          CONTROLS"), scroll="viewport"):

        style_prefix "help"

        if not persistent.yandere_menu_enabled == "easteregg":

            vbox:

                spacing 25

                hbox:
                    label _("Enter")
                    text _("Advances dialogue and activates the interface.")

                hbox:
                    label _("Space")
                    text _("Advances dialogue without selecting choices.")

                hbox:
                    label _("Arrow Keys")
                    text _("Navigate the interface.")

                hbox:
                    label _("Ctrl")
                    text _("Skips dialogue while held down.")

                hbox:
                    label _("Tab")
                    text _("Toggles dialogue skipping.")

                hbox:
                    label _("Delete")
                    text _("Deletes the hovered save file.")

                hbox:
                    label "H"
                    text _("Hides the user interface.")

                hbox:
                    label "S"
                    text _("Takes a screenshot.")

                hbox:
                    label _("Left Click")
                    text _("Advances dialogue and activates the interface.")

                hbox:
                    label _("Middle Click")
                    text _("Hides the user interface.")

                if main_menu and persistent.game_started_once:
                    
                    hbox:
                        label _("E")
                        text _(random_text(40))


        if persistent.yandere_menu_enabled == "easteregg":

            vbox:
            
                spacing 25

                hbox:
                    label _("E")
                    text _(random_text(40))

                hbox:
                    label _("E")
                    text _(random_text(40))

                hbox:
                    label _("E")
                    text _(random_text(40))

                hbox:
                    label _("E")
                    text _(random_text(40))

                hbox:
                    label _("E")
                    text _(random_text(40))

                hbox:
                    label _("E")
                    text _(random_text(40))

                hbox:
                    label _("E")
                    text _(random_text(40))

                hbox:
                    label _("E")
                    text _(random_text(40))

                hbox:
                    label _("E")
                    text _(random_text(40))

                hbox:
                    label _("E")
                    text _(random_text(40))

                hbox:
                    label _("E")
                    text _(random_text(40))