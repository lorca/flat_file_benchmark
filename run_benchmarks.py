from benchmark import benchmark

margin = 0
delay  = 1
#benchmark("./output/gawk4.benchmark", ("/usr/local/bin/gawk-4.0.0", "-f", "progs/read_file.awk", "input/mydata.csv"), margin, delay)
#benchmark("./output/ruby187.benchmark", ("/usr/bin/ruby1.8", "progs/read_file.rb", "input/mydata.csv"), margin, delay)
#benchmark("./output/ruby193.benchmark", ("/usr/bin/ruby1.9.1", "progs/read_file.rb", "input/mydata.csv"), margin, delay)
#benchmark("./output/perl5124.benchmark", ("/usr/bin/perl", "progs/read_file.pl", "input/mydata.csv"), margin, delay)
benchmark("./output/perl5124_stevan.benchmark", ("/usr/bin/perl", "progs/read_file_stevan.pl", "input/mydata.csv"), margin, delay)
#benchmark("./output/perl5124_stevan_map.benchmark", ("/usr/bin/perl", "progs/read_file_stevan_map.pl", "input/mydata.csv"), margin, delay)
#benchmark("./output/python272.benchmark", ("/usr/bin/python", "progs/read_file.py", "input/mydata.csv"), margin, delay)
#benchmark("./output/python272.benchmark", ("/usr/bin/python", "progs/read_file.py", "input/mydata.csv"), margin, delay)
benchmark("./output/pypy_tuple.benchmark", ("/opt/pypy/bin/pypy", "progs/read_file_tuple.py", "input/mydata.csv"), margin, delay)
benchmark("./output/pypy_tuple_fun.benchmark", ("/opt/pypy/bin/pypy", "progs/read_file_tuple_fun.py", "input/mydata.csv"), margin, delay)
benchmark("./output/python272_tuple_fun.benchmark", ("/usr/bin/python", "progs/read_file_tuple_fun.py", "input/mydata.csv"), margin, delay)
benchmark("./output/python272_tuple.benchmark", ("/usr/bin/python", "progs/read_file_tuple.py", "input/mydata.csv"), margin, delay)
#benchmark("./output/python272_tuple_unicode.benchmark", ("/usr/bin/python", "progs/read_file_tuple_unicode.py", "input/mydata.csv"), margin, delay)
#benchmark("./output/python272_tuple_tuple.benchmark", ("/usr/bin/python", "progs/read_file_tuple_tuple.py", "input/mydata.csv"), margin, delay)
#benchmark("./output/python322.benchmark", ("/usr/bin/python3", "progs/read_file3.py", "input/mydata.csv"), margin, delay)
#benchmark("./output/python272_csv.benchmark", ("/usr/bin/python", "progs/read_file_csv_tomasz.py", "input/mydata.csv"), margin,delay)
#benchmark("./output/java7b147.benchmark", ("/usr/bin/java", "-Xmx3000m", "progs/ReadFileArrayList", "input/mydata.csv"), margin, delay)
#benchmark("./output/c.benchmark", ("progs/read_file", "input/mydata.csv"), margin, delay)
#benchmark("./output/python272_numpy.benchmark", ("/usr/bin/python", "progs/read_file_numpy.py", "input/mydata.csv"), margin, delay)
