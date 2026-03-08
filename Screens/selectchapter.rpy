screen select_chapter:

    $ persistent.new_game_clicked = True

    add "gui/overlay/confirm.png"

    add "images/Chapter Select/UI/BG Effect 1.webp" at chapter_select_bg
    add "images/Chapter Select/UI/BG Effect 2.webp" at chapter_select_bg2


    default selected_chapter = 1

    if selected_chapter == 1:

        add "images/Chapter Select/Chapter Images/Chapter 1 Image.webp" at chapter_image

        vbox:
            xalign 0.5
            yalign 0.82

            text _("{size=+10}{color=#ff54e2}Chapter 1 - Welcome to Forever") at title_show
            text _("{size=-5}Our protagonist [persistent.playername] has always been treated as a burden by his family.\nNo one, not even his parents, ever supported his dreams or his existence.\nOne day, he finally meets someone who truly understands and accepts him.\nBut can a bond born from loneliness ever become something truly healthy?") at description_show

        hbox:

            yalign 0.5
            xalign 0.5
            spacing 1600

            imagebutton idle "images/Chapter Select/UI/previous_button_disabled.webp"
            imagebutton idle "images/Chapter Select/UI/next_button_idle.webp" hover "images/Chapter Select/UI/next_button_hover.webp" action [SetScreenVariable("selected_chapter", 2), Function(play_click_sound)]

        textbutton _("START") action [Hide("select_chapter"), Function(play_click_sound), Function(start_game_with_fade), SetField(persistent, "new_game_clicked", False), SetField(persistent, "selected_chapter", 1)] xalign 0.97 yalign 0.97


    elif selected_chapter == 2:

        add "images/Chapter Select/Chapter Images/Chapter 2 Image.webp" at chapter_image
        
        if not persistent.chapter2enabled:
            add "images/Chapter Select/Chapter Images/Locked Chapter.webp" at chapter_image

        vbox:
            xalign 0.5
            yalign 0.82

            text _("{size=+10}{color=#ff54e2}Chapter 2 - The First Sacrifice") at title_show
            text _("{size=-5}Akira and [persistent.playername] are together now, bound by obsession and devotion.\nTheir love grows deeper, but so does their hatred for anyone who interferes.\nThey are willing to destroy everything that dares to stand between them.\nBut can they take their revenge without drawing unwanted attention?") at description_show

        hbox:

            yalign 0.5
            xalign 0.5
            spacing 1600

            imagebutton idle "images/Chapter Select/UI/previous_button_idle.webp" hover "images/Chapter Select/UI/previous_button_hover.webp" action [SetScreenVariable("selected_chapter", 1), Function(play_click_sound)]
            imagebutton idle "images/Chapter Select/UI/next_button_idle.webp" hover "images/Chapter Select/UI/next_button_hover.webp" action [SetScreenVariable("selected_chapter", 3), Function(play_click_sound)]

        if persistent.chapter2enabled:
            textbutton _("START") action [Hide("select_chapter"), Function(play_click_sound), Function(start_game_with_fade), SetField(persistent, "new_game_clicked", False), SetField(persistent, "selected_chapter", 2)] xalign 0.97 yalign 0.97
        else:
            textbutton _("START") xalign 0.97 yalign 0.97

    elif selected_chapter == 3:

        add "images/Chapter Select/Chapter Images/Chapter 3 Image.webp" at chapter_image

        if not persistent.chapter3enabled:
            add "images/Chapter Select/Chapter Images/Locked Chapter.webp" at chapter_image

        vbox:
            xalign 0.5
            yalign 0.82

            text _("{size=+10}{color=#ff54e2}Chapter 3 - The Slaughter") at title_show
            text _("{size=-5}Akira and [persistent.playername] decide that no one else deserves to exist around them.\nTheir actions turn the school into a scene of blood and terror.\nSome students survive long enough to call the police for help.\nWill they escape before their twisted love is finally exposed?") at description_show

        hbox:

            yalign 0.5
            xalign 0.5
            spacing 1600

            imagebutton idle "images/Chapter Select/UI/previous_button_idle.webp" hover "images/Chapter Select/UI/previous_button_hover.webp" action [SetScreenVariable("selected_chapter", 2), Function(play_click_sound)]
            imagebutton idle "images/Chapter Select/UI/next_button_idle.webp" hover "images/Chapter Select/UI/next_button_hover.webp" action [SetScreenVariable("selected_chapter", 4), Function(play_click_sound)]

        if persistent.chapter3enabled:
            textbutton _("START") action [Hide("select_chapter"), Function(play_click_sound), Function(start_game_with_fade), SetField(persistent, "new_game_clicked", False), SetField(persistent, "selected_chapter", 3)] xalign 0.97 yalign 0.97
        else:
            textbutton _("START") xalign 0.97 yalign 0.97

    elif selected_chapter == 4:

        add "images/Chapter Select/Chapter Images/Chapter 4 Image.webp" at chapter_image

        if not persistent.chapter4enabled:
            add "images/Chapter Select/Chapter Images/Locked Chapter.webp" at chapter_image

        vbox:
            xalign 0.5
            yalign 0.82

            text _("{size=+10}{color=#ff54e2}Chapter 4 - No Witnesses") at title_show
            text _("{size=-5}After the massacre at school, two students witness Akira and [persistent.playername]'s crimes.\nThey continue to spread the truth, insisting they are the real killers.\nFor their own safety, Akira and [persistent.playername] make a cruel decision.\nHow far will they go to silence those who know too much?") at description_show

        hbox:

            yalign 0.5
            xalign 0.5
            spacing 1600

            imagebutton idle "images/Chapter Select/UI/previous_button_idle.webp" hover "images/Chapter Select/UI/previous_button_hover.webp" action [SetScreenVariable("selected_chapter", 3), Function(play_click_sound)]
            imagebutton idle "images/Chapter Select/UI/next_button_idle.webp" hover "images/Chapter Select/UI/next_button_hover.webp" action [SetScreenVariable("selected_chapter", 5), Function(play_click_sound)]

        if persistent.chapter4enabled:
            textbutton _("START") action [Hide("select_chapter"), Function(play_click_sound), Function(start_game_with_fade), SetField(persistent, "new_game_clicked", False), SetField(persistent, "selected_chapter", 4)] xalign 0.97 yalign 0.97
        else:
            textbutton _("START") xalign 0.97 yalign 0.97

    elif selected_chapter == 5:

        add "images/Chapter Select/Chapter Images/Chapter 5 Image.webp" at chapter_image

        if not persistent.chapter5enabled:
            add "images/Chapter Select/Chapter Images/Locked Chapter.webp" at chapter_image

        vbox:
            xalign 0.5
            yalign 0.82

            text _("{size=+10}{color=#ff54e2}Chapter 5 - Uneasy Silence") at title_show
            text _("{size=-5}Committing crimes repeatedly only increases the risk of being noticed.\nAkira and [persistent.playername] understand this and choose to stay quiet for a day.\nNo violence, no blood, just an uneasy silence hanging over the school.\nBut can paranoia ever truly fade once fear has taken root?") at description_show

        hbox:

            yalign 0.5
            xalign 0.5
            spacing 1600

            imagebutton idle "images/Chapter Select/UI/previous_button_idle.webp" hover "images/Chapter Select/UI/previous_button_hover.webp" action [SetScreenVariable("selected_chapter", 4), Function(play_click_sound)]
            imagebutton idle "images/Chapter Select/UI/next_button_idle.webp" hover "images/Chapter Select/UI/next_button_hover.webp" action [SetScreenVariable("selected_chapter", 6), Function(play_click_sound)]

        if persistent.chapter5enabled:
            textbutton _("START") action [Hide("select_chapter"), Function(play_click_sound), Function(start_game_with_fade), SetField(persistent, "new_game_clicked", False), SetField(persistent, "selected_chapter", 5)] xalign 0.97 yalign 0.97
        else:
            textbutton _("START") xalign 0.97 yalign 0.97

    elif selected_chapter == 6:

        add "images/Chapter Select/Chapter Images/Chapter 6 Image.webp" at chapter_image

        if not persistent.chapter6enabled:
            add "images/Chapter Select/Chapter Images/Locked Chapter.webp" at chapter_image

        vbox:
            xalign 0.5
            yalign 0.82

            text _("{size=+10}{color=#ff54e2}Chapter 6 - Silence Before Storm") at title_show
            text _("{size=-5}On the first day of the weekend, Akira and [persistent.playername] go on a date together.\nNo murders, no blood, just a moment of fragile normalcy.\nYet even without violence, their twisted bond remains deeply dangerous.\nAfter all, the most terrifying monsters often go completely unnoticed.") at description_show

        hbox:

            yalign 0.5
            xalign 0.5
            spacing 1600

            imagebutton idle "images/Chapter Select/UI/previous_button_idle.webp" hover "images/Chapter Select/UI/previous_button_hover.webp" action [SetScreenVariable("selected_chapter", 5), Function(play_click_sound)]
            imagebutton idle "images/Chapter Select/UI/next_button_idle.webp" hover "images/Chapter Select/UI/next_button_hover.webp" action [SetScreenVariable("selected_chapter", 7), Function(play_click_sound)]

        if persistent.chapter6enabled:
            textbutton _("START") action [Hide("select_chapter"), Function(play_click_sound), Function(start_game_with_fade), SetField(persistent, "new_game_clicked", False), SetField(persistent, "selected_chapter", 6)] xalign 0.97 yalign 0.97
        else:
            textbutton _("START") xalign 0.97 yalign 0.97
    
    elif selected_chapter == 7:

        add "images/Chapter Select/Chapter Images/Chapter 7 Image.webp" at chapter_image

        if not persistent.chapter7enabled:
            add "images/Chapter Select/Chapter Images/Locked Chapter.webp" at chapter_image

        vbox:
            xalign 0.5
            yalign 0.82

            text _("{size=+10}{color=#ff54e2}Chapter 7 - Before the Fall") at title_show
            text _("{size=-5}On the final day of the weekend, Akira and [persistent.playername] prepare for what comes next.\nEvery detail matters as they carefully plan their next move.\nOne mistake could expose everything they have tried to protect.\nWill they be able to execute their plan without drawing suspicion?") at description_show

        hbox:

            yalign 0.5
            xalign 0.5
            spacing 1600

            imagebutton idle "images/Chapter Select/UI/previous_button_idle.webp" hover "images/Chapter Select/UI/previous_button_hover.webp" action [SetScreenVariable("selected_chapter", 6), Function(play_click_sound)]
            imagebutton idle "images/Chapter Select/UI/next_button_idle.webp" hover "images/Chapter Select/UI/next_button_hover.webp" action [SetScreenVariable("selected_chapter", 8), Function(play_click_sound)]

        if persistent.chapter7enabled:
            textbutton _("START") action [Hide("select_chapter"), Function(play_click_sound), Function(start_game_with_fade), SetField(persistent, "new_game_clicked", False), SetField(persistent, "selected_chapter", 7)] xalign 0.97 yalign 0.97
        else:
            textbutton _("START") xalign 0.97 yalign 0.97

    elif selected_chapter == 8:

        add "images/Chapter Select/Chapter Images/Chapter 8 Image.webp" at chapter_image

        if not persistent.chapter8enabled:
            add "images/Chapter Select/Chapter Images/Locked Chapter.webp" at chapter_image

        vbox:
            xalign 0.5
            yalign 0.82

            text _("{size=+10}{color=#ff54e2}Chapter 8 - Echoes in the Hallway") at title_show
            text _("{size=-5}As Akira and [persistent.playername] move to execute their plans, fear must stay alive.\nThey decide that silence alone is no longer enough to terrify the students.\nSoon, unsettling signs begin to appear where no one expects them.\nHow will the students react when fear starts speaking directly to them?") at description_show

        hbox:

            yalign 0.5
            xalign 0.5
            spacing 1600

            imagebutton idle "images/Chapter Select/UI/previous_button_idle.webp" hover "images/Chapter Select/UI/previous_button_hover.webp" action [SetScreenVariable("selected_chapter", 7), Function(play_click_sound)]
            imagebutton idle "images/Chapter Select/UI/next_button_idle.webp" hover "images/Chapter Select/UI/next_button_hover.webp" action [SetScreenVariable("selected_chapter", 9), Function(play_click_sound)]

        if persistent.chapter8enabled:
            textbutton _("START") action [Hide("select_chapter"), Function(play_click_sound), Function(start_game_with_fade), SetField(persistent, "new_game_clicked", False), SetField(persistent, "selected_chapter", 8)] xalign 0.97 yalign 0.97
        else:
            textbutton _("START") xalign 0.97 yalign 0.97

    elif selected_chapter == 9:

        add "images/Chapter Select/Chapter Images/Chapter 9 Image.webp" at chapter_image

        if not persistent.chapter9enabled:
            add "images/Chapter Select/Chapter Images/Locked Chapter.webp" at chapter_image

        vbox:
            xalign 0.5
            yalign 0.82

            text _("{size=+10}{color=#ff54e2}Chapter 9 - A Wrong Arrest") at title_show
            text _("{size=-5}Akira and [persistent.playername] decide to deceive the students and lower their guard.\nThey carefully frame another student as the true murderer.\nWhen an innocent student is arrested, relief spreads through the school.\nWill anyone realize the danger never truly disappeared?") at description_show

        hbox:

            yalign 0.5
            xalign 0.5
            spacing 1600

            imagebutton idle "images/Chapter Select/UI/previous_button_idle.webp" hover "images/Chapter Select/UI/previous_button_hover.webp" action [SetScreenVariable("selected_chapter", 8), Function(play_click_sound)]
            imagebutton idle "images/Chapter Select/UI/next_button_idle.webp" hover "images/Chapter Select/UI/next_button_hover.webp" action [SetScreenVariable("selected_chapter", 10), Function(play_click_sound)]

        if persistent.chapter9enabled:
            textbutton _("START") action [Hide("select_chapter"), Function(play_click_sound), Function(start_game_with_fade), SetField(persistent, "new_game_clicked", False), SetField(persistent, "selected_chapter", 9)] xalign 0.97 yalign 0.97
        else:
            textbutton _("START") xalign 0.97 yalign 0.97

    elif selected_chapter == 10:

        add "images/Chapter Select/Chapter Images/Chapter 10 Image.webp" at chapter_image

        if not persistent.chapter10enabled:
            add "images/Chapter Select/Chapter Images/Locked Chapter.webp" at chapter_image

        vbox:
            xalign 0.5
            yalign 0.82

            text _("{size=+10}{color=#ff54e2}Chapter 10 - The Lurker Remains") at title_show
            text _("{size=-5}Believing the killer is gone, the students finally feel safe again.\nAkira and [persistent.playername] use this moment to approach their next target.\nBy acting friendly, they ensure no suspicion falls upon them.\nWill they manage to strike before anyone realizes the truth?") at description_show

        hbox:

            yalign 0.5
            xalign 0.5
            spacing 1600

            imagebutton idle "images/Chapter Select/UI/previous_button_idle.webp" hover "images/Chapter Select/UI/previous_button_hover.webp" action [SetScreenVariable("selected_chapter", 9), Function(play_click_sound)]
            imagebutton idle "images/Chapter Select/UI/next_button_idle.webp" hover "images/Chapter Select/UI/next_button_hover.webp" action [SetScreenVariable("selected_chapter", 11), Function(play_click_sound)]

        if persistent.chapter10enabled:
            textbutton _("START") action [Hide("select_chapter"), Function(play_click_sound), Function(start_game_with_fade), SetField(persistent, "new_game_clicked", False), SetField(persistent, "selected_chapter", 10)] xalign 0.97 yalign 0.97
        else:
            textbutton _("START") xalign 0.97 yalign 0.97

    elif selected_chapter == 11:

        add "images/Chapter Select/Chapter Images/Chapter 11 Image.webp" at chapter_image

        if not persistent.chapter11enabled:
            add "images/Chapter Select/Chapter Images/Locked Chapter.webp" at chapter_image

        vbox:
            xalign 0.5
            yalign 0.82

            text _("{size=+10}{color=#ff54e2}Chapter 11 - Massacre Reborn") at title_show
            text _("{size=-5}After being questioned by the Guidance Counselor, anger begins to boil over.\nAkira and [persistent.playername] decide the other students must pay the price.\nTheir restraint fades as destruction becomes their only answer.\nWill they succeed in hunting everyone down without being stopped?") at description_show

        hbox:

            yalign 0.5
            xalign 0.5
            spacing 1600

            imagebutton idle "images/Chapter Select/UI/previous_button_idle.webp" hover "images/Chapter Select/UI/previous_button_hover.webp" action [SetScreenVariable("selected_chapter", 10), Function(play_click_sound)]
            imagebutton idle "images/Chapter Select/UI/next_button_idle.webp" hover "images/Chapter Select/UI/next_button_hover.webp" action [SetScreenVariable("selected_chapter", 12), Function(play_click_sound)]

        if persistent.chapter11enabled:
            textbutton _("START") action [Hide("select_chapter"), Function(play_click_sound), Function(start_game_with_fade), SetField(persistent, "new_game_clicked", False), SetField(persistent, "selected_chapter", 11)] xalign 0.97 yalign 0.97
        else:
            textbutton _("START") xalign 0.97 yalign 0.97

    elif selected_chapter == 12:

        add "images/Chapter Select/Chapter Images/Chapter 12 Image.webp" at chapter_image

        if not persistent.chapter12enabled:
            add "images/Chapter Select/Chapter Images/Locked Chapter.webp" at chapter_image

        vbox:
            xalign 0.5
            yalign 0.82

            text _("{size=+10}{color=#ff54e2}Chapter 12 - A New Horizon") at title_show
            text _("{size=-5}After the second massacre, Akira and [persistent.playername] wake up to a new day.\nBefore heading to school, they come across an unexpected piece of news.\nAs they read it, they realize everything they knew is about to change.\nFrom this moment on, nothing will ever be the same again.") at description_show

        hbox:

            yalign 0.5
            xalign 0.5
            spacing 1600

            imagebutton idle "images/Chapter Select/UI/previous_button_idle.webp" hover "images/Chapter Select/UI/previous_button_hover.webp" action [SetScreenVariable("selected_chapter", 11), Function(play_click_sound)]
            imagebutton idle "images/Chapter Select/UI/next_button_disabled.webp"

        if persistent.chapter12enabled:
            textbutton _("START") action [Function(play_click_sound), Show("ch12_warning")] xalign 0.97 yalign 0.97
        else:
            textbutton _("START") xalign 0.97 yalign 0.97

    textbutton _("GO BACK") action [Hide("select_chapter"), Function(play_click_sound), SetField(persistent, "new_game_clicked", False)] xalign 0.03 yalign 0.97
