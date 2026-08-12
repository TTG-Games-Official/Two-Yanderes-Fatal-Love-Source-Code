init python:
    build.classify('**~', None)
    build.classify('**.bak', None)
    build.classify('**/.**', None)
    build.classify('**/#**', None)
    build.classify('**/thumbs.db', None)
    build.documentation('*.html')
    build.documentation('*.txt')

    
    build.classify('game/**.png', 'archive')
    build.classify('game/**.jpg', 'archive')
    build.classify('game/**.webp', 'archive')
    build.classify('game/**.ogg', 'archive')
    build.classify('game/**.opus', 'archive')
    build.classify('game/**.mp3', 'archive')
    build.classify('game/**.wav', 'archive')

    # Allowing People to Access Font Files
    # build.classify('game/**.ttf', 'archive')
    # build.classify('game/**.otf', 'archive')
    # build.classify('game/**.ttc', 'archive')

    # Allowing People to Access Code Files
    # build.classify('game/**.rpy', 'archive')
    # build.classify('game/**.rpyc', 'archive') 