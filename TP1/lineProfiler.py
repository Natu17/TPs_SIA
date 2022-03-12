import line_profiler ,search,rubik


profiler = line_profiler.LineProfiler()
profiler.add_function(search.search)

# wrapper = profiler(search.bfs)
# wrapper('owwobbbbyyoogggrwwrry' , rubik.actions, rubik.check)

# wrapper = profiler(search.dfs)
# wrapper('wwgrwrybobwogobogrbyy' , rubik.actions, rubik.check)

wrapper = profiler(search.dfsvl)
wrapper('ybbggbrwgwrwoywrooyob' , rubik.actions, rubik.check,5,3)


profiler.print_stats(open("line_profiler","w"))


