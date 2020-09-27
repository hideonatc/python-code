import pylab
def f(x):
	return pylab.sin(x)
a,b,n = -pylab.pi,pylab.pi,10
xs = pylab.linspace(a,b,n)
ys = f(xs)
pylab.plot(xs,ys)
pylab.grid()
pylab.title("test")
pylab.xlabel("x")
pylab.ylabel("y")
pylab.show()