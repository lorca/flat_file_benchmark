#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <stdint.h>
#include <stdbool.h>
#include <unistd.h>

typedef struct slice
{
    size_t size;
    char *string;
} slice;

static uint32_t countColumns(char *currentPosition, char *endOfMap)
{
    uint32_t rtn = 0;
    uint32_t candidateRtn = 0;
    while (currentPosition < endOfMap)
    {
        if ((*currentPosition == '\t') || (*currentPosition == '\n'))
        {
            candidateRtn++;
            if (*currentPosition == '\n')
            {
                rtn = candidateRtn;
                break;
            }
        }
        currentPosition++;
    }
    return rtn;
}

static bool parseLine(char **currentPosition, slice **tokens, uint32_t numColumns, char *endOfMap)
{
    bool rtn = false;
    slice *candidateTokens = malloc(sizeof(slice) * numColumns);
    if (candidateTokens)
    {
        char *pos = *currentPosition;
        char *start = pos;
        uint32_t columnIndex = 0;
        while (pos < endOfMap)
        {
            if (columnIndex == numColumns)
                break;
            if ((*pos == '\t') || (*pos == '\n'))
            {
                candidateTokens[columnIndex].size = pos - start;
                candidateTokens[columnIndex++].string = start;
                start = pos + 1;
                if (*pos == '\n')
                    break;
            }
            pos++;
        }
        if ((*pos == '\n') && (columnIndex == numColumns))
        {
            *tokens = candidateTokens;
            rtn = true;
            *currentPosition = pos+1;
        }
        if (!rtn)
            free(candidateTokens);
    }
    return rtn;
}

#define STARTING_ROWSIZE 1024

int main(int argc, char *argv[])
{
    uint32_t i;
    if (argc > 1)
    {
        int dataDescriptor = open(argv[1], O_RDONLY);
        if (dataDescriptor >= 0)
        {
            struct stat dataStats;
            if (!fstat(dataDescriptor, &dataStats))
            {
                char *dataMapping = mmap(NULL, dataStats.st_size, PROT_READ, MAP_PRIVATE, dataDescriptor, 0);
                if (dataMapping != MAP_FAILED)
                {
                    char *endOfMap = dataMapping + dataStats.st_size;
                    char *currentPosition = dataMapping;
                    uint32_t numColumns = countColumns(currentPosition, endOfMap);
                    if (numColumns)
                    {
                        slice *tokens = NULL;
                        uint32_t numRows = 0;
                        uint32_t maxRowSize = STARTING_ROWSIZE;
                        slice **rows = malloc(sizeof(slice *) * maxRowSize);
                        if (rows)
                        {
                            while (parseLine(&currentPosition, &tokens, numColumns, endOfMap))
                            {
                                rows[numRows++] = tokens;
                                if (numRows == maxRowSize)
                                {
                                    maxRowSize *= 2;
                                    rows = realloc(rows, sizeof(slice *) * maxRowSize);
                                }
                            }
                            if (numRows > 1)
                            {
                                for (i = 0; i < numColumns; i++)
                                    printf("%s%.*s",((i == 0) ? "" : ",") , (int)rows[1][i].size, rows[1][i].string);
                                printf("\n");
                            }
                            // uncomment to have things cleanup as they exit...
/*                            for (uint32_t i = 0; i < numRows; i++)
                                free(rows[i]);
                            free(rows); */
                        }
                    }
//                    munmap(dataMapping, dataStats.st_size);
                }
            }
  //          close(dataDescriptor);
        }
    }

    return EXIT_SUCCESS;
}
