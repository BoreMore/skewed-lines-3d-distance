import numpy as np

p1 = np.fromstring(input("p1 (separate array vals with a space and don't use square brackets): "), sep=" ")
p2 = np.fromstring(input("p2: "), sep=" ")
v1 = np.fromstring(input("v1: "), sep=" ")
v2 = np.fromstring(input("v2: "), sep=" ")

# sample:
"""p1 = [-3,-7,2]
p2 = [-3,-3,1]
v1 = [2,4,-4]
v2 = [2,6,-2]"""



# formula:
# d= | ((v1xv2) . p1p2 ) | / |v1xv2|

v1xv2 = np.cross(v1, v2)
p1p2 = np.subtract(p1, p2)

print("sqrt(" + str(np.sum(np.dot(v1xv2, p1p2))**2) + " / " + str(np.sum(v1xv2**2)) + ")")
