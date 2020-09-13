#sleep_in
#The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
#sleep_in(False, False) → True
#sleep_in(True, False) → False
#sleep_in(False, True) → True
def sleep_in(weekday, vacation):
  if not weekday or vacation:
    return True
  else:
    return False

#monkey_trouble
#We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
#monkey_trouble(True, True) → True
#monkey_trouble(False, False) → True
#monkey_trouble(True, False) → False
def monkey_trouble(a_smile, b_smile):
  if a_smile and b_smile:
    return True
  if not a_smile and not b_smile:
    return True
  return False

#sum_double
#Given two int values, return their sum. Unless the two values are the same, then return double their sum.
#sum_double(1, 2) → 3
#sum_double(3, 2) → 5
#sum_double(2, 2) → 8
def sum_double(a, b):
  if a != b:
    return a+b
  if a == b:
    return (a+b)*2
