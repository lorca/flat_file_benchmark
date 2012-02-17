lines = []
File.open(ARGV[0], "r").each_line do |line|
  lines.push(line.split("\t"))
end

print lines[1].join(",")

