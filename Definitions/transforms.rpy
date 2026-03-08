# This part defines how characters appear, disappear, and move on the screen (character animations).
# Appearing in the Screen
transform ss(x, ys=-0.12, ye=-0.02, zs=0.45, ze=0.49, t=0.2): # Character appears in speaking mode (slightly bigger size).
    alpha 0.0
    matrixcolor atm_matrix()

    parallel:
        xalign x - 0.0040
        yalign ys
        zoom zs
        linear t yalign ye zoom ze
    parallel:
        linear t alpha 1.0

    block: # These blocks are idle animations.
        linear 1.75 xalign x + 0.0040
        linear 1.75 xalign x - 0.0040
        repeat

transform si(x, ys=-0.12, ye=-0.09, zs=0.45, ze=0.47, t=0.2): # Character appears in idle mode (original size).
    alpha 0.0
    matrixcolor atm_matrix()

    parallel:
        xalign x - 0.0040
        yalign ys
        zoom zs
        linear t yalign ye zoom ze
    parallel:
        linear t alpha 1.0

    block:
        linear 1.75 xalign x + 0.0040
        linear 1.75 xalign x - 0.0040
        repeat

# Disappearing From the Screen
transform hs(ys=-0.02, ye=-0.12, zs=0.49, ze=0.45, t=0.2): # Hiding the speaking character.
    matrixcolor atm_matrix()
    alpha 1.0

    parallel:
        yalign ys
        zoom zs
        linear t yalign ye zoom ze
    parallel:
        linear t alpha 0.0

transform hi(ys=-0.09, ye=-0.12, zs=0.47, ze=0.45, t=0.2): # Hiding the idle character.
    matrixcolor atm_matrix()
    alpha 1.0

    parallel:
        yalign ys
        zoom zs
        linear t yalign ye zoom ze
    parallel:
        linear t alpha 0.0


# Making characters slightly grow when speaking and return to their normal size when they stop speaking.
transform bin(x): # When character starts speaking (character gets slightly bigger).
    yalign -0.09
    zoom 0.47
    alpha 1.0
    matrixcolor atm_matrix()
    linear 0.2 yalign -0.02 zoom 0.49 xalign x - 0.0040

    block:
        linear 1.75 xalign x + 0.0040
        linear 1.75 xalign x - 0.0040
        repeat

transform bout(x): # When character stops speaking (character gets its original size, idle mode).
    yalign -0.02
    zoom 0.49
    alpha 1.0
    matrixcolor atm_matrix()
    linear 0.2 yalign -0.09 zoom 0.47 xalign x - 0.0040

    block:
        linear 1.75 xalign x + 0.0040
        linear 1.75 xalign x - 0.0040
        repeat


# Movement-related transformations. Characters smoothly move between positions on the screen.
transform mcm(xs, xe, ys, ye, zs, ze, t=0.5): # Custom movement transform for exceptions.
    xalign xs - 0.0040
    yalign ys
    zoom zs
    alpha 1.0
    matrixcolor atm_matrix()
    linear t xalign xe yalign ye zoom ze

    block:
        linear 1.75 xalign xe + 0.004
        linear 1.75 xalign xe - 0.004
        repeat

transform mi(xs, xe, t=0.5): # Moving the idle character.
    xalign xs - 0.0040
    yalign -0.09
    zoom 0.47
    alpha 1.0
    matrixcolor atm_matrix()
    easein t xalign xe

    block:
        linear 1.75 xalign xe + 0.004
        linear 1.75 xalign xe - 0.004
        repeat

transform ms(xs, xe, t=0.5): # Moving the speaking character.
    xalign xs - 0.0040
    yalign -0.02
    zoom 0.49
    alpha 1.0
    matrixcolor atm_matrix()
    easein t xalign xe

    block:
        linear 1.75 xalign xe + 0.004
        linear 1.75 xalign xe - 0.004
        repeat

transform mbin(xs, xe, t=0.5): # Moving the idle character and starts speaking during the movement (character gets slightly bigger while moving).
    xalign xs - 0.0040
    yalign -0.09
    zoom 0.47
    alpha 1.0
    matrixcolor atm_matrix()
    easein t xalign xe yalign -0.02 zoom 0.49

    block:
        linear 1.75 xalign xe + 0.004
        linear 1.75 xalign xe - 0.004
        repeat

transform mbout(xs, xe, t=0.5): # Moving the speaking character and stops speaking during the movement (character gets its original size while moving).
    xalign xs - 0.0040
    yalign -0.02
    zoom 0.49
    alpha 1.0
    matrixcolor atm_matrix()
    easein t xalign xe yalign -0.09 zoom 0.47

    block:
        linear 1.75 xalign xe + 0.004
        linear 1.75 xalign xe - 0.004
        repeat


# Characters' jumping transformations. When used, character jumps a bit.
transform ji(x): # Jumping the idle character.
    yalign -0.09
    zoom 0.47
    alpha 1.0
    matrixcolor atm_matrix()
    linear 0.09 yalign -0.03 zoom 0.47 xalign x - 0.0040
    linear 0.09 yalign -0.09 zoom 0.47 xalign x - 0.0040

    block:
        linear 1.75 xalign x + 0.0040
        linear 1.75 xalign x - 0.0040
        repeat

transform js(x): # Jumping the speaking character.
    yalign -0.02
    zoom 0.49
    alpha 1.0
    matrixcolor atm_matrix()
    linear 0.09 yalign 0.04 zoom 0.49 xalign x - 0.0040
    linear 0.09 yalign -0.02 zoom 0.49 xalign x - 0.0040

    block:
        linear 1.75 xalign x + 0.0040
        linear 1.75 xalign x - 0.0040
        repeat

transform jss(x): # Jumping the idle character and starts speaking.
    yalign -0.09
    zoom 0.47
    alpha 1.0
    matrixcolor atm_matrix()
    linear 0.09 yalign 0.00 zoom 0.46 xalign x - 0.0040
    linear 0.09 yalign -0.02 zoom 0.49 xalign x - 0.0040

    block:
        linear 1.75 xalign x + 0.0040
        linear 1.75 xalign x - 0.0040
        repeat


# Main Menu Character Animations
# Showing the character in the main menu.
transform show_akira_menu:
    matrixcolor SaturationMatrix(1.2)
    xalign 1.710
    yalign -0.1
    zoom 0.47
    alpha 1.0
    easein 1.5 xalign 0.8


# Idle movement of the character in the main menu.
transform akira_menu:
    matrixcolor SaturationMatrix(1.2)
    xalign 0.8
    yalign -0.1
    zoom 0.47
    alpha 1.0

    block:
        ease 2.5 xalign 0.8 - 0.0250
        ease 2.5 xalign 0.8
        repeat


# Idle movement of the character in the music player.
transform akira_ost:
    matrixcolor SaturationMatrix(1.2)
    xalign 0.92
    yalign -0.1
    zoom 0.49
    alpha 1.0

    block:
        ease 2.5 xalign 0.92 - 0.035
        ease 2.5 xalign 0.92
        repeat


# Menu Image Animations
transform menugrid1: # First game menu gradient image (red moving light in the background).
    xalign 0.5
    yalign 0.5
    alpha 1.0

    block:
        easein 3.0 alpha 0.0
        easeout 3.0 alpha 1.0
        repeat

transform menugrid2: # Second game menu gradient image (red moving light in the background).
    xalign 0.5
    yalign 0.5
    alpha 0.0

    block:
        easeout 3.0 alpha 1.0
        easein 3.0 alpha 0.0
        repeat


# Screen Movements
transform salign(x=0.5, y=0.5, z=1.0):
    xalign x yalign y zoom z

transform smove(xs=0.5, xe=0.5, ys=0.5, ye=0.5, zs=1.0, ze=1.0, t=0.5):

    xalign xs - 0.0040 yalign ys zoom zs
    linear t xalign xe yalign ye zoom ze


# These transformations control screen and character shaking effects for dramatic scenes. The intensity and duration of the shaking can be customized.
transform sshake(x=0.5, y=0.5, z=1.0, duringzoom=1.04, duration=1, t=0.3): # Screen Shake Effect

    xalign x yalign y zoom z

    parallel:
            
        linear t / 8 xpos x + 0.02 ypos y - 0.02 zoom duringzoom
        linear t / 8 xpos x + 0.02 ypos y + 0.02 zoom duringzoom
        linear t / 8 xpos x - 0.02 ypos y + 0.02 zoom duringzoom
        linear t / 8 xpos x - 0.02 ypos y - 0.02 zoom duringzoom
        linear t / 8 xpos x + 0.02 ypos y - 0.02 zoom duringzoom
        linear t / 8 xpos x + 0.02 ypos y + 0.02 zoom duringzoom
        linear t / 8 xpos x - 0.02 ypos y + 0.02 zoom duringzoom
        linear t / 8 xpos x - 0.02 ypos y - 0.02 zoom duringzoom
        repeat duration

    parallel:

        pause (t * duration)
        linear t / 8 xalign x yalign y zoom z

transform cshake(x, y, z, duration=1, t=0.3): # Character Shake Effect

    xalign x yalign y zoom z 

    parallel:

        linear t / 8 xpos x + 0.02 ypos y - 0.02
        linear t / 8 xpos x + 0.02 ypos y + 0.02
        linear t / 8 xpos x - 0.02 ypos y + 0.02
        linear t / 8 xpos x - 0.02 ypos y - 0.02
        linear t / 8 xpos x + 0.02 ypos y - 0.02
        linear t / 8 xpos x + 0.02 ypos y + 0.02
        linear t / 8 xpos x - 0.02 ypos y + 0.02
        linear t / 8 xpos x - 0.02 ypos y - 0.02
        repeat duration

    parallel:
        pause (t * duration)
        linear t / 8 xalign x - 0.0040 yalign y zoom z

    block:
        linear 1.75 xalign x + 0.0040
        linear 1.75 xalign x - 0.0040
        repeat

transform xcshake(x, y, z, duration=1, t=0.3): # Character Shake Effect (Only X Line)

    xalign x yalign y zoom z

    parallel:

        linear t / 8 xpos x + 0.01
        linear t / 8 xpos x - 0.01
        linear t / 8 xpos x + 0.01
        linear t / 8 xpos x - 0.01
        linear t / 8 xpos x + 0.01
        linear t / 8 xpos x - 0.01
        linear t / 8 xpos x + 0.01
        linear t / 8 xpos x - 0.01
        repeat duration

    parallel:
        pause (t * duration)
        linear t / 8 xalign x - 0.0040 zoom z
    block:
        linear 1.75 xalign x + 0.0040
        linear 1.75 xalign x - 0.0040
        repeat


# Mini Transforms for Other Adjustments
transform middle:
    xalign 0.5
    yalign 0.5
    zoom 1.75

transform middle2:
    xalign 0.5
    yalign 0.5

transform zoom(zoom=1.0):
    zoom zoom

transform transparent(opacity=1.0):
    alpha opacity

transform saturation(saturation=1.0):
    matrixcolor SaturationMatrix(saturation)

transform show_dissolve_date:
    xalign 0.5
    yalign 0.26
    alpha 0.0
    linear 1.0 alpha 1.0

transform move_date:
    xalign 0.5
    yalign 0.26
    alpha 1.0
    linear 1.4 yalign 0.5

transform show_dissolve(time=0.5):
    alpha 0.0
    linear time alpha 1.0

transform hide_dissolve(time=0.5):
    alpha 1.0
    linear time alpha 0.0

transform show_slide_destiny:
    xpos 0.25
    ypos -0.1

    easein 0.8 xpos 0.0
    pause 6
    easeout 0.8 xpos 0.25

transform show_slide_achievement:
    xpos 0.25
    ypos -0.1

    easein 0.8 xpos 0.0
    pause 6
    easeout 0.8 xpos 0.25

transform show_slide_achievement2:
    xpos 0.25
    ypos +0.05

    easein 0.8 xpos 0.0
    pause 6
    easeout 0.8 xpos 0.25


# Other Transforms
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat

transform notify_appear:
    on show:
        alpha 0
        linear 0.25 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0

transform sanity_shake:
    xpos 0.94 ypos 0.113
    
    block:
        linear 0.03 xpos 0.936 ypos 0.112
        linear 0.03 xpos 0.937 ypos 0.112
        linear 0.03 xpos 0.937 ypos 0.113
        linear 0.03 xpos 0.936 ypos 0.113
        repeat

transform ostbg_move:
    xalign 1.0
    yalign 1.0
    linear 60 xalign 0.0 yalign 0.0
    repeat

transform credits_scroll:
    yalign -2.1
    xalign 0.5
    pause 1.5
    linear 45.0 yalign 3.1

transform credits_scroll_logo:
    yalign 1.0
    xalign 0.5
    alpha 0.0

    linear 1.5 alpha 1.0
    linear 45.0 yalign -3.7

transform atm_sun_behavior:
    function update_sun

transform atm_cloud_behavior:
    function update_cloud

transform atm_shift_chr:

    xalign 0.5
    yalign -0.09
    zoom 0.47
    matrixcolor SaturationMatrix(0.35) * ContrastMatrix(0.75) * BrightnessMatrix(-0.04)

    linear 2 matrixcolor SaturationMatrix(1.2) * ContrastMatrix(1.0) * BrightnessMatrix(0.0)

transform atm_shift_scene:

    matrixcolor SaturationMatrix(0.35) * ContrastMatrix(0.48) * BrightnessMatrix(-0.3)

    linear 2 matrixcolor SaturationMatrix(1.1) * ContrastMatrix(1.0) * BrightnessMatrix(0.0)

transform chapter_select_bg:

    zoom 0.5
    alpha 0.0
    yalign 0.5  
    xalign 0.5

    linear 0.7 zoom 1.0 alpha 1.25
    linear 0.7 zoom 1.5 alpha 0.0
    pause 0.4
    repeat

transform chapter_select_bg2:
    zoom 0.2
    alpha 0.0
    yalign 0.5
    xalign 0.5

    pause 0.8

    block:

        zoom 0.5
        alpha 0.0

        linear 0.7 zoom 1.0 alpha 1.25
        linear 0.7 zoom 1.5 alpha 0.0
        pause 0.4
        repeat

transform chapter_image:

    xalign 0.5
    yalign 0.2
    alpha 0.0
    zoom 1.2

    linear 0.5 alpha 1.0

transform title_show:

    xalign 0.5
    alpha 0.0

    pause 0.4

    linear 0.5 alpha 1.0

transform description_show:

    xalign 0.5
    alpha 0.0

    pause 0.8

    linear 0.5 alpha 1.0