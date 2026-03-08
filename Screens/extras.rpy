screen extras:

    tag menu

    use game_menu(_("                          EXTRAS"), scroll="viewport"):

        vbox:
            xpos + 150
            spacing 30

            hbox:
            
                spacing 60

                textbutton _("Achievements") action [Function(play_click_sound), SetVariable("extras_category", "achievements")]
                textbutton _("Videos") action [Function(play_click_sound), SetVariable("extras_category", "videos")]

            if extras_category == "achievements":
                text _("Click on an achievement to see the details.")
                use achievements

            elif extras_category == "videos":
                text _("Click on a video name to watch the video on YouTube.")
                use videos


screen achievements:

    default expand = None

    vbox:

        ypos + 20

        if not persistent.game_finished_once:
            textbutton _("{color=#959595}{size=45}1- Forever Yours") action [Function(play_click_sound), SetScreenVariable("expand", "forever_yours")]
            if expand == "forever_yours":
                text _("{size=30}You chose the path of love... You belong to her now.")
                text _("{size=30}> Reach the main (true) ending once.")
                text " "
        else:
            textbutton _("{size=45}1- Forever Yours") action [Function(play_click_sound), SetScreenVariable("expand", "forever_yours")]
            if expand == "forever_yours":
                text _("{size=30}You chose the path of love... You belong to her now.")
                text _("{size=30}> Reach the main (true) ending once.")
                text " "
        

        if not persistent.reached_bad_ending_once:
            textbutton _("{color=#959595}{size=45}2- Wrong Love Story") action [Function(play_click_sound), SetScreenVariable("expand", "wrong_love")]
            if expand == "wrong_love":
                text _("{size=30}Not every love story ends well. Especially not this one.")
                text _("{size=30}> Reach the alternative bad ending once.")
                text " "
        else:
            textbutton _("{size=45}2- Wrong Love Story") action [Function(play_click_sound), SetScreenVariable("expand", "wrong_love")]
            if expand == "wrong_love":
                text _("{size=30}Not every love story ends well. Especially not this one.")
                text _("{size=30}> Reach the alternative bad ending once.")
                text " "


        if not persistent.police_not_caught_once:
            textbutton _("{color=#959595}{size=45}3- Still as Stone") action [Function(play_click_sound), SetScreenVariable("expand", "still_stone")]
            if expand == "still_stone":
                text _("{size=30}Yes officer, everything is {i}definitely{/i} normal...")
                text _("{size=30}> Complete a police interrogation without being caught by the police.")
                text " "
        else:
            textbutton _("{size=45}3- Still as Stone") action [Function(play_click_sound), SetScreenVariable("expand", "still_stone")]
            if expand == "still_stone":
                text _("{size=30}Yes officer, everything is {i}definitely{/i} normal...")
                text _("{size=30}> Complete a police interrogation without being caught by the police.")
                text " "


        if not persistent.police_0suspicion_once:
            textbutton _("{color=#959595}{size=45}4- Perfect Innocence") action [Function(play_click_sound), SetScreenVariable("expand", "p_innocence")]
            if expand == "p_innocence":
                text _("{size=30}You're good at lying... But I see through every word. Every. Single. One.")
                text _("{size=30}> Complete a police interrogation with 0% suspicion.")
                text " "
        else:
            textbutton _("{size=45}4- Perfect Innocence") action [Function(play_click_sound), SetScreenVariable("expand", "p_innocence")]
            if expand == "p_innocence":
                text _("{size=30}You're good at lying... But I see through every word. Every. Single. One.")
                text _("{size=30}> Complete a police interrogation with 0% suspicion.")
                text " "


        if not persistent.police_caught_once:
            textbutton _("{color=#959595}{size=45}5- Cuffed and Loved") action [Function(play_click_sound), SetScreenVariable("expand", "cuffed")]
            if expand == "cuffed":
                text _("{size=30}They would say love is not a crime. It was a lie.")
                text _("{size=30}> Complete a police interrogation by being caught by the police.")
                text " "
        else:
            textbutton _("{size=45}5- Cuffed and Loved") action [Function(play_click_sound), SetScreenVariable("expand", "cuffed")]
            if expand == "cuffed":
                text _("{size=30}They would say love is not a crime. It was a lie.")
                text _("{size=30}> Complete a police interrogation by being caught by the police.")
                text " "


        if not persistent.police_100suspicion_once:
            textbutton _("{color=#959595}{size=45}6- Abnormal Panic") action [Function(play_click_sound), SetScreenVariable("expand", "eyes_on_you")]
            if expand == "eyes_on_you":
                text _("{size=30}No! We are not the criminal! We swear!")
                text _("{size=30}> Complete a police interrogation with 100% suspicion.")
                text " "
        else:
            textbutton _("{size=45}6- Abnormal Panic") action [Function(play_click_sound), SetScreenVariable("expand", "eyes_on_you")]
            if expand == "eyes_on_you":
                text _("{size=30}No! We are not the criminal! We swear!")
                text _("{size=30}> Complete a police interrogation with 100% suspicion.")
                text " "


        if not persistent.counselor_suspended_once:
            textbutton _("{color=#959595}{size=45}7- Too Careless") action [Function(play_click_sound), SetScreenVariable("expand", "too_careless")]
            if expand == "too_careless":
                text _("{size=30}A trivial punishment, like suspension from school, is not enough to stop us.")
                text _("{size=30}> Get suspension punishment from the school by the guidance counselor.")
                text " "
        else:
            textbutton _("{size=45}7- Too Careless") action [Function(play_click_sound), SetScreenVariable("expand", "too_careless")]
            if expand == "too_careless":
                text _("{size=30}A trivial punishment, like suspension from school, is not enough to stop us.")
                text _("{size=30}> Get suspension punishment from the school by the guidance counselor.")
                text " "


        if not persistent.counselor_not_suspended_once:
            textbutton _("{color=#959595}{size=45}8- Behind the Mask") action [Function(play_click_sound), SetScreenVariable("expand", "behind_the_mask")]
            if expand == "behind_the_mask":
                text _("{size=30}We are strong enough to deceive even the guidance counselor.")
                text _("{size=30}> Deceive the guidance counselor successfully to avoid being suspended from school.")
                text " "
        else:
            textbutton _("{size=45}8- Behind the Mask") action [Function(play_click_sound), SetScreenVariable("expand", "behind_the_mask")]
            if expand == "behind_the_mask":
                text _("{size=30}We are strong enough to deceive even the guidance counselor.")
                text _("{size=30}> Deceive the guidance counselor successfully to avoid being suspended from school.")
                text " "

        # There Are Secret Achievements From Here

        # Example Usage:

        #    if not persistent.secret_achievement_unlocked:
        #        textbutton _("{color=#959595}{size=45}9- (Secret Achievement)") action [Function(play_click_sound), SetScreenVariable("expand", "secret_achievement")]
        #        if expand == "secret_achievement":
        #            text "{size=30}[random_text(50)]"
        #            text "{size=30}> [random_text(35)]"
        #            text " "
        #    else:
        #        textbutton _("{size=45}9- Secret Achievement Name") action [Function(play_click_sound), SetScreenVariable("expand", "secret_achievement")]
        #        if expand == "secret_achievement":
        #            text _("{size=30}A text about the secret achievement.")
        #            text _("{size=30}> Unlock condition for the secret achievement.")
        #            text " "


        # This part is here to prevent the cut under the achievement list.
        text " "
        text " "
        text " "
        text " "


screen videos:

    vbox:
    
        spacing 15
        ypos + 20
        text "{color=#1E90FF}- {/color}{a=https://www.youtube.com/watch?v=sVoXv3f28vk}{color=#1E90FF}Updated Visuals, New System and\nNew Language | v3.0.0 Update{a}{/color}"
        text "{color=#1E90FF}- {/color}{a=https://www.youtube.com/watch?v=rCGkmBDzieo}{color=#1E90FF}Updated Game Trailer{a}{/color}"
        text "{color=#1E90FF}- {/color}{a=https://www.youtube.com/watch?v=8YZmo0JJAV8}{color=#1E90FF}2.0.0 Update in 141 Seconds{a}{/color}"
        text "{color=#1E90FF}- {/color}{a=https://www.youtube.com/watch?v=JrqJb4LBBy4}{color=#1E90FF}Official Release Trailer{a}{/color}"
        text "{color=#1E90FF}- {/color}{a=https://www.youtube.com/watch?v=fu5SapmTmzw}{color=#1E90FF}She found you... Now there is no escape...{a}{/color}"
        text "{color=#1E90FF}- {/color}{a=https://www.youtube.com/watch?v=WB1GEyy8ppY}{color=#1E90FF}How Sanity System Works?{a}{/color}"
        text "{color=#1E90FF}- {/color}{a=https://www.youtube.com/watch?v=7lq3_Zpea6o}{color=#1E90FF}How a Yandere Couple Spends Their Day?{a}{/color}"
        text "{color=#1E90FF}- {/color}{a=https://www.youtube.com/watch?v=6_nZwxSQ5gs}{color=#1E90FF}HOW TO FLIRT - YANDERE EDITION{a}{/color}"
        text "{color=#1E90FF}- {/color}{a=https://www.youtube.com/watch?v=gq2U0EQnTLc}{color=#1E90FF}Meet Akira - The Pyschopath Yandere{a}{/color}"