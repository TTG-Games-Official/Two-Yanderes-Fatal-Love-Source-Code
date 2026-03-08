label after_load:
    $ persistent.ymenu_enabled_saved = yandere_menu_afterload
    $ persistent.yandere_menu_enabled = persistent.ymenu_enabled_saved 

    if not persistent.skip_hint_shown:
        show screen skip_hint
        $ persistent.skip_hint_shown = True

    $ akira_mc = Character(_("Akira & [persistent.playername]"), who_color="#fff700", ctc="ctc", ctc_position="fixed")
    $ mc = Character(_(persistent.playername), who_color="#29bf00", ctc="ctc", ctc_position="fixed")
    $ player = persistent.playername

    $ unlock_dismiss()