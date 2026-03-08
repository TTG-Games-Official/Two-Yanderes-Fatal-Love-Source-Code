screen quick_menu():

    zorder 100

    if quick_menu:

        add "quickmenu/rightbg.webp" ypos + 15
        add "quickmenu/leftbg.webp" ypos + 15

        if persistent.show_sanity == True and hide_sanity_force == False or show_sanity_important == True and persistent.show_sanity == "dynamic" and hide_sanity_force == False:

            add "quickmenu/sanity_bg.webp"
            add sanity_cardiograph xalign 1.0 yalign 0.108
            add "quickmenu/sanity_icon.webp"

            if persistent.language == "Türkçe":

                if sanity > 79:
                    text "{color=#ff54e2}{size=32}%[sanity]" xpos 0.936 ypos 0.113
                elif sanity > 59:
                    text "{color=#ff9eea}{size=32}%[sanity]" xpos 0.936 ypos 0.113
                elif sanity > 40:
                    text "{color=#ff7f7f}{size=32}%[sanity]" xpos 0.936 ypos 0.113
                elif sanity > 20:
                    text "{color=#ff0000}{size=32}%[sanity]" xpos 0.936 ypos 0.113
                else:
                    text "{color=#a80000}{size=32}%[sanity]" at sanity_shake

            else:
                
                if sanity > 79:
                    text "{color=#ff54e2}{size=32}[sanity]%" xpos 0.936 ypos 0.113
                elif sanity > 59:
                    text "{color=#ff9eea}{size=32}[sanity]%" xpos 0.936 ypos 0.113
                elif sanity > 40:
                    text "{color=#ff7f7f}{size=32}[sanity]%" xpos 0.936 ypos 0.113
                elif sanity > 20:
                    text "{color=#ff0000}{size=32}[sanity]%" xpos 0.936 ypos 0.113
                else:
                    text "{color=#a80000}{size=32}[sanity]%" at sanity_shake

        if show_police_suspect:

            if persistent.language == "Türkçe":
                add "images/Destiny/Türkçe/Sus Level.webp"

                if police_investigation_no == 1:

                    if suspicion == 100:
                        text "{color=#ff0000}{size=80}%[suspicion]" xpos 0.018 ypos 0.44
                    elif suspicion > 29 and suspicion < 100:
                        text "{color=#ff0000}{size=80}%[suspicion]" xpos 0.03 ypos 0.44
                    elif suspicion < 30 and suspicion > 9:
                        text "{color=#00aeff}{size=80}%[suspicion]" xpos 0.03 ypos 0.44
                    elif suspicion < 10:
                        text "{color=#00aeff}{size=80}%0[suspicion]" xpos 0.03 ypos 0.44

                elif police_investigation_no == 2:

                    if suspicion == 100:
                        text "{color=#ff0000}{size=80}%[suspicion]" xpos 0.018 ypos 0.44
                    elif suspicion > 49 and suspicion < 100:
                        text "{color=#ff0000}{size=80}%[suspicion]" xpos 0.03 ypos 0.44
                    elif suspicion < 50 and suspicion > 9:
                        text "{color=#00aeff}{size=80}%[suspicion]" xpos 0.03 ypos 0.44
                    elif suspicion < 10:
                        text "{color=#00aeff}{size=80}%0[suspicion]" xpos 0.03 ypos 0.44

            else:
                add "images/Destiny/English/Sus Level.webp"

                if police_investigation_no == 1:

                    if suspicion == 100:
                        text "{color=#ff0000}{size=80}[suspicion]%" xpos 0.018 ypos 0.44
                    elif suspicion > 29 and suspicion < 100:
                        text "{color=#ff0000}{size=80}[suspicion]%" xpos 0.03 ypos 0.44
                    elif suspicion < 30 and suspicion > 9:
                        text "{color=#00aeff}{size=80}[suspicion]%" xpos 0.03 ypos 0.44
                    elif suspicion < 10:
                        text "{color=#00aeff}{size=80}0[suspicion]%" xpos 0.03 ypos 0.44

                elif police_investigation_no == 2:

                    if suspicion == 100:
                        text "{color=#ff0000}{size=80}[suspicion]%" xpos 0.018 ypos 0.44
                    elif suspicion > 49 and suspicion < 100:
                        text "{color=#ff0000}{size=80}[suspicion]%" xpos 0.03 ypos 0.44
                    elif suspicion < 50 and suspicion > 9:
                        text "{color=#00aeff}{size=80}[suspicion]%" xpos 0.03 ypos 0.44
                    elif suspicion < 10:
                        text "{color=#00aeff}{size=80}0[suspicion]%" xpos 0.03 ypos 0.44


        hbox:

            style_prefix "quick"
            
            spacing 15
            yalign 0.0593
            xpos + 20

            if settings_enabled and not style.say_dialogue == style.scarytext:
                imagebutton idle "quickmenu/settings_idle.webp" hover "quickmenu/settings_hover.webp" action [Function(play_click_sound), ShowMenu('stats')]
            else:
                imagebutton idle "quickmenu/settings_disabled.webp"

            if history_enabled and not style.say_dialogue == style.scarytext:
                imagebutton idle "quickmenu/history_idle.webp" hover "quickmenu/history_hover.webp" action [Function(play_click_sound), ShowMenu('history')]
            else:
                imagebutton idle "quickmenu/history_disabled.webp"

        hbox:
        
            spacing 15
            yalign 0.0593
            xalign 0.99

            imagebutton idle "quickmenu/skip_idle.webp" action [Function(play_click_sound), Skip()] alternate Skip(fast=True) selected_idle "quickmenu/skip_active.webp" hover "quickmenu/skip_hover.webp" selected_hover "quickmenu/skip_active.webp" insensitive "quickmenu/skip_disabled.webp"
            
            if auto_enabled:
                imagebutton idle "quickmenu/auto_idle.webp" action [Function(play_click_sound), Preference("auto-forward", "toggle")] selected_idle "quickmenu/auto_active.webp" hover "quickmenu/auto_hover.webp" selected_hover "quickmenu/auto_active.webp"
            else:
                imagebutton idle "quickmenu/auto_disabled.webp"

            if hide_enabled and not config.keymap['dismiss'] == []:
                imagebutton idle "quickmenu/hide_idle.webp" action [Function(play_click_sound), HideInterface()] hover "quickmenu/hide_hover.webp"
            else:
                imagebutton idle "quickmenu/hide_disabled.webp"