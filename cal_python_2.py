import pylab as pl
def fh(x):
	return 2.5464*pl.cos(2*x)+2.5464*pl.cos(6*x)+2.5465*pl.cos(10*x)+2.54646*pl.cos(14*x)+2.54646*pl.cos(18*x)
def h(x):
	return 1.2732*pl.sin(2*x)+0.4244*pl.sin(6*x)+0.25465*pl.sin(10*x)+0.18189*pl.sin(14*x)+0.14147*pl.sin(18*x)
a,b,n = -pl.pi,pl.pi,10000
h_xs = pl.linspace(a,b,n)
h_ys = h(h_xs)
h_xs_f = pl.linspace(a,b,n)
h_ys_f = fh(h_xs_f)
pl.plot(h_xs,h_ys,label='h(t)')
pl.plot(h_xs_f,h_ys_f,label="h'(t)")
pl.grid()
pl.xlabel("X")
pl.ylabel("Y")
pl.legend(loc=4)
pl.title("sawtooth function approximation and derivative")
pl.show()