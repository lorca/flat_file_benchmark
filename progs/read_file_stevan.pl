
# You may get some speed/memory improvements by turning the `while` statement in Perl into a statement modifier.
push @rows, [split(/\t/)] while <>;

print join(",",@{$rows[1]});
