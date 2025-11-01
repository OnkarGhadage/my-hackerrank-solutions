# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB = int(input())
BC = int(input())
angle = round(math.degrees(math.atan(AB/BC)))
# print(angle,"\u00b0")   # The space comes between angle and \u00b0 cause test case fail
print(f"{angle}\u00b0")   # Correct way no space between
