#include <stdio.h>
#include <string.h>
#include <ctype.h>

#define MAX_WORDS 1000
#define MAX_WORD_LENGTH 100

typedef struct {
    char word[MAX_WORD_LENGTH];
    int count;
} WordFrequency;

void toLowerCase(char *str) {
    for (int i = 0; str[i]; i++) {
        str[i] = tolower(str[i]);
    }
}

int main() {
    WordFrequency wordList[MAX_WORDS];
    int wordCount = 0;
    char paragraph[1000];
    char *token;

    printf("Enter a paragraph:\n");
    fgets(paragraph, sizeof(paragraph), stdin);

    // Tokenize the paragraph
    token = strtok(paragraph, " \n");

    while (token != NULL) {
        toLowerCase(token);
        int found = 0;

        for (int i = 0; i < wordCount; i++) {
            if (strcmp(wordList[i].word, token) == 0) {
                wordList[i].count++;
                found = 1;
                break;
            }
        }

        if (!found) {
            strcpy(wordList[wordCount].word, token);
            wordList[wordCount].count = 1;
            wordCount++;
        }

        token = strtok(NULL, " \n");
    }

    printf("Word frequencies:\n");
    for (int i = 0; i < wordCount; i++) {
        printf("%s: %d\n", wordList[i].word, wordList[i].count);
    }

    return 0;
}