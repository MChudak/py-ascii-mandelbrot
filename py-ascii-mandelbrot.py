# -*- coding: utf-8 -*-

f=open('py-ascii-mandelrender','w')

ra=-2.0		# fractal is drawn from z0=ra+ia*j to z1=rb+ib*j
rb= 1.0		# whole (?) set: ra=-2.0, rb= 1.0, ia=-1.0, ib= 1.0
ia=-1.0
ib= 1.0
		# maxx/maxy best 3/2, it's width/height [in ascii chars!]
maxy=200.0
maxx=maxy*2.0*(rb-ra)/(ib-ia)

maxiter=200	# maxiter defines precision of telling if a point\
		# belongs to the set;
		# it should be: d(maxiter)/d(min(|rb-ra|,|ib-ia|)) < 0,
		# meaning: if you magnify, it's harder to tell the points apart
		# also: higher value => slower, but better quality

brdr=5.0	# look for right brdr by guess :p

pix='W'		# it's PIXel, HALf, and EMPty - program's brushes
hal='x'
emp='.'

y=0
while y<maxy:
    line=''
    
    x=0
    while x<maxx:
        z0=ra+(x/maxx)*(rb-ra)+(ia+(y/maxy)*(ib-ia))*1j
        z=z0
        
        i=0
        while i<maxiter:
            z=z*z+z0		# <- all magic is here!
            i+=1
            
        if ((abs(z.real)*15<brdr)&(abs(z.imag)*15<brdr)):
            line+=hal
        elif ((abs(z.real)<brdr)&(abs(z.imag)<brdr)):
            line+=pix
        else:
            line+=emp
            
        x+=1

    line+='\n'
    f.write(line)

    y+=1

