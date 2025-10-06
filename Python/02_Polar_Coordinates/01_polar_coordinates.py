# This solution is written and tested by me
# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
z = complex(input())
Polar = cmath.polar(z)
for i in Polar:
    print(i)


#-----Solution END here-----#


# Extra learnings 
# Printing the complex num from polar nums
r = Polar[0]
i = Polar[1]
print(cmath.rect(r,i))
