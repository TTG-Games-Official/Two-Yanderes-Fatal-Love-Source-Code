label dontskip:

    hide screen countdown
    hide screen countdown_nolimit

    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    $ settings_enabled = False
    $ history_enabled = False
    $ hide_enabled = False

    $ save_sanity_percent = sanity
    $ save_textbox_state = textbox

    $ yblack_saved_transparent = 1.0 - pow(sanity / 100, 1)

    $ saved_atmosphere = atmosphere

    if sanity >= 70:
        $ saved_sanity_mode = "high"
    elif sanity > 35:
        $ saved_sanity_mode = "medium"
    else:
        $ saved_sanity_mode = "low"

    $ hide_sanity_force = True
    $ set_sanity(100)
    $ set_atmosphere(100)

    hide yandereblack onlayer yblack

    $ renpy.music.set_volume(0.0, channel='music')
    $ renpy.music.set_volume(0.0, channel='lsanity')
    $ renpy.music.set_volume(0.0, channel='msanity')
    $ renpy.music.set_volume(0.0, channel='hsanity')

    stop sound
    stop sound2
    play sound tvparasite volume 0.7
    
    show tvparasite zorder 30

    $ lock_dismiss()
    "{cps=120}[random_text(120)]{nw}"
    $ unlock_dismiss()

    $ textbox = get_allowed_textbox_type("yandere")
    hide tvparasite
    stop sound
    play skipmusic thatzenmoment
    show black zorder 5
    $ quick_menu = True

    $ get_achievement("are_you_trying_to_skip")

    show a k y se om happy zorder 10 at ss(0.5) onlayer askip

    $ lock_dismiss()
    akira "{cps=15}Oh? Are you trying to skip, my love~?{nw}"
    $ unlock_dismiss()
    akira "Oh? Are you trying to skip, my love~?{fast}"

    show a k y se cm happy onlayer askip

    $ lock_dismiss()
    akira "{cps=20}I am not boring you, am I?{nw}"
    $ unlock_dismiss()
    akira "I am not boring you, am I?{fast}"

    show a k y se cm happy at bout(0.5) onlayer askip

    window hide
    $ time = 10
    $ timer_range = 10
    $ timeout_label = "silent_cinema"
    show screen countdown

    menu:

        "W-What's happening?":
            hide screen countdown
            window show
            jump akira_what

        "I already saw this scene...":
            hide screen countdown
            window show
            jump akira_seen

        "Yes, you are boring me!":
            hide screen countdown
            window show
            jump akira_boring


label silent_cinema:

    window show

    show a k n ce cm happy at bin(0.5) onlayer askip

    $ lock_dismiss()
    akira "{cps=20}Are we playing silent cinema, darling~?{nw}"
    $ unlock_dismiss()
    akira "Are we playing silent cinema, darling~?{fast}"

    show a k n ce cm happy onlayer askip

    $ lock_dismiss()
    akira "{cps=20}Did I really shock you {i}that{/i} much~?{nw}"
    $ unlock_dismiss()
    akira "Did I really shock you {i}that{/i} much~?{fast}"

    show a k y se cm happy onlayer askip

    $ lock_dismiss()
    akira "{cps=25}Well, now that you learned that I'm aware about this game, you will be a good listener; will you, my sweetheart~?{nw}"
    $ unlock_dismiss()
    akira "Well, now that you learned that I'm aware about this game, you will be a good listener; will you, my sweetheart~?{fast}"

    show a k n oe om happy onlayer askip

    $ lock_dismiss()
    akira "{cps=25}I'm gonna enable the skip function now and let you continue the story. Buuut, I won't break the fourth wall again for this at least.{nw}"
    $ unlock_dismiss()
    akira "I'm gonna enable the skip function now and let you continue the story. Buuut, I won't break the fourth wall again for this at least.{fast}"

    show a k n ce cm happy onlayer askip

    $ lock_dismiss()
    akira "{cps=20}Enjoy our {i}perfect{/i} story, darling~!{nw}"
    $ unlock_dismiss()
    akira "Enjoy our {i}perfect{/i} story, darling~!{fast}"

    jump continue_story


label akira_what:

    show a k y ce om mocking at bin(0.5) onlayer askip

    $ lock_dismiss()
    akira "{cps=25}AHAHAHA! Were you really thinking that I'm not aware about this game? I'm just pretending that I'm not.{nw}"
    $ unlock_dismiss()
    akira "AHAHAHA! Were you really thinking that I'm not aware about this game? I'm just pretending that I'm not.{fast}"

    show a k y se cm mocking onlayer askip

    $ lock_dismiss()
    akira "{cps=25}So you'd better be a good [persistent.gender] and read the story, especially my words... Since you downloaded this game to romance with me~{nw}"
    $ unlock_dismiss()
    akira "So you'd better be a good [persistent.gender] and read the story, especially my words... Since you downloaded this game to romance with me~{fast}"

    show a k y oe om happy onlayer askip

    $ lock_dismiss()
    akira "{cps=25}I'm gonna enable your skip function now. Buuut, I'm not going to break the fourth wall again for this at least.{nw}"
    $ unlock_dismiss()
    akira "I'm gonna enable your skip function now. Buuut, I'm not going to break the fourth wall again for this at least.{fast}"

    show a k y se cm mocking onlayer askip

    $ lock_dismiss()
    akira "{cps=25}However, don't dare to skip all the story without reading it. Or else I will find your house and tell the game's story myself. Promise?{nw}"
    $ unlock_dismiss()
    akira "However, don't dare to skip all the story without reading it. Or else I will find your house and tell the game's story myself. Promise?{fast}"

    show a k y se cm mocking at bout(0.5) onlayer askip

    window hide
    $ time = 5
    $ timer_range = 5
    $ timeout_label = "promise_shout"
    show screen countdown

    menu:

        "I Promise...":

            hide screen countdown
            window show
            jump akira_goodboy


label promise_shout:

    $ style.say_dialogue = style.scarytext
    show a k y se om angry at bin(0.5) onlayer askip

    window show

    $ lock_dismiss()
    akira "{cps=20}PROMISE ME YOU WILL READ THE STORY!{nw}"
    $ unlock_dismiss()
    akira "PROMISE ME YOU WILL READ THE STORY!{fast}"

    show a k y se cm angry at bout(0.5) onlayer askip

    window hide
    $ time = 8
    $ timer_range = 8
    $ timeout_label = "akira_game_exit"
    show screen countdown

    menu:

        "I PROMISE! PLEASE DON'T HURT ME!":
            pass

        "I WILL! I SWEAR ON MY LIFE!":
            pass

        "I PROMISE! I WILL READ EVERYTHING!":
            pass

        "{size=-6}PLEASE! DON'T HURT ME! I PROMISE! I REALLY DO!":
            pass

        "{size=-5}I PROMISE! JUST PUT THE KNIFE DOWN, PLEASE!":
            pass

    hide screen countdown
    window show

label akira_goodboy:

    $ style.say_dialogue = style.normaltext
    show a k n oe cm happy at bin(0.5) onlayer askip

    $ lock_dismiss()
    akira "{cps=20}Good [persistent.gender]~{nw}"
    $ unlock_dismiss()
    akira "Good [persistent.gender]~{fast}"

    show a k n ce om happy onlayer askip
    
    $ lock_dismiss()
    akira "{cps=20}Then, let's continue to our {i}perfect{/i} story~{nw}"
    $ unlock_dismiss()
    akira "Then, let's continue to our {i}perfect{/i} story~{fast}"

    jump continue_story


label akira_game_exit:

    window show
    $ style.say_dialogue = style.normaltext
    show a k y ce cm angry at bin(0.5) onlayer askip

    $ lock_dismiss()
    akira "{cps=20}...{nw}"
    $ unlock_dismiss()
    akira "...{fast}"

    show a k y oe cm angry onlayer askip

    $ lock_dismiss()
    akira "{cps=20}Fine... Seems like you hate me enough to ignore my words.{nw}"
    $ unlock_dismiss()
    akira "Fine... Seems like you hate me enough to ignore my words.{fast}"

    show a k y se om angry onlayer askip

    $ lock_dismiss()
    akira "{cps=20}Then... GET OUT OF HERE!{nw}"
    $ unlock_dismiss()
    akira "Then... GET OUT OF HERE!{fast}"

    $ persistent.tried_skip = True
    $ persistent.akira_ignored = True

    $ renpy.quit()


label akira_seen:

    show a k y se cm happy at bin(0.5) onlayer askip

    $ lock_dismiss()
    akira "{cps=25}Good~ Because I would kill you if you were trying to skip the story without reading it.{nw}"
    $ unlock_dismiss()
    akira "Good~ Because I would kill you if you were trying to skip the story without reading it.{fast}"

    show a k y se om mocking onlayer askip

    $ lock_dismiss()
    akira "{cps=20}Don't forget to read all the story at least once. Especially my words...{nw}"
    $ unlock_dismiss()
    akira "Don't forget to read all the story at least once. Especially my words...{fast}"

    show a k n oe cm happy onlayer askip

    $ lock_dismiss()
    akira "{cps=25}Let's continue to our {i}perfect{/i} story. Just be sure that I won't break the fourth wall again for this at least.{nw}"
    $ unlock_dismiss()
    akira "Let's continue to our {i}perfect{/i} story. Just be sure that I won't break the fourth wall again for this at least.{fast}"

    show a k n se cm happy onlayer askip

    $ lock_dismiss()
    akira "{cps=20}So please be a good [persistent.gender], my darling~{nw}"
    $ unlock_dismiss()
    akira "So please be a good [persistent.gender], my darling~{fast}"

    jump continue_story


label akira_boring:

    show a nk n oe cm neutral at bin(0.5) onlayer askip

    $ lock_dismiss()
    akira "{cps=20}Huh? Then why did you download this game in the first place?{nw}"
    $ unlock_dismiss()
    akira "Huh? Then why did you download this game in the first place?{fast}"

    show a nk n ce cm angry onlayer askip

    $ lock_dismiss()
    akira "{cps=25}Tch... Nevermind. If the story is boring you, go and delete this game. And leave the main character and me alone.{nw}"
    $ unlock_dismiss()
    akira "Tch... Nevermind. If the story is boring you, go and delete this game. And leave the main character and me alone.{fast}"
    
    show a nk n se cm angry onlayer askip

    $ lock_dismiss()
    akira "{cps=20}You are not one of us, you are not the person I {i}really{/i} love.{nw}"
    $ unlock_dismiss()
    akira "You are not one of us, you are not the person I {i}really{/i} love.{fast}"

    show a nk n ce cm angry_neutral onlayer askip

    $ lock_dismiss()
    akira "{cps=20}I'm going to enable the skip function now. After all, it doesn't matter anymore.{nw}"
    $ unlock_dismiss()
    akira "I'm going to enable the skip function now. After all, it doesn't matter anymore.{fast}"

    show a nk n ce cm verysad onlayer askip

    $ lock_dismiss()
    akira "{cps=20}You didn't love me, you {i}never{/i} loved me!{nw}"
    $ unlock_dismiss()
    akira "You didn't love me, you {i}never{/i} loved me!{fast}"

    show a nk n ce om angry onlayer askip

    $ lock_dismiss()
    akira "{cps=20}Screw you! *sob*{nw}"
    $ unlock_dismiss()
    akira "Screw you! *sob*{fast}"

    jump continue_story


label continue_story:

    window hide
    stop skipmusic fadeout 1
    show black2 onlayer askip zorder 15 with ff__
    hide a onlayer askip

    $ renpy.pause(1.0, hard=True)

    $ persistent.tried_skip = True
    $ monitor_skip_call_active = False
    $ config.allow_skipping = True
    $ settings_enabled = True
    $ history_enabled = True
    $ hide_sanity_force = False
    $ hide_enabled = True
    
    if persistent.lock_sanity_level:
        $ set_sanity(persistent.locked_sanity_percentage)
    else:
        $ set_sanity(save_sanity_percent)

    $ textbox = save_textbox_state

    if sanity >= 70:
        $ sanity_mode("high", 0)
    elif sanity >= 36:
        $ sanity_mode("medium", 0)
    else:
        $ sanity_mode("low", 0)

    $ renpy.music.set_volume(1.0, channel='music')

    if persistent.lock_atmosphere_level:
        $ set_atmosphere(persistent.locked_atmosphere_percentage)
    else:
        $ set_atmosphere(saved_atmosphere)

    hide black2 onlayer askip
    hide black
    show yandereblack onlayer yblack at transparent(1.0 - (sanity / 100))

    return
