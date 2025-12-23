#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // getting the name from the user
    string name = get_string("Please type your name, ");

    // printing the name to the screen
    printf("hello, %s\n", name);
}
