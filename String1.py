#hello_name
#Given a string name, e.g. "Bob", return a greeting of the form "Hello Bob!".
#hello_name('Bob') → 'Hello Bob!'
#hello_name('Alice') → 'Hello Alice!'
#hello_name('X') → 'Hello X!'
def hello_name(name):
  return 'Hello ' + name+'!'

#make_abba
#Given two strings, a and b, return the result of putting them together in the order abba, e.g. "Hi" and "Bye" returns "HiByeByeHi".
#make_abba('Hi', 'Bye') → 'HiByeByeHi'
#make_abba('Yo', 'Alice') → 'YoAliceAliceYo'
#make_abba('What', 'Up') → 'WhatUpUpWhat
def make_abba(a, b):
  return a+b+b+a

#make_tags
#The web is built with HTML strings like "<i>Yay</i>" which draws Yay as italic text. In this example, the "i" tag makes <i> and </i> which surround the word "Yay". Given tag and word strings, create the HTML string with tags around the word, e.g. "<i>Yay</i>".
#make_tags('i', 'Yay') → '<i>Yay</i>'
#make_tags('i', 'Hello') → '<i>Hello</i>'
#make_tags('cite', 'Yay') → '<cite>Yay</cite>'
def make_tags(tag, word):
  return "<"+tag+">"+word+"</"+tag+">"

#make_out_word
#Given an "out" string length 4, such as "<<>>", and a word, return a new string where the word is in the middle of the out string, e.g. "<<word>>".
#make_out_word('<<>>', 'Yay') → '<<Yay>>'
#make_out_word('<<>>', 'WooHoo') → '<<WooHoo>>'
#make_out_word('[[]]', 'word') → '[[word]]'
def make_out_word(out, word):
  return out[:2]+word+out[2:]

#
