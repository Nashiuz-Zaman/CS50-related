#include <stdio.h>
#include <string.h>

int main(void)
{

    int size;
    printf("Please type a number to make the grid \n");
    scanf("%d", &size);

    for (int i = 0; i < size; i++)
    {

        for (int j = 0; j < size; j++)
        {
            printf("#");
        }
        printf("\n");
    }
}
