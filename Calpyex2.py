import pylab as py
from numpy import *

a,b,n = 0 , 100*py.pi , 10000
ang = linspace(a,b,n)
rs = cos(py.pi*ang)
py.polar(ang,rs,lw=1,color='b')
py.fill(ang,rs,color = 'w')
py.title("graph of cos(pi x) for x in [0,100pi] using 10000 points",color='r')
py.show()