import cProfile, pstats ,algo,rubik


profiler = cProfile.Profile()
profiler.enable()
#algo.bfs( 'gwoyowbogrbgoyrgrbrwybyw' , rubik.actions, rubik.check)
algo.dfs( 'wgrgyowrwowrbgogryboybby' , rubik.actions, rubik.check)
profiler.disable()
stats = pstats.Stats(profiler).strip_dirs().sort_stats('cumtime')
stats.print_stats()
