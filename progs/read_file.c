#include <sys/mman.h>
#include <stdlib.h>
#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>


static char* parse_line(char *line, char *maxaddr, char ***parsed, int *ncols)
{
  char **arr = malloc(sizeof(char*) * 1);
  int n = 0;
  char *start = line;
  char *cur = line;
  int curwasnl = 0;
  
  for(;!curwasnl; ++cur, ++n)
  {
    start = cur;
    for(; *cur != '\t' && *cur != '\n' && cur < maxaddr; ++cur)
    {
    }
    arr = realloc(arr, sizeof(char*) * (n + 1));
    arr[n] = start;
    curwasnl = (*cur == '\n') || cur == maxaddr;
    *cur = '\0';
  }
  *ncols = n;
  *parsed = arr;
  return cur; 
} 


int main(int argc, char **argv)
{
  int fd;
  struct stat st;  
  fd = open(argv[1], O_RDONLY);
  fstat(fd, &st);
  off_t size = st.st_size;
  char *mapped = mmap(NULL, size, PROT_READ|PROT_WRITE, MAP_PRIVATE, fd, 0);  
  
  char *maxaddr = mapped + size;
  
  char *line = mapped;
  size_t n = 0;
  struct row
  {
    char **cols;
    int ncols;
  };
  
  struct row *rows = malloc(sizeof(struct row));
  struct row currow;
  while( line < maxaddr )
  {
    line = parse_line(line, maxaddr, &currow.cols, &currow.ncols);
    rows = realloc(rows, sizeof(struct row) * (n + 1));
    rows[n].cols = currow.cols;
    rows[n].ncols = currow.ncols;
    n++;
  }


  for(int i = 0; i != rows[1].ncols; ++i)
  {
     if( i != 0 ) printf(",");
     printf("%s", rows[1].cols[i]);
  }
  printf("\n");

  return 0; 
  
}
   
  


