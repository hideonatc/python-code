import pylab as pl
def f(x):
	return (pl.cos(x)**2)/pl.sqrt(pl.maximum(1,2*x-1))
a,b,n = 0,10*pl.pi,1000
xs = pl.linspace(a,b,n)
ys = f(xs)
pl.plot(xs,ys)
pl.grid()
pl.xlabel("X")
pl.ylabel("Y")
pl.title("f(x) = cos(x)^2/sqrt(max(1,2x-1))")
pl.show()