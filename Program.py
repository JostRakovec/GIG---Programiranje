import math
import sys

print (40 * '-')
print ("PROGRAM ZA PRETVORBO KOORDINAT")
print ("AVTOR: Jošt Rakovec")
print (40 * '-')
print ("1. ELIPSOIDNE --> KARTEZIČNE")
print ("2. KARTEZIČNE --> ELIPSOIDNE")

choice = input('Napiši svojo izbiro [1 ali 2] : ')
choice = int(choice)

if choice == 1:
	print (40 * '-')
	print ("OBLIKA KOORDINAT")
	print (40 * '-')
	print ("1. Stopinje, minute, sekunde")
	print ("2. Decimalne stopinje")
	print ("3. Radiani")
	choice = input('Napiši svojo izbiro [1,2 ali 3] : ')
	choice = int(choice)
	if choice == 1:
		print (40 * '-')
		print ("Navodilo: spodaj napišite decimalne koordinate fi in lambda (primer: 45 26 46.21866) ter višino v metrih")
		print (40 * '-')
		st1 = []
		m1 = []
		ss1 = []
		st2 = []
		m2 = []
		ss2 = []
		fi11 = input("fi = ")
		besede1 = fi11.split()
		st1.append(int(besede1[0]))
		m1.append(int(besede1[1]))
		ss1.append(float(besede1[2]))
		lam11 = input("lam = ")
		besede2 = lam11.split()
		st2.append(int(besede1[0]))
		m2.append(int(besede1[1]))
		ss2.append(float(besede1[2]))
		h11 = float(input('h = '))
		N11 = a11/math.sqrt(1 - (e11**2*(math.sin(fir11)**2)))
		x11 = (N11 + h11)*math.cos(fir11)*math.cos(lamr11)
		y11 = (N11 + h11)*math.cos(fir11)*math.sin(lamr11)
		z11 = (N11*(1-e11**2)+ h11)*math.sin(fir11)
		print (40 * '-')
		print ("REZULTATI:")
		print ("x = {:10.3f} m".format(x11))
		print ("y = {:10.3f} m".format(y11))
		print ("z = {:10.3f} m".format(z11))
	if choice == 2:
		a11 = 6378137.000
		e11 = 0.081819191
		print (40 * '-')
		print ("Navodilo: spodaj napišite decimalne koordinate fi in lambda (primer: 45.2646218) ter višino v metrih")
		print (40 * '-')
		fi12 = float(input('fi = '))
		lam12 = float(input('lam = '))
		h12 = float(input('h = '))
		fir12 = math.radians(fi12)
		lamr12 = math.radians(lam12)
		N12 = a11/math.sqrt(1 - (e11**2*(math.sin(fir12)**2)))
		x12 = (N12 + h12)*math.cos(fir12)*math.cos(lamr12)
		y12 = (N12 + h12)*math.cos(fir12)*math.sin(lamr12)
		z12 = (N12*(1-e11**2)+ h12)*math.sin(fir12)
		print (40 * '-')
		print ("REZULTATI:")
		print ("x = {:10.3f} m".format(x12))
		print ("y = {:10.3f} m".format(y12))
		print ("z = {:10.3f} m".format(z12))
	if choice == 3:
		print (40 * '-')
		print ("Navodilo: spodaj napišite koordinate fi in lambda v radianih (primer: 0.745155) ter višino v metrih")
		print (40 * '-')
		fir13 = float(input('fi = '))
		lamr13 = float(input('lam = '))
		h13 = float(input('h = '))
		N13 = a11/math.sqrt(1 - (e11**2*(math.sin(fir13)**2)))
		x13 = (N13 + h13)*math.cos(fir13)*math.cos(lamr13)
		y13 = (N13 + h13)*math.cos(fir13)*math.sin(lamr13)
		z13 = (N13*(1-e11**2)+ h12)*math.sin(fir13)
		print (40 * '-')
		print ("REZULTATI:")
		print ("x = {:10.3f} m".format(x13))
		print ("y = {:10.3f} m".format(y13))
		print ("z = {:10.3f} m".format(z13))
else:
	print (40 * '-')
	print ("Navodilo: spodaj napišite koordinate x, y in z (primer: 4526696.045)")
	print (40 * '-')
	a21 = 6378137.000
	e21 = 0.081819191
	print (40 * '-')
	print ("Navodilo: spodaj napišite koordinate x, y in z (primer: 4526696.045)")
	print (40 * '-')
	x21 = float(input('x ='))
	y21 = float(input('y ='))
	z21 = float(input('z ='))
	p1 = math.sqrt(x21**2 + y21**2)
	b1 = a21 * math.sqrt(1 - e21**2)
	e201 = math.sqrt(e21**2 / (1 - e21**2))
	o1 = math.atan((z21 * a21)/(p1 * b1))
	fir21 = math.atan((z21 + e201**2 * b1 * math.sin(o1)**3)/(p1- e21**2 * a21 * math.cos(o1)**3))
	N21 = a21 / (math.sqrt(1 - e21**2 * math.sin(fir21)**2))
	lamr21 = math.atan(y21/x21)
	fi21 = math.degrees(fir21)
	lam21 = math.degrees(lamr21)
	h21 = (p1/math.cos(fir21))- N21
	print ("REZULTATI:")
	print ("fi = {:10.8f} stopinj".format(fi21))
	print ("y = {:10.8f} stopinj".format(lam21))
	print ("h = {:10.3f} m".format(h21))
		
		
