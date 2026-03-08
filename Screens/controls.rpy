screen help():

    tag menu

    use game_menu(_("                          CONTROLS"), scroll="viewport"):

        style_prefix "help"

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