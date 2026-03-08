# This section defines all background music tracks used in the game.
# Incompetech
define thatzenmoment = "<loop 5.019>audio/music/Incompetech/That Zen Moment.opus"
define stay_the_course = "<loop 0.0>audio/music/Incompetech/Stay the Course.opus"

# Pixabay
define sound_of_sea = "<loop 0.0>audio/music/Pixabay/Sound of the Sea.opus"
define freedom = "<loop 33.075>audio/music/Pixabay/Freedom.opus"
define config.main_menu_music = "<loop 0.0>audio/music/Pixabay/My First Love.opus"
define scaryhorror = "<loop 9.613>audio/music/Pixabay/Scary Horror Music.opus"
define myfirstlove = "<loop 0.0>audio/music/Pixabay/My First Love.opus"

# TTG Games
define corpse_panic = "<loop 0.0>audio/music/TTG Games/Corpse Panic.opus"
define arrest_panic = "<loop 0.0>audio/music/TTG Games/Arrest Panic.opus"
define unfixable_pain = "<loop 0.0>audio/music/TTG Games/Unfixable Pain.opus"

define schoolday_h_h = "<loop 0.0>audio/music/TTG Games/Schoolday/Schoolday Normal ATM High Sanity.opus"
define schoolday_h_m = "<loop 0.0>audio/music/TTG Games/Schoolday/Schoolday Normal ATM Medium Sanity.opus"
define schoolday_h_l = "<loop 0.0>audio/music/TTG Games/Schoolday/Schoolday Normal ATM Low Sanity.opus"
define schoolday_m_h = "<loop 0.0>audio/music/TTG Games/Schoolday/Schoolday Medium ATM High Sanity.opus"
define schoolday_m_m = "<loop 0.0>audio/music/TTG Games/Schoolday/Schoolday Medium ATM Medium Sanity.opus"
define schoolday_m_l = "<loop 0.0>audio/music/TTG Games/Schoolday/Schoolday Medium ATM Low Sanity.opus"
define schoolday_l_h = "<loop 0.0>audio/music/TTG Games/Schoolday/Schoolday Low ATM High Sanity.opus"
define schoolday_l_m = "<loop 0.0>audio/music/TTG Games/Schoolday/Schoolday Low ATM Medium Sanity.opus"
define schoolday_l_l = "<loop 0.0>audio/music/TTG Games/Schoolday/Schoolday Low ATM Low Sanity.opus"

define echoesoflove_h_h = "<loop 0.0>audio/music/TTG Games/Echoes of Love/Echoes of Love Normal ATM High Sanity.opus"
define echoesoflove_h_m = "<loop 0.0>audio/music/TTG Games/Echoes of Love/Echoes of Love Normal ATM Medium Sanity.opus"
define echoesoflove_h_l = "<loop 0.0>audio/music/TTG Games/Echoes of Love/Echoes of Love Normal ATM Low Sanity.opus"
define echoesoflove_l_h = "<loop 0.0>audio/music/TTG Games/Echoes of Love/Echoes of Love Low ATM High Sanity.opus"
define echoesoflove_l_m = "<loop 0.0>audio/music/TTG Games/Echoes of Love/Echoes of Love Low ATM Medium Sanity.opus"
define echoesoflove_l_l = "<loop 0.0>audio/music/TTG Games/Echoes of Love/Echoes of Love Low ATM Low Sanity.opus"

define evening_glow_h_h = "<loop 0.0>audio/music/TTG Games/Evening Glow/Evening Glow High Sanity.opus"
define evening_glow_h_m = "<loop 0.0>audio/music/TTG Games/Evening Glow/Evening Glow Medium Sanity.opus"
define evening_glow_h_l = "<loop 0.0>audio/music/TTG Games/Evening Glow/Evening Glow Low Sanity.opus"

init python:

    global atmosphere
    global ignore_atm

    def play_music(musicname, fadein=0):
        
        if ignore_atm:
            check_atm = 100 
        else:
            check_atm = atmosphere

        if musicname == "evening_glow":
            if check_atm >= 0:
                renpy.music.play(evening_glow_h_h, channel="hsanity", loop=True, fadein=fadein)
                renpy.music.play(evening_glow_h_m, channel="msanity", loop=True, fadein=fadein)
                renpy.music.play(evening_glow_h_l, channel="lsanity", loop=True, fadein=fadein)

        elif musicname == "schoolday":
            if check_atm > 67:
                renpy.music.play(schoolday_h_h, channel="hsanity", loop=True, fadein=fadein)
                renpy.music.play(schoolday_h_m, channel="msanity", loop=True, fadein=fadein)
                renpy.music.play(schoolday_h_l, channel="lsanity", loop=True, fadein=fadein)
            elif check_atm > 33:
                renpy.music.play(schoolday_m_h, channel="hsanity", loop=True, fadein=fadein)
                renpy.music.play(schoolday_m_m, channel="msanity", loop=True, fadein=fadein)
                renpy.music.play(schoolday_m_l, channel="lsanity", loop=True, fadein=fadein)
            else:
                renpy.music.play(schoolday_l_h, channel="hsanity", loop=True, fadein=fadein)
                renpy.music.play(schoolday_l_m, channel="msanity", loop=True, fadein=fadein)
                renpy.music.play(schoolday_l_l, channel="lsanity", loop=True, fadein=fadein)

        elif musicname == "echoes_of_love":
            if check_atm > 50:
                renpy.music.play(echoesoflove_h_h, channel="hsanity", loop=True, fadein=fadein)
                renpy.music.play(echoesoflove_h_m, channel="msanity", loop=True, fadein=fadein)
                renpy.music.play(echoesoflove_h_l, channel="lsanity", loop=True, fadein=fadein)
            else:
                renpy.music.play(echoesoflove_l_h, channel="hsanity", loop=True, fadein=fadein)
                renpy.music.play(echoesoflove_l_m, channel="msanity", loop=True, fadein=fadein)
                renpy.music.play(echoesoflove_l_l, channel="lsanity", loop=True, fadein=fadein)

        else:
            pass


# This section defines the sound effects used in the game.
# TTG Games
define syringe = "audio/sfx/TTG Games/Syringe Inject.opus"
define deskhit = "audio/sfx/TTG Games/Fierce Desk Hit.opus"
define yanderescary = "audio/sfx/TTG Games/Yandere Scary.opus"
define caught = "audio/sfx/TTG Games/Caught.opus"

define click = "audio/sfx/TTG Games/Button Click Sound.opus"
define click_echo = "audio/sfx/TTG Games/Button Click Sound Echo.opus"

define stab = "audio/sfx/TTG Games/Multiple Stabs.opus"
define stab_echo = "audio/sfx/TTG Games/Multiple Stabs Echo.opus"

define clothrustle = "audio/sfx/TTG Games/Cloth Rustle.opus"
define clothrustle_echo = "audio/sfx/TTG Games/Cloth Rustle Echo.opus"

define girl_scream = "audio/sfx/TTG Games/Girl Scream 1.opus"
define girl_scream_echo = "audio/sfx/TTG Games/Girl Scream 1 Echo.opus"
define girl_scream2 = "audio/sfx/TTG Games/Girl Scream 2.opus"
define girl_scream2_echo = "audio/sfx/TTG Games/Girl Scream 2 Echo.opus"

define boy_scream = "audio/sfx/TTG Games/Boy Scream 1.opus"
define boy_scream_echo = "audio/sfx/TTG Games/Boy Scream 1 Echo.opus"
define boy_scream2 = "audio/sfx/TTG Games/Boy Scream 2.opus"
define boy_scream2_echo = "audio/sfx/TTG Games/Boy Scream 2 Echo.opus"
define boy_scream3 = "audio/sfx/TTG Games/Boy Scream 3.opus"
define boy_scream3_echo = "audio/sfx/TTG Games/Boy Scream 3 Echo.opus"
define boy_scream4 = "audio/sfx/TTG Games/Boy Scream 4.opus"
define boy_scream4_echo = "audio/sfx/TTG Games/Boy Scream 4 Echo.opus"

define yboy_laugh = "audio/sfx/TTG Games/Yandere Boy Laugh.opus"
define yboy_laugh_echo = "audio/sfx/TTG Games/Yandere Boy Laugh Echo.opus"


# Pixabay
define ygirl_laugh = "audio/sfx/Pixabay/Yandere Girl Laugh.opus"
define ygirl_laugh_echo = "audio/sfx/Pixabay/Yandere Girl Laugh Echo.opus"
define giggle = "audio/sfx/Pixabay/Girl Giggle.opus"

define paper =  "audio/sfx/Pixabay/Paper.opus"
define blanket = "audio/sfx/Pixabay/Blanket Rustle.opus"
define walk = "audio/sfx/Pixabay/Footsteps Walk.opus"
define knife_grab = "audio/sfx/Pixabay/Knife Grab.opus"
define tvparasite = "audio/sfx/Pixabay/TV Parasite.opus"
define slap_hands = "audio/sfx/Pixabay/Slap Hands.opus"
define incinerator = "audio/sfx/Pixabay/Incinerator Start.opus"
define bell = "audio/sfx/Pixabay/School Bell.opus"
define crash = "audio/sfx/Pixabay/Car Crash.opus"

define run = "audio/sfx/Pixabay/Footsteps Run.opus"
define run_echo = "audio/sfx/Pixabay/Footsteps Run Echo.opus"

define cat_meow_1 = "audio/sfx/Pixabay/Cat Meow 1.opus"
define cat_meow_2 = "audio/sfx/Pixabay/Cat Meow 2.opus"
define cat_meow_3 = "audio/sfx/Pixabay/Cat Meow 3.opus"
define cat_meow_4 = "audio/sfx/Pixabay/Cat Meow 4.opus"

define cat_hiss = "audio/sfx/Pixabay/Cat Hiss.opus"