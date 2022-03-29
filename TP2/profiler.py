import cProfile, pstats, main

profiler = cProfile.Profile()
profiler.enable()
main.main()
profiler.disable()
stats = pstats.Stats(profiler).strip_dirs().sort_stats('tottime')
stats.print_stats()
