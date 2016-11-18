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

a = 6378137.000
e = 0.081819191
if choice == 1:
	print (40 * '-')
	print ("OBLIKA KOORDINAT")
	print (40 * '-')
	print ("1. Stopinje, minute, sekunde")
	print ("2. Decimalne stopinje")
	print ("3. Radiani")
	print ("4. Branje iz tekstovne datoteke")
	
	choice = input('Napiši svojo izbiro [1, 2, 3 ali 4] : ')
	choice = int(choice)
	if choice == 1:
	
		print (40 * '-')
		print ("Navodilo: spodaj napišite koordinati fi in lambda (primer: 45 26 46.21866) ter višino v metrih")
		print (40 * '-')
		
		st1 = []
		m1 = []
		ss1 = []
		
		fi11 = input("fi = ")
		for i in range(1):
			besede1 = fi11.split()
			st1.append(int(besede1[0]))
			m1.append(int(besede1[1]))
			ss1.append(float(besede1[2]))

		fi111 = st1[i] + m1[i]/60 + ss1[i]/3600
		fir11 = math.radians(fi111)

		st2 = []
		m2 = []
		ss2 = []
		
		lam11 = input("lam = ")
		for t in range(1):
			besede11 = lam11.split()
			st2.append(int(besede11[0]))
			m2.append(int(besede11[1]))
			ss2.append(float(besede11[2]))
	
		lam111 = st2[i] + m2[i]/60 + ss2[i]/3600
		lamr11 = math.radians(lam111)
		
		h11 = float(input('h = '))
		
		N11 = a/math.sqrt(1 - (e**2*(math.sin(fir11)**2)))
		x11 = (N11 + h11)*math.cos(fir11)*math.cos(lamr11)
		y11 = (N11 + h11)*math.cos(fir11)*math.sin(lamr11)
		z11 = (N11*(1-e**2)+ h11)*math.sin(fir11)
		
		print (40 * '-')
		print ("REZULTATI:")
		print ("x = {:10.3f} m".format(x11))
		print ("y = {:10.3f} m".format(y11))
		print ("z = {:10.3f} m".format(z11))
		
	if choice == 2:
		print (40 * '-')
		print ("Navodilo: spodaj napišite decimalne koordinate fi in lambda (primer: 45.2646218) ter višino v metrih")
		print (40 * '-')
		
		fi12 = float(input('fi = '))
		lam12 = float(input('lam = '))
		h12 = float(input('h = '))
		
		fir12 = math.radians(fi12)
		lamr12 = math.radians(lam12)
		
		N12 = a/math.sqrt(1 - (e**2*(math.sin(fir12)**2)))
		x12 = (N12 + h12)*math.cos(fir12)*math.cos(lamr12)
		y12 = (N12 + h12)*math.cos(fir12)*math.sin(lamr12)
		z12 = (N12*(1-e**2)+ h12)*math.sin(fir12)
		
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
		
		N13 = a/math.sqrt(1 - (e**2*(math.sin(fir13)**2)))
		x13 = (N13 + h13)*math.cos(fir13)*math.cos(lamr13)
		y13 = (N13 + h13)*math.cos(fir13)*math.sin(lamr13)
		z13 = (N13*(1-e**2)+ h13)*math.sin(fir13)
		
		print (40 * '-')
		print ("REZULTATI:")
		print ("x = {:10.3f} m".format(x13))
		print ("y = {:10.3f} m".format(y13))
		print ("z = {:10.3f} m".format(z13))
	if choice == 4:
		print (40 * '-')
		datoteka1 = input('Ime datoteke: ')
		dat = open(datoteka1, "r")
		
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
		for i in range(n1):
			fir4 = fir4 + math.radians(x4[i])
			lamr4 = lamr4 + math.radians(y4[i])
			N4 = N4 + (a/math.sqrt(1 - (e**2*(math.sin(fir4)**2))))
			x5 = x5 + (N4 + z4[i])*math.cos(fir4)*math.cos(lamr4)
			y5 = (N4 + z4[i])*math.cos(fir4)*math.sin(lamr4)
			z5 = (N4*(1-e**2)+ z4[i])*math.sin(fir4)
		print (40 * '-')
		izpis = "{:>6} | {:>15} | {:>15} | {:>15}|".format("Točka", "x[m]", "y[m]", "z[m]")
		print (izpis)
		print (len(izpis) * '-')
		for i in range(n1):
			print("{:6} | {:15.3f} | {:15.3f} | {:15.3f}|".format(im1[i], x5, y5, z5))
else:
	print (40 * '-')
	print ("MOŽNOSTI")
	print (40 * '-')
	print ("1. Napišem x, y, z koordinate")
	print ("2. Branje koordinat iz tekstovne datoteke")
	
	choice = input('Napiši svojo izbiro [1 ali 2] : ')
	choice = int(choice)
	
	if choice == 1:
		print (40 * '-')
		print ("Navodilo: spodaj napišite koordinate x, y in z (primer: 4526696.045)")
		print (40 * '-')
		x21 = float(input('x ='))
		y21 = float(input('y ='))
		z21 = float(input('z ='))
		
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
	else:
		print (40 * '-')
		datoteka = input('Ime datoteke: ')
		dat = open(datoteka, "r")
		
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
			print (40 * '-')
		izpis = "{:>6} | {:>15} | {:>15} | {:>15}|".format("Točka", "fi", "lambda", "h[m]")
		print (izpis)
		print (len(izpis) * '-')
		for i in range(n):
			print("{:6} | {:15.10f} | {:15.10f} | {:15.10f}|".format(im[i], fi22, lam22, h22))

		