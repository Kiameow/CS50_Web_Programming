import sys

try:
  x = int(input("x = "))
  y = int(input("y = "))
except ValueError:
  print("invalid input")
  sys.exit(1)
try:
  result = x / y
except ZeroDivisionError:
  print("can't be divided by zero")
  sys.exit(1)
