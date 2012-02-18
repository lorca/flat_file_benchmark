my @rows;
while (<>) {
    push @rows, [split(/\t/)];
}

print join(",",@{$rows[1]});
