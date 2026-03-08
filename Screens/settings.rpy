screen preferences():

    tag menu

    default settings_category = "general"

    use game_menu(_("                          SETTINGS"), scroll="viewport"):

        vbox:

            xpos + 150

            hbox:
            
                spacing 60

                textbutton _("General Settings") action [Function(play_click_sound), SetScreenVariable("settings_category", "general")]
                textbutton _("Text Settings") action [Function(play_click_sound), SetScreenVariable("settings_category", "text")]
                textbutton _("Audio Settings") action [Function(play_click_sound), SetScreenVariable("settings_category", "audio")]
                textbutton _("Other") action [Function(play_click_sound), SetScreenVariable("settings_category", "other")]

            if settings_category == "general":
                use general_settings
            elif settings_category == "text":
                use text_settings
            elif settings_category == "audio":
                use audio_settings
            elif settings_category == "other":
                use other_settings


screen general_settings():

    vbox:

        ypos + 50
        xpos + 20
        spacing 25

        box_wrap True

        hbox:

            spacing 50

            vbox:

                style_prefix "radio"
                label _("DISPLAY MODE")

                textbutton _("Windowed") action [Function(play_click_sound), Preference("display", "window"), SetField(persistent, "display", 1)] hovered SetVariable("whichtooltip", "Display Window"):
                    if persistent.language == "Türkçe":
                        tooltip "Oyunu yeniden boyutlandırılabilir bir pencerede çalıştırır. Böylece oyun\naçıkken diğer uygulamalara da erişebilirsin."
                    else:
                        tooltip "Runs the game in a resizable window, allowing you to adjust its size while\nkeeping access to other applications."
                textbutton _("Fullscreen") action [Function(play_click_sound), Preference("display", "fullscreen"), SetField(persistent, "display", 2)] hovered SetVariable("whichtooltip", "Display Fullscreen"):
                    if persistent.language == "Türkçe":
                        tooltip "Oyunu tüm ekranı kaplayacak şekilde çalıştırır."
                    else:
                        tooltip "Expands the game to fill your entire screen."

            vbox:

                style_prefix "check"

                label _("SKIP OPTIONS")
                textbutton _("Unseen Text") action [Function(play_click_sound), Preference("skip", "toggle")] hovered SetVariable("whichtooltip", "Skip Unseen Text"):
                    if persistent.language == "Türkçe":
                        tooltip "Daha önce görmediğin diyalogları atlamana izin verir."
                    else:
                        tooltip "Allows you to skip the dialogue texts you haven't seen yet."
                textbutton _("After Choices") action [Function(play_click_sound), Preference("after choices", "toggle")] hovered SetVariable("whichtooltip", "Skip After Choices"):
                    if persistent.language == "Türkçe":
                        tooltip "Bir seçim yaptıktan sonra diyalogları atlamaya devam etmene izin verir."
                    else:
                        tooltip "Allows you to continue skipping dialogues after selecting a choice."
                textbutton _("Intro") action [Function(play_click_sound), ToggleField(persistent, "intro", true_value=False, false_value=True)] hovered SetVariable("whichtooltip", "Skip Intro"):
                    if persistent.language == "Türkçe":
                        tooltip "Hikâyenin birinci bölümüne başlarken giriş sahnesini atlar."
                    else:
                        tooltip "Skip the intro when starting the first chapter."
            
            vbox:
                style_prefix "radio"

                vbox:

                    hbox:

                        label _("SHOW SANITY")
                        imagebutton idle im.Scale("gui/overlay/Question Mark.webp", 45, 45) hover im.Scale("gui/overlay/Question Mark.webp", 45, 45) action NullAction() hovered SetVariable("whichtooltip", "Sanity Info") ypos + 15 xpos + 10:
                            if persistent.language == "Türkçe":
                                tooltip "\nAkıl sağlığı yüzdesi ana karakterin zihinsel dengesini temsil eder. Değer\ndüştükçe ekran kararır. Bu ayar, oynanışı veya hikâye gidişatını etkilemez."
                            else:
                                tooltip "The sanity percentage represents the mental stability of the main character.\nThe lower it gets, the darker the screen becomes. It does not affect gameplay\nor story progression."

                    textbutton _("Always") action [Function(play_click_sound), SetField(persistent, "show_sanity", True)] hovered SetVariable("whichtooltip", "Showing Sanity"):
                        if persistent.language == "Türkçe":
                            tooltip "Akıl sağlığı yüzdesi durum ne olursa olsun her zaman ekranda görünür."
                        else:
                            tooltip "The sanity percentage will always be visible, no matter the situation."
                    textbutton _("Dynamic") action [Function(play_click_sound), SetField(persistent, "show_sanity", "dynamic")] hovered SetVariable("whichtooltip", "Showing Sanity Two Column"):
                        if persistent.language == "Türkçe":
                            tooltip "Akıl sağlığı yüzdesi yalnızca önemli sahnelerde veya önemli anlarda görünür."
                        else:
                            tooltip "The sanity percentage will appear only during significant scenes or moments\nwhen your state changes."
                    textbutton _("Hidden") action [Function(play_click_sound), SetField(persistent, "show_sanity", False)] hovered SetVariable("whichtooltip", "Showing Sanity Two Column"):
                        if persistent.language == "Türkçe":
                            tooltip "Akıl sağlığı yüzdesi oyun boyunca değişse bile tamamen gizlenir."
                        else:
                            tooltip "The sanity percentage will be completely hidden throughout the game, even\nwhen it changes."

        hbox:
            
            spacing 50
            ypos + 20   

            vbox:

                style_prefix "radio"

                hbox:

                    label _("LOW FPS OPTIMIZATION")
                    imagebutton idle im.Scale("gui/overlay/Question Mark.webp", 45, 45) hover im.Scale("gui/overlay/Question Mark.webp", 45, 45) action NullAction() hovered SetVariable("whichtooltip", "Low FPS Optimize Info") ypos + 55 xpos + 10:
                        if persistent.language == "Türkçe":
                            tooltip "{size=-7}Eğer düşük FPS alıyorsanız (40-50 altı), akıl sağlığı, atmosfer, ve şüphe seviyesi gibi yüzdelik değerler\nçok yavaş değişebilir ve bu oyun deneyimini yavaşlatabilir. Bu optimizasyon, düşük sistemlerde bu\ndeğişimleri hızlandırarak daha akıcı bir oyun deneyimi sunar. Ancak yüksek kare hızlarında bu değişim\nanimasyonları çok hızlı olabilir.\n{color=#00ff00}50 FPS altında çalışan sistemler için önerilir.{/color}\n{color=#ff0000}Yüksek performanslı sistemler için önerilmez.{/color}"
                        else:
                            tooltip "{size=-7}If you're getting low FPS (below 40-50), the sanity, atmosphere, and suspicion percentages may increase or\ndecrease too slowly, making the gameplay feel sluggish. This optimization makes these variable changes\nfaster, ensuring smoother and more balanced pacing on low-end systems. However, at higher frame rates,\nthe animations may appear too fast.\n{color=#00ff00}Recommended for systems running below 50 FPS.{/color}\n{color=#ff0000}Not recommended for high-performance systems.{/color}"

                textbutton _("Enable") action [Function(play_click_sound), SetField(persistent, "low_fps_optimization", True)] hovered SetVariable("whichtooltip", "Low FPS Optimization"):
                    if persistent.language == "Türkçe":
                        tooltip "Akıl sağlığı, atmosfer ve şüphe yüzdeleri {color=#ffdd00}kare başına %5{/color} oranında artar veya azalır,\nbu da değişimleri daha hızlı yapar."
                    else:
                        tooltip "The sanity, atmosphere, and suspicion percentages will increase or decrease\nby {color=#ffdd00}5% per frame,{/color} making changes much more faster."
                textbutton _("Disable") action [Function(play_click_sound), SetField(persistent, "low_fps_optimization", False)] hovered SetVariable("whichtooltip", "Low FPS Optimization"):
                    if persistent.language == "Türkçe":
                        tooltip "Akıl sağlığı, atmosfer ve şüphe yüzdeleri {color=#ffdd00}kare başına %1{/color} oranında artar veya azalır,\nbu da değişimleri daha yumuşak yapar."
                    else:
                        tooltip "The sanity, atmosphere, and suspicion percentages will increase or decrease\nby {color=#ffdd00}1% per frame,{/color} making changes much more smoother."

            vbox:

                style_prefix "radio"

                label _("LANGUAGE")

                textbutton _("English (English)") action [Function(play_click_sound), Language(None), SetField(persistent, "language", "English")] hovered SetVariable("whichtooltip", "Language"):
                    if persistent.language == "Türkçe":
                        tooltip "Oyunun dilini İngilizce yapar."
                    else:
                        tooltip "Makes the game's language English."
                textbutton _("Türkçe (Turkish)") action [Function(play_click_sound), Language("turkish"), SetField(persistent, "language", "Türkçe")] hovered SetVariable("whichtooltip", "Language"):
                    if persistent.language == "Türkçe":
                        tooltip "Oyunun dilini Türkçe yapar."
                    else:
                        tooltip "Makes the game's language Turkish."

            vbox:

                ypos + 15

                label _("CHANGE YOUR NAME")

                if persistent.playername == "":
                    text _("{color=#ffbf00}{size=-10}Current Name: N/A")
                else:    
                    text _("{color=#ffbf00}{size=-10}Current Name: [persistent.playername]")

                if main_menu:
                    textbutton _("Change") action [Function(play_click_sound), Show("change_name")]
                else:
                    textbutton _("Change") action [Function(play_click_sound), Show("change_name_error")]

        null height (4 * gui.pref_spacing)
    
    $ tooltip = GetTooltip()

    if tooltip:

        vbox:
            xpos 0.5
            xanchor 0.5

            if whichtooltip == "Display Window" or whichtooltip == "Showing Sanity Two Column" or whichtooltip == "Low FPS Optimization":
                
                if persistent.language == "Türkçe" and whichtooltip == "Showing Sanity Two Column":
                    ypos 2.0
                else:
                    ypos 1.0

            elif whichtooltip == "Showing Sanity":
                ypos 2.0
            elif whichtooltip == "Sanity Info":
                ypos 0.5
            elif whichtooltip == "Low FPS Optimize Info":
                ypos 0.0
            else:
                ypos 2.0

            frame:
                background None
                padding (10, 5)
                text "[GetTooltip()]" size 30

screen text_settings():

    vbox:

        ypos + 50
        xpos + 20

        label _("Text Speed")
        hbox:
            bar value FieldValue(_preferences, "text_cps", range=180, max_is_zero=False, offset=20) hovered SetVariable("whichtooltip", "Text Speed") style "custom_bar":
                if persistent.language == "Türkçe":
                    tooltip "Yazıların diyalog kutusunda ne kadar hızlı görüneceğini {color=#ffdd00}saniye başında gösterilen\nharf sayısını değiştirerek{/color} belirler. Yüksek bir değer yazıların görünmesini\nhızlandırırken düşük bir değer yavaşlatır."
                else:
                    tooltip "Controls how fast the text appears in the dialogue box by adjusting {color=#ffdd00}the number of\nletters displayed per second.{/color} A higher value makes the text appear faster, while a\nlower value slows it down."

            text "[round(preferences.text_cps)]" xpos + 10 ypos - 7

        label _("Auto-Forward Delay")
        hbox:
            bar value Preference("auto-forward time", range=20) hovered SetVariable("whichtooltip", "Auto-Forward Delay") style "custom_bar":
                if persistent.language == "Türkçe":
                    tooltip "Otomatik ilerleme modu sırasında bir sonraki repliğe otomatik olarak geçmeden önce\nne kadar süre bekleneceğini belirler. Yüksek bir değer replikler arası daha uzun\nbekleme süresi anlamına gelirken düşük bir değer daha kısa bekleme süresi demektir."
                else:
                    tooltip "Determines how long the game waits before automatically advancing to the next line\nof dialogue during auto-progress. A higher value means longer pauses between lines,\nwhile a lower value makes dialogue progress faster."

            text "[round(preferences.afm_time)]" xpos + 10 ypos - 7

    null height (4 * gui.pref_spacing)
    
    $ tooltip = GetTooltip()

    if tooltip:

        vbox:
        
            xpos 0.5
            xanchor 0.5
            ypos 3.2

            frame:
                background None
                padding (10, 5)
                text "[GetTooltip()]" size 30

screen audio_settings():

    vbox:

        ypos + 50
        xpos + 20

        if config.has_music:

            label _("Music Volume")
            hbox:
                bar value FieldValue(persistent, "music_volume", range=1.0) hovered SetVariable("whichtooltip", "Music Volume") style "custom_bar":
                    if persistent.language == "Türkçe":
                        tooltip "\nHem ana menü hem de oyun içinde arka plan müziklerinin ses seviyesini ayarlar."
                    else:                        
                        tooltip "Adjusts the volume level of background music in both the main menu and during\ngameplay."
                $ preferences.volumes['music'] = persistent.music_volume ** 2

                if persistent.language == "Türkçe":
                    text "%[round(persistent.music_volume * 100)]" xpos + 10 ypos - 7
                else:
                    text "[round(persistent.music_volume * 100)]%" xpos + 10 ypos - 7

        if config.has_sound:

            label _("Sound Volume")
            hbox:
                bar value FieldValue(persistent, "sfx_volume", range=1.0) hovered SetVariable("whichtooltip", "SFX Volume") style "custom_bar":
                    if persistent.language == "Türkçe":
                        tooltip "\nHem ana menü hem de oyun içinde ses efektlerinin ses seviyesini ayarlar."
                    else:                        
                        tooltip "Adjusts the volume level of sound effects in both the main menu and during\ngameplay."
                $ preferences.volumes['sfx'] = persistent.sfx_volume ** 2

                if persistent.language == "Türkçe":
                    text "%[round(persistent.sfx_volume * 100)]" xpos + 10 ypos - 7
                else:
                    text "[round(persistent.sfx_volume * 100)]%" xpos + 10 ypos - 7
                
        if config.has_voice:

            label _("Voice Volume")
            hbox:
                bar value FieldValue(persistent, "voice_volume", range=1.0) hovered SetVariable("whichtooltip", "Voice Volume") style "custom_bar":
                    if persistent.language == "Türkçe":
                        tooltip "Oyun içi karakter seslendirmelerinin ses seviyesini ayarlar."
                    else:                        
                        tooltip "Adjusts the volume level of character voice lines."
                $ preferences.volumes['voice'] = persistent.voice_volume ** 2

                if persistent.language == "Türkçe":
                    text "%[round(persistent.voice_volume * 100)]" xpos + 10 ypos - 7
                else:
                    text "[round(persistent.voice_volume * 100)]%" xpos + 10 ypos - 7

        if config.has_music or config.has_sound or config.has_voice:

            null height gui.pref_spacing

            textbutton _("Mute All"):

                style "mute_all_button"

                action [Function(play_click_sound), Preference("all mute", "toggle")]
                hovered SetVariable("whichtooltip", "Mute All")

                if config.has_voice:
                    if persistent.language == "Türkçe":
                        tooltip "Müzik, ses efektleri ve karakter seslendirmeleri dahil oyundaki tüm sesleri kapatır."
                    else:
                        tooltip "Completely disables all game sounds including music, sound effects and voice lines."
                else:
                    if persistent.language == "Türkçe":
                        tooltip "Müzik ve ses efektleri dahil oyundaki tüm sesleri kapatır."
                    else:
                        tooltip "Completely disables all game sounds including music and sound effects."

            null height (4 * gui.pref_spacing)
    
    $ tooltip = GetTooltip()

    if tooltip:

        vbox:

            xpos 0.5
            xanchor 0.5

            if whichtooltip == "Mute All":

                if config.has_voice:
                    ypos 5.8
                    xpos 0.48
                else:
                    ypos 7.5
                    xpos 0.55

            else:

                if config.has_voice:
                    if whichtooltip == "Voice Volume":
                        ypos 5.75
                        xpos 0.65
                    else:
                        ypos 3.0
                else:
                    ypos 4.0

            frame:
                background None
                padding (10, 5)
                text "[GetTooltip()]" size 30

screen other_settings():

    vbox:

        ypos + 40
        xpos + 7
        spacing 25

        text _("{color=#1E90FF}{/color}{a=https://sites.google.com/view/privacy-policy-tyfl/home}{color=#1E90FF}Show Privacy Policy{a}{/color}")
        text _("{color=#1E90FF}{/color}{a=https://sites.google.com/view/terms-of-use-tyfl/home}{color=#1E90FF}Show License Agreement & Terms of Use{a}{/color}")