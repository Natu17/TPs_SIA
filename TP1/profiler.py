import cProfile, pstats ,search,rubik


profiler = cProfile.Profile()
profiler.enable()
#search.bfs( 'gwoyowbogrbgoyrbrwbyw' , rubik.actions, rubik.check)
#search.dfs( 'wgrgyowrwowrbgoybobby' , rubik.actions, rubik.check)
#search.dfslv( 'wgrgyowrwowrbgoybobby' , rubik.actions, rubik.check,4,5)
search.a('gowwoyryrbgobrgwobybw', rubik.actions,rubik.check, rubik.heurManDist)
profiler.disable()
stats = pstats.Stats(profiler).strip_dirs().sort_stats('tottime')
stats.print_stats()
