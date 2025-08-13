package main 
import ( 
  "fmt"
  "strings"
  )
func isVowel(word string) bool {
  if len(word)==0{
    return false}
  vowels:="aeiouAEIOU"
  return strings.ContainsRune(vowels,rune(word[0]))
  func toGoatlatin(sentence string)string{
    words:=strings.Fields(sentence)
    var result[]string
    for i , word:= range words{
      if isVowel(word){
        word= word+"ma"
        }else{
        word=word[1:]+string(word[0])+"ma"
        }
      word= strings.Repeat("a",i+1)
      result= append(result,word)
      }
    return strings.Join(result," ")
    }
  func main(){
    fmt.Println(toGoatLatin("I speak goat latin)
                            }
