import argparse
import math

a = 6378137.000
e = 0.081819191
parser = argparse.ArgumentParser()
parser.add_argument("fi", type=float, help="koordinata fi")
parser.add_argument("lam", type=float, help="koordinata lam")
parser.add_argument("h", type=float, help="višina")
args = parser.parse_args()

fir12 = math.radians(args.fi)
lamr12 = math.radians(args.lam)
h12 = args.h

N12 = a/math.sqrt(1 - (e**2*(math.sin(fir12)**2)))
x12 = (N12 + h12)*math.cos(fir12)*math.cos(lamr12)
y12 = (N12 + h12)*math.cos(fir12)*math.sin(lamr12)
z12 = (N12*(1-e**2)+ h12)*math.sin(fir12)

print ("REZULTATI:")
print ("x = {:10.3f} m".format(x12))
print ("y = {:10.3f} m".format(y12))
print ("z = {:10.3f} m".format(z12))
