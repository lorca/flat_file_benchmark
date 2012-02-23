proc read_file {fn} {
  set fd [open $fn r]
  fconfigure $fd -encoding ascii
  set rows [list]
  foreach {col1 col2 col3 col4 col5} [split [read $fd] \n\t] {
    lappend rows [list $col1 $col2 $col3 $col4 $col5]
  }
  close $fd
  puts [join [lindex $rows 1] ,] 
}
read_file [lindex $argv 0]
