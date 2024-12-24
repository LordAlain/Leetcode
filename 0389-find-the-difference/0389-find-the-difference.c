char findTheDifference(char* s, char* t) {
    char res = 0;
    while (*s) res ^= *s++;
    while (*t) res ^= *t++;
    return res;
}