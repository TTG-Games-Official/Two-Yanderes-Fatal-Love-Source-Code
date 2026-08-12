screen main_menu():

    tag menu

    if persistent.yandere_menu_enabled == "easteregg":
        
        add "mainmenu/Black.webp"
        add "a nk y se om happy" at akira_menu_easteregg()

    elif persistent.yandere_menu_enabled == True:

        add "front_school_scary"
        add "a k y se om happy" at akira_menu()

    else:

        add "front_school"
        add "a nk n oe cm happy" at akira_menu()
    
    add "mainmenu/menugamelogo.webp"

    if not persistent.new_game_clicked:
        
        add "mainmenu/navigationbg.webp"

        if persistent.yandere_menu_enabled == "easteregg": 

            textbutton _("No Privacy") action OpenURL("https://sites.google.com/view/privacy-policy-tyfl/home") xalign 0.98 yalign 0.92
            textbutton _("Terms of Relationship") action OpenURL("https://sites.google.com/view/terms-of-use-tyfl/home") xalign 0.98 yalign 0.98

            text "{color=#ff54e2}{size=+10}v9.9.9" xalign 0.02 yalign 0.98

        else:

            if persistent.game_finished_once:
                textbutton _("Cheats") action [Function(play_click_sound), Show("cheats")] xalign 0.98 yalign 0.86
            
            textbutton _("Privacy Policy") action OpenURL("https://sites.google.com/view/privacy-policy-tyfl/home") xalign 0.98 yalign 0.92
            textbutton _("Terms of Use") action OpenURL("https://sites.google.com/view/terms-of-use-tyfl/home") xalign 0.98 yalign 0.98

            text "{color=#ff54e2}{size=+10}v[config.version]" xalign 0.02 yalign 0.98

        vbox:

            xalign 1.0
            yalign 0.0

            imagebutton idle localized_asset_path("images/Source Code/{folder}/Source Code Idle {code}.webp") hover localized_asset_path("images/Source Code/{folder}/Source Code Hover {code}.webp") action [Function(play_click_sound), Show("source_code_spoiler_warning")]

            imagebutton idle "images/YouTube Idle.webp" hover "images/YouTube Hover.webp" action [Function(play_click_sound), OpenURL("https://www.youtube.com/@TTG_Games_Official/")] xalign 0.5
            imagebutton idle "images/Discord Idle.webp" hover "images/Discord Hover.webp" action [Function(play_click_sound), OpenURL("https://discord.gg/pT9e9exeES")] xalign 0.5
    
    frame:
        style "main_menu_frame"

    use navigation
    
    if persistent.yandere_menu_enabled == True:
        add "images/Vignette.webp" at transparent(0.3)
