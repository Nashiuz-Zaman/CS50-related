#include <stdio.h>
#include <string.h>

int main() {
    char name[50];
    char proceed;

    // Greet the user and ask for their name
    printf("Hello, who is this?\n");
    fgets(name, sizeof(name), stdin);  // Reading input with spaces

    // Strip newline character if present
    name[strcspn(name, "\n")] = '\0';

    // Respond to the user
    printf("Oh hey, %s! Would you like me to proceed further? (y/n): ", name);
    scanf(" %c", &proceed);

    // Check if the user wants to proceed
    if (proceed == 'y' || proceed == 'Y') {
        printf("Happy Halloween!\n");
    } else {
        printf("Alright, maybe next time!\n");
    }

    return 0;
}
    