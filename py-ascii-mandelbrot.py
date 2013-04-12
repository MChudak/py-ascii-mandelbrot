#!/usr/bin/env python
from numpy import linspace
from sys import argv

ra = -2.0	# fractal is drawn from z0 = ra + ia*j to z1 = rb + ib*j
rb =  1.0	# whole (?) set: ra = -2.0, rb= 1.0, ia = -1.0, ib= 1.0
ia = -1.0
ib =  1.0

# maxx/maxy best 3/2, it's width/height [in ascii chars!]
if len(argv) <= 1:
    maxx = 60.0
else:
    maxx = float(argv[1])
maxy = maxx*0.5*(ib - ia)/(rb - ra)

brdr = 5.0	# look for right brdr by guess :p

maxiter = 200
# maxiter defines precision of telling if a point
# belongs to the set;
# it should be: d(maxiter)/d(min(|rb - ra|,|ib - ia|)) < 0,
# meaning: if you magnify, it's harder to tell the points apart
# also: higher value => slower, but better quality

pix = 'W'	# it's PIXel, HALf, and EMPty - program's brushes
hal = 'x'
emp = '.'

for imaginary in linspace(ia, ib, maxy):
    line = ''
    for real in linspace(ra, rb, maxx):
        z0 = z = real + imaginary*1j
        for i in range(maxiter):
            z = z*z + z0	# <- all magic is here!
        if (abs(z.real)*15<brdr) and (abs(z.imag)*15<brdr):
            line += hal
        elif ((abs(z.real)<brdr)&(abs(z.imag)<brdr)):
            line += pix
        else:
            line += emp
    print(line)

