screen stats():

    tag menu

    use game_menu(_("                          STATS"), scroll="viewport"):

        style_prefix "help"

        vbox:

            xpos + 150
            spacing 50
            
            vbox:

                spacing 50

                if persistent.language == "Türkçe":

                    if chapter == "Chapter 1 - Welcome to Forever":
                        text "{size=60}Bölüm 1 - Sonsuzluğa Hoş Geldin"

                    elif chapter == "Chapter 2 - The First Sacrifice":
                        text "{size=60}Bölüm 2 - İlk Kurban"

                    elif chapter == "Chapter 3 - The Slaughter":
                        text "{size=60}Bölüm 3 - Okul Katliamı"

                    elif chapter == "Chapter 4 - No Witnesses":
                        text "{size=60}Bölüm 4 - Tanıklara Yer Yok"

                    elif chapter == "Chapter 5 - Uneasy Silence":
                        text "{size=60}Bölüm 5 - Rahat Olmayan Sessizlik"

                    elif chapter == "Chapter 6 - Silence Before Storm":
                        text "{size=60}Bölüm 6 - Fırtına Öncesi Sessizlik"

                    elif chapter == "Chapter 7 - Before the Fall":
                        text "{size=60}Bölüm 7 - Çöküşten Önce"

                    elif chapter == "Chapter 8 - Echoes in the Hallway":
                        text "{size=60}Bölüm 8 - Koridordaki Yankılar"

                    elif chapter == "Chapter 9 - A Wrong Arrest":
                        text "{size=60}Bölüm 9 - Yanlış Tutuklama"

                    elif chapter == "Chapter 10 - The Lurker Remains":
                        text "{size=60}Bölüm 10 - Tehlike Hâlâ Bitmedi"

                    elif chapter == "Chapter 11 - Massacre Reborn":
                        text "{size=60}Bölüm 11 - Katliamın Yeniden Doğuşu"

                    elif chapter == "Chapter 12 - A New Horizon":
                        text "{size=60}Bölüm 12 - Yeni Bir Ufuk"

                else:
                    text "{size=60}[chapter]"

                vbox:

                    spacing 25
                    
                    text _("{color=#ff00ff}{u}{size=50}GAME")

                    if sanity > 79:
                        text _("Current Sanity: {color=#ff00ff}[sanity]% (High)")
                    elif sanity >= 70:
                        text _("Current Sanity: {color=#ff9eea}[sanity]% (High)")
                    elif sanity > 59:
                        text _("Current Sanity: {color=#ff9eea}[sanity]% (Medium)")
                    elif sanity > 40:
                        text _("Current Sanity: {color=#ff7f7f}[sanity]% (Medium)")
                    elif sanity > 35:
                        text _("Current Sanity: {color=#ff0000}[sanity]% (Medium)")
                    elif sanity > 20:
                        text _("Current Sanity: {color=#ff0000}[sanity]% (Low)")
                    else:
                        text _("Current Sanity: {color=#a80000}[sanity]% (Low)")

                    
                    if atmosphere >= 80:
                        text _("School Atmosphere: {color=#ff00ff}[atmosphere]% (High)")
                    elif atmosphere > 67:
                        text _("School Atmosphere: {color=#ff71ff}[atmosphere]% (High)")
                    elif atmosphere >= 60:
                        text _("School Atmosphere: {color=#ff71ff}[atmosphere]% (Medium)")
                    elif atmosphere >= 40:
                        text _("School Atmosphere: {color=#d283d2}[atmosphere]% (Medium)")
                    elif atmosphere > 33:
                        text _("School Atmosphere: {color=#ab79ab}[atmosphere]% (Medium)")
                    elif atmosphere >= 20:
                        text _("School Atmosphere: {color=#ab79ab}[atmosphere]% (Low)")
                    else:
                        text _("School Atmosphere: {color=#8e8e8e}[atmosphere]% (Low)")

                        
                vbox:

                    spacing 25

                    text _("{color=#ff00ff}{u}{size=50}DESTINY")

                    vbox:
                        spacing 10

                        if destroy_completely == None and police_suspect == None and cat_akira_approved == None and suspended == None and caught == None:
                            text _("{color=#959595}No Important Events")

                        vbox:

                            if suspended == True:
                                text _("- Akira and [player] have been temporarly suspended\nfrom school.")
                            elif suspended == False:
                                text _("- Akira and [player] managed to avoid getting suspended\nfrom school.")

                            if caught == "blood":
                                text _("- Akira and [player] were caught by the guidance\ncounselor covered in blood.")
                            elif caught == "insane":
                                text _("- Akira and [player] were caught by the guidance\ncounselor insane.")

                            if cat_akira_approved == True:
                                text _("- [player] choose to see Akira with cat ears all the time.")
                            elif cat_akira_approved == False:
                                text _("- [player] choose to see Akira for who she truly is.")

                            if police_suspect == True:
                                text _("- The police suspect Akira and [player] of being\ninvolved in the crime.")
                            elif police_suspect == False:
                                text _("- The police don't suspect [player] and Akira of\nany wrongdoing.{size=+0}")

                            if destroy_completely == True:
                                text _("- Akira and [player] chose to completely destroy the\nevidence.")
                            elif destroy_completely == False:
                                text _("- Akira and [player] chose to clean the blood from the\nevidence.")


                            if suspended == "truedone":
                                text _("{color=#959595}- Akira and [player] have been temporarly suspended\nfrom school. (Done)")
                            elif suspended == "falsedone":
                                text _("{color=#959595}- Akira and [player] managed to avoid getting suspended\nfrom school. (Done)")

                            if caught == "blood_done":
                                text _("{color=#959595}- Akira and [player] were caught by the guidance counselor\ncovered in blood. (Done)")
                            elif caught == "insane_done":
                                text _("{color=#959595}- Akira and [player] were caught by the guidance counselor\ninsane. (Done)")

                            if police_suspect == "truedone":
                                text _("{color=#959595}- The police suspect Akira and [player] of being involved\nin the crime. (Done)")
                            elif police_suspect == "falsedone":
                                text _("{color=#959595}- The police don't suspect [player] and Akira of any\nwrongdoing. (Done)")

                            if destroy_completely == "truedone":
                                text _("{color=#959595}- Akira and [player] chose to completely destroy the\nevidence. (Done)")
                            elif destroy_completely == "falsedone":
                                text _("{color=#959595}- Akira and [player] chose to clean the blood from the\nevidence. (Done)")

                    text ""