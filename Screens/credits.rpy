screen credits():

    tag menu

    use game_menu(_("                          CREDITS"), scroll="viewport"):

        style_prefix "help"
        
        vbox:

            ypos - 8
            xpos + 150
            spacing 20

            text _("(CC): A small number of music used in this game was\ncomposed by Kevin Macleod and is licensed under the\nCreative Commons Attribution 4.0. See the 'Music' section\nbelow for more details.")
            
            vbox:

                spacing 40
            

                vbox:
                    spacing 40
                
                    vbox:
                    
                        text _("Creator & Developer") style "credits_title"
                        text _("- TTG Games") style "credits_item"

                    vbox:
                    
                        text _("Story & Writing, Game Design and Programming") style "credits_title"
                        text _("- TTG Games") style "credits_item"

                    vbox:
                    
                        text _("Game Engine") style "credits_title"
                        text _("- Powered by Ren'Py") style "credits_item" 

                    vbox:
                    
                        text _("Background & Character Art") style "credits_title"
                        text _("- TTG Games (Character)") style "credits_item"
                        text _("{color=#1E90FF}- {/color}{a=https://potat0master.itch.io/free-visual-novel-backgrounds-school-mini-pack-1}{color=#1E90FF}Potat0Master (Background)") style "credits_item"
                        text _("{color=#1E90FF}- {/color}{a=https://noranekogames.itch.io/yumebackground}{color=#1E90FF}Noraneko Games (Background){a}{/color}") style "credits_item"
                        text _("{color=#1E90FF}- {/color}{a=https://www.fiverr.com/belsiartwork/draw-landscape-background-for-you-in-studio-ghibli-style#}{color=#1E90FF}Belsartwork (Background){a}{/color}") style "credits_item"
                        text _("{color=#1E90FF}- {/color}{a=https://lemmasoft.renai.us/forums/viewtopic.php?f=52&t=17302#p226871}{color=#1E90FF}Uncle Mugen (Background){a}{/color}") style "credits_item"
                        text _("{color=#1E90FF}- {/color}{a=https://panditastudio.itch.io/assets-pack-vol1-vn-backgrounds-school}{color=#1E90FF}Pandita Studio (Background){a}{/color}") style "credits_item"
                        text _("{color=#1E90FF}- {/color}{a=https://quarkyifu.itch.io/visual-novel-backgrounds-431-mage-bg-set}{color=#1E90FF}Quark_Yifu (Background){a}{/color}") style "credits_item"

                    vbox:
                        
                        text _("Music") style "credits_title"

                        text _("{u}Artists and Licenses") style "credits_item"
                        text _("{color=#1E90FF}- {/color}{a=https://www.bandlab.com/ttg_games}{color=#1E90FF}TTG Games{a}{/color}") style "credits_item"
                        text _("{color=#1E90FF}- {/color}{a=https://incompetech.com/}{color=#1E90FF}Kevin Macleod (Incompetech){a}{/color}") style "credits_item"
                        text _("{color=#1E90FF}- {/color}{a=https://creativecommons.org/licenses/by/4.0/}{color=#1E90FF}Creative Commons Attribution 4.0{a}{/color}") style "credits_item"


                        text _("{u}Websites") style "credits_item" ypos + 10

                        text _("{color=#1E90FF}- {/color}{a=https://pixabay.com}{color=#1E90FF}Pixabay{a}{/color}") style "credits_item" ypos + 10

        # This part is here to prevent the cut under the credits list.
        text ""
        text ""