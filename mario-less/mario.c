#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int n;

    // prompt the user until we get a positive integer for the height
    do
    {
        n = get_int("Please enter a height for the pyramid: ");
    }
    while (n < 1);

    // print the pyramid
    for (int i = 0; i < n; i++)
    {
        // find out the amount of spaces to push the # right by
        int spaces = n - (i + 1);

        // print the spaces
        for (int j = 0; j < spaces; j++)
        {
            printf(" ");
        }

        // print the bricks or #
        for (int k = 0; k < i + 1; k++)
        {
            printf("#");
        }

        // print a new line
        printf("\n");
    }

    return 0;
}
