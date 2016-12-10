import argparse
import math

a = 6378137.000
e = 0.081819191

parser = argparse.ArgumentParser()
parser.add_argument("x", type=float, help="koordinata x")
parser.add_argument("y", type=float, help="koordinata y")
parser.add_argument("z", type=float, help="koordinata z")
args = parser.parse_args()
x21 = args.x
y21 = args.y
z21 = args.z

p1 = math.sqrt(x21**2 + y21**2)
b1 = a * math.sqrt(1 - e**2)
e201 = math.sqrt(e**2 / (1 - e**2))
o1 = math.atan((z21 * a)/(p1 * b1))
fir21 = math.atan((z21 + e201**2 * b1 * math.sin(o1)**3)/(p1- e**2 * a * math.cos(o1)**3))
N21 = a/ (math.sqrt(1 - e**2 * math.sin(fir21)**2))
lamr21 = math.atan(y21/x21)
fi21 = math.degrees(fir21)
lam21 = math.degrees(lamr21)
h21 = (p1/math.cos(fir21))- N21

print ("REZULTATI:")
print ("fi = {:10.10f} ".format(fi21))
print ("lam = {:10.10f}".format(lam21))
print ("h = {:10.3f} m".format(h21))
