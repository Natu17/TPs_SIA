import line_profiler, main, selections


profiler = line_profiler.LineProfiler()

#profiler.add_function(selections.roulette)
profiler.add_function(selections.roulette_base)
wrapper = profiler(main.main)
wrapper()


profiler.print_stats(open("line_profiler","w"),output_unit=1)


