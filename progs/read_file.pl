open(FILE, $ARGV[0]) or die $!;

my @rows;
while (<>) {
    push @rows, [split(/\t/)];
}

print join(",",@{$rows[1]});

close(FILE) or die $!;
