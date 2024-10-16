#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#define MAX 100

char stack[MAX];
int top =-1;

void push (char c){
  if (top<MAX-1){
    stack[++top]=c;
  }
}

char pop(){
  if (top>=0){
return stack[top--];
  }
return '\0';
}

void reversestring(char* str){
  int length=strlen(str);
for (int i=0;i<length;i++){
    push(str[i);
}
for (int i=0 ;i<length;i++){
  str[i]=pop();
}
}
int main() {
    char str[MAX];
    printf("Enter a string: ");
    fgets(str, MAX, stdin); 
    str[strcspn(str, "\n")] = '\0';
    reverseString(str);
    printf("Reversed string: %s\n", str);
    return 0;
}
  
