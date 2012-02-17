from benchmark import benchmark

margin = 0
delay  = 1
#benchmark("./output/awk.benchmark", ("/usr/bin/awk", "-f", "progs/read_file.awk", "input/mydata.csv"), margin, delay)
#benchmark("./output/ruby187.benchmark", ("/usr/bin/ruby1.8", "progs/read_file.rb", "input/mydata.csv"), margin, delay)
#benchmark("./output/ruby193.benchmark", ("/usr/bin/ruby1.9.1", "progs/read_file.rb", "input/mydata.csv"), margin, delay)
#benchmark("./output/perl5124.benchmark", ("/usr/bin/perl", "progs/read_file.pl", "input/mydata.csv"), margin, delay)
#benchmark("./output/python272.benchmark", ("/usr/bin/python", "progs/read_file.py", "input/mydata.csv"), margin, delay)
#benchmark("./output/python322.benchmark", ("/usr/bin/python3", "progs/read_file3.py", "input/mydata.csv"), margin, delay)
#benchmark("./output/java7b147.benchmark", ("/usr/bin/java", "-Xmx3000m", "progs/ReadFile", "input/mydata.csv"), margin, delay)
#benchmark("./output/java7b147.benchmark", ("/usr/bin/java", "-Xmx3000m", "progs/ReadFile", "input/mydata.csv"), margin, delay)
benchmark("./output/python272_numpy.benchmark", ("/usr/bin/python", "progs/read_file_numpy.py", "input/mydata.csv"), margin, delay)
