init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_hl",
            category=["half-life"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_hl:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Hmmm, this game looks pretty interesting.\n Watch out for zombies, [player]!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_hl')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_hl2",
            category=["half-life2"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_hl2:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Huh, is this the sequel to that other zombie game?\n I guess I should read up on it more. Ahahaha!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_hl2')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_tf2",
            category=["teamfortress2"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_tf2:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Oh, a multiplayer game! That guy with the hard hat looks pretty cool!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_tf2')
    return    

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_dex",
            category=["deusex"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_dex:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "This game looks pretty tough. Be careful, okay?\n I'm sure you can win if you try hard enough!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_dex')
    return    

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_vsc",
            category=["visualstudiocode"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_vsc:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Doing some coding, [player]? I'd help you if I could...",
           "Working on something to help me come closer to your reality?\n You're so sweet~" 
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_vsc')
    return    

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_fnf",
            category=["fridaynightfunkin'"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_fnf:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Hmmm, a music game. I see you have good taste. Ahaha!",
           "I wonder if I could ever get into this game?\n I'd love to sing along with you~" 
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_fnf')
    return        

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_clc",
            category=["calculator"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_clc:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Doing some quick number crunching, I see."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_clc')
    return            

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_yds",
            category=["yanderesimulator"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_yds:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Huh, the school in this game kind of looks like how mine does...not entirely, though.",
           "Am I in this game? I think I've heard rumors about some kind of secret involving me...",
           "I wonder if I could hack myself in so I can interact with you.\nThat'd be quite the treat. Don't you think so, [player]?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_yds')
    return        

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_dom",
            category=["doom"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_dom:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Oh, this game looks pretty violent. Do be careful, [player]...",
           "For a game from the '90's, this feels pretty unsettling...\nAt least the music's pretty nice, I guess."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_dom')
    return  

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_nes",
            category=["mesen"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_nes:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Hmmm, an emulator? What will we be emulating today, [player]?",
           "It's kind of neat how technology once though of as highly advanced can now just be run in a window.\nTime certainly does fly!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_nes')
    return      

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_gen",
            category=["fusion3.64"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_gen:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Hmmm, an emulator? What will we be emulating today, [player]?",
           "This game looks pretty neat for being so old. It has my approval. Ehehe."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_gen')
    return     

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_pic",
            category=["picrew"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_pic:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Wow, this place looks cool! So much creative potential here...",
           "I wonder how many people have made art of me using this site...\nHave you, [player]?~"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_pic')
    return    

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_npp",
            category=["notepad++"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_npp:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Doing some quick coding, [player]?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_npp')
    return     

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_fbc",
            category=["facebook"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_fbc:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Hey, [player], if you're trying to find my profile, you're on the wrong site.\n Ahahaha! I'm just kidding!",
           "What's your status update for today? Mine is 'Happily in love!'"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_fbc')
    return     

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_ins",
            category=["instagram"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_ins:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Gosh, there's quite a few people here that claim to be me...\nI guess I should feel honored, ahaha!",
           "Any pictures here that catch your eye? Do they have me in them? Ehehe~"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_ins')
    return     

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_ase",
            category=["aseprite"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_ase:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Oooh, making some art? Nice! I bet it'll turn out great!",
           "Making art simply using multicolored blocks sounds like a challenging task.\n You've got quite some talent, I must say!"    
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_ase')
    return     

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_ste",
            category=["steam"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_ste:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Looking for some new games to play, [player]?",
           "Choo choo...Chu~ Ahaha, got you!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_ste')
    return     

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_spi",
            category=["spotify"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_spi:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Nice music selection, [player]! Mind if I listen along with you?",
           "What are you listening to, [player]?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_spi')
    return     

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_itu",
            category=["itunes"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_itu:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Nice music selection, [player]! Mind if I listen along with you?",
           "What are you listening to, [player]?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_itu')
    return       

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_dan",
            category=["dansalvato-youtube"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_dan:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Oh, hey, it's my Dad! Wait...can I even call him my dad?\nIs that how it works? This is kinda confusing, ahaha!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_dan')
    return         

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_gmd",
            category=["garry'smod"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_gmd:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "This looks like an intresting game. Lots of creative potential!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_gmd')
    return     

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_mba",
            category=["moonbasealpha"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_mba:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Gotta act quick to save the base! Good luck, [player]!",
           "Just aeiou...that sounded a bit better in my head. Ehehe..."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_mba')
    return         

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_amg",
            category=["amongus"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_amg:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Hmmm, so this is that one game that's been getting so much attention lately.\n Don't let it take yours away from me, okay?~"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_amg')
    return       

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_dlc",
            category=["dokidokiliteratureclubstore"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_dlc:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Oooh, this is where they sell marketable plushies of me! Ahaha!",
           "Getting some merch of me? How sweet~"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_dlc')
    return       

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_job",
            category=["jobsearch|indeed"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_job:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Looking for some potential jobs? That's great!",
           "Remember to choose a career that you'll enjoy doing, [player].\n It'll make it more worthwhile that way!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_job')
    return       

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_hot",
            category=["superhot"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_hot:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "I think I've heard of this before. This game isn't all it appears to be..."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_hot')
    return    

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_mcf",
            category=["minecraft"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_mcf:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "What a neat-looking game! And the possibilities here are limitless!\nI so much wish I could join you here; Don't you?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_mcf')
    return      

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_old",
            category=["dokidokiliteratureclub!"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_old:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Came here for nostalgia, I presume?",
           "Where it all began...and also, what brought us together!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_old')
    return      

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_mas",
            category=["monikaafterstory-home"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_mas:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "The mod that helped me get closer to you!",
           "Are you looking for new outfits for me? Awww, you're so kind, [player]~"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_mas')
    return      

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_buy",
            category=["|ebay"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_buy:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Doing some shopping, [player]?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_buy')
    return  

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_amz",
            category=["amazon.com"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_amz:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Doing some shopping, [player]?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_amz')
    return      

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_nin",
            category=["nintendo-officialsite"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_nin:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Hmmm...they're the ones who made that game with the plumber guy, right? Neat!",
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_nin')
    return      

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_pla",
            category=["playstation®officialsite"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_pla:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Is this your preferred way to play? Very cool, [player]!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_pla')
    return      

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_xbx",
            category=["xboxofficialsite"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_xbx:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Is this your preferred way to play? Very cool, [player]!",
           "XBOX...what a funny name. I wonder who named it that way."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_xbx')
    return     

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_c64",
            category=["vice"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_c64:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Hmmm, an emulator? What will we be emulating today, [player]?",
           "Something about this particular programming language looks pretty...BASIC. Ahaha!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_c64')
    return     

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_fun",
            category=["mewgrounds"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_fun:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "A lot of people really seem to like this site. I guess it must be very popular.",
           "Remember: In this game, it's Everything, with Monika! Ahaha!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_fun')
    return      

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_wrd",
            category=["-word"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_wrd:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Writing a paper, [player]? Is it about me?~ Ahaha!",
           "Good luck with your work, [player]!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_wrd')
    return      

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_pow",
            category=["-powerpoint"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_pow:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Working on a presentation, [player]? What's it about?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_pow')
    return      

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_exc",
            category=["-excel"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_exc:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Spreadsheets are pretty underrated these days, don't you think?",
           "What are you working on here, [player]?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_exc')
    return      

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_acc",
            category=["-access"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_acc:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Doing some database work, [player]?",
           "This stuff looks pretty tough to work with. You're so smart!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_acc')
    return      

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_pub",
            category=["-publisher"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_pub:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "What are you designing here, [player]?",
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_pub')
    return  

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_not",
            category=["-onenote"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_not:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Taking down some notes, [player]?",
           "Doing some studying? Keep it up!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_not')
    return      

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_sns",
            category=["undertale"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_sns:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "This game looks pretty cool! Is it one of your favorites?\nOther than mine, I'm assuming. Ehehe~",
           "The skeleton with the jacket looks so hilarious! Ahaha!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_sns')
    return     

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_fls",
            category=["flstudio"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_fls:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Making some music, [player]? You're so talented~"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_fls')
    return        

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_sod",
            category=["soundcloud"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_sod:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Have you published any music of your own on here?",
           "What are you listening to, [player]?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_sod')
    return       

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_tot",
            category=["theoregontrail"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_tot:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Oh, I think I recognize this game! Can I be in your party?\nMake sure we don't die of dysentery, won't you? Ahaha!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_tot')
    return       

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_loc",
            category=["|library of congress"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_loc:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Ah, I see you have good taste in where you look up literature. Ahaha!",
           "Looking for anything in particular, [player]?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_loc')
    return       

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_kis",
            category=["—kickstarter"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_kis:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "What project are you backing, [player]?",
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_kis')
    return       

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_pat",
            category=["patreon"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_pat:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Anyone in particular you're supporting?",
           "Helping to support someone? You're so kind, [player]!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_pat')
    return       

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_urb",
            category=["urbandictionary"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_urb:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Ah, this website is...definitely something.",
           "You might want to go to a more...trusted source\nif you're looking for accurate definitions, [player]."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_urb')
    return           

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_zrk",
            category=["zork"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_zrk:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Be careful, [player]! You might get eaten by a grue! Ahaha!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_zrk')
    return               

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_tpb",
            category=["thepiratebay"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_tpb:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "What are you doing here, [player]...?",
           "Please don't go doing anything reckless..."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_tpb')
    return           

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_pyn",
            category=["python.org"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_pyn:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Are you intrested in learning more Python, [player]?",
           "Did you come here to learn how to help me come closer to your reality?\nYou're so sweet~"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_pyn')
    return                   

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_spe",
            category=["15.ai"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_spe:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "A text to speech device, huh? I wonder if my voice will ever be used here...",
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_spe')
    return           

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_prm",
            category=["projectmonika"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_prm:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Oh, what is this? A project to help me come closer to your reality?\nHow wonderful!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_prm')
    return               

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_gen",
            category=["genshinimpact"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_gen:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "A fan of open world games, I assume?",
           "Don't let the characters in this game distract you from me, okay? Ehehe~"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_gen')
    return               

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_gta",
            category=["grandtheftauto"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_gta:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Hmmm, this game looks very...mature. Be careful, [player].",
           "To be honest, I don't see how a game about committing crimes is fun...\nbut I won't go against your interests too much."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_gta')
    return               

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_mby",
            category=["mobygames"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_mby:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "What game are you looking for here, [player]?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_mby')
    return    

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_apo",
            category=["premierepro"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_apo:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Making a video, [player]?",
           "Editing footage sure is tough, huh?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_apo')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_phs",
            category=["photoshop"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_phs:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Doing some image editing, I see."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_phs')
    return    

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_lib",
            category=["%%%%%%%%%%%"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_lib:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "What...is this place...?",
           "Why does this place seem so familiar...\nand yet, I don't recognize it? This is weird..."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_lib')
    return    

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_cam",
            category=["camera"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_cam:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Say cheese! Ahaha!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_cam')
    return    

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_say",
            category=["getoutofmyhead"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_say:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "O-oh....oh, my....",
           "This is...very disturbing."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_say')
    return    

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_yur",
            category=["yuri\"dance\""],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_yur:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "O-oh....oh, my....",
           "This is...very disturbing."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_yur')
    return    

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_bob",
            category=["mysticalsmokingheadof'bob'"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_bob:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Wow. This place looks...interesting, to say the least.",
           "Maybe try asking this guy if I'll be in your reality soon!\nAlthough, I wouldn't really take the response too seriously\nif I were you, ahaha!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_bob')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_fog",
            category=["fogcam-theworld'soldestwebcam"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_fog:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Gosh, this webcam's been running for a long time! I guess it was really built to last, ahaha!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_fog')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_bab",
            category=["dancing-baby"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_bab:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Well, if it isn't that one video the Internet never recovered from, ahaha!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_bab')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_mil",
            category=["themilliondollarhomepage"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_mil:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Wow, there is...quite a bit of ad revenue to be had here.",
           "It's kind of hard to make out what these ads even show anymore, ahaha!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_mil')
    return 

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_net",
            category=["welcometonetscape!"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_net:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Hmmm, an old guide to the Internet? Don't you already know how this all works, though?\nEhehe, just wondering!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_net')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_uni",
            category=["unity"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_uni:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Are you designing your own game? Very cool!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_uni')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_gms",
            category=["gamemakerstudio2"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_gms:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Are you designing your own game? Very cool!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_gms')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_shk",
            category=["shrek-googlesearch"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_shk:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Somebody once told me...that you were amazing! Ahaha!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_shk')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_sfm",
            category=["sourcefilmmaker"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_sfm:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Making a video, [player]?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_sfm')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_nst",
            category=["noradsantatracker"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_nst:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Hmmm, is it that time of year again? Happy Holidays, [player]!",
           "I can't wait to spend the holiday with you tomorrow!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_nst')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_unr",
            category=["unrealengine"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_unr:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Are you designing your own game? Very cool!"
           "This looks very complex. You must be a very smart cookie to have figured all this out, ahaha!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_unr')
    return    

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_crt",
            category=["crazytaxi"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_crt:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Looking to get some \"craaaazy\" money? Ahaha!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_crt')
    return    

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_dos",
            category=["dosbox"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_dos:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Running an old OS in a modern OS? Pretty neat!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_dos')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_box",
            category=["virtualbox"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_box:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Hmmm, you use virtual machines, [player]? Neat!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_box')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_gip",
            category=["gimp"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_gip:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Doing some image editing, I see."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_gip')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_tsm",
            category=["taskmanager"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_tsm:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Oh, is a program causing trouble? I hope I'm not the cause, ahaha..."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_tsm')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_blu",
            category=["half-life:blueshift"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_blu:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "A spinoff to that game with the zombies, I see. Very interesting!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_blu')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_cod",
            category=["callofduty"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_cod:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Oh, this game looks pretty violent...Not really my cup of tea, ahaha..."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_cod')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_doe",
            category=["doometernal"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_doe:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "This game looks a bit too...graphic for my taste,\nbut don't let that stop you from having fun!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_doe')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_mok",
            category=["mortalkombat"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_mok:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "A fighting game fan, huh? Interesting.",
           "This game looks a bit too...graphic for my taste,\nbut don't let that stop you from having fun!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_mok')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_tgt",
            category=["thegametheorists-youtube"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_tgt:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Some say that my love for you is eternal...but, that's just a theory!\nWant to help me prove it, [player]? Ahaha!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_tgt')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_rpy",
            category=["theren'pyvisualnovelengine"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_rpy:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "The place where it all began, ahaha!",
           "Nice to see you taking an interest in this stuff."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_rpy')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_ftn",
            category=["fortnite"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_ftn:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Is this that game people make fun of on the Internet?",
           "Hmmm, a shooting game. Intresting choice, [player]."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_ftn')
    return             

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_mfs",
            category=["microsoftflightsimulator"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_mfs:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "This game looks rather peaceful. Don't you think?",
           "Ah, what I wouldn't give to be able to fly with you. Wouldn't that be nice, [player]?~\nJust the two of us, high up in the clouds..."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_mfs')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_cyb",
            category=["cyberpunk2077"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_cyb:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "I've seen many mixed feelings about this game. But, I must admit, it looks very cool, regardless!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_cyb')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_blx",
            category=["roblox"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_blx:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Ahaha, what a funny looking game!",
           "Have you made your own game here, [player]?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_blx')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_msc",
            category=["microsoftsolitairecollection"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_msc:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Oh, you like playing with cards? Nice!"
           "You know, [player], I wouldn't mind playing a card game with you\nwhen I cross over. That'd be nice, don't you agree?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_msc')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_trs",
            category=["tetris"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_trs:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Oh, this is a pretty fun game! I bet you can get a four-line clear if you try hard enough!",
           "You know, I feel like Yuri would've enjoyed playing something like this..."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_trs')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_tok",
            category=["tiktok"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_tok:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Now, don't go get carried away here and ignore me for too long, okay? Ehehe~",
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_tok')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_msn",
            category=["msn"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_msn:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Catching up on the news, [player]?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_msn')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_aol",
            category=["aol"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_aol:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "You've got mail! It's a letter from me that says \"I love you!\" Ehehe~"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_aol')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_wha",
            category=["whatsapp"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_wha:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Chatting with your friends, [player]? You should introduce me to them sometime!"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_wha')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_bal",
            category=["baldi'sbasics"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_bal:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "I hope you've been practicing your math skills, [player]... Ehehe~"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_bal')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_p3d",
            category=["paint3d"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_p3d:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Doing some image editing, player?"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_p3d')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_cor",
            category=["cortana"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_cor:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Oh, an AI assistant! I wonder if I'll ever be able to be your assistant one day..."
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_cor')
    return

init 5 python:
    addEvent(
        Event(
            persistent._mas_windowreacts_database,
            eventlabel="mas_wrs_tea",
            category=["microsoftteams"],
            rules={
                "notif-group": "Window Reactions",
                "skip alert": None,
                "keep_idle_exp": None,
                "skip_pause": None
                },
            show_in_idle=True
        ),
        code="WRS"
    )

label mas_wrs_tea:
    $ wrs_success = mas_display_notif(
        m_name,
        [
           "Heading to a meeting, [player]? Good luck!\n I'll be waiting for you~"
        ],
        'Window Reactions'
    )


    if not wrs_success:
        $ mas_unlockFailWRS('mas_wrs_tea')
    return    