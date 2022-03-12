import line_profiler ,algo,rubik


profiler = line_profiler.LineProfiler()
profiler.add_function(algo.search)

# wrapper = profiler(algo.bfs)
# wrapper('owwobbbbyyooggggrrwwyrry' , rubik.actions, rubik.check)

# wrapper = profiler(algo.dfs)
# wrapper('wwgrwrybobwogobgrogrybyy' , rubik.actions, rubik.check)

wrapper = profiler(algo.dfslv)
wrapper('wgrgyowrwowrbgogryboybby' , rubik.actions, rubik.check,4,5)


profiler.print_stats(open("line_profiler","w"))


