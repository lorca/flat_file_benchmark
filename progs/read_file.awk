
function join(array, sep, len) {
   result = array[0]
   for (i = 1; i < len; i++) {
       result = result sep array[i]
   }
   return result
}

BEGIN {
   FS="\t"
}

{
   for (i=1; i<=NF; i++) {
       rows[line_number][i-1] = $i; 
   }
   ++line_number
}

END {

   for (i=1; i<=NF; i++) {
       rows[line_number][i-1] = $i; 
   }

   print join(rows[1],",",NF)
}
