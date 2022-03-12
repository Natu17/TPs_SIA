import line_profiler ,algo,rubik


profiler = line_profiler.LineProfiler()
profiler.add_function(algo.search)

# wrapper = profiler(algo.bfs)
# wrapper('owwobbbbyyoogggrwwrry' , rubik.actions, rubik.check)

# wrapper = profiler(algo.dfs)
# wrapper('wwgrwrybobwogobogrbyy' , rubik.actions, rubik.check)

wrapper = profiler(algo.dfsvl)
wrapper('ybbggbrwgwrwoywrooyob' , rubik.actions, rubik.check,5,3)


profiler.print_stats(open("line_profiler","w"))


