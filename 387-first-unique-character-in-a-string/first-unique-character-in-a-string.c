int firstUniqChar(char* s) {
    int count[256] = {0};  //ascii
    int len = strlen(s);
    for (int i = 0; i < len; ++i) { count[s[i]]++;}
    for (int i = 0; i < len; ++i) { if (count[s[i]] == 1) { return i;}}
    
    return -1;  
}