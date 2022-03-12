import line_profiler ,algo,rubik


profiler = line_profiler.LineProfiler()
#profiler.add_function(algo.search)

# wrapper = profiler(algo.bfs)
# wrapper('owwobbbbyyoogggrwwrry' , rubik.actions, rubik.check)

# wrapper = profiler(algo.dfs)
# wrapper('wwgrwrybobwogobogrbyy' , rubik.actions, rubik.check)

wrapper = profiler(algo.dfslv)
wrapper('wgrgyowrwowrbgoybobby' , rubik.actions, rubik.check,4,5)


profiler.print_stats(open("line_profiler","w"))


