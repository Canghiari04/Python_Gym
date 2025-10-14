"""
Write a Python program (not a function!) that asks the user for non-negative
integers that represent measurements of the daily amount of rain.
When the user enters the value 99999, the program prints the average
of the numbers received before that value.

If the user enters negative numbers, they are ignored.

The system will automatically input some values (shown, one at a time) to
test your program

To make the automatic system work:
    - The input descriptive string should be exactly R: (with no black
      spaces: hence you should use input("R:")).
    - The output should be the print of float, mandatory rounded using
      function round to two decimal digits, without any other characters.
    - If there is no valid input, the program does not print anything.

In this exercise only you are allowed, and required, to use print.
"""

x = 0
count = 0
list_amount = []

while x != 99999:
    x = int(input("R:"))

    if x > 0 and x != 99999:
        list_amount.append(x)

    count += 1

_str = " ".join(["R:" * count])
if len(list_amount) > 0:
    average = round((sum(list_amount) / len(list_amount)), 2)
    _str = _str + str(average)

print(_str)