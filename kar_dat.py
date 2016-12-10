import argparse
import math

a = 6378137.000
e = 0.081819191

parser = argparse.ArgumentParser()
parser.add_argument("datot", type=str, help="datoteka", default = 0)
args = parser.parse_args()

datoteka1 = args.datot
dat = open(datoteka1, "r")

n = int(dat.readline())

im = []
x = []
y = []
z = []
for i in range(n):
	vrstica = dat.readline()
	besede3 = vrstica.split()
	
	im.append(besede3[0])
	x.append(float(besede3[1]))
	y.append(float(besede3[2]))
	z.append(float(besede3[3]))

dat.close

p12 = 0.0
b12 = 0.0
o2 = 0.0
fir22 = 0.0
N22 = 0.0
lamr22 = 0.0
fi22 = 0.0
lam22 = 0.0
h22 = 0.0
print (40 * '-')
izpis = "{:>6} | {:>15} | {:>15} | {:>15}|".format("Točka", "fi", "lambda", "h[m]")
print (izpis)
print (len(izpis) * '-')
for i in range(n):
	p12 = p12 + math.sqrt(x[i]**2 + y[i]**2)
	b12 = b12 + (a * math.sqrt(1 - e**2))
	e201 = math.sqrt(e**2 / (1 - e**2))
	o2 = o2 + (math.atan((z[i] * a)/(p12 * b12)))
	fir22 = fir22 + (math.atan((z[i] + e201**2 * b12 * math.sin(o2)**3)/(p12- e**2 * a * math.cos(o2)**3)))
	N22 = N22 + (a/ (math.sqrt(1 - e**2 * math.sin(fir22)**2)))
	lamr22 = lamr22 + (math.atan(y[i]/x[i]))
	fi22 = fi22 + (math.degrees(fir22))
	lam22 = lam22 + (math.degrees(lamr22))
	h22 = h22 + (p12/math.cos(fir22))- N22
	print("{:6} | {:15.10f} | {:15.10f} | {:15.3f}|".format(im[i], fi22, lam22, h22))
