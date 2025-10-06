# Problem Statement

## Task
You are given a complex z. Your task is to convert it to polar coordinates.
## Input Format
A single line containing the complex number z. Note: complex() function can be used in python to convert the input as a complex number.
## Constraints
Given number is a valid complex number
## Output Format
Output two lines:
The first line should contain the value of r.
The second line should contain the value of .
## Sample Input
`1+2j`
## Sample Output
`2.23606797749979`  
`1.1071487177940904`
<hr>

# My Approach
I have idea about Polar Coordinates but it's not a big deal to anyone to solve this problem without knowing the polar coordinates.
The information that is required to know is given by the HackerRank in Problem Statement.

The format of complex number is z = x + yi where, x - real part & y - imaginary part.
We have to give the output of value of r and phi in saperate line. We don't have to calculate the value of r & phi the python inbuilt lib cmath helps to calculate the polar coordinates.

Firstly I take input of string and converted it into the complex number form by `complex()`. This function used to convert the input into complex number.  

Then used function of cmath lib. which is `cmath.polar(x)` which returns the representation of complex number x in a polar coordinates i.e. (r, phi) and this tuple is stored in Polar variable.  

Ans lastly printed the tuple using for loop because we need the both number r and phi in new line.

### Extra work
Did some extra i.e. converted the Polar coordinates return back into complex number using `cmath.rect(r,phi)`. It returns the complex number directly.
