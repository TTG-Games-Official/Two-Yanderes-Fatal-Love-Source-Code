transform atm_sky_color:
    alpha get_atm_sky_alpha()
    matrixcolor ContrastMatrix(2.0)
    
# Backgrounds - Potat0Master
image night = "backgrounds/Potat0Master/Night.webp"
image mc_room = "backgrounds/Potat0Master/MC Room.webp"
image school_hallway = "backgrounds/Potat0Master/School Hallway.webp"
image school_hallway_noon = "backgrounds/Potat0Master/School Hallway Noon.webp"
image school_hallway_11 = "backgrounds/Potat0Master/School Hallway 1-1.webp"
image school_hallway_noon_11 = "backgrounds/Potat0Master/School Hallway 1-1 Noon.webp"
image school_hallway_21 = "backgrounds/Potat0Master/School Hallway 2-1.webp"
image classroom_9am = "backgrounds/Potat0Master/Classroom 9 AM.webp"
image classroom_12pm = "backgrounds/Potat0Master/Classroom 12 PM.webp"
image classroom_4pm = "backgrounds/Potat0Master/Classroom 4 PM.webp"
image stairs = "backgrounds/Potat0Master/Stairs.webp"
image teachers_room = "backgrounds/Potat0Master/Room Entrance.webp"
image artclub = "backgrounds/Potat0Master/Art Club.webp"
image musicclub = "backgrounds/Potat0Master/Music Club.webp"
image town = "backgrounds/Potat0Master/Town.webp"

# Backgrounds - Belsartwork
image basement = "backgrounds/Belsartwork/Basement.webp"
image counselor_office = "backgrounds/Belsartwork/Counselor Office.webp"
image amusement_park = "backgrounds/Belsartwork/Amusement Park.webp"
image roller_coaster = "backgrounds/Belsartwork/Roller Coaster.webp"

# Backgrounds - Uncle Mugen
image front_school_intro = "backgrounds/Uncle Mugen/Front School/Front School.webp"
layeredimage front_school:

    always:
        "backgrounds/Uncle Mugen/Front School/Front School.webp"
    
    if persistent.atm_sky_color == "default":
        "backgrounds/Uncle Mugen/Front School/Front School High ATM.webp"
    
    if persistent.atm_sky_color == "default":
        "backgrounds/Uncle Mugen/Front School/Front School Low ATM.webp"
        at atm_sky_color

layeredimage behind_school:

    always:
        "backgrounds/Uncle Mugen/Behind School/Behind School.webp"
    
    if persistent.atm_sky_color == "default":
        "backgrounds/Uncle Mugen/Behind School/Behind School High ATM.webp"
    
    if persistent.atm_sky_color == "default":
        "backgrounds/Uncle Mugen/Behind School/Behind School Low ATM.webp"
        at atm_sky_color

image front_school_scary = "backgrounds/Uncle Mugen/Front School Scary.webp"
image science_lab = "backgrounds/Uncle Mugen/School Science Lab.webp"
image cafe = "backgrounds/Uncle Mugen/Cafe Memoria.webp"
image cafe_outside = "backgrounds/Uncle Mugen/Cafe Memoria Outside.webp"
image shower = "backgrounds/Uncle Mugen/Shower.webp"

# Backgrounds - Pandita Studio
layeredimage rooftop:

    always:
        "backgrounds/Pandita Studio/Rooftop/Rooftop.webp"
    
    if persistent.atm_sky_color == "default":
        "backgrounds/Pandita Studio/Rooftop/Rooftop High ATM.webp"
    
    if persistent.atm_sky_color == "default":
        "backgrounds/Pandita Studio/Rooftop/Rooftop Low ATM.webp"
        at atm_sky_color

image cafeteria = "backgrounds/Pandita Studio/Cafeteria.webp"

# Backgrounds - Noraneko Games
image bedroom_day = "backgrounds/Noraneko Games/Bedroom Day.webp"
image bedroom_night = "backgrounds/Noraneko Games/Bedroom Night.webp"
image livingroom_night = "backgrounds/Noraneko Games/Livingroom Night.webp"
image livingroom_day = "backgrounds/Noraneko Games/Livingroom Day.webp"
image kitchen = "backgrounds/Noraneko Games/Kitchen Day.webp"
image street_day = "backgrounds/Noraneko Games/Street Summer Day.webp"
image street_evening = "backgrounds/Noraneko Games/Street Summer Evening.webp"
image street_night = "backgrounds/Noraneko Games/Street Summer Night.webp"

# Backgrounds - Quark_Yifu
image shopping_mall = "backgrounds/Quark_Yifu/Shopping Mall.webp"


# Chapter Start Date Images
image day0_en = "images/Atmosphere/Date/English/11.webp"
image day1_en = "images/Atmosphere/Date/English/12.webp"
image day2_en = "images/Atmosphere/Date/English/13.webp"
image day3_en = "images/Atmosphere/Date/English/14.webp"
image day4_en = "images/Atmosphere/Date/English/15.webp"
image day5_en = "images/Atmosphere/Date/English/16.webp"
image day6_en = "images/Atmosphere/Date/English/17.webp"
image day7_en = "images/Atmosphere/Date/English/18.webp"
image day8_en = "images/Atmosphere/Date/English/19.webp"
image day9_en = "images/Atmosphere/Date/English/20.webp"
image day10_en = "images/Atmosphere/Date/English/21.webp"
image day11_en = "images/Atmosphere/Date/English/22.webp"
image day12_en = "images/Atmosphere/Date/English/23.webp"
image day13_en = "images/Atmosphere/Date/English/24.webp"
image day14_en = "images/Atmosphere/Date/English/25.webp"
image day15_en = "images/Atmosphere/Date/English/26.webp"
image day16_en = "images/Atmosphere/Date/English/27.webp"
image day17_en = "images/Atmosphere/Date/English/28.webp"
image day18_en = "images/Atmosphere/Date/English/29.webp"

image day0_tr = "images/Atmosphere/Date/Turkce/11.webp"
image day1_tr = "images/Atmosphere/Date/Turkce/12.webp"
image day2_tr = "images/Atmosphere/Date/Turkce/13.webp"
image day3_tr = "images/Atmosphere/Date/Turkce/14.webp"
image day4_tr = "images/Atmosphere/Date/Turkce/15.webp"
image day5_tr = "images/Atmosphere/Date/Turkce/16.webp"
image day6_tr = "images/Atmosphere/Date/Turkce/17.webp"
image day7_tr = "images/Atmosphere/Date/Turkce/18.webp"
image day8_tr = "images/Atmosphere/Date/Turkce/19.webp"
image day9_tr = "images/Atmosphere/Date/Turkce/20.webp"
image day10_tr = "images/Atmosphere/Date/Turkce/21.webp"
image day11_tr = "images/Atmosphere/Date/Turkce/22.webp"
image day12_tr = "images/Atmosphere/Date/Turkce/23.webp"
image day13_tr = "images/Atmosphere/Date/Turkce/24.webp"
image day14_tr = "images/Atmosphere/Date/Turkce/25.webp"
image day15_tr = "images/Atmosphere/Date/Turkce/26.webp"
image day16_tr = "images/Atmosphere/Date/Turkce/27.webp"
image day17_tr = "images/Atmosphere/Date/Turkce/28.webp"
image day18_tr = "images/Atmosphere/Date/Turkce/29.webp"

image day0_es = "images/Atmosphere/Date/Espanol/11.webp"
image day1_es = "images/Atmosphere/Date/Espanol/12.webp"
image day2_es = "images/Atmosphere/Date/Espanol/13.webp"
image day3_es = "images/Atmosphere/Date/Espanol/14.webp"
image day4_es = "images/Atmosphere/Date/Espanol/15.webp"
image day5_es = "images/Atmosphere/Date/Espanol/16.webp"
image day6_es = "images/Atmosphere/Date/Espanol/17.webp"
image day7_es = "images/Atmosphere/Date/Espanol/18.webp"
image day8_es = "images/Atmosphere/Date/Espanol/19.webp"
image day9_es = "images/Atmosphere/Date/Espanol/20.webp"
image day10_es = "images/Atmosphere/Date/Espanol/21.webp"
image day11_es = "images/Atmosphere/Date/Espanol/22.webp"
image day12_es = "images/Atmosphere/Date/Espanol/23.webp"
image day13_es = "images/Atmosphere/Date/Espanol/24.webp"
image day14_es = "images/Atmosphere/Date/Espanol/25.webp"
image day15_es = "images/Atmosphere/Date/Espanol/26.webp"
image day16_es = "images/Atmosphere/Date/Espanol/27.webp"
image day17_es = "images/Atmosphere/Date/Espanol/28.webp"
image day18_es = "images/Atmosphere/Date/Espanol/29.webp"

image day0_ru = "images/Atmosphere/Date/Russian/11.webp"
image day1_ru = "images/Atmosphere/Date/Russian/12.webp"
image day2_ru = "images/Atmosphere/Date/Russian/13.webp"
image day3_ru = "images/Atmosphere/Date/Russian/14.webp"
image day4_ru = "images/Atmosphere/Date/Russian/15.webp"
image day5_ru = "images/Atmosphere/Date/Russian/16.webp"
image day6_ru = "images/Atmosphere/Date/Russian/17.webp"
image day7_ru = "images/Atmosphere/Date/Russian/18.webp"
image day8_ru = "images/Atmosphere/Date/Russian/19.webp"
image day9_ru = "images/Atmosphere/Date/Russian/20.webp"
image day10_ru = "images/Atmosphere/Date/Russian/21.webp"
image day11_ru = "images/Atmosphere/Date/Russian/22.webp"
image day12_ru = "images/Atmosphere/Date/Russian/23.webp"
image day13_ru = "images/Atmosphere/Date/Russian/24.webp"
image day14_ru = "images/Atmosphere/Date/Russian/25.webp"
image day15_ru = "images/Atmosphere/Date/Russian/26.webp"
image day16_ru = "images/Atmosphere/Date/Russian/27.webp"
image day17_ru = "images/Atmosphere/Date/Russian/28.webp"
image day18_ru = "images/Atmosphere/Date/Russian/29.webp"


# Achievement Notification Images
image ac_forever_yours_en = "images/Achievements/English/Forever Yours.webp"
image ac_wrong_love_story_en = "images/Achievements/English/Wrong Love Story.webp"
image ac_just_a_student_en = "images/Achievements/English/Just a Student.webp"
image ac_perfect_innocence_en = "images/Achievements/English/Perfect Innocence.webp"
image ac_cuffed_and_loved_en = "images/Achievements/English/Cuffed and Loved.webp"
image ac_abnormal_panic_en = "images/Achievements/English/Abnormal Panic.webp"
image ac_too_careless_en = "images/Achievements/English/Too Careless.webp"
image ac_behind_the_mask_en = "images/Achievements/English/Behind the Mask.webp"
image ac_rickrolled_en = "images/Achievements/English/Rickrolled.webp"
image ac_are_you_trying_to_skip_en = "images/Achievements/English/Are You Trying to Skip.webp"
image ac_this_is_her_game_en = "images/Achievements/English/This is Her Game.webp"
image ac_she_is_always_watching_en = "images/Achievements/English/She is Always Watching.webp"
image ac_loyal_player_en = "images/Achievements/English/Loyal Player.webp"

image ac_forever_yours_tr = "images/Achievements/Turkce/Forever Yours.webp"
image ac_wrong_love_story_tr = "images/Achievements/Turkce/Wrong Love Story.webp"
image ac_just_a_student_tr = "images/Achievements/Turkce/Just a Student.webp"
image ac_perfect_innocence_tr = "images/Achievements/Turkce/Perfect Innocence.webp"
image ac_cuffed_and_loved_tr = "images/Achievements/Turkce/Cuffed and Loved.webp"
image ac_abnormal_panic_tr = "images/Achievements/Turkce/Abnormal Panic.webp"
image ac_too_careless_tr = "images/Achievements/Turkce/Too Careless.webp"
image ac_behind_the_mask_tr = "images/Achievements/Turkce/Behind the Mask.webp"
image ac_rickrolled_tr = "images/Achievements/Turkce/Rickrolled.webp"
image ac_are_you_trying_to_skip_tr = "images/Achievements/Turkce/Are You Trying to Skip.webp"
image ac_this_is_her_game_tr = "images/Achievements/Turkce/This is Her Game.webp"
image ac_she_is_always_watching_tr = "images/Achievements/Turkce/She is Always Watching.webp"
image ac_loyal_player_tr = "images/Achievements/Turkce/Loyal Player.webp"

image ac_forever_yours_es = "images/Achievements/Espanol/Forever Yours.webp"
image ac_wrong_love_story_es = "images/Achievements/Espanol/Wrong Love Story.webp"
image ac_just_a_student_es = "images/Achievements/Espanol/Just a Student.webp"
image ac_perfect_innocence_es = "images/Achievements/Espanol/Perfect Innocence.webp"
image ac_cuffed_and_loved_es = "images/Achievements/Espanol/Cuffed and Loved.webp"
image ac_abnormal_panic_es = "images/Achievements/Espanol/Abnormal Panic.webp"
image ac_too_careless_es = "images/Achievements/Espanol/Too Careless.webp"
image ac_behind_the_mask_es = "images/Achievements/Espanol/Behind the Mask.webp"
image ac_rickrolled_es = "images/Achievements/Espanol/Rickrolled.webp"
image ac_are_you_trying_to_skip_es = "images/Achievements/Espanol/Are You Trying to Skip.webp"
image ac_this_is_her_game_es = "images/Achievements/Espanol/This is Her Game.webp"
image ac_she_is_always_watching_es = "images/Achievements/Espanol/She is Always Watching.webp"
image ac_loyal_player_es = "images/Achievements/Espanol/Loyal Player.webp"

image ac_forever_yours_ru = "images/Achievements/Russian/Forever Yours.webp"
image ac_wrong_love_story_ru = "images/Achievements/Russian/Wrong Love Story.webp"
image ac_just_a_student_ru = "images/Achievements/Russian/Just a Student.webp"
image ac_perfect_innocence_ru = "images/Achievements/Russian/Perfect Innocence.webp"
image ac_cuffed_and_loved_ru = "images/Achievements/Russian/Cuffed and Loved.webp"
image ac_abnormal_panic_ru = "images/Achievements/Russian/Abnormal Panic.webp"
image ac_too_careless_ru = "images/Achievements/Russian/Too Careless.webp"
image ac_behind_the_mask_ru = "images/Achievements/Russian/Behind the Mask.webp"
image ac_rickrolled_ru = "images/Achievements/Russian/Rickrolled.webp"
image ac_are_you_trying_to_skip_ru = "images/Achievements/Russian/Are You Trying to Skip.webp"
image ac_she_is_always_watching_ru = "images/Achievements/Russian/She is Always Watching.webp"
image ac_loyal_player_ru = "images/Achievements/Russian/Loyal Player.webp"


# Destiny Change Indicator and Hint Notification Images
image destroy_everything_en = "images/Destiny/English/Destroy Everything.webp"
image wash_blood_en = "images/Destiny/English/Wash Blood.webp"
image criminal_en = "images/Destiny/English/Criminal.webp"
image non_criminal_en = "images/Destiny/English/No Criminal.webp"
image akira_cat_en = "images/Destiny/English/Cat Akira Approved.webp"
image akira_normal_en = "images/Destiny/English/Cat Akira Denied.webp"
image suspended_en = "images/Destiny/English/Suspended.webp"
image not_suspended_en = "images/Destiny/English/Not Suspended.webp"
image caught_blood_en = "images/Destiny/English/Visibly Bloody.webp"
image caught_insane_en = "images/Destiny/English/Visibly Insane.webp"
image silent_hint_en = "images/Destiny/English/Silent Hint.webp"
image suspect_level_en = "images/Destiny/English/Sus Level.webp"

image destroy_everything_tr = "images/Destiny/Turkce/Destroy Everything.webp"
image wash_blood_tr = "images/Destiny/Turkce/Wash Blood.webp"
image criminal_tr = "images/Destiny/Turkce/Criminal.webp"
image non_criminal_tr = "images/Destiny/Turkce/No Criminal.webp"
image akira_cat_tr = "images/Destiny/Turkce/Cat Akira Approved.webp"
image akira_normal_tr = "images/Destiny/Turkce/Cat Akira Denied.webp"
image suspended_tr = "images/Destiny/Turkce/Suspended.webp"
image not_suspended_tr = "images/Destiny/Turkce/Not Suspended.webp"
image caught_blood_tr = "images/Destiny/Turkce/Visibly Bloody.webp"
image caught_insane_tr = "images/Destiny/Turkce/Visibly Insane.webp"
image silent_hint_tr = "images/Destiny/Turkce/Silent Hint.webp"
image suspect_level_tr = "images/Destiny/Turkce/Sus Level.webp"

image destroy_everything_es = "images/Destiny/Espanol/Destroy Everything.webp"
image wash_blood_es = "images/Destiny/Espanol/Wash Blood.webp"
image criminal_es = "images/Destiny/Espanol/Criminal.webp"
image non_criminal_es = "images/Destiny/Espanol/No Criminal.webp"
image akira_cat_es = "images/Destiny/Espanol/Cat Akira Approved.webp"
image akira_normal_es = "images/Destiny/Espanol/Cat Akira Denied.webp"
image suspended_es = "images/Destiny/Espanol/Suspended.webp"
image not_suspended_es = "images/Destiny/Espanol/Not Suspended.webp"
image caught_blood_es = "images/Destiny/Espanol/Visibly Bloody.webp"
image caught_insane_es = "images/Destiny/Espanol/Visibly Insane.webp"
image silent_hint_es = "images/Destiny/Espanol/Silent Hint.webp"
image suspect_level_es = "images/Destiny/Espanol/Sus Level.webp"

image destroy_everything_ru = "images/Destiny/Russian/Destroy Everything.webp"
image wash_blood_ru = "images/Destiny/Russian/Wash Blood.webp"
image criminal_ru = "images/Destiny/Russian/Criminal.webp"
image non_criminal_ru = "images/Destiny/Russian/No Criminal.webp"
image akira_cat_ru = "images/Destiny/Russian/Cat Akira Approved.webp"
image akira_normal_ru = "images/Destiny/Russian/Cat Akira Denied.webp"
image suspended_ru = "images/Destiny/Russian/Suspended.webp"
image not_suspended_ru = "images/Destiny/Russian/Not Suspended.webp"
image caught_blood_ru = "images/Destiny/Russian/Visibly Bloody.webp"
image caught_insane_ru = "images/Destiny/Russian/Visibly Insane.webp"
image silent_hint_ru = "images/Destiny/Russian/Silent Hint.webp"
image suspect_level_ru = "images/Destiny/Russian/Sus Level.webp"


# Main Menu and GUI Images
image logos = "mainmenu/Logos.webp"
image menulogo = "mainmenu/menugamelogo.webp"
image previous_save = "gui/overlay/previous_save_bg.webp"


# Solid Color Images
image white = Solid('#fff')
image black = Solid('#000')
image black2 = Solid('#000')
image red = Solid("#ff0000")


# Side Character Images
image girl1 = "othercharacters/girl/student/1.webp"
image girl2 = "othercharacters/girl/student/2.webp"
image girl3 = "othercharacters/girl/student/3.webp"
image girl4 = "othercharacters/girl/student/4.webp"
image girl5 = "othercharacters/girl/student/5.webp"
image girl6 = "othercharacters/girl/student/6.webp"
image girl7 = "othercharacters/girl/student/7.webp"
image girl8 = "othercharacters/girl/student/8.webp"
image girl9 = "othercharacters/girl/student/9.webp"
image girl10 = "othercharacters/girl/student/10.webp"
image girl11 = "othercharacters/girl/adult/1.webp"
image girl12 = "othercharacters/girl/adult/2.webp"
image girl13 = "othercharacters/girl/adult/3.webp"
image girl14 = "othercharacters/girl/adult/2.webp"

image boy1 = "othercharacters/boy/1.webp"
image boy2 = "othercharacters/boy/2.webp"
image boy3 = "othercharacters/boy/3.webp"
image boy4 = "othercharacters/boy/4.webp"
image boy5 = "othercharacters/boy/5.webp"
image boy6 = "othercharacters/boy/6.webp"
image boy7 = "othercharacters/boy/7.webp"
image boy8 = "othercharacters/boy/8.webp"
image boy9 = "othercharacters/boy/9.webp"
image boy10 = "othercharacters/boy/10.webp"

image mother = "othercharacters/Mother.webp"
image father = "othercharacters/Father.webp"

image cat = Transform("characters/Cat.webp")
image kitten = Transform("characters/Kitten.webp")


# Atmosphere and Overlay Images
image yandereblack = "images/Yandere Effect.webp"
image vignette = "images/Vignette.webp"

image atm_vignette = "images/Atmosphere/ATM Vignette.webp"
image atm_sun = "images/Atmosphere/ATM Sun.webp"
image atm_cloud = "images/Atmosphere/ATM Cloud.webp"
image pink_bg = "images/Atmosphere/Pink BG.webp"

# Say Screen Indicator
image ctc:

    xalign 0.8 yalign 0.972 xoffset -6 alpha 0.8 zoom 0.63 subpixel True

    "gui/overlay/ctc.webp"
    
    block:
        linear 0.5 xoffset 0
        linear 0.5 xoffset -6
        repeat

# Animated Effect Images
image tvparasite = Animation(
    "images/TV Parasite/1.webp", 0.05,
    "images/TV Parasite/2.webp", 0.05,
    "images/TV Parasite/3.webp", 0.05,
    "images/TV Parasite/4.webp", 0.05,
)

image speedeffect = Animation(
    "images/Speed Effect/1.webp", 0.075,
    "images/Speed Effect/2.webp", 0.075,
)

# Music Player Images
image ostbg_yandere = "images/OST Screen/OST Video BG Yandere.webp"
image ostbg_normal = "images/OST Screen/OST Video BG Normal.webp"
