rows = {}

for line in io.lines(arg[1]) do
   local tokens = {}
   for token in line:gmatch('[^\t]+') do
      table.insert(tokens, token)
   end
   table.insert(rows, tokens)
end

print(table.concat(rows[2], ','))
