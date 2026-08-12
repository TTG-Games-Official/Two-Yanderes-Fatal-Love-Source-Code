init python:

    def settings_tooltip(key):

        mode = "easteregg" if persistent.yandere_menu_enabled == "easteregg" else "normal"

        if persistent.language == "Türkçe":
            language = "Türkçe"
        elif persistent.language == "Español":
            language = "Español"
        elif persistent.language == "Russian":
            language = "Russian"
        else:
            language = "English"

        table = settings_tooltips.get(mode, {})

        if key not in table:
            table = settings_tooltips.get("normal", {})

        tooltip = table.get(key, {})
        return tooltip.get(language, tooltip.get("English", ""))

    settings_tooltip_groups = {

        "display": (
            ("Windowed", "Display Window"),
            ("Fullscreen", "Display Fullscreen"),
        ),

        "skip": (
            ("Unseen Text", "Skip Unseen Text"),
            ("After Choices", "Skip After Choices"),
            ("Intro", "Skip Intro"),
        ),

        "sanity": (
            (None, "Sanity Info"),
            ("Always", "Showing Sanity Always"),
            ("Dynamic", "Showing Sanity Dynamic"),
            ("Hidden", "Showing Sanity Hidden"),
        ),

        "low_fps": (
            (None, "Low FPS Optimize Info"),
            ("Enable", "Low FPS Enable"),
            ("Disable", "Low FPS Disable"),
        ),

        "sky": (
            (None, "Sky Color Info"),
            ("Default", "Sky Color Default"),
            ("Realistic", "Sky Color Realistic"),
        ),

        "text_speed": ((None, "Text Speed"),),
        "auto_forward": ((None, "Auto-Forward Delay"),),
        "music": ((None, "Music Volume"),),
        "sfx": ((None, "SFX Volume"),),
        "voice": ((None, "Voice Volume"),),
        "language": ((None, "Non-Native Language Warning"),),
    }

    easteregg_settings_tooltip_groups = {

        "display": (
            ("Only a Glimpse", "Display Window"),
            ("All of Me", "Display Fullscreen"),
        ),

        "skip": (
            ("Don't Skip!", "Skip Unseen Text"),
            ("No Skipping!", "Skip After Choices"),
            ("No Way!", "Skip Intro"),
        ),
    }

    def settings_panel_tooltip(group):

        parts = []

        entries = settings_tooltip_groups.get(group, ())

        if persistent.yandere_menu_enabled == "easteregg":
            entries = easteregg_settings_tooltip_groups.get(group, entries)

        for title, key in entries:

            body = settings_tooltip(key)

            if title:
                title = renpy.translate_string(title)
                parts.append("{color=#ff00ff}%s:{/color} %s" % (title, body))
            else:
                parts.append(body)

        return "\n\n".join(parts)


screen preferences():

    tag menu

    default settings_category = "general"

    use game_menu(_("                          SETTINGS"), scroll="viewport"):

        vbox:

            xpos + 150

            hbox:

                if persistent.language == "Russian":
                    spacing 50
                else:
                    spacing 20

                textbutton _("General Settings") action [Function(play_click_sound), SetScreenVariable("settings_category", "general")]
                textbutton _("Text Settings") action [Function(play_click_sound), SetScreenVariable("settings_category", "text")]
                textbutton _("Audio Settings") action [Function(play_click_sound), SetScreenVariable("settings_category", "audio")]
                textbutton _("Language Settings") action [Function(play_click_sound), SetScreenVariable("settings_category", "language")]

            if settings_category == "general":
                use general_settings
            elif settings_category == "text":
                use text_settings
            elif settings_category == "audio":
                use audio_settings
            elif settings_category == "language":
                use language_settings


screen general_settings():

    if not persistent.yandere_menu_enabled == "easteregg":

        vbox:

            ypos + 50
            spacing 50

            box_wrap True

            hbox:

                spacing 20

                vbox:

                    style_prefix "radio"

                    hbox:

                        label _("DISPLAY MODE")
                        imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("display"))] xpos 10 ypos 15

                    textbutton _("Windowed") action [Function(play_click_sound), Preference("display", "window"), SetField(persistent, "display", 1)]
                    textbutton _("Fullscreen") action [Function(play_click_sound), Preference("display", "fullscreen"), SetField(persistent, "display", 2)]

                vbox:

                    style_prefix "check"

                    hbox:

                        label _("SKIP OPTIONS")
                        imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("skip"))] xpos 10 ypos 15

                    textbutton _("Unseen Text") action [Function(play_click_sound), Preference("skip", "toggle")]
                    textbutton _("After Choices") action [Function(play_click_sound), Preference("after choices", "toggle")]
                    textbutton _("Intro") action [Function(play_click_sound), ToggleField(persistent, "intro", true_value=False, false_value=True)]

                vbox:
                    style_prefix "radio"

                    vbox:

                        hbox:

                            label _("SHOW SANITY")

                            imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("sanity"))] xpos 10 ypos 15 

                        textbutton _("Always") action [Function(play_click_sound), SetField(persistent, "show_sanity", True)]
                        textbutton _("Dynamic") action [Function(play_click_sound), SetField(persistent, "show_sanity", "dynamic")]
                        textbutton _("Hidden") action [Function(play_click_sound), SetField(persistent, "show_sanity", False)]

            hbox:

                spacing 20

                vbox:

                    style_prefix "radio"

                    hbox:

                        label _("LOW FPS OPTIMIZATION")

                        imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("low_fps"))] ypos + 55 xpos + 10

                    textbutton _("Enable") action [Function(play_click_sound), SetField(persistent, "low_fps_optimization", True)]
                    textbutton _("Disable") action [Function(play_click_sound), SetField(persistent, "low_fps_optimization", False)]

                vbox:

                    style_prefix "radio"

                    hbox:

                        label _("SCHOOL SKY COLOR")

                        imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("sky"))] ypos + 15 xpos + 10

                    textbutton _("Default") action [Function(play_click_sound), SetField(persistent, "atm_sky_color", "default")]
                    textbutton _("Realistic") action [Function(play_click_sound), SetField(persistent, "atm_sky_color", "realistic")]

                vbox:

                    ypos + 15

                    label _("CHANGE YOUR NAME")

                    if persistent.playername == "":
                        text _("{color=#ffbf00}{size=-10}Current Name: N/A")
                    else:
                        text _("{color=#ffbf00}{size=-10}Current Name: [persistent.playername]")

                    if persistent.gender == "boy":
                        text _("{color=#ffbf00}{size=-10}Current Gender: Male")
                    elif persistent.gender == "girl":
                        text _("{color=#ffbf00}{size=-10}Current Gender: Female")
                    else:
                        text _("{color=#ffbf00}{size=-10}Current Gender: N/A")


                    if main_menu:
                        textbutton _("Change") action [Function(play_click_sound), Show("change_name")]
                    else:
                        textbutton _("Change") action [Function(play_click_sound), Show("change_name_error")]

            null height (4 * gui.pref_spacing)


    if persistent.yandere_menu_enabled == "easteregg":

        vbox:

            spacing 50
            ypos + 50

            box_wrap True

            hbox:

                spacing 20

                vbox:

                    style_prefix "radio"

                    hbox:

                        label _("DISPLAY MODE")
                        imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("display"))] xpos 10 ypos 15

                    textbutton _("Only a Glimpse") action [Function(play_click_sound), Preference("display", "window"), SetField(persistent, "display", 1)]
                    textbutton _("All of Me") action [Function(play_click_sound), Preference("display", "fullscreen"), SetField(persistent, "display", 2)]

                vbox:

                    style_prefix "check"

                    hbox:

                        label _("SKIP OPTIONS")
                        imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("skip"))] xpos 10 ypos 15

                    textbutton _("Don't Skip!") action [Function(play_click_sound), Preference("skip", "toggle")]
                    textbutton _("No Skipping!") action [Function(play_click_sound), Preference("after choices", "toggle")]
                    textbutton _("No Way!") action [Function(play_click_sound), ToggleField(persistent, "intro", true_value=False, false_value=True)]

                vbox:

                    style_prefix "radio"

                    vbox:

                        hbox:

                            label _("SHOW SANITY")

                            imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("sanity"))] ypos + 15 xpos + 10

                        textbutton _("Always") action [Function(play_click_sound), SetField(persistent, "show_sanity", True)]
                        textbutton _("Dynamic") action [Function(play_click_sound), SetField(persistent, "show_sanity", "dynamic")]
                        textbutton _("Hidden") action [Function(play_click_sound), SetField(persistent, "show_sanity", False)]


            hbox:
            
                style_prefix "radio"
                spacing 20

                vbox:

                    hbox:

                        label _("LOW FPS OPTIMIZATION")

                        imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("low_fps"))] ypos + 55 xpos + 10

                    textbutton _("Enable") action [Function(play_click_sound), SetField(persistent, "low_fps_optimization", True)]
                    textbutton _("Disable") action [Function(play_click_sound), SetField(persistent, "low_fps_optimization", False)]

                vbox:

                    style_prefix "radio"

                    hbox:

                        label _("SCHOOL SKY COLOR")

                        imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("sky"))] ypos + 15 xpos + 10

                    textbutton _("Default") action [Function(play_click_sound), SetField(persistent, "atm_sky_color", "default")]
                    textbutton _("Realistic") action [Function(play_click_sound), SetField(persistent, "atm_sky_color", "realistic")]

                vbox:

                    label _("CHANGE YOUR NAME")

                    if persistent.playername == "":
                        text _("{color=#ffbf00}{size=-10}Current Name: N/A")
                    else:
                        text _("{color=#ffbf00}{size=-10}Current Name: [persistent.playername]")

                    if persistent.gender == "boy":
                        text _("{color=#ffbf00}{size=-10}Current Gender: Male")
                    elif persistent.gender == "girl":
                        text _("{color=#ffbf00}{size=-10}Current Gender: Female")
                    else:
                        text _("{color=#ffbf00}{size=-10}Current Gender: N/A")

                    if main_menu:
                        textbutton _("Change") action [Function(play_click_sound), Show("change_name")]
                    else:
                        textbutton _("Change") action [Function(play_click_sound), Show("change_name_error")]

            null height (4 * gui.pref_spacing)

screen text_settings():

    if not persistent.yandere_menu_enabled == "easteregg":

        vbox:

            ypos + 50
            xpos + 20

            hbox:

                label _("Text Speed")
                imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("text_speed"))] xpos 10 ypos -3

            hbox:

                bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, offset=20) style "custom_bar"

                text "[round(preferences.text_cps)]" xpos + 10 ypos - 7

            hbox:

                label _("Auto-Forward Delay")
                imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("auto_forward"))] xpos 10 ypos -3

            hbox:

                bar value Preference("auto-forward time", range=20) style "custom_bar"

                text "[round(preferences.afm_time)]" xpos + 10 ypos - 7

        null height (4 * gui.pref_spacing)


    if persistent.yandere_menu_enabled == "easteregg":

        vbox:

            ypos + 50
            xpos + 20

            hbox:

                label _("How Fast You Read, My Love?")
                imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("text_speed"))] xpos 10 ypos -3

            hbox:

                bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, offset=20) style "custom_bar"

                text "[round(preferences.text_cps)]" xpos + 10 ypos - 7

            hbox:

                label _("Let Me Decide When You Move On")
                imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("auto_forward"))] xpos 10 ypos -3

            hbox:

                bar value Preference("auto-forward time", range=20) style "custom_bar"

                text "[round(preferences.afm_time)]" xpos + 10 ypos - 7

        null height (4 * gui.pref_spacing)

screen audio_settings():

    if not persistent.yandere_menu_enabled == "easteregg":

        vbox:

            ypos + 50
            xpos + 20

            if config.has_music:

                hbox:

                    label _("Music Volume")
                    imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("music"))] xpos 10 ypos -3

                hbox:

                    bar value audio_volume_bar_value("music", "music_volume") style "custom_bar"

                    if persistent.language == "Türkçe":
                        text "%[round(persistent.music_volume * 100)]" xpos + 10 ypos - 7
                    else:
                        text "[round(persistent.music_volume * 100)]%" xpos + 10 ypos - 7

            if config.has_sound:

                hbox:

                    label _("Sound Volume")
                    imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("sfx"))] xpos 10 ypos -3

                hbox:

                    bar value audio_volume_bar_value("sfx", "sfx_volume") style "custom_bar"

                    if persistent.language == "Türkçe":
                        text "%[round(persistent.sfx_volume * 100)]" xpos + 10 ypos - 7
                    else:
                        text "[round(persistent.sfx_volume * 100)]%" xpos + 10 ypos - 7

            if config.has_voice:

                hbox:

                    label _("Voice Volume")
                    imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("voice"))] xpos 10 ypos -3

                hbox:

                    bar value audio_volume_bar_value("voice", "voice_volume") style "custom_bar"

                    if persistent.language == "Türkçe":
                        text "%[round(persistent.voice_volume * 100)]" xpos + 10 ypos - 7
                    else:
                        text "[round(persistent.voice_volume * 100)]%" xpos + 10 ypos - 7

            if config.has_music or config.has_sound or config.has_voice:

                null height gui.pref_spacing

            hbox:

                textbutton _("Mute All"):

                    style "mute_all_button"
                    action [Function(play_click_sound), Preference("all mute", "toggle")]

                null height (4 * gui.pref_spacing)


    if persistent.yandere_menu_enabled == "easteregg":

        vbox:

            ypos + 50
            xpos + 20

            if config.has_music:

                hbox:

                    label _("Music Volume")
                    imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("music"))] xpos 10 ypos -3

                hbox:

                    bar value audio_volume_bar_value("music", "music_volume") style "custom_bar"

                    if persistent.language == "Türkçe":
                        text "%[round(persistent.music_volume * 100)]" xpos + 10 ypos - 7
                    else:
                        text "[round(persistent.music_volume * 100)]%" xpos + 10 ypos - 7

            if config.has_sound:

                hbox:

                    label _("Sound Volume")
                    imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("sfx"))] xpos 10 ypos -3

                hbox:

                    bar value audio_volume_bar_value("sfx", "sfx_volume") style "custom_bar"

                    if persistent.language == "Türkçe":
                        text "%[round(persistent.sfx_volume * 100)]" xpos + 10 ypos - 7
                    else:
                        text "[round(persistent.sfx_volume * 100)]%" xpos + 10 ypos - 7

            if config.has_voice:

                hbox:

                    label _("Voice Volume")
                    imagebutton idle "gui/overlay/Question Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("voice"))] xpos 10 ypos -3

                hbox:

                    bar value audio_volume_bar_value("voice", "voice_volume") style "custom_bar"

                    if persistent.language == "Türkçe":
                        text "%[round(persistent.voice_volume * 100)]" xpos + 10 ypos - 7
                    else:
                        text "[round(persistent.voice_volume * 100)]%" xpos + 10 ypos - 7

            if config.has_music or config.has_sound or config.has_voice:

                null height gui.pref_spacing

                hbox:

                    textbutton _("MY EARS ARE BLEEDING"):

                        style "mute_all_button"
                        action [Function(play_click_sound), Preference("all mute", "toggle")]

                null height (4 * gui.pref_spacing)

screen language_settings():

    hbox:

        vbox:

            ypos + 40
            xpos + 7

            style_prefix "radio"

            textbutton _("English (English)") action [Function(play_click_sound), Language(None), SetField(persistent, "language", "English")]
            textbutton _("Türkçe (Turkish)") action [Function(play_click_sound), Language("turkish"), SetField(persistent, "language", "Türkçe")]

            hbox:

                textbutton _("Español (Spanish)") action [Function(play_click_sound), Language("spanish"), SetField(persistent, "language", "Español")]

                imagebutton idle "gui/overlay/Warning Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("language"))] ypos + 10 xpos + 7

            hbox:

                textbutton _("Русский (Russian)") action [Function(play_click_sound), Language("russian"), SetField(persistent, "language", "Russian")]

                imagebutton idle "gui/overlay/Warning Mark.webp" action [Function(play_click_sound), Show("settings_info", message=settings_panel_tooltip("language"))] ypos + 10 xpos + 7
