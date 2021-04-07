#!/usr/bin/python2.4 -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Additional basic string exercises

# D. verbing
# Given a string, if its length is at least 3,
# add 'ing' to its end.
# Unless it already ends in 'ing', in which case
# add 'ly' instead.
# If the string length is less than 3, leave it unchanged.
# Return the resulting string.
def verbing(s):
    # +++your code here+++
    if len(s)<3:
        return s    
    
    endString = s[len(s)-3:]

    if endString == "ing":
        return s + "ly"

    return  s + "ing"


# E. not_bad
# Given a string, find the first appearance of the
# substring 'not' and 'bad'. If the 'bad' follows
# the 'not', replace the whole 'not'...'bad' substring
# with 'good'.
# Return the resulting string.
# So 'This dinner is not that bad!' yields:
# This dinner is good!
def not_bad(s):
  # +++your code here+++
  
  # need to look through whole string for "bad" if "bad" is not found return string
  # "bad" should be higher index if after not so bad > not will need that replace with "good"
  # need to use .find, .rfind finds the last occurrence while .find finds the first occurrence 
  
  badCheck = s.find("bad")
  notCheck = s.find("not")

  if notCheck < badCheck:
    sub = s[notCheck:badCheck+3]
    s = s.replace(sub, "good", 1)

  return s


# F. front_back
# Consider dividing a string into two halves.
# If the length is even, the front and back halves are the same length.
# If the length is odd, we'll say that the extra char goes in the front half.
# e.g. 'abcde', the front half is 'abc', the back half 'de'.
# Given 2 strings, a and b, return a string of the form
#  a-front + b-front + a-back + b-back
def front_back(a, b):
  # +++your code here+++
  if len(a) % 2 == 0:
    aFront = a[:int(len(a)/2)]
    aBack = a[int(len(a)/2):]
  else:
    # if I had a string of 3 then I would want to get the first two characters for the return string 
    # i need to break the string into the form 2n+1
    # going to assume strings are bigger than 1 
    # 3 = 2 + 1
    # 5 = 4 + 1 = 2+2+1 =2(1+1)+1 = 2(2)+1 -> 2(2) is front and back while the +1 is the middle character of the odd string
    # 5-1 = 4 -> int(4/2) = 2 -> aFront = a[:int((len(a)-1)/2)+1] while aBack = a=[int((len(a)-1)/2):]
    
    aFront = a[:int((len(a)-1)/2)+1]
    aBack = a[int((len(a)-1)/2)+1:]

  if len(b) % 2 == 0:
    bFront = b[:int(len(b)/2)]
    bBack = b[int(len(b)/2):]
  else:
    bFront = b[:int((len(b)-1)/2)+1]
    bBack = b[int((len(b)-1)/2)+1:]

  return aFront + bFront + aBack + bBack


# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print()
  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
