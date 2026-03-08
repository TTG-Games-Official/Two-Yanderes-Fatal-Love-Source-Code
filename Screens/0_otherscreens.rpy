init offset = -1

screen credits_screen:
    
    add Transform("images/Two Yanderes & Fatal Love Logo.webp", zoom=0.5, xalign=0.5, yalign=0.5) at credits_scroll_logo

    text credits_text:
        size 40
        xalign 0.5
        yalign 0.5
        at credits_scroll


screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"


screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action [Function(play_click_sound), i.action]


screen history():

    tag menu

    use game_menu(_("                          HISTORY"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        if "color" in h.who_args:
                            text_color h.who_args["color"]
                        

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("The dialogue history is empty.")


screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Skipping")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


screen start_game():
    frame:
        background "#000000"
        xfill True
        yfill True
    timer 2.0 action Start()


screen start_game_ost():
    frame:
        background "#000000"
        xfill True
        yfill True
    timer 2.0 action Start(label="ost")


screen block_input(duration):
    timer duration action Hide("block_input")
    key "dismiss" action NullAction()
    key "mouseup_2" action NullAction()
    key "mousedown_4" action NullAction()
    key "mousedown_5" action NullAction()
    key "mouseup_1" action NullAction()


screen skip:
    text _("[[CTRL] Skip") yalign 0.02 xalign 0.99 size 40

screen introskip(text):
    text text xalign 0.99 yalign 0.02


screen countdown:

    hbox:
        xalign 0.5
        yalign 0.1

        timer 0.04 action If(time > 1, SetVariable("time", time - 0.04), [Hide("countdown"), SetVariable("time", 0), Jump(timeout_label)]) repeat True
        bar:
            value AnimatedValue(value=time - 1 , range=timer_range - 1)
            xmaximum 300

screen countdown_nolimit:

    hbox:
        xalign 0.5
        yalign 0.1

        bar:
            value AnimatedValue(value=0)
            xmaximum 300


screen destiny:

    layer "yblack"

    hbox:

        spacing 15
        xalign 0.5
        yalign 0.373

        text _("{size=+15}{u}DESTINY")

    vbox:
        
        spacing 15
        xalign 0.5
        yalign 0.55

        if destroy_completely == None and police_suspect == None and cat_akira_approved == None and suspended == None and caught == None:
            text _("{color=#959595}No Important Events")

        vbox:

            if suspended == True:
                text _("- Akira and [player] have been temporarly suspended from school.")
            elif suspended == False:
                text _("- Akira and [player] managed to avoid getting suspended from school.")

            if caught == "blood":
                text _("- Akira and [player] were caught by the guidance counselor covered in blood.")
            elif caught == "insane":
                text _("- Akira and [player] were caught by the guidance counselor insane.")

            if cat_akira_approved == True:
                text _("- [player] choose to see Akira with cat ears all the time.")
            elif cat_akira_approved == False:
                text _("- [player] choose to see Akira for who she truly is.")

            if police_suspect == True:
                text _("- The police suspect Akira and [player] of being involved in the crime.")
            elif police_suspect == False:
                text _("- The police don't suspect [player] and Akira of any wrongdoing.")


            if suspended == "truedone":
                text _("{color=#959595}- Akira and [player] have been temporarly suspended from school. (Done)")
            elif suspended == "falsedone":
                text _("{color=#959595}- Akira and [player] managed to avoid getting suspended from school. (Done)")

            if caught == "blood_done":
                text _("{color=#959595}- Akira and [player] were caught by the guidance counselor covered in blood. (Done)")
            elif caught == "insane_done":
                text _("{color=#959595}- Akira and [player] were caught by the guidance counselor insane. (Done)")

            if police_suspect == "truedone":
                text _("{color=#959595}- The police suspect Akira and [player] of being involved in the crime. (Done)")
            elif police_suspect == "falsedone":
                text _("{color=#959595}- The police don't suspect [player] and Akira of any wrongdoing. (Done)")

            if destroy_completely == "truedone":
                text _("{color=#959595}- Akira and [player] chose to completely destroy the evidence. (Done)")
            elif destroy_completely == "falsedone":
                text _("{color=#959595}- Akira and [player] chose to clean the blood from the evidence. (Done)")

screen atm_percent:

    if persistent.language == "Türkçe":

        if atmosphere >= 80:
            text "{color=#ff00ff}{size=-4}%[atmosphere]" xalign 0.5 yalign 0.106
        elif atmosphere >= 60:
            text "{color=#ff71ff}{size=-4}%[atmosphere]" xalign 0.5 yalign 0.106
        elif atmosphere >= 40:
            text "{color=#d283d2}{size=-4}%[atmosphere]" xalign 0.5 yalign 0.106
        elif atmosphere >= 20:
            text "{color=#ab79ab}{size=-4}%[atmosphere]" xalign 0.5 yalign 0.106
        else:
            text "{color=#8e8e8e}{size=-4}%[atmosphere]" xalign 0.5 yalign 0.106

    else:

        if atmosphere >= 80:
            text "{color=#ff00ff}{size=-4}[atmosphere]%" xalign 0.5 yalign 0.106
        elif atmosphere >= 60:
            text "{color=#ff71ff}{size=-4}[atmosphere]%" xalign 0.5 yalign 0.106
        elif atmosphere >= 40:
            text "{color=#d283d2}{size=-4}[atmosphere]%" xalign 0.5 yalign 0.106
        elif atmosphere >= 20:
            text "{color=#ab79ab}{size=-4}[atmosphere]%" xalign 0.5 yalign 0.106
        else:
            text "{color=#8e8e8e}{size=-4}[atmosphere]%" xalign 0.5 yalign 0.106