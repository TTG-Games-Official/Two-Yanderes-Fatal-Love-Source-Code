screen main_menu():

    tag menu

    if persistent.yandere_menu_enabled == True:
        add "backgrounds/Uncle Mugen/Front School Scary.webp"
        add Animation(im.Composite((1797, 3992), (0, 0), "characters/akira/body.webp", (0, 0), "characters/akira/knife.webp", (0, 0), "characters/akira/small_eyes.webp", (0, 0), "characters/akira/forehead_dark_open_eyes.webp", (0, 0), "characters/akira/expressions/open_mouth/happy.webp"), 3.0, im.Composite((1797, 3992), (0, 0), "characters/akira/body.webp", (0, 0), "characters/akira/knife.webp", (0, 0), "characters/akira/eyelashes_sad.webp", (0, 0), "characters/akira/forehead_dark_closed_eyes.webp", (0, 0), "characters/akira/expressions/open_mouth/happy.webp"), 0.1) at akira_menu()

    else:
        add "backgrounds/Uncle Mugen/Front School.webp"
        add Animation(im.Composite((1797, 3992), (0, 0), "characters/akira/body.webp", (0, 0), "characters/akira/normal_eyes.webp", (0, 0), "characters/akira/expressions/closed_mouth/happy.webp"), 3.0, im.Composite((1797, 3992), (0, 0), "characters/akira/body.webp", (0, 0), "characters/akira/eyelashes_sad.webp", (0, 0), "characters/akira/expressions/closed_mouth/happy.webp"), 0.1) at akira_menu()

    add "mainmenu/menugamelogo.webp"

    if not persistent.new_game_clicked:
        
        add "mainmenu/navigationbg.webp"

        text "{color=#ff54e2}{size=+10}v[config.version]" xalign 0.98 yalign 0.98

        if persistent.language == "Türkçe":
            imagebutton idle "images/Source Code Idle TR.webp" hover "images/Source Code Hover TR.webp" action [Function(play_click_sound), Show("source_code_spoiler_warning")] xalign 1.0 yalign 0.0
        else:
            imagebutton idle "images/Source Code Idle EN.webp" hover "images/Source Code Hover EN.webp" action [Function(play_click_sound), Show("source_code_spoiler_warning")] xalign 1.0 yalign 0.0

    frame:
        style "main_menu_frame"

    use navigation
    
    if persistent.yandere_menu_enabled == True:
        add "images/Vignette.webp" at transparent(0.3)