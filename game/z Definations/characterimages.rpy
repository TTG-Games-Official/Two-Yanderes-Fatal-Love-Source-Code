# Clara
layeredimage c:

    always:
        "characters/clara/body.webp"

    group eyes:

        attribute open default:

            Animation(
                "characters/clara/eyes.webp", 3.8,
                "characters/clara/eyelashes.webp", 0.1
            )

        attribute o:

            Animation(
                "characters/clara/eyes.webp", 3.8,
                "characters/clara/eyelashes.webp", 0.1
            )
            
        attribute c:
            "characters/clara/eyelashes.webp"

        attribute co:
            "characters/clara/eyelashes.webp"

    group mouth:

        attribute neutral default:
            "characters/clara/closed_mouth/neutral.webp"

        attribute sad:
            "characters/clara/closed_mouth/sad.webp"
            when not o and not co

        attribute sad:
            "characters/clara/open_mouth/sad.webp"
            when o or co

        attribute verysad:
            "characters/clara/closed_mouth/verysad.webp"
            when not o and not co

        attribute verysad:
            "characters/clara/open_mouth/verysad.webp"
            when o or co

        attribute angry:
            "characters/clara/closed_mouth/angry.webp"
            when not o and not co

        attribute angry:
            "characters/clara/open_mouth/angry.webp"
            when o or co

        attribute scared:
            "characters/clara/open_mouth/scared.webp"


# Police
layeredimage mpolice:

    always:
        "characters/police/male_police_body.webp"

    group eyes:

        attribute open default:

            Animation(
                "characters/police/male_police_normal.webp", 4.5,
                "characters/police/male_police_closed.webp", 0.1
            )

        attribute c:
            "characters/police/male_police_closed.webp"

layeredimage fpolice:

    always:
        "characters/police/female_police_body.webp"

    group eyes:

        attribute open default:

            Animation(
                "characters/police/female_police_normal.webp", 4.0,
                "characters/police/female_police_closed.webp", 0.1
            )

        attribute c:
            "characters/police/female_police_closed.webp"


# Guidance Counselor
layeredimage counselor:

    always:
        "characters/counselor/body.webp"

    group expression:
        attribute normal default null
        attribute angry null

    group mouth:
        attribute base default null
        attribute o null
        attribute c null
        attribute co null

    always:
        Animation(
            "characters/counselor/normal.webp", 4.5,
            "characters/counselor/normal_closed.webp", 0.1
        )
        when normal and base

    always:
        Animation(
            "characters/counselor/normal_open.webp", 4.5,
            "characters/counselor/normal_open_closed.webp", 0.1
        )
        when normal and o

    always:
        "characters/counselor/normal_closed.webp"
        when normal and c

    always:
        "characters/counselor/normal_open_closed.webp"
        when normal and co

    always:
        Animation(
            "characters/counselor/angry.webp", 4.5,
            "characters/counselor/angry_closed.webp", 0.1
        )
        when angry and base

    always:
        Animation(
            "characters/counselor/angry_open.webp", 4.5,
            "characters/counselor/angry_open_closed.webp", 0.1
        )
        when angry and o

    always:
        "characters/counselor/angry_closed.webp"
        when angry and c

    always:
        "characters/counselor/angry_open_closed.webp"
        when angry and co


# Frame Murder Girl
layeredimage g:

    always:
        "characters/frame murder girl/body.webp"

    group eyes:

        attribute open default:

            Animation(
                "characters/frame murder girl/eyes.webp", 3.5,
                "characters/frame murder girl/eyelashes_sad.webp", 0.1
            )

        attribute o:

            Animation(
                "characters/frame murder girl/eyes.webp", 3.5,
                "characters/frame murder girl/eyelashes_sad.webp", 0.1
            )

        attribute c:
            "characters/frame murder girl/eyelashes_sad.webp"

        attribute co:
            "characters/frame murder girl/eyelashes_sad.webp"

    group mouth:
    
        attribute sad default:
            "characters/frame murder girl/closed_mouth/sad.webp"
            when not o and not co

        attribute sad:
            "characters/frame murder girl/open_mouth/sad.webp"
            when o or co

        attribute shy:
            "characters/frame murder girl/closed_mouth/shy.webp"

        attribute verysad:
            "characters/frame murder girl/closed_mouth/verysad.webp"
            when not o and not co

        attribute verysad:
            "characters/frame murder girl/open_mouth/verysad.webp"
            when o or co

        attribute surprised:
            "characters/frame murder girl/open_mouth/surprised.webp"
            when o or co


# Akira

# Prefixes:
# a = Akira
# g = With Gloves (No Gloves if there is no "g" prefix.)
# b = Bloody Character (Normal Character if there is no "b" prefix.)

# nk = No Knife (Empty Hand)
# k = Knife
# bk = Bloody Knife

# n = Normal (No Shadow on the Forehead)
# y = Yandere (Shadow on the Forehead)

# oe = Open Eyes
# ce = Closed Eyes
# se = Small Eyes (Yandere Eyes)

# cm = Closed Mouth
# om = Open Mouth

layeredimage a:

    always:
        "characters/akira/body.webp"

    group gloves:

        attribute no_g default null

        attribute g:
            "characters/akira/gloves.webp"

    group blood_stains:

        attribute no_b default null

        attribute b:
            "characters/akira/blood.webp"

    group weapon:

        attribute nk default null

        attribute k:
            "characters/akira/knife.webp"
        attribute bk:
            "characters/akira/bloody_knife.webp"

    group mood:

        attribute n default null
        attribute y null

    group eyes:

        attribute oe default:

            Animation(
                "characters/akira/normal_eyes.webp", 3.4,
                "characters/akira/eyelashes_sad.webp", 0.1
            )
            when n

        attribute oe:

            Animation(
                "characters/akira/no_highlight_eyes.webp", 3.4,
                "characters/akira/eyelashes_sad.webp", 0.1
            )
            when y

        attribute se:

            Animation(
                "characters/akira/small_eyes.webp", 3.4,
                "characters/akira/eyelashes_sad.webp", 0.1
            )

        attribute ce:

            "characters/akira/eyelashes_happy.webp"
            when happy

        attribute ce:

            "characters/akira/eyelashes_sad.webp"
            when not happy

    attribute y:

        Animation(
            "characters/akira/forehead_dark_open_eyes.webp", 3.4,
            "characters/akira/forehead_dark_closed_eyes.webp", 0.1
        )
        when oe or se

    attribute y:
        "characters/akira/forehead_dark_closed_eyes.webp"
        when ce

    group mouth:

        attribute cm default null
        attribute om null

    group expression:

        attribute happy default:
            "characters/akira/expressions/closed_mouth/happy.webp"
            when cm

        attribute happy:
            "characters/akira/expressions/open_mouth/happy.webp"
            when om

        attribute neutral:
            "characters/akira/expressions/closed_mouth/neutral.webp"
            when cm

        attribute neutral:
            "characters/akira/expressions/open_mouth/neutral.webp"
            when om

        attribute sad:
            "characters/akira/expressions/closed_mouth/sad.webp"
            when cm

        attribute sad:
            "characters/akira/expressions/open_mouth/sad.webp"
            when om

        attribute surprised:
            "characters/akira/expressions/closed_mouth/surprised.webp"
            when cm

        attribute surprised:
            "characters/akira/expressions/open_mouth/surprised.webp"
            when om

        attribute mocking:
            "characters/akira/expressions/closed_mouth/mocking.webp"
            when cm

        attribute mocking:
            "characters/akira/expressions/open_mouth/mocking.webp"
            when om

        attribute angry_neutral:
            "characters/akira/expressions/closed_mouth/angry_neutral.webp"
            when cm

        attribute angry_neutral:
            "characters/akira/expressions/open_mouth/angry_neutral.webp"
            when om

        attribute angry:
            "characters/akira/expressions/closed_mouth/angry.webp"
            when cm

        attribute angry:
            "characters/akira/expressions/open_mouth/angry.webp"
            when om

        attribute shy:
            "characters/akira/expressions/closed_mouth/shy.webp"
            when cm

        attribute shy:
            "characters/akira/expressions/open_mouth/shy.webp"
            when om

        attribute verysad_neutral:
            "characters/akira/expressions/closed_mouth/verysad_neutral.webp"
            when cm

        attribute verysad_neutral:
            "characters/akira/expressions/open_mouth/verysad_neutral.webp"
            when om

        attribute verysad:
            "characters/akira/expressions/closed_mouth/verysad.webp"
            when cm

        attribute verysad:
            "characters/akira/expressions/open_mouth/verysad.webp"
            when om

    if akira_cat:
        "characters/akira/cat_ears.webp"