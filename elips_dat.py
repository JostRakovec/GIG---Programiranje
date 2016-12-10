import argparse
import math

a = 6378137.000
e = 0.081819191
parser = argparse.ArgumentParser()
parser.add_argument("dato", type=str, help="datoteka", default = 0)
args = parser.parse_args()
datoteka = args.dato
dat = open(datoteka, "r")
n1 = int(dat.readline())

im1 = []
x4 = []
y4 = []
z4 = []
for i in range(n1):
	vrstica1 = dat.readline()
	besede4 = vrstica1.split()
	im1.append(besede4[0])
	x4.append(float(besede4[1]))
	y4.append(float(besede4[2]))
	z4.append(float(besede4[3]))
	
dat.close
	
fir4 = 0.0
lamr4 = 0.0
N4 = 0.0
x5 = 0.0
y5 = 0.0
z5 = 0.0
print (40 * '-')
izpis = "{:>6} | {:>15} | {:>15} | {:>15}|".format("Točka", "x[m]", "y[m]", "z[m]")
print (izpis)
print (len(izpis) * '-')
for i in range(n1):
	fir4 = fir4 + math.radians(x4[i])
	lamr4 = lamr4 + math.radians(y4[i])
	N4 = N4 + (a/math.sqrt(1 - (e**2*(math.sin(fir4)**2))))
	x5 = x5 + (N4 + z4[i])*math.cos(fir4)*math.cos(lamr4)
	y5 = (N4 + z4[i])*math.cos(fir4)*math.sin(lamr4)
	z5 = (N4*(1-e**2)+ z4[i])*math.sin(fir4)
	print("{:6} | {:15.3f} | {:15.3f} | {:15.3f}|".format(im1[i], x5, y5, z5))