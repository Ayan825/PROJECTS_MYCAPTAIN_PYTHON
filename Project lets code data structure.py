#Python program which accepts the radius of a circle from the user and computes area

import math

radius = float(input(" Enter radius of circle : "))
area = math.pi *radius *radius

print(area)



#Python program to accept a filename from the user and print the extension of that.

fn= input("Enter Filename: ")
f = fn.split(".")
print ("Extension of the file is : " + f[-1])


