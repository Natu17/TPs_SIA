import cProfile, pstats ,search,rubik


profiler = cProfile.Profile()
profiler.enable()
search.bfs( 'gwoyowbogrbgoyrbrwbyw' , rubik.actions, rubik.check)
#search.dfs( 'wgrgyowrwowrbgoybobby' , rubik.actions, rubik.check)
#search.dfslv( 'wgrgyowrwowrbgoybobby' , rubik.actions, rubik.check,4,5)
profiler.disable()
stats = pstats.Stats(profiler).strip_dirs().sort_stats('cumtime')
stats.print_stats()
