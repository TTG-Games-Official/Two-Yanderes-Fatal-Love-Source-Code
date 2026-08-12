init python:

    def stats_chapter_title(chapter_name):
        title = stats_chapter_titles.get(chapter_name, {}).get(persistent.language, chapter_name)
        size = 55 if persistent.language == "Español" and chapter_name == "Chapter 6 - Silence Before Storm" else 60
        return "{size=%d}%s" % (size, title)

    def stats_sanity_line(value):

        if value > 79:
            return _("Current Sanity: {color=#ff00ff}[sanity]% (High)")
    
        if value >= 70:
            return _("Current Sanity: {color=#ff9eea}[sanity]% (High)")

        if value > 59:
            return _("Current Sanity: {color=#ff9eea}[sanity]% (Medium)")

        if value > 40:
            return _("Current Sanity: {color=#ff7f7f}[sanity]% (Medium)")

        if value > 35:
            return _("Current Sanity: {color=#ff0000}[sanity]% (Medium)")

        if value > 20:
            return _("Current Sanity: {color=#ff0000}[sanity]% (Low)")

        return _("Current Sanity: {color=#a80000}[sanity]% (Low)")

    def stats_atmosphere_line(value):

        if value >= 80:
            return _("School Mood: {color=#ff00ff}[atmosphere]% (High)")

        if value > 67:
            return _("School Mood: {color=#ff71ff}[atmosphere]% (High)")

        if value >= 60:
            return _("School Mood: {color=#ff71ff}[atmosphere]% (Medium)")

        if value >= 40:
            return _("School Mood: {color=#d283d2}[atmosphere]% (Medium)")

        if value > 33:
            return _("School Mood: {color=#ab79ab}[atmosphere]% (Medium)")

        if value >= 20:
            return _("School Mood: {color=#ab79ab}[atmosphere]% (Low)")

        return _("School Mood: {color=#8e8e8e}[atmosphere]% (Low)")

    def stats_destiny_lines():

        lines = []

        if suspended is True:
            lines.append(stats_destiny_texts["suspended_true"])
        elif suspended is False:
            lines.append(stats_destiny_texts["suspended_false"])

        if caught == "blood":
            lines.append(stats_destiny_texts["caught_blood"])
        elif caught == "insane":
            lines.append(stats_destiny_texts["caught_insane"])

        if cat_akira_approved is True:
            lines.append(stats_destiny_texts["cat_true"])
        elif cat_akira_approved is False:
            lines.append(stats_destiny_texts["cat_false"])

        if police_suspect is True:
            lines.append(stats_destiny_texts["police_true"])
        elif police_suspect is False:
            lines.append(stats_destiny_texts["police_false"])

        if destroy_completely is True:
            lines.append(stats_destiny_texts["destroy_true"])
        elif destroy_completely is False:
            lines.append(stats_destiny_texts["destroy_false"])

        done_keys = (
            ("suspended", suspended),
            ("caught", caught),
            ("police", police_suspect),
            ("destroy", destroy_completely),
        )

        for prefix, value in done_keys:

            key = "%s_%s" % (prefix, value)

            if key in stats_destiny_texts:
                lines.append(stats_destiny_texts[key])

        return lines


screen stats():

    tag menu

    use game_menu(_("                          STATS"), scroll="viewport"):

        style_prefix "help"

        vbox:

            xpos + 150
            spacing 50

            vbox:

                spacing 50

                text stats_chapter_title(chapter)

                vbox:

                    spacing 25

                    text _("{color=#ff00ff}{u}{size=50}GAME")
                    text _(stats_sanity_line(sanity))
                    text _(stats_atmosphere_line(atmosphere))

                vbox:

                    spacing 25

                    text _("{color=#ff00ff}{u}{size=50}DESTINY")

                    vbox:

                        spacing 10

                        $ destiny_lines = stats_destiny_lines()

                        if not destiny_lines:
                            text _("{color=#959595}No Important Events")

                        vbox:

                            for line in destiny_lines:
                                text _(line)

                    text ""