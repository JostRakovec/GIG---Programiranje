import argparse
import math

a = 6378137.000
e = 0.081819191

parser = argparse.ArgumentParser()
parser.add_argument("fi", type=float, help="koordinata fi")
parser.add_argument("lam", type=float, help="koordinata lam")
parser.add_argument("h", type=float, help="višina")
args = parser.parse_args()

h13 = args.h
fir13 = args.fi
lamr13 = args.lam

N13 = a/math.sqrt(1 - (e**2*(math.sin(fir13)**2)))
x13 = (N13 + h13)*math.cos(fir13)*math.cos(lamr13)
y13 = (N13 + h13)*math.cos(fir13)*math.sin(lamr13)
z13 = (N13*(1-e**2)+ h13)*math.sin(fir13)

print ("REZULTATI:")
print ("x = {:10.3f} m".format(x13))
print ("y = {:10.3f} m".format(y13))
print ("z = {:10.3f} m".format(z13))