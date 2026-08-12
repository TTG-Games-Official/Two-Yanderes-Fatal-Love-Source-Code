default expanded_achievement = None

init python:

    extras_broken_text = "¥ŔĬşĢø¾₺¿ŁΔü"

    def extras_achievement_unlocked(achievement):

        return achievement_is_unlocked(achievement["id"])


screen extras():

    tag menu

    use game_menu(_("                          EXTRAS"), scroll="viewport"):

        $ yandere_extras = persistent.yandere_menu_enabled == "easteregg"

        vbox:
        
            xpos + 150
            spacing 30

            hbox:

                spacing 60

                if yandere_extras:
                    textbutton _("Achieve Love") action [Function(play_click_sound), SetVariable("extras_category", "achievements")]
                    textbutton _("My Videos, Only For You!") action [Function(play_click_sound), SetVariable("extras_category", "videos")]
                    textbutton _(extras_broken_text) action [Function(play_click_sound), Show("broken_text")]
                else:
                    textbutton _("Achievements") action [Function(play_click_sound), SetVariable("extras_category", "achievements")]
                    textbutton _("Videos") action [Function(play_click_sound), SetVariable("extras_category", "videos")]
                    
                    if persistent.game_started_once:
                        textbutton _(extras_broken_text) action [Function(play_click_sound), Show("broken_text")]

            if extras_category == "achievements":

                if yandere_extras:
                    text _("Click on an achievement to see the lovely details, darling...")
                else:
                    text _("Click on an achievement to see the details.")
                
                use achievements

            elif extras_category == "videos":

                if yandere_extras:
                    text _("Click on a video name to watch the wonderful videos about\nme, darling...")
                else:
                    text _("Click on a video name to watch the video on YouTube.")
               
                use videos

            elif extras_category == "something":
                use something


screen achievements():

    vbox:

        ypos + 20

        for achievement in extras_achievement_data:

            if not achievement.get("debug_only", False) or 1 == 5: # Fix the equalition to see this 13th achievement in your game.

                $ unlocked = extras_achievement_unlocked(achievement)
                $ title = achievement["title"] if unlocked else achievement["locked_title"]

                textbutton _(title) action [Function(play_click_sound), SetVariable("expanded_achievement", achievement["id"])]

                if expanded_achievement == achievement["id"]:

                    if achievement.get("secret", False) and not unlocked:

                        text "{size=30}[random_text(50)]"
                        text "{size=30}> [random_text(35)]"

                    else:

                        for detail in achievement["details"]:
                            text _(detail)

                    text " "

        text " "
        text " "
        text " "


screen videos():

    vbox:

        spacing 15
        ypos + 20

        for video_link in extras_video_links:
            text video_link


screen something():

    vbox:

        ypos + 20

        text "{color=#ffd000}Never gonna give you up,\nNever gonna let you down,\nNever gonna run around and desert you,\nNever gonna make you cry,\nNever gonna say goodbye,\nNever gonna tell a lie and hurt you."
