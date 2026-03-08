screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic Saves"))

    use game_menu(title):

        fixed:

            xpos + 50

            order_reverse True

            button:

                style "page_label"

                key_events True
                xalign 0.5
                
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            grid gui.file_slot_cols gui.file_slot_rows:

                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing


                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                    
                        action FileAction(slot)
                        
                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("Empty Slot")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            vbox:

                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:

                    xalign 0.5
                    spacing gui.page_spacing

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action [Function(play_click_sound), FilePage("auto")]

                    for page in range(1, 11):
                        textbutton "[page]" action [Function(play_click_sound), FilePage(page)]

                    text "  |  " ypos + 2

                    textbutton _("Delete All Saves") action [Function(play_click_sound), Show("delete_saves")]

screen save():
    tag menu
    use file_slots(_("                          SAVE GAME"))

screen load():
    tag menu
    use file_slots(_("                          LOAD SAVE"))
