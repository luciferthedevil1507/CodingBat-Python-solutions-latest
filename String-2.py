#double_char
#Given a string, return a string where for every char in the original, there are two chars.
#double_char('The') → 'TThhee'
#double_char('AAbb') → 'AAAAbbbb'
#double_char('Hi-There') → 'HHii--TThheerree'
def double_char(str):
  result = ''
  for char in str:
    result += (char+char)
  return result

#count_hi
#Return the number of times that the string "hi" appears anywhere in the given string.
#count_hi('abc hi ho') → 1
#count_hi('ABChi hi') → 2
#count_hi('hihi') → 2
def count_hi(str):
  counter = 0
  for i in range (len(str)-1):
    if str[i] == 'h' and str[i+1] == 'i':
      counter+=1
  return counter
  
#cat_dog
#Return True if the string "cat" and "dog" appear the same number of times in the given string.
#cat_dog('catdog') → True
#cat_dog('catcat') → False
#cat_dog('1cat1cadodog') → True
def cat_dog(str):
  counter1 = 0
  counter2 = 0
  counter1 = str.count("cat")
  counter2 = str.count("dog")
  if(counter1 == counter2):
    return True
  else:
    return False
  
#count_code
#Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.
#count_code('aaacodebbb') → 1
#count_code('codexxcode') → 2
#count_code('cozexxcope') → 2
def count_code(str):
  counter = 0
  for i in range (len(str)-3):
    if str[i] == 'c' and str[i+1] == 'o' and str[i+3] == 'e':
      counter += 1
  return counter
