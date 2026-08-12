screen chapter_select_preview(chapter, unlocked):

    add chapter["image"] at chapter_image

    if not unlocked:
        add "images/Chapter Select/Chapter Images/Locked Chapter.webp" at chapter_image

    vbox:
        xalign 0.5
        yalign 0.82

        text _(chapter["title"]) at title_show
        text _(chapter["description"]) at description_show


screen select_chapter():

    $ persistent.new_game_clicked = True

    add "gui/overlay/confirm.png"

    add "images/Chapter Select/UI/BG Effect 1.webp" at chapter_select_bg
    add "images/Chapter Select/UI/BG Effect 2.webp" at chapter_select_bg2

    default selected_chapter = 1

    $ chapter_unlocked = (selected_chapter == 1) or getattr(persistent, "chapter{}enabled".format(selected_chapter), False)

    if selected_chapter == 1:
        use chapter_select_preview(chapter_select_data[0], chapter_unlocked)
    elif selected_chapter == 2:
        use chapter_select_preview(chapter_select_data[1], chapter_unlocked)
    elif selected_chapter == 3:
        use chapter_select_preview(chapter_select_data[2], chapter_unlocked)
    elif selected_chapter == 4:
        use chapter_select_preview(chapter_select_data[3], chapter_unlocked)
    elif selected_chapter == 5:
        use chapter_select_preview(chapter_select_data[4], chapter_unlocked)
    elif selected_chapter == 6:
        use chapter_select_preview(chapter_select_data[5], chapter_unlocked)
    elif selected_chapter == 7:
        use chapter_select_preview(chapter_select_data[6], chapter_unlocked)
    elif selected_chapter == 8:
        use chapter_select_preview(chapter_select_data[7], chapter_unlocked)
    elif selected_chapter == 9:
        use chapter_select_preview(chapter_select_data[8], chapter_unlocked)
    elif selected_chapter == 10:
        use chapter_select_preview(chapter_select_data[9], chapter_unlocked)
    elif selected_chapter == 11:
        use chapter_select_preview(chapter_select_data[10], chapter_unlocked)
    elif selected_chapter == 12:
        use chapter_select_preview(chapter_select_data[11], chapter_unlocked)

    hbox:

        yalign 0.5
        xalign 0.5
        spacing 1600

        if selected_chapter == 1:
            imagebutton idle "images/Chapter Select/UI/previous_button_disabled.webp"
        else:
            imagebutton idle "images/Chapter Select/UI/previous_button_idle.webp" hover "images/Chapter Select/UI/previous_button_hover.webp" action [SetScreenVariable("selected_chapter", selected_chapter - 1), Function(play_click_sound)]

        if selected_chapter == 12:
            imagebutton idle "images/Chapter Select/UI/next_button_disabled.webp"
        else:
            imagebutton idle "images/Chapter Select/UI/next_button_idle.webp" hover "images/Chapter Select/UI/next_button_hover.webp" action [SetScreenVariable("selected_chapter", selected_chapter + 1), Function(play_click_sound)]

    if chapter_unlocked:

        if selected_chapter == 12:
            textbutton _("START") action [Function(play_click_sound), Show("ch12_warning")] xalign 0.97 yalign 0.97
        else:
            textbutton _("START") action [Hide("select_chapter"), Function(play_click_sound), Function(start_game_with_fade), SetField(persistent, "new_game_clicked", False), SetField(persistent, "selected_chapter", selected_chapter)] xalign 0.97 yalign 0.97
    
    else:
        textbutton _("START") xalign 0.97 yalign 0.97

    textbutton _("GO BACK") action [Hide("select_chapter"), Function(play_click_sound), SetField(persistent, "new_game_clicked", False)] xalign 0.03 yalign 0.97
